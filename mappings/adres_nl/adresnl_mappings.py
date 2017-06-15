# from domainmodel_hl7_rim.entity_domain import AdresNL
from domainmodel.valueset_domain import Buurt, Gemeente
from pyelt.datalayers.sor import SorQuery
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToValueSetMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile
# from etl_mappings.adres_nl._adresnl_unzip import PostcodesNL


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []

    data_path = pipe.config['data_path']

    ###############################
    # adresnl
    ###############################
    adresnl_file = pipe.config['adresnl_file']
    if adresnl_file:
        source_file = CsvFile(data_path + adresnl_file, delimiter=';')
        source_file.set_primary_key(['wijkcode', 'lettercombinatie', 'huisnr', 'huisnr_bag_letter', 'huisnr_bag_toevoeging'])
        sor_mapping = SourceToSorMapping(source_file, 'adresnl_hstage', auto_map=True)
        mappings.append(sor_mapping)

    ###############################
    # adresnl updates
    ###############################
    adresnl_file = pipe.config['adresnl_update_file']
    if adresnl_file:
        source_file = CsvFile(data_path + adresnl_file, delimiter=';')
        source_file.set_primary_key(
            ['update_type','wijkcode', 'lettercombinatie', 'huisnr', 'huisnr_bag_letter', 'huisnr_bag_toevoeging'])

        sor_mapping = SourceToSorMapping(source_file, 'adresnl_update_hstage', auto_map=True)
        mappings.append(sor_mapping)

    ###############################
    # cbsbuurten
    ###############################
    cbs_buurten_file = pipe.config['cbs_buurten_file']
    if cbs_buurten_file:
        source_file = CsvFile(data_path + cbs_buurten_file, delimiter=';')  # compleet adresbestand ,geen empty lines aan eind document
        source_file.set_primary_key(['POSTCODE', 'HUISNUMMER'])
        sor_mapping = SourceToSorMapping(source_file, 'cbsbuurten_hstage', auto_map=True)
        mappings.append(sor_mapping)

    ###############################
    # cbsregio's en gemeenten
    ###############################
    #BRON:     # http://statline.cbs.nl/
    #ZIE prepare voor prepareren van bestand
    cbs_gemeenten_file = pipe.config['cbs_gemeenten_file']
    if cbs_gemeenten_file:
        source_file = CsvFile(data_path + cbs_gemeenten_file, delimiter=';')
        source_file.reflect()
        source_file.set_primary_key(['code'])
        sor_mapping = SourceToSorMapping(source_file, 'cbsgemeenten_hstage', auto_map=True)
        mappings.append(sor_mapping)




    return mappings

