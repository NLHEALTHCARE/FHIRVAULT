# from domainmodel_hl7_rim.entity_domain import AdresNL
from domainmodel.valueset_domain import Buurt, Gemeente
from mappings.cbs.cbs_gebieden_prepare import prepare_cbs_data
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
    # test om fout te genereren
    ###############################



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
    cbs_gebieden_file = pipe.config['cbs_gebieden_file']
    prepared_file = cbs_gebieden_file.lower().replace('cbs', 'prepared')
    if cbs_gebieden_file:
        # prepared_file = 'prepared_gebieden_in_nederland.csv'
        # prepare_cbs_data(path=pipe.config['data_path'], from_file=cbs_gebieden_file, to_file=prepared_file)
        source_file = CsvFile(data_path + prepared_file, delimiter=';')
        source_file.reflect()
        source_file.set_primary_key(['code'])
        sor_mapping = SourceToSorMapping(source_file, 'cbsgemeenten_hstage', auto_map=True)
        mappings.append(sor_mapping)
    return mappings

def init_sor_to_valset_mappings(pipe):
    mappings = []
    #postcode, huisnummer, gemeenteco, gemeentena, wijkcode, wijknaam, buurtcode, buurtmnaam
    sor_sql = """SELECT DISTINCT _valid, _active, _runid, LEFT(postcode, 4) as pc4, gemeenteco, gemeentena, wijkcode, wijknaam, buurtcode, buurtmnaam
    FROM sor_cbs.cbsbuurten_hstage WHERE _valid AND _active
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
    mappings.append(mapping)


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

