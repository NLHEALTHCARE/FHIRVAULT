import glob, os, io, zipfile
# from mappings.vektis_agb.vektis_importdef import vektis_import_def
from domainmodel_fhir.identity_domain import Practitioner, Organization
from domainmodels.role_domain import *
from mappings.vektis_agb.vektis_agb_importdef import vektis_import_def

from mappings.vektis_agb.vektis_agb_reference_data import vektis_ref_data
from mappings.vektis_agb.vektis_agb_transformations import VektisTransformations
from pyelt.mappings.base import ConstantValue
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping, SorToValueSetMapping, EntityViewToEntityMapping, EntityViewToLinkMapping, \
    SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.mappings.transformations import FieldTransformation
from pyelt.mappings.validations import Validation
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
        sor_mapping = SourceToSorMapping(source_file, '{}_hstage'.format(def_name), auto_map=True)
        mappings.append(sor_mapping)
    return mappings


def init_sor_to_ref_mappings(pipe):
    mappings = []
    for key, items in vektis_ref_data.items():
        ref_mapping = SorToValueSetMapping(items, key)
        mappings.append(ref_mapping)
    return mappings


def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor
    mapping = SorToEntityMapping('fagbx_20_all_ab_hstage', Practitioner, sor)
    #bk
    mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))

    # default-sat
    mapping.map_field(VektisTransformations.text_to_date_transform('geboortedatum'), Practitioner.Default.birthdate)
    mapping.map_field(VektisTransformations.agb_code_to_gender("geslacht"), Practitioner.Default.gender);

    #identifier-sat
    #mapping.map_field("concat(zorgverlenersoort, nadere_verbijzondering_zvl_srt)", Practitioner.Default..Identifier.id_type, )
    mapping.map_field(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'), Practitioner.Identifier.value, type=Practitioner.Identifier.Types.official)

    #name-sat
    mapping.map_field("initcap(naam)", Practitioner.Name.family, type=Practitioner.Name.Types.usual)
    #mapping.map_field("voorletters", Practitioner.Name, , type=Practitioner.Name.Types.usual)
    mapping.map_field("lower(voorvoegsel)", Practitioner.Name.prefix, type=Practitioner.Name.Types.usual)
    #mapping.map_field("adellijke_titel", Zorgverlener.Titels.adelijke_titel, ref='adelijke titels')
    #mapping.map_field("lower(academische_titel)", Zorgverlener.Titels.academische_titel, ref='academische_titels')
    #mapping.map_field("CONCAT(initcap(naam)", Practitioner.Name.text, type=Practitioner.Name.Types.usual)

    #address-sat
    mapping.map_field("straat", Practitioner.Address.line, type=Practitioner.Address.Types.work)
    #mapping.map_field("huisnummer::integer", Practitioner.Address.line, type=Practitioner.Address.Types.work)
    #mapping.map_field("huisnummer_toevoeging", Practitioner.Address.line, type=Practitioner.Address.Types.work)
    mapping.map_field("postcode", Practitioner.Address.postalcode, type=Practitioner.Address.Types.work)
    mapping.map_field("initcap(plaatsnaam)", Practitioner.Address.city, type=Practitioner.Address.Types.work)
    #todo text

    #telecom-sat
    mapping.map_field("telefoonnummer", Practitioner.Telecom.value, type=Practitioner.Telecom.Systems.phone + '-' + Practitioner.Telecom.Types.work)

    #beroep
    # mapping.map_field(VektisTransformations.text_to_date_transform('datum_aanvang_beroep'), Zorgverlener.BeroepsGegevens.datum_aanvang_beroep);
    # mapping.map_field("sor_vektis.convert_to_date(datum_einde_beroep)", Zorgverlener.BeroepsGegevens.datum_einde_beroep);
    # mapping.map_field(VektisTransformations.text_to_date_transform('datum_einde_beroep'), Zorgverlener.BeroepsGegevens.datum_einde_beroep);
    # mapping.map_field("nadere_verbijzondering_zvl_srt", ); #todo\review ZBIS moet dit misschien "Zorgverlener.Default.specialisme_code worden?    mapping.map_field("mutatiesoort",                   => mutatiesoort text")
    # mapping.map_field("reserve", );
    mappings.append(mapping)

    # mapping = SorToEntityMapping('fagbx_21_all_ab_hstage', Practitioner, sor)
    # mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    # mapping.map_field("aanduiding_oud", );
    # mapping.map_field("bestandcode",  );
    # mapping.map_field("zorgverlenersoort", Zorgverlener.Default.zorgverlener_rol)
    # mapping.map_field("zorgverlenersnummer", Zorgverlener.Default.zorgverlener_identificatienummer)
    #vervolg beroep
    # mapping.map_field("(case when indicatie_hoogleraar='1' then True else False end)", Zorgverlener.BeroepsGegevens.is_hoogleraar);
    # mapping.map_field("reden_einde_beroep", Zorgverlener.BeroepsGegevens.reden_einde_beroep);
    # mapping.map_field("mutatiesoort", );
    # mapping.map_field("reserve", );
    # mappings.append(mapping)

    #####################################
    # ORGANIZATION
    #####################################

    mapping = SorToEntityMapping('fagbx_23_all_ab_hstage', Organization, sor)
    mapping.map_bk(VektisTransformations.make_agb('zorgverlenersoort', 'praktijknummer'))
    # mapping.map_field("aanduiding_oud", );
    # mapping.map_field("bestandcode", );

    #default-sat
    mapping.map_field("initcap(naam_deel_1)", Organization.Default.org_name)
    #mapping.map_field("zorgverlenersoort", Organization.Default.afdeling_specialisme_code)
    #mapping.map_field("organisatievorm", Organization.Default.organisatie_type)

    #identifier-sat
    mapping.map_field("praktijknummer", Organization.Identifier.value, type = Organization.Identifier.Types.official)



    #telecom_sat
    mapping.map_field("telefoonnummer", Organization.Telecom.value, type=Organization.Telecom.Systems.phone + '-' +  Organization.Telecom.Types.work)
    # mapping.map_field("datum_aanvang_praktijk", );  # todo
    # mapping.map_field("datum_einde_praktijk", );  # todo
    # mapping.map_field("filler", );
    # mapping.map_field("mutatiesoort", );
    # mapping.map_field("reserve", );
    mappings.append(mapping)

    return mappings

    mapping = SorToEntityMapping('fagbx25_hstage', Zorgaanbieder, sor)
    mapping.map_bk(VektisTransformations.make_agb("zorgverlenersoort", "praktijknummer"))
    # mapping.map_field("aanduiding_oud", );
    # mapping.map_field("bestandcode", );
    # mapping.map_field("zorgverlenersoort", Zorgaanbieder.Default.afdeling_specialisme_code)
    mapping.map_field(VektisTransformations.make_agb("zorgverlenersoort", "praktijknummer"),   Zorgaanbieder.Identificatie.agb_code)
    # mapping.map_field("praktijkadres_volgnummer", ); #todo
    mapping.map_field(ConstantValue('NL'), Zorgaanbieder.Adres.land_code,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("straat", Zorgaanbieder.Adres.straat, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer::integer", Zorgaanbieder.Adres.huisnummer,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer_toevoeging", Zorgaanbieder.Adres.huisnummertoevoeging,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("postcode", Zorgaanbieder.Adres.postcode, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("initcap(plaatsnaam)", Zorgaanbieder.Adres.woonplaats,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    # mapping.map_field("mutatiesoort", );
    # mapping.map_field("reserve", );
    mapping.filter = "praktijkadres_volgnummer='1'"
    mappings.append(mapping)

    mapping = SorToEntityMapping('instel_hstage', Zorgaanbieder, sor)
    # mapping.map_bk(['soort_instelling||instellingsnummer'])
    mapping.map_bk(VektisTransformations.make_agb('soort_instelling', 'instellingsnummer'))
    mapping.map_field("soort_instelling", Zorgaanbieder.Default.organisatie_type)
    mapping.map_field(VektisTransformations.make_agb('soort_instelling', 'instellingsnummer'),
                      Zorgaanbieder.Identificatie.agb_code)
    mapping.map_field("initcap(naam_instelling)", Zorgaanbieder.Default.naam)
    mapping.map_field(ConstantValue('NL'), Zorgaanbieder.Adres.land_code,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("straat", Zorgaanbieder.Adres.straat, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer::integer", Zorgaanbieder.Adres.huisnummer,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("huisnummer_toevoeging", Zorgaanbieder.Adres.huisnummertoevoeging,
                      type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("postcode", Zorgaanbieder.Adres.postcode, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("initcap(plaats)", Zorgaanbieder.Adres.woonplaats, type=Zorgaanbieder.Adres.Types.officieel_adres)
    mapping.map_field("telefoon", Zorgaanbieder.Telefoon.nummer, type=Zorgaanbieder.Telefoon.Types.zakelijk)
    # mapping.map_field("datum_einde", ); #todo
    mappings.append(mapping)


    #####################################
    # LINKS ORGANIZATION
    #####################################
    link_mapping = SorToLinkMapping('fagbx22_hstage', ZorgverlenerZorgaanbiederLink, sor)
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgverlener,
                            bk=VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgaanbieder,
                            bk=VektisTransformations.make_agb('zorgverlenersoort', 'praktijknummer'))
    mappings.append(link_mapping)

    link_mapping = SorToLinkMapping('fagbx24_hstage', ZorgverlenerZorgaanbiederLink, sor)
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgverlener, bk=VektisTransformations.make_agb('zorgverlenersoort', 'zorgverlenersnummer'))
    link_mapping.map_entity(ZorgverlenerZorgaanbiederLink.zorgaanbieder, bk=VektisTransformations.make_agb('zorgverlenersoort', 'instellingsnummer'))
    mappings.append(link_mapping)

    # mapping = SorToEntityMapping('fagbx24.s01.csv_hstage', 'fagbx24.s01.csv_entity')
    # mapping.map_field("aanduiding_oud                 => aanduiding_oud text")
    # mapping.map_field("bestandcode                    => bestandcode text")
    # mapping.map_field("zorgverlenersoort              => zorgverlenersoort text")
    # mapping.map_field("zorgverlenersnummer            => zorgverlenersnummer text")
    # mapping.map_field("instellingsnummer              => instellingsnummer text")
    # mapping.map_field("datum_toetreding_praktijk      => datum_toetreding_praktijk text")
    # mapping.map_field("datum_uittreding_praktijk      => datum_uittreding_praktijk text")
    # mapping.map_field("status_in_de_instelling        => status_in_de_instelling text")
    # mapping.map_field("mutatiesoort                   => mutatiesoort text")
    # mapping.map_field("reserve                        => reserve text")
    # mappings.append(mapping)


    return mappings
