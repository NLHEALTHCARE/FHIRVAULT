import glob
import os

from domainmodel.identity_domain import Zorgverlener, Zorgaanbieder, ZorgverlenerZorgaanbiederLink
from domainmodel.valueset_domain import Valueset
from etl_mappings.vektis_agb.vektis_agb_importdef import vektis_import_def
from etl_mappings.vektis_agb.vektis_agb_transformations import VektisTransformations
from pyelt.mappings.base import ConstantValue
from pyelt.mappings.sor_to_dv_mappings import SorToLinkMapping, SorToValueSetMapping, SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(path):
    mappings = []
    fixed_length_file_defs = vektis_import_def

    os.chdir(path)
    for file_name in glob.glob("*.csv"):
        if not file_name.endswith('AB.csv'):
            continue
        def_name = file_name.split('.')[0]
        key_names = []

        import_def = fixed_length_file_defs[def_name]

        for field_def in import_def:
            if len(field_def) == 3:
                field_name = field_def[0]
                is_key = field_def[2]
                if is_key:
                    key_names.append(field_name)

        source_file = CsvFile('{}{}'.format(path, file_name), delimiter=';', encoding='utf8')
        source_file.reflect()
        source_file.set_primary_key(key_names)
        target_table = '{}_hstage'.format(def_name).lower()
        sor_mapping = SourceToSorMapping(source_file, target_table, auto_map=True)
        mappings.append(sor_mapping)

    # VALUESETS
    path = os.path.dirname(os.path.abspath(__file__))
    source_file = CsvFile('{}/vektis_agb_valueset_data.csv'.format(path), delimiter=';', encoding='utf8')
    source_file.reflect()
    source_file.set_primary_key(['source_code'])
    target_table = 'valueset_translations_hstage'.format(def_name).lower()
    sor_mapping = SourceToSorMapping(source_file, target_table, auto_map=True)
    mappings.append(sor_mapping)
    return mappings