def init_sor_to_valset_mappings(pipe):
    mappings = []
    #postcode, huisnummer, gemeenteco, gemeentena, wijkcode, wijknaam, buurtcode, buurtmnaam
    sor_sql = """SELECT DISTINCT _valid, _active, _runid, LEFT(postcode, 4) as pc4, gemeenteco, gemeentena, wijkcode, wijknaam, buurtcode, buurtmnaam
    FROM sor_adresnl.cbsbuurten_hstage WHERE _valid AND _active
    """
    sor_query = SorQuery(sor_sql, pipe.sor)
    mapping = SorToValueSetMapping(sor_query, Buurt, pipe.sor)
    # mapping.map_field("(postcode || '-' ||huisnummer) ", Buurt.code)
    # mapping.map_field("(buurtmnaam) as omschr", Buurt.omschrijving)
    # mapping.map_field("postcode", Buurt.postcode)
    # mapping.map_field("huisnummer", Buurt.huisnummer)
    mapping.map_field("pc4", Buurt.code)
    mapping.map_field("(buurtmnaam) as omschr", Buurt.omschrijving)
    mapping.map_field("gemeenteco", Buurt.gemeente_code)
    mapping.map_field("gemeentena", Buurt.gemeentenaam)
    mapping.map_field("wijkcode", Buurt.wijk_code)
    mapping.map_field("buurtcode", Buurt.buurt_code)
    mapping.map_field("buurtmnaam", Buurt.buurtnaam)
    # mappings.append(mapping)


    mapping = SorToValueSetMapping('cbsgemeenten_hstage', Gemeente, pipe.sor)
    mapping.map_field("REPLACE(code, 'GM', '')", Gemeente.code)
    mapping.map_field("naam", Gemeente.omschrijving)
    mapping.map_field("sortering_naam", Gemeente.sortering_naam)
    mapping.map_field("arbeidsmarktregios_code", Gemeente.arbeidsmarktregios_code)
    mapping.map_field("arbeidsmarktregios_naam", Gemeente.arbeidsmarktregios_naam)
    mapping.map_field("arrondissementen_rechtsgebieden_code", Gemeente.arrondissementen_rechtsgebieden_code)
    mapping.map_field("arrondissementen_rechtsgebieden_naam", Gemeente.arrondissementen_rechtsgebieden_naam)
    mapping.map_field("corop_gebieden_code", Gemeente.corop_gebieden_code)
    mapping.map_field("corop_gebieden_naam", Gemeente.corop_gebieden_naam)
    mapping.map_field("corop_subgebieden_code", Gemeente.corop_subgebieden_code)
    mapping.map_field("corop_subgebieden_naam", Gemeente.corop_subgebieden_naam)
    mapping.map_field("corop_plusgebieden_code", Gemeente.corop_plusgebieden_code)
    mapping.map_field("corop_plusgebieden_naam", Gemeente.corop_plusgebieden_naam)
    mapping.map_field("ggd_regios_code", Gemeente.ggd_regios_code)
    mapping.map_field("ggd_regios_naam", Gemeente.ggd_regios_naam)
    mapping.map_field("jeugdzorgregios_code", Gemeente.jeugdzorgregios_code)
    mapping.map_field("jeugdzorgregios_naam", Gemeente.jeugdzorgregios_naam)
    mapping.map_field("kamer_van_koophandel_code", Gemeente.kamer_van_koophandel_code)
    mapping.map_field("kamer_van_koophandel_naam", Gemeente.kamer_van_koophandel_naam)
    mapping.map_field("landbouwgebieden_code", Gemeente.landbouwgebieden_code)
    mapping.map_field("landbouwgebieden_naam", Gemeente.landbouwgebieden_naam)
    mapping.map_field("landbouwgebieden_groepen_code", Gemeente.landbouwgebieden_groepen_code)
    mapping.map_field("landbouwgebieden_groepen_naam", Gemeente.landbouwgebieden_groepen_naam)
    mapping.map_field("landsdelen_code", Gemeente.landsdelen_code)
    mapping.map_field("landsdelen_naam", Gemeente.landsdelen_naam)
    mapping.map_field("nuts1_gebieden_code", Gemeente.nuts1_gebieden_code)
    mapping.map_field("nuts1_gebieden_naam", Gemeente.nuts1_gebieden_naam)
    mapping.map_field("nuts2_gebieden_code", Gemeente.nuts2_gebieden_code)
    mapping.map_field("nuts2_gebieden_naam", Gemeente.nuts2_gebieden_naam)
    mapping.map_field("nuts3_gebieden_code", Gemeente.nuts3_gebieden_code)
    mapping.map_field("nuts3_gebieden_naam", Gemeente.nuts3_gebieden_naam)
    mapping.map_field("politie_regionale_eenheden_code", Gemeente.politie_regionale_eenheden_code)
    mapping.map_field("politie_regionale_eenheden_naam", Gemeente.politie_regionale_eenheden_naam)
    mapping.map_field("provincies_code", Gemeente.provincies_code)
    mapping.map_field("provincies_naam", Gemeente.provincies_naam)
    mapping.map_field("ressorten_rechtsgebieden_code", Gemeente.ressorten_rechtsgebieden_code)
    mapping.map_field("ressorten_rechtsgebieden_naam", Gemeente.ressorten_rechtsgebieden_naam)
    mapping.map_field("rpa_gebieden_code", Gemeente.rpa_gebieden_code)
    mapping.map_field("rpa_gebieden_naam", Gemeente.rpa_gebieden_naam)
    mapping.map_field("toeristengebieden_code", Gemeente.toeristengebieden_code)
    mapping.map_field("toeristengebieden_naam", Gemeente.toeristengebieden_naam)
    mapping.map_field("veiligheidsregios_code", Gemeente.veiligheidsregios_code)
    mapping.map_field("veiligheidsregios_naam", Gemeente.veiligheidsregios_naam)
    mapping.map_field("wgr_samenwerkingsgebieden_code", Gemeente.wgr_samenwerkingsgebieden_code)
    mapping.map_field("wgr_samenwerkingsgebieden_naam", Gemeente.wgr_samenwerkingsgebieden_naam)
    mapping.map_field("zorgkantoorregios_code", Gemeente.zorgkantoorregios_code)
    mapping.map_field("zorgkantoorregios_naam", Gemeente.zorgkantoorregios_naam)
    mapping.map_field("gemeentegrootte_code", Gemeente.gemeentegrootte_code)
    mapping.map_field("gemeentegrootte_omschrijving", Gemeente.gemeentegrootte_omschrijving)
    mapping.map_field("stedelijkheid_code", Gemeente.stedelijkheid_code)
    mapping.map_field("stedelijkheid_omschrijving", Gemeente.stedelijkheid_omschrijving)
    mapping.map_field("inwonertal", Gemeente.inwonertal)
    mapping.map_field("omgevingsadressendichtheid", Gemeente.omgevingsadressendichtheid)
    mappings.append(mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor
    return mappings

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

    # mapping.map_field('update_type', AdresNL.ExtraInfo.update_type)
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

     # mapping.map_field('bag_nummeraandingid', AdresNL.Deleted.bag_nummeraanduiding_del)
    # mapping.map_field('bag_adresseerbaarobjectid', AdresNL.Deleted.bag_adresseerbaarobject_del)
    mapping.map_field('update_type', AdresNL.RecordStatus.status)

    mappings.append(mapping)

    # deleted adresses:
    adresnl_filter = "update_type = 'delete'"
    mapping = SorToEntityMapping('adresnl_hstage', AdresNL, sor, filter=adresnl_filter)
    mapping.map_bk(["""wijkcode||lettercombinatie|| '.'||
                            (CASE WHEN straatnaam = 'Postbus' then huisnr_van ||'tm' || huisnr_tm  ELSE huisnr END)||
                            (CASE WHEN huisnr_bag_letter IS NOT NULL THEN '-' || huisnr_bag_letter ELSE '' END)
                            || (CASE WHEN huisnr_bag_toevoeging IS NOT NULL THEN '-' || huisnr_bag_toevoeging
                            ELSE '' END)"""])

    # mapping.map_field('bag_nummeraandingid', AdresNL.Deleted.bag_nummeraanduiding_del)
    # mapping.map_field('bag_adresseerbaarobjectid', AdresNL.Deleted.bag_adresseerbaarobject_del)
    mapping.map_field('update_type', AdresNL.RecordStatus.status)

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
