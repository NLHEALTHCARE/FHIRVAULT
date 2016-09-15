from domainmodels.role_domain import Zorgaanbieder
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(path):
    mappings = []
    source_file = CsvFile('{}{}'.format(path, 'hierarchie_ondernemingen_zorgaanbieders.csv'), delimiter=';', encoding='utf8')
    source_file.reflect()
    source_file.set_primary_key(['kvk_nummer', 'kvk_vestigingsnummer', 'agb_code'])
    sor_mapping = SourceToSorMapping(source_file, 'klinieken_hstage', auto_map=True)
    mappings.append(sor_mapping)
    return mappings


def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor
    mapping = SorToEntityMapping('klinieken_hstage', Zorgaanbieder, sor)
    mapping.filter = "timeff_code != ''"
    mapping.map_bk(['kvk_nummer', 'agb_code'])
    mapping.map_field("bv_naam", Zorgaanbieder.Default.naam)
    mapping.map_field("organisatie_soort", Zorgaanbieder.Default.organisatie_type)
    mapping.map_field("agb_code", Zorgaanbieder.Identificatie.agb_code)
    mapping.map_field("kvk_nummer", Zorgaanbieder.Identificatie.kvk_nummer)
    mapping.map_field("kvk_vestigingsnummer", Zorgaanbieder.Identificatie.kvk_vestigingsnummer)
    mapping.map_field("timeff_code", Zorgaanbieder.ExternalKeys.key, type=Zorgaanbieder.ExternalKeys.Types.timeff_code)
    mappings.append(mapping)

    # bv_naam;kvk_nummer;kvk_vestigingsnummer;parent_kvk_nummer;organisatie_soort;opmerking;platform;agb_code;bk_kliniek;kliniek_locaties;timeff_code;timeff_nrint


    return mappings
