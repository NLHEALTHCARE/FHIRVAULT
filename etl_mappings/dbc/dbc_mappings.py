from domainmodel.identity_domain import Zorgverlener
from etl_mappings.dbc.dbc_transformations import DbcTransformations
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToValueSetMapping
from domainmodel.valueset_domain import *
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(pipe):
    mappings = []
    path = pipe.config['data_path']

    source_file = CsvFile('{}{}'.format(path, 'Zorgproductgroepen Tabel v20150701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['zorgproductgroep_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgproductgroepen_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, 'Zorgactiviteiten Tabel v20151119.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['zorgactiviteit_code', 'ingangsdatum'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgactiviteiten_hstage', auto_map=True)
    mappings.append(sor_mapping)

    # todo[jan] Controle of key klopt
    source_file = CsvFile('{}{}'.format(path, 'Tarieven Tabel v20151119.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(
        ['agb_specialisme', 'agb_uitvoerder', 'productgroepcode', 'declaratiecode', 'kostensoort', 'tarieftype', 'declaratie_eenheid', 'soort_tarief', 'segment_aanduiding', 'soort_honorarium',
         'ingangsdatum', 'einddatum'])
    sor_mapping = SourceToSorMapping(source_file, 'tarieven_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, 'Diagnose Combinatie Tabel v20151119.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['specialisme_code', 'diagnose_dbc1', 'diagnose_dbc2', 'ingangsdatum', 'einddatum'])
    sor_mapping = SourceToSorMapping(source_file, 'diagnose_combinatie_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, 'Afsluitregels Tabel v20151119.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['afsluitregelcode', 'groepnummer', 'specialismecode', 'componentcode', 'ingangsdatum', 'einddatum'])
    sor_mapping = SourceToSorMapping(source_file, 'afsluitregels_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, 'Afsluitreden Tabel v20150701.csv'), delimiter=';', encoding='latin1')
    source_file.reflect()
    source_file.set_primary_key(['afsluitreden_code', 'ingangsdatum', 'einddatum'])
    sor_mapping = SourceToSorMapping(source_file, 'afsluitreden_hstage', auto_map=True)
    mappings.append(sor_mapping)

    return mappings

def init_sor_to_valset_mappings(pipe):
    mappings = []

    mapping = SorToValueSetMapping('zorgproductgroepen_hstage', Zorgproductgroep)
    mapping.map_field("zorgproductgroep_code", Zorgproductgroep.code)
    mapping.map_field("zorgproductgroep_omschrijving", Zorgproductgroep.omschrijving)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgproductgroep.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgproductgroep.einddatum)
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
    # mappings.append(mapping)

    # Beschikbare velden DIAGNOSE_COMBINATIE_HSTAGE:
    # specialisme_code, diagnose_dbc1, diagnose_dbc2, indicatie, ingangsdatum, einddatum, mutatie,
    mapping = SorToValueSetMapping('diagnose_combinatie_hstage', DiagnoseCombinatie)
    mapping.map_field("(specialisme_code || '-' || diagnose_dbc1 || '-' || diagnose_dbc2 || '-' || ingangsdatum)", DiagnoseCombinatie.code)
    mapping.map_field("diagnose_dbc1", DiagnoseCombinatie.dbc1)
    mapping.map_field("diagnose_dbc2", DiagnoseCombinatie.dbc2)
    mapping.map_field("", DiagnoseCombinatie.omschrijving)
    mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), DiagnoseCombinatie.ingangsdatum)
    mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), DiagnoseCombinatie.einddatum)
    mapping.map_field("indicatie", DiagnoseCombinatie.indicatie)  # todo: wat betekend dit veld?
    mapping.map_field("specialisme_code", DiagnoseCombinatie.specialisme_code)
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
    mappings.append(mapping)

    return  mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor
    return mappings
    #
    #
    #
    #
    # def init_sor_diagnose_combinatie_hstage_to_diagnosecombinatie_mappings(sor):
    #     mappings = []
    #
    #     # ###########################
    #     # Beschikbare velden DIAGNOSE_COMBINATIE_HSTAGE:
    #     # specialisme_code, diagnose_dbc1, diagnose_dbc2, indicatie, ingangsdatum, einddatum, mutatie,
    #
    #     mapping = SorToEntityMapping('diagnose_combinatie_hstage', DiagnoseCombinatie, sor)
    #     mapping.map_bk(['specialisme_code', 'diagnose_dbc1', 'diagnose_dbc2', 'ingangsdatum'])
    #
    #     #SAT DiagnoseCombinatie.Default
    #     mapping.map_field("diagnose_dbc1", DiagnoseCombinatie.Default.dbc1)
    #     mapping.map_field("diagnose_dbc2", DiagnoseCombinatie.Default.dbc2)
    #     mapping.map_field("", DiagnoseCombinatie.Default.omschrijving)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), DiagnoseCombinatie.Default.ingangsdatum)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), DiagnoseCombinatie.Default.einddatum)
    #     mapping.map_field("indicatie", DiagnoseCombinatie.Default.indicatie) #todo: wat betekend dit veld?
    #     mapping.map_field("specialisme_code", DiagnoseCombinatie.Default.specialisme_code)
    #     mappings.append(mapping)
    #     return mappings
    #
    # def init_sor_afsluitregels_hstage_to_afsluitregel_mappings(sor):
    #     mappings = []
    #
    #     # ###########################
    #     # Beschikbare velden AFSLUITREGELS_HSTAGE:
    #     # afsluitregelcode, afsluitregelomschrijving, groepnummer, specialismecode, componenttype, componentcode, ingangsdatum, einddatum, mutatie,
    #
    #     mapping = SorToEntityMapping('afsluitregels_hstage', AfsluitRegel, sor)
    #     mapping.map_bk([''])
    #
    #     #SAT AfsluitRegel.Default
    #     mapping.map_field("", AfsluitRegel.Default.code)
    #     mapping.map_field("", AfsluitRegel.Default.omschrijving)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), AfsluitRegel.Default.ingangsdatum)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), AfsluitRegel.Default.einddatum)
    #     mapping.map_field("", AfsluitRegel.Default.specialisme_code)
    #     mapping.map_field("", AfsluitRegel.Default.component_types)
    #     mapping.map_field("", AfsluitRegel.Default.component_code)
    #     mapping.map_field("", AfsluitRegel.Default.groepsnummer)
    #     mappings.append(mapping)
    #     return mappings
    #
    # def init_sor_afsluitreden_hstage_to_afsluitreden_mappings(sor):
    #     mappings = []
    #
    #     # ###########################
    #     # Beschikbare velden AFSLUITREDEN_HSTAGE:
    #     # afsluitreden_code, afsluitreden_omschrijving, korte_omschrijving, ingangsdatum, einddatum, mutatie,
    #
    #     mapping = SorToEntityMapping('afsluitreden_hstage', AfsluitReden, sor)
    #     mapping.map_bk([''])
    #
    #     #SAT AfsluitReden.Default
    #     mapping.map_field("", AfsluitReden.Default.code)
    #     mapping.map_field("", AfsluitReden.Default.omschrijving)
    #     mapping.map_field("", AfsluitReden.Default.omschrijving_kort)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), AfsluitReden.Default.ingangsdatum)
    #     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), AfsluitReden.Default.einddatum)
    #     mappings.append(mapping)
    #     return mappings

    # mappings.extend(init_sor_zorgproductgroepen_hstage_to_zorgproductgroep_mappings(sor))
    # mappings.extend(init_sor_zorgactiviteiten_hstage_to_zorgactiviteit_mappings(sor))
    # # mappings.extend(init_sor_tarieven_hstage_to_tarief_mappings(sor))
    # mappings.extend(init_sor_diagnose_combinatie_hstage_to_diagnosecombinatie_mappings(sor))
    # # mappings.extend(init_sor_afsluitregels_hstage_to_afsluitregel_mappings(sor))
    # # mappings.extend(init_sor_afsluitreden_hstage_to_afsluitreden_mappings(sor))
    # return mappings