def init_sor_to_valuesets_mappings(pipe):
    mappings = []
    mapping = SorToValueSetMapping('valueset_translations_hstage', Valueset)
    mapping.map_field("target_valueset", Valueset.valueset_naam)
    mapping.map_field("target_code", Valueset.code)
    mapping.map_field("target_descr", Valueset.omschrijving)
    mappings.append(mapping)
    #
    # for key, items in vektis_valuesets_data.items():
    #     ref_mapping = SorToValueSetMapping(items, key)
    #     mappings.append(ref_mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor
    schema_name = sor.name

    mapping = SorToEntityMapping('fagbx_20_all_ab_hstage', Zorgverlener, sor)
    mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    #Default-sat
    mapping.map_field(VektisTransformations.text_to_date_transform('geboortedatum'), Zorgverlener.Default.geboortedatum)
    mapping.map_field(VektisTransformations.agb_to_valueset_code("geslacht", 'geslacht_types'), Zorgverlener.Default.geslacht_code);
    # Identificatie-sat
    mapping.map_field(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'), Zorgverlener.Identificatie.agb_code)
    # Naamgegevens-sat
    mapping.map_field("initcap(naam)", Zorgverlener.Naamgegevens.geslachtsnaam)
    mapping.map_field("voorletters", Zorgverlener.Naamgegevens.initialen)
    mapping.map_field("lower(voorvoegsel)", Zorgverlener.Naamgegevens.geslachtsnaam_voorvoegsels)
    # Titels-sat
    mapping.map_field("adellijke_titel", Zorgverlener.Titels.adelijke_titel, ref='adelijke titels')
    mapping.map_field("lower(academische_titel)", Zorgverlener.Titels.academische_titel, ref='academische_titels')
    # Adres-sat
    mapping.map_field("straat", Zorgverlener.Adres.straat, type=Zorgverlener.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer::integer", Zorgverlener.Adres.huisnummer, type=Zorgverlener.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer_toevoeging", Zorgverlener.Adres.huisnummertoevoeging, type=Zorgverlener.Adres.Types.officieel_adres)
    mapping.map_field("postcode", Zorgverlener.Adres.postcode, type=Zorgverlener.Adres.Types.officieel_adres)
    mapping.map_field("initcap(plaatsnaam)", Zorgverlener.Adres.woonplaats, type=Zorgverlener.Adres.Types.officieel_adres)
    # Telefoon-sat
    mapping.map_field("telefoonnummer", Zorgverlener.Telefoon.nummer, type=Zorgverlener.Telefoon.Types.zakelijk)
    mappings.append(mapping)

    #########################################

    sor_sql = """SELECT fag20.*, fag21.indicatie_hoogleraar, fag21.reden_einde_beroep
                FROM {0}.fagbx_20_all_ab_hstage AS fag20 JOIN {0}.fagbx_21_all_ab_hstage AS fag21 ON fag20.zorgverlenersoort = fag21.zorgverlenersoort AND fag20.zorgverlenersnummer = fag21.zorgverlenersnummer """.format(
        schema_name)

    mapping = SorToEntityMapping(sor_sql, Zorgverlener, sor)
    mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    # BeroepsGegevens-sat
    mapping.map_field(VektisTransformations.text_to_date_transform('datum_aanvang_beroep'),
                      Zorgverlener.BeroepsGegevens.datum_aanvang_beroep);
    mapping.map_field(VektisTransformations.text_to_date_transform('datum_einde_beroep'),
                      Zorgverlener.BeroepsGegevens.datum_einde_beroep);
    mapping.map_field("(case when indicatie_hoogleraar='1' then True else False end)",            Zorgverlener.BeroepsGegevens.is_hoogleraar);
    mapping.map_field("reden_einde_beroep", Zorgverlener.BeroepsGegevens.reden_einde_beroep);
    mapping.map_field("nadere_verbijzondering_zvl_srt", Zorgverlener.BeroepsGegevens.specialisme_bijzondering_code);
    mapping.map_field("zorgverlenersoort", Zorgverlener.BeroepsGegevens.specialisme_code)
    mappings.append(mapping)


    #########################################

    link_mapping = SorToLinkMapping('fagbx_22_all_ab_hstage', ZorgverlenerZorgaanbiederLink, sor)
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgverlener, bk=VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgaanbieder, bk=VektisTransformations.make_agb('zorgverlenersoort', 'praktijknummer'))
    mappings.append(link_mapping)

    #########################################

    mapping = SorToEntityMapping('fagbx_23_all_ab_hstage', Zorgaanbieder, sor, type='praktijk')
    mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'praktijknummer'))
    mapping.map_field("zorgverlenersoort", Zorgaanbieder.Default.specialisme_code)
    mapping.map_field("organisatievorm", Zorgaanbieder.Default.organisatie_type)

    mapping.map_field(VektisTransformations.make_agb("zorgverlenersoort", "praktijknummer"), Zorgaanbieder.Identificatie.agb_code)
    mapping.map_field("initcap(naam_deel_1)", Zorgaanbieder.Default.naam)
    mapping.map_field("telefoonnummer", Zorgaanbieder.Telefoon.nummer, type=Zorgaanbieder.Telefoon.Types.zakelijk)
    mapping.map_field(VektisTransformations.text_to_date_transform("datum_aanvang_praktijk"), Zorgaanbieder.PraktijkGegevens.datum_aanvang_praktijk);
    mapping.map_field(VektisTransformations.text_to_date_transform("datum_einde_praktijk"), Zorgaanbieder.PraktijkGegevens.datum_einde_praktijk);

    mappings.append(mapping)

    #########################################

    link_mapping = SorToLinkMapping('fagbx_24_all_ab_hstage', ZorgverlenerZorgaanbiederLink, sor)
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgverlener, bk=VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgaanbieder, bk=VektisTransformations.make_agb('zorgverlenersoort', 'instellingsnummer'))
    #todo sat bij link vullen
    # link_mapping.map_field(VektisTransformations.text_to_date_transform("datum_toetreding_praktijk"), ZorgverlenerZorgaanbiederLink.Default.datum_toetreding);
    # link_mapping.map_field(VektisTransformations.text_to_date_transform("datum_uittreding_praktijk"), ZorgverlenerZorgaanbiederLink.Default.datum_uittreding);
    # link_mapping.map_field("status_in_de_instelling",ZorgverlenerZorgaanbiederLink.Default.status)
    mappings.append(link_mapping)

    #########################################

    sor_sql = """SELECT fag25.*
   FROM sor_vektis.fagbx_25_all_ab_hstage fag25
   join (select zorgverlenersoort, praktijknummer, max(praktijkadres_volgnummer) max_praktijkadres_volgnummer from sor_vektis.fagbx_25_all_ab_hstage group by zorgverlenersoort, praktijknummer) sub_query
on sub_query.zorgverlenersoort = fag25.zorgverlenersoort and sub_query.praktijknummer = fag25.praktijknummer and sub_query.max_praktijkadres_volgnummer = fag25.praktijkadres_volgnummer"""
    mapping = SorToEntityMapping(sor_sql, Zorgaanbieder, sor, type='praktijk')
    mapping.map_bk(VektisTransformations.make_agb("zorgverlenersoort", "praktijknummer"))
    # Adres-sat
    mapping.map_field(ConstantValue('NL'), Zorgaanbieder.Adres.land_code, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("straat", Zorgaanbieder.Adres.straat, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer::integer", Zorgaanbieder.Adres.huisnummer, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer_toevoeging", Zorgaanbieder.Adres.huisnummertoevoeging, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("postcode", Zorgaanbieder.Adres.postcode, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("initcap(plaatsnaam)", Zorgaanbieder.Adres.woonplaats, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.filter="praktijkadres_volgnummer='1'"
    mappings.append(mapping)

    #########################################

    mapping = SorToEntityMapping('agbu_759_ab_hstage', Zorgaanbieder, sor, type='instelling')
    mapping.map_bk(VektisTransformations.make_agb('soort_instelling', 'instellingsnummer'))
    mapping.map_field("soort_instelling", Zorgaanbieder.Default.organisatie_type)
    mapping.map_field(VektisTransformations.make_agb('soort_instelling', 'instellingsnummer'), Zorgaanbieder.Identificatie.agb_code)
    mapping.map_field("initcap(naam_instelling)", Zorgaanbieder.Default.naam)
    mapping.map_field(ConstantValue('NL'), Zorgaanbieder.Adres.land_code, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("straat", Zorgaanbieder.Adres.straat, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer::integer", Zorgaanbieder.Adres.huisnummer, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer_toevoeging", Zorgaanbieder.Adres.huisnummertoevoeging, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("postcode", Zorgaanbieder.Adres.postcode, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("initcap(plaats)", Zorgaanbieder.Adres.woonplaats, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("telefoon", Zorgaanbieder.Telefoon.nummer, type=Zorgaanbieder.Telefoon.Types.zakelijk)
    mapping.map_field(VektisTransformations.text_to_date_transform("datum_einde"), Zorgaanbieder.PraktijkGegevens.datum_einde_praktijk);
    mappings.append(mapping)

    return mappings
