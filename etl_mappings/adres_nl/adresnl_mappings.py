from domainmodels.entity_domain import AdresNL

from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile
# from etl_mappings.adres_nl._adresnl_unzip import PostcodesNL


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []

    ###############################
    # adresnl
    ###############################
    data_path = pipe.config['data_path']
    adresnl_file = pipe.config['adresnl_file']
    source_file = CsvFile(data_path + adresnl_file, delimiter=';')
    source_file.reflect()
    source_file.set_primary_key(['wijkcode', 'lettercombinatie', 'huisnr', 'huisnr_bag_letter', 'huisnr_bag_toevoeging'])

    sor_mapping = SourceToSorMapping(source_file, 'adresnl_hstage', auto_map=True)
    mappings.append(sor_mapping)
    # source_file = CsvFile(data_path + 'pcdata_output2.csv', delimiter=';')  #deel adresnlbestand
    # source_file = CsvFile(data_path + 'adresnl_voorpostbussentesten.csv', delimiter=';')  #deel adresnlbestand bevat ook postbussen om te testen
    # source_file = CsvFile(data_path + 'adresnl_1000.csv', delimiter=';')  # deel adresnlbestand
      # compleetadresnlbestand
    # source_file = CsvFile(data_path + '/adresnl_update_20160801-20160905.csv', delimiter=';')  #  update van adresnlbestand
    # source_file = CsvFile(data_path + '{}'.format(pcnl.csv_name), delimiter=';')  #  update van adresnlbestand



    ###############################
    # cbsbuurten
    ###############################
    cbs_buurten_file = pipe.config['cbs_buurten_file']
    source_file = CsvFile(data_path + cbs_buurten_file, delimiter=';')  # compleet adresbestand ,geen empty lines aan eind document
    source_file.reflect()
    source_file.set_primary_key(['POSTCODE', 'HUISNUMMER'])
    sor_mapping = SourceToSorMapping(source_file, 'cbsbuurten_hstage', auto_map=True)
    mappings.append(sor_mapping)
    # source_file = CsvFile(data_path + '/cbs_buurten_compleet.txt', delimiter=';') # compleetadresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_tm1011DD.txt', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_encodingtest.txt', encoding='Latin-1', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_utf8.txt', delimiter=';')  # deel adresnlbestand
    # source_file = CsvFile(data_path + '/cbs_buurten_compleet_utf8m.txt', delimiter=';')  # compleet adresbestand ,geen empty lines aan eind document










    return mappings


def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor

    ###############################
    # adresnl
    ###############################




    #####

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

#     mapping.map_field('update_type', AdresNL.ExtraInfo.status_temp)
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


    adresnl_filter = "update_type = 'update'"


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

#     mapping.map_field('update_type', AdresNL.ExtraInfo.update_type)
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

    # downdate data waarvan de bijhorende update ervoor zorgt dat de bk van dat adres is verandert (bv verandering in huisnr_bag_letter)
    # adresnl_filter = "update_type = 'delete'"

    adresnl_filter = """ exists (select r.wijkcode, r.lettercombinatie, r.huisnr, r.huisnr_bag_letter, r.huisnr_bag_toevoeging, r.bag_nummeraandingid, r.bag_adresseerbaarobjectid, count(*)
                        from sor_adresnl.adresnl_hstage  as r
                        where (r.update_type = 'downdate' or r.update_type = 'update')
                        and hstg.bag_nummeraandingid = r.bag_nummeraandingid
                        group  by r.wijkcode, r.lettercombinatie, r.huisnr, r.huisnr_bag_letter, r.huisnr_bag_toevoeging, r.bag_nummeraandingid, r.bag_adresseerbaarobjectid
                        having count(*) = 1
                        ) and hstg.update_type = 'downdate'"""
    mapping = SorToEntityMapping('adresnl_hstage', AdresNL, sor, filter=adresnl_filter)
    mapping.map_bk(["""wijkcode||lettercombinatie|| '.'||
                            (CASE WHEN straatnaam = 'Postbus' then huisnr_van ||'tm' || huisnr_tm  ELSE huisnr END)||
                            (CASE WHEN huisnr_bag_letter IS NOT NULL THEN '-' || huisnr_bag_letter ELSE '' END)
                            || (CASE WHEN huisnr_bag_toevoeging IS NOT NULL THEN '-' || huisnr_bag_toevoeging
                            ELSE '' END)"""])

    mapping.map_field('bag_nummeraandingid', AdresNL.Deleted.bag_nummeraanduiding_del)
    mapping.map_field('bag_adresseerbaarobjectid', AdresNL.Deleted.bag_adresseerobject_del)
    mapping.map_field('update_type', AdresNL.Deleted.update_type_del)

    mappings.append(mapping)

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
    mapping.map_field('update_type', AdresNL.Deleted.update_type_del)

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
