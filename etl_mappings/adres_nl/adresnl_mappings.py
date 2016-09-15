from pyelt.mappings.base import ConstantValue
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile

from domainmodels.entity_domain import AdresNL
from pipelines.general_clinical_configs import adresnl_config


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []

    ###############################
    # adresnl
    ###############################
    data_path = adresnl_config['data_path']
    # source_file = CsvFile(data_path + 'pcdata_output2.csv', delimiter=';')  #deel adresnlbestand
    # source_file = CsvFile(data_path + 'adresnl_voorpostbussentesten.csv', delimiter=';')  #deel adresnlbestand bevat ook postbussen om te testen
    source_file = CsvFile(data_path + 'adresnl_1000b.csv', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/adresnl_compleet.csv', delimiter=';')  # compleetadresnlbestand
    # source_file = CsvFile(data_path + '/adresnl_update_augsep2016.csv', delimiter=';')  #  update van adresnlbestand

    source_file.reflect()
    source_file.set_primary_key(['wijkcode', 'lettercombinatie', 'huisnr', 'huisnr_bag_letter', 'huisnr_bag_toevoeging'])

    sor_mapping = SourceToSorMapping(source_file, 'adresnl_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ###############################
    # cbsbuurten
    ###############################

    data_path = adresnl_config['data_path']
    # source_file = CsvFile(data_path + '/cbs_buurten_compleet.txt', delimiter=';') # compleetadresnlbestand
    source_file = CsvFile(data_path + '/cbs_buurten_tm1011DD.txt', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_encodingtest.txt', encoding='Latin-1', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_utf8.txt', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_compleet_utf8m.txt', delimiter=';')  # compleet adresbestand ,geen empty lines aan eind document




    source_file.reflect()
    source_file.set_primary_key(['POSTCODE', 'HUISNUMMER'])
    sor_mapping = SourceToSorMapping(source_file, 'cbsbuurten_hstage', auto_map=True)
    if "update_field" not in sor_mapping.get_fields():
        sor_mapping.map_field(ConstantValue('insert'), 'update_field')

    mappings.append(sor_mapping)

    # validation = SorValidation(tbl='cbsbuurten_hstage', schema=pipe.sor)
    #
    # validation.msg = 'duplicate key error'
    # validation.set_check_for_duplicate_keys(['POSTCODE', 'HUISNUMMER'])
    # validations.append(validation)

    # return mappings, validations
    return mappings


def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor

    ###############################
    # adresnl
    ###############################


    #  mapping.map_field('provincienaam',AdresNL.Deleted.provincie_del)



    #####


    # deleted adresses:
    adresnl_filter = "update_type = 'delete'"
    mapping = SorToEntityMapping('adresnl_hstage', AdresNL, sor, filter=adresnl_filter)
    mapping.map_bk(["""wijkcode||lettercombinatie|| '.'||
                            (CASE WHEN straatnaam = 'Postbus' then huisnr_van ||'tm' || huisnr_tm  ELSE huisnr END)||
                            (CASE WHEN huisnr_bag_letter IS NOT NULL THEN '-' || huisnr_bag_letter ELSE '' END)
                            || (CASE WHEN huisnr_bag_toevoeging IS NOT NULL THEN '-' || huisnr_bag_toevoeging
                            ELSE '' END)"""])

    mapping.map_field('bag_nummeraandingid', AdresNL.Deleted.bag_nummeraanduiding_del)
    mapping.map_field('bag_adresseerbaarobjectid', AdresNL.Deleted.bag_adresseerobject_del)

    mappings.append(mapping)

    # new adresses:
    adresnl_filter = "update_type = 'insert'"

    mapping = SorToEntityMapping('adresnl_hstage', AdresNL, sor, filter=adresnl_filter)
    mapping.map_bk(["""wijkcode||lettercombinatie|| '.'||
                            (CASE WHEN straatnaam = 'Postbus' then huisnr_van ||'tm' || huisnr_tm  ELSE huisnr END)||
                            (CASE WHEN huisnr_bag_letter IS NOT NULL THEN '-' || huisnr_bag_letter ELSE '' END)
                            || (CASE WHEN huisnr_bag_toevoeging IS NOT NULL THEN '-' || huisnr_bag_toevoeging
                            ELSE '' END)"""])

    mapping.map_field('straatnaam', AdresNL.Default.straat)
    mapping.map_field('huisnr::integer', AdresNL.Default.huisnummer)
    mapping.map_field('huisnr_bag_letter', AdresNL.Default.huisnummerletter)
    mapping.map_field('huisnr_bag_toevoeging', AdresNL.Default.huisnummertoevoeging)
    # mapping.map_field('??',AdresNL.Default.aanduiding_bij_nummer_code)
    mapping.map_field('plaatsnaam', AdresNL.Default.woonplaats)
    mapping.map_field('gemeentenaam', AdresNL.Default.gemeente)
    # mapping.map_field('??',AdresNL.Default.land_code)
    mapping.map_field("(wijkcode||lettercombinatie)", AdresNL.Default.postcode)
    # mapping.map_field('??',AdresNL.Default.additionele_informatie)
    mapping.map_field('provincienaam', AdresNL.Default.provincie)

    mapping.map_field('perceeltype ', AdresNL.ExtraInfo.perceeltype)
    mapping.map_field('huisnr_bag_toevoeging', AdresNL.ExtraInfo.bag_huisnummertoevoeging)
    mapping.map_field('gebruiksdoel', AdresNL.ExtraInfo.gebruiksdoel)

    mapping.map_field('wijkcode', AdresNL.PostcodeDetails.wijkcode)
    mapping.map_field('lettercombinatie', AdresNL.PostcodeDetails.lettercombinatie)
    mapping.map_field('huisnr_van', AdresNL.PostcodeDetails.huisnr_van)
    mapping.map_field('huisnr_tm', AdresNL.PostcodeDetails.huisnr_tm)
    mapping.map_field('reeksindicatie', AdresNL.PostcodeDetails.reeksindicatie)

    mapping.map_field('breedtegraad', AdresNL.GeoInfo.breedtegraad)
    mapping.map_field('lengtegraad', AdresNL.GeoInfo.lengtegraad)
    mapping.map_field('rdx', AdresNL.GeoInfo.rdx)
    mapping.map_field('rdy', AdresNL.GeoInfo.rdy)
    mapping.map_field('oppervlakte', AdresNL.GeoInfo.oppervlakte)

    mapping.map_field('perceelid::integer', AdresNL.Identificatie.perceelid)
    mapping.map_field('bag_nummeraandingid', AdresNL.Identificatie.bag_nummeraandingid)

    mapping.map_field('bag_adresseerbaarobjectid', AdresNL.Identificatie.bag_adresseerbaarobjectid)
    mapping.map_field('reeksid', AdresNL.Identificatie.reeksid)
    mapping.map_field('plaatsid::integer', AdresNL.Identificatie.plaatsid)
    # mapping.map_field('gemeenteid::integer',AdresNL.Identificatie.gemeenteid)

    mapping.map_field('straatnaam_nen', AdresNL.Afkortingen.straat_nen)
    mapping.map_field('plaatsnaam_nen', AdresNL.Afkortingen.plaats_nen)
    mapping.map_field('gemeentenaam_nen', AdresNL.Afkortingen.gemeente_nen)
    mapping.map_field('gemeentecode::integer', AdresNL.Afkortingen.gemeentecode)
    mapping.map_field('cebucocode::integer', AdresNL.Afkortingen.cebucocode)
    mapping.map_field('provinciecode', AdresNL.Afkortingen.provinciecode)

    mappings.append(mapping)

    ###############################
    # cbsbuurten
    ###############################

    sor_sql = """SELECT adresnl.*, buurten.WIJKCODE as cbs_wijkcode, buurten.WIJKNAAM, buurten.BUURTCODE, buurten.BUURTMNAAM
        FROM sor_adresnl.adresnl_hstage AS adresnl JOIN sor_adresnl.cbsbuurten_hstage buurten ON (adresnl.wijkcode||lettercombinatie) = buurten.postcode AND adresnl.huisnr = buurten.huisnummer"""
    mapping = SorToEntityMapping(sor_sql, AdresNL, sor)
    mapping.map_field('WIJKCODE::integer', AdresNL.CBS_buurten.wijkcode)
    mapping.map_field('WIJKNAAM', AdresNL.CBS_buurten.wijknaam)
    mapping.map_field('BUURTCODE::integer', AdresNL.CBS_buurten.buurtcode)
    mapping.map_field('BUURTMNAAM', AdresNL.CBS_buurten.buurtnaam)
    mappings.append(mapping)
    return mappings