# def init_sor_zorgproductgroepen_hstage_to_zorgproductgroep_mappings(sor):
#     mappings = []
#
#     mapping = SorToEntityMapping('zorgproductgroepen_hstage', Zorgproductgroep, sor)
#     mapping.map_bk(['zorgproductgroep_code'])
#
#     # SAT Zorgproductgroep.Default
#     mapping.map_field("zorgproductgroep_code", Zorgproductgroep.Default.code)
#     mapping.map_field("zorgproductgroep_omschrijving", Zorgproductgroep.Default.omschrijving)
#     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgproductgroep.Default.ingangsdatum)
#     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgproductgroep.Default.einddatum)
#     mappings.append(mapping)
#     return mappings

# def init_sor_zorgactiviteiten_hstage_to_zorgactiviteit_mappings(sor):
#     mappings = []
# 
#     # ###########################
#     # Beschikbare velden ZORGACTIVITEITEN_HSTAGE:
#     # zorgactiviteit_code, zorgactiviteit_omschrijving, op_nota, zorgactiviteit_consumenten_omschrijving, zpk_code, zpk_omschrijving, spmenr_01, spmenr_02, spmenr_03, spmenr_04,
#     # spmenr_05, spmenr_06, spmenr_07, spmenr_08, spmenr_10, spmenr_13, spmenr_16, spmenr_18, spmenr_20, spmenr_22,
#     # spmenr_24, spmenr_26, spmenr_27, spmenr_28, spmenr_29, spmenr_30, spmenr_35, spmenr_61, spmenr_62, spmenr_89,
#     # spmenr_90, wbmv_code, eenheid, aantal_eenheden, aanspraak_code, indicatie_addon, ingangsdatum, einddatum, mutatie,
# 
#     mapping = SorToEntityMapping('zorgactiviteiten_hstage', Zorgactiviteit, sor)
#     mapping.map_bk(['zorgactiviteit_code'])
# 
#     # SAT Zorgactiviteit.Default
#     mapping.map_field("zorgactiviteit_code", Zorgactiviteit.Default.code)
#     mapping.map_field("zorgactiviteit_omschrijving", Zorgactiviteit.Default.omschrijving)
#     mapping.map_field("zorgactiviteit_consumenten_omschrijving", Zorgactiviteit.Default.omschrijving_consument)
#     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Zorgactiviteit.Default.ingangsdatum)
#     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Zorgactiviteit.Default.einddatum)
# 
#     mapping.map_field("(CASE WHEN op_nota='J' THEN true ELSE false END)", Zorgactiviteit.Default.op_nota)
#     # field_list = ['zpk_code','zpk_omschrijving','spmenr_01','spmenr_02','spmenr_03','spmenr_04','spmenr_05','spmenr_06','spmenr_07','spmenr_08','spmenr_10','spmenr_13','spmenr_16','spmenr_18','spmenr_20','spmenr_22','spmenr_24','spmenr_26','spmenr_27','spmenr_28','spmenr_29','spmenr_30','spmenr_35','spmenr_61','spmenr_62','spmenr_89','spmenr_90']
#     # mapping.map_field(field_list, Zorgactiviteit.Default.extra)
#     mappings.append(mapping)
#     return mappings

