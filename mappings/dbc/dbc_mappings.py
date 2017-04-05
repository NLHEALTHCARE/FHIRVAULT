from domainmodel.identity_domain import Zorgverlener
from mappings.dbc.dbc_transformations import DbcTransformations
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToValueSetMapping
from domainmodel.valueset_domain import *
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile

"""DBC Csv data inlezen in sor en hierna in valset
Data te vinden op http://werkenmetdbcs.nza.nl/ziekenhuiszorg-artikelen/dbc-pakket-2018/menu-ID-2792

"""

def init_source_to_sor_mappings(pipe):
    mappings = []
    path = pipe.config['data_path']

    source_file = CsvFile('{}{}'.format(path, '20170101 Zorgproducten Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['Zorgproductcode', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgproducten_hstage', auto_map=True)
    mappings.append(sor_mapping)


    source_file = CsvFile('{}{}'.format(path, '20170101 Zorgproductgroepen Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['zorgproductgroep_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgproductgroepen_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '20170101 Zorgactiviteiten Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['zorgactiviteit_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgactiviteiten_hstage', auto_map=True)
    mappings.append(sor_mapping)

    # todo[jan] Controle of key klopt
    source_file = CsvFile('{}{}'.format(path, '20170101 Tarieven Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(
        ['agb_specialisme', 'agb_uitvoerder', 'productgroepcode', 'declaratiecode', 'kostensoort', 'tarieftype', 'declaratie_eenheid', 'soort_tarief', 'segment_aanduiding', 'soort_honorarium',
         'ingangsdatum', 'einddatum'])
    sor_mapping = SourceToSorMapping(source_file, 'tarieven_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '20170101 Diagnose Combinatie Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['specialisme_code', 'diagnose_dbc1', 'diagnose_dbc2', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'diagnose_combinatie_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '20170101 Afsluitregels Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['afsluitregelcode', 'groepnummer', 'specialismecode', 'componentcode', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'afsluitregels_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '20170101 Afsluitreden Tabel v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['afsluitreden_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'afsluitreden_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '20170101 Elektronische Typeringslijst v20160701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['specialisme_code_agb', 'as_code', 'component_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'typeringslijst_hstage', auto_map=True)
    mappings.append(sor_mapping)
    return mappings

def init_sor_to_valset_mappings(pipe):

    mappings = []
    mapping = SorToValueSetMapping('zorgproducten_hstage', Zorgproduct)
    mapping.map_field("zorgproductcode", Zorgproduct.code)
    mapping.map_field("zorgproductomschrijving", Zorgproduct.omschrijving)
    mapping.map_field("zorgproduct_latijnse_omschrijving", Zorgproduct.omschrijving_latijn)
    mapping.map_field("zorgproduct_consumentenomschrijving", Zorgproduct.omschrijving_consument)
    mapping.map_field("declaratiecode_verzekerde_zorg", Zorgproduct.declaratie_code_verzekerde_zorg)
    mapping.map_field("declaratiecode_onverzekerde_zorg", Zorgproduct.declaratie_code_onverzekerde_zorg)
    mapping.map_field("zorgproduct_wbmv_code", Zorgproduct.wbmv_code)
    mapping.map_field("zorgproductgroep_code", Zorgproduct.zorgproductgroep_code)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgproduct.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgproduct.einddatum)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.zorgproducten_hstage mx where mx.zorgproductcode = hstg.zorgproductcode)'
    mappings.append(mapping)

    mapping = SorToValueSetMapping('zorgproductgroepen_hstage', Zorgproductgroep)
    mapping.map_field("zorgproductgroep_code", Zorgproductgroep.code)
    mapping.map_field("zorgproductgroep_omschrijving", Zorgproductgroep.omschrijving)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgproductgroep.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgproductgroep.einddatum)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.zorgproductgroepen_hstage mx where mx.zorgproductgroep_code = hstg.zorgproductgroep_code)'
    mappings.append(mapping)

    # Beschikbare velden ZORGACTIVITEITEN_HSTAGE:
    # zorgactiviteit_code, zorgactiviteit_omschrijving, op_nota, zorgactiviteit_consumenten_omschrijving, zpk_code, zpk_omschrijving, spmenr_01, spmenr_02, spmenr_03, spmenr_04,
    # spmenr_05, spmenr_06, spmenr_07, spmenr_08, spmenr_10, spmenr_13, spmenr_16, spmenr_18, spmenr_20, spmenr_22,
    # spmenr_24, spmenr_26, spmenr_27, spmenr_28, spmenr_29, spmenr_30, spmenr_35, spmenr_61, spmenr_62, spmenr_89,
    # spmenr_90, wbmv_code, eenheid, aantal_eenheden, aanspraak_code, indicatie_addon, ingangsdatum, einddatum, mutatie,
    mapping = SorToValueSetMapping('zorgactiviteiten_hstage', Zorgactiviteit)
    mapping.map_field("zorgactiviteit_code", Zorgactiviteit.code)
    mapping.map_field("zorgactiviteit_omschrijving", Zorgactiviteit.omschrijving)
    mapping.map_field("zorgactiviteit_consumenten_omschrijving", Zorgactiviteit.omschrijving_consument)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgactiviteit.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgactiviteit.einddatum)
    mapping.map_field("(CASE WHEN op_nota='J' THEN true ELSE false END)", Zorgactiviteit.op_nota)
    mapping.map_field("zpk_code", Zorgactiviteit.groep_code)
    mapping.map_field("LOWER(zpk_omschrijving)", Zorgactiviteit.groep_omschrijving)
    mapping.map_field("(CASE WHEN indicatie_addon='J' THEN true ELSE false END)", Zorgactiviteit.is_addon)
    mapping.map_field("wbmv_code", Zorgactiviteit.wbmv_code)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.zorgactiviteiten_hstage mx where mx.zorgactiviteit_code = hstg.zorgactiviteit_code)'
    mappings.append(mapping)

    # Beschikbare velden TARIEVEN_HSTAGE:
    # agb_specialisme, agb_uitvoerder, declaratiecode, productgroepcode, tarief, kostensoort, ingangsdatum, einddatum, omschrijving_declaratiecode, tarieftype,
    # declaratie_eenheid, soort_tarief, segment_aanduiding, soort_honorarium, mutatie_toelichting, declaratie_regel, mutatie,
    mapping = SorToValueSetMapping('tarieven_hstage', Tarief)
    mapping.map_field("", Tarief.code)
    mapping.map_field("", Tarief.omschrijving)
    mapping.map_field("", Tarief.declaratiecode)
    mapping.map_field("", Tarief.omschrijving_declaratiecode)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Tarief.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Tarief.einddatum)
    mapping.map_field("", Tarief.specialisme_code)
    mapping.map_field("", Tarief.agb_uitvoerder)
    mapping.map_field("", Tarief.productgroepcode)
    mapping.map_field("::numeric", Tarief.tarief)
    mapping.map_field("", Tarief.kostensoort)
    mapping.map_field("", Tarief.tarieftype)
    mapping.map_field("", Tarief.declaratie_eenheid)
    mapping.map_field("", Tarief.tariefsoort)
    mapping.map_field("", Tarief.segment_aanduiding)
    mapping.map_field("", Tarief.honorarium_soort)
    mapping.map_field("", Tarief.declaratie_regel)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.tarieven_hstage mx where mx.zorgactiviteit_code = hstg.zorgactiviteit_code)'
    # mappings.append(mapping)

    # Beschikbare velden DIAGNOSE_COMBINATIE_HSTAGE:
    # specialisme_code, diagnose_dbc1, diagnose_dbc2, indicatie, ingangsdatum, einddatum, mutatie,
    mapping = SorToValueSetMapping('diagnose_combinatie_hstage', DiagnoseCombinatie)
    mapping.map_field("(specialisme_code || '-' || diagnose_dbc1 || '-' || diagnose_dbc2)", DiagnoseCombinatie.code)
    mapping.map_field("diagnose_dbc1", DiagnoseCombinatie.dbc1)
    mapping.map_field("diagnose_dbc2", DiagnoseCombinatie.dbc2)
    mapping.map_field("", DiagnoseCombinatie.omschrijving)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), DiagnoseCombinatie.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), DiagnoseCombinatie.einddatum)
    mapping.map_field("indicatie", DiagnoseCombinatie.indicatie)  # todo: wat betekend dit veld?
    mapping.map_field("specialisme_code", DiagnoseCombinatie.specialisme_code)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.diagnose_combinatie_hstage mx where mx.diagnose_dbc1 = hstg.diagnose_dbc1 and mx.diagnose_dbc2 = hstg.diagnose_dbc2)'
    mappings.append(mapping)

    # Beschikbare velden AFSLUITREGELS_HSTAGE:
    # afsluitregelcode, afsluitregelomschrijving, groepnummer, specialismecode, componenttype, componentcode, ingangsdatum, einddatum, mutatie,
    mapping = SorToValueSetMapping('afsluitregels_hstage', AfsluitRegel)
    mapping.map_field("afsluitregelcode", AfsluitRegel.code)
    mapping.map_field("afsluitregelomschrijving", AfsluitRegel.omschrijving)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), AfsluitRegel.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), AfsluitRegel.einddatum)
    mapping.map_field("specialismecode", AfsluitRegel.specialisme_code)
    mapping.map_field("componenttype", AfsluitRegel.component_types)
    mapping.map_field("componentcode", AfsluitRegel.component_code)
    mapping.map_field("groepnummer", AfsluitRegel.groepsnummer)
    # mappings.append(mapping)

    # Beschikbare velden AFSLUITREDEN_HSTAGE:
    # afsluitreden_code, afsluitreden_omschrijving, korte_omschrijving, ingangsdatum, einddatum, mutatie,
    mapping = SorToValueSetMapping('afsluitreden_hstage', AfsluitReden)
    mapping.map_field("afsluitreden_code", AfsluitReden.code)
    mapping.map_field("afsluitreden_omschrijving", AfsluitReden.omschrijving)
    mapping.map_field("korte_omschrijving", AfsluitReden.omschrijving_kort)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), AfsluitReden.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), AfsluitReden.einddatum)
    # mapping.filter = 'ingangsdatum = (select max(ingangsdatum) from sor_dbc.afsluitreden_hstage mx where mx.afsluitreden_code = hstg.afsluitreden_code)'
    mappings.append(mapping)

    """as_code, as_omschrijving, component_code, component_omschrijving_kort,
       component_omschrijving_lang, subgroep_code, subgroep_omschrijving_kort,
       subgroep_omschrijving_lang, hoofdgroep_code, hoofdgroep_omschrijving_kort,
       hoofdgroep_omschrijving_lang, ingangsdatum, afloopdatum, mutatie_reden,
       vervangende_component_code, mutatie_toelichting, behandelsetting,
       automatisch_verlengen_toegestaan, mutatie"""

    mapping = SorToValueSetMapping('typeringslijst_hstage', Zorgtype)
    mapping.map_field("specialisme_code_agb||'-'||component_code", Zorgtype.code)
    mapping.map_field("specialisme_code_agb", Zorgtype.specialisme_code)
    mapping.map_field("component_code", Zorgtype.zorgtype_code)
    mapping.map_field("component_omschrijving_kort", Zorgtype.omschrijving)
    mapping.map_field("component_omschrijving_lang", Zorgtype.omschrijving_lang)
    mapping.map_field("hoofdgroep_code", Zorgtype.hoofdgroep_code)
    mapping.map_field("hoofdgroep_omschrijving_kort", Zorgtype.hoofdgroep_omschrijving_kort)
    mapping.map_field("hoofdgroep_omschrijving_lang", Zorgtype.hoofdgroep_omschrijving_lang)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgtype.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("afloopdatum"), Zorgtype.einddatum)
    mapping.filter = "as_code = '1'"
    mappings.append(mapping)

    mapping = SorToValueSetMapping('typeringslijst_hstage', Zorgvraag)
    mapping.map_field("specialisme_code_agb||'-'||component_code", Zorgvraag.code)
    mapping.map_field("specialisme_code_agb", Zorgvraag.specialisme_code)
    mapping.map_field("component_code", Zorgvraag.zorgvraag_code)
    mapping.map_field("component_omschrijving_kort", Zorgvraag.omschrijving)
    mapping.map_field("component_omschrijving_lang", Zorgvraag.omschrijving_lang)
    mapping.map_field("hoofdgroep_code", Zorgvraag.hoofdgroep_code)
    mapping.map_field("hoofdgroep_omschrijving_kort", Zorgvraag.hoofdgroep_omschrijving_kort)
    mapping.map_field("hoofdgroep_omschrijving_lang", Zorgvraag.hoofdgroep_omschrijving_lang)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgvraag.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("afloopdatum"), Zorgvraag.einddatum)
    mapping.filter = "as_code = '2'"
    mappings.append(mapping)

    mapping = SorToValueSetMapping('typeringslijst_hstage', Diagnose)
    mapping.map_field("specialisme_code_agb||'-'||component_code", Diagnose.code)
    mapping.map_field("lpad(specialisme_code_agb, 4, '0')", Diagnose.specialisme_code)
    mapping.map_field("lpad(component_code, 4, '0')", Diagnose.diagnose_code)
    mapping.map_field("component_omschrijving_kort", Diagnose.omschrijving)
    mapping.map_field("component_omschrijving_lang", Diagnose.omschrijving_lang)
    mapping.map_field("subgroep_code", Diagnose.subgroep_code)
    mapping.map_field("subgroep_omschrijving_kort", Diagnose.subgroep_omschrijving_kort)
    mapping.map_field("subgroep_omschrijving_lang", Diagnose.subgroep_omschrijving_lang)
    mapping.map_field("hoofdgroep_code", Diagnose.hoofdgroep_code)
    mapping.map_field("hoofdgroep_omschrijving_kort", Diagnose.hoofdgroep_omschrijving_kort)
    mapping.map_field("hoofdgroep_omschrijving_lang", Diagnose.hoofdgroep_omschrijving_lang)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Diagnose.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("afloopdatum"), Diagnose.einddatum)
    mapping.filter = "as_code = '3'"
    mappings.append(mapping)

    mapping = SorToValueSetMapping('typeringslijst_hstage', Behandeling)
    mapping.map_field("specialisme_code_agb||'-'||component_code", Behandeling.code)
    mapping.map_field("specialisme_code_agb", Behandeling.specialisme_code)
    mapping.map_field("component_code", Behandeling.behandeling_code)
    mapping.map_field("component_omschrijving_kort", Behandeling.omschrijving)
    mapping.map_field("component_omschrijving_lang", Behandeling.omschrijving_lang)
    mapping.map_field("subgroep_code", Behandeling.subgroep_code)
    mapping.map_field("subgroep_omschrijving_kort", Behandeling.subgroep_omschrijving_kort)
    mapping.map_field("subgroep_omschrijving_lang", Behandeling.subgroep_omschrijving_lang)
    mapping.map_field("hoofdgroep_code", Behandeling.hoofdgroep_code)
    mapping.map_field("hoofdgroep_omschrijving_kort", Behandeling.hoofdgroep_omschrijving_kort)
    mapping.map_field("hoofdgroep_omschrijving_lang", Behandeling.hoofdgroep_omschrijving_lang)
    mapping.map_field("vervangende_component_code", Behandeling.vervangende_component_code)
    mapping.map_field("behandelsetting", Behandeling.behandeling_setting_code)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Behandeling.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("afloopdatum"), Behandeling.einddatum)
    mapping.filter = "as_code = '4'"
    mappings.append(mapping)


    return mappings