# def init_sor_tarieven_hstage_to_tarief_mappings(sor):
#     mappings = []
#
#     # ###########################
#     # Beschikbare velden TARIEVEN_HSTAGE:
#     # agb_specialisme, agb_uitvoerder, declaratiecode, productgroepcode, tarief, kostensoort, ingangsdatum, einddatum, omschrijving_declaratiecode, tarieftype,
#     # declaratie_eenheid, soort_tarief, segment_aanduiding, soort_honorarium, mutatie_toelichting, declaratie_regel, mutatie,
#
#     mapping = SorToEntityMapping('tarieven_hstage', Tarief, sor)
#     mapping.map_bk(
#         ['agb_specialisme', 'agb_uitvoerder', 'productgroepcode', 'declaratiecode', 'kostensoort', 'tarieftype', 'declaratie_eenheid', 'soort_tarief', 'segment_aanduiding', 'soort_honorarium',
#          'ingangsdatum', 'einddatum'])
#
#     # SAT Tarief.Default
#     mapping.map_field("", Tarief.Default.code)
#     mapping.map_field("", Tarief.Default.omschrijving)
#     mapping.map_field("", Tarief.Default.declaratiecode)
#     mapping.map_field("", Tarief.Default.omschrijving_declaratiecode)
#     mapping.map_field(DbcTransformations.text_to_date_transform("ingangsdatum"), Tarief.Default.ingangsdatum)
#     mapping.map_field(DbcTransformations.text_to_date_transform("einddatum"), Tarief.Default.einddatum)
#     mapping.map_field("", Tarief.Default.specialisme_code)
#     mapping.map_field("", Tarief.Default.agb_uitvoerder)
#     mapping.map_field("", Tarief.Default.productgroepcode)
#     mapping.map_field("::numeric", Tarief.Default.tarief)
#     mapping.map_field("", Tarief.Default.kostensoort)
#     mapping.map_field("", Tarief.Default.tarieftype)
#     mapping.map_field("", Tarief.Default.declaratie_eenheid)
#     mapping.map_field("", Tarief.Default.tariefsoort)
#     mapping.map_field("", Tarief.Default.segment_aanduiding)
#     mapping.map_field("", Tarief.Default.honorarium_soort)
#     mapping.map_field("", Tarief.Default.declaratie_regel)
#     mappings.append(mapping)
#     return mappings
