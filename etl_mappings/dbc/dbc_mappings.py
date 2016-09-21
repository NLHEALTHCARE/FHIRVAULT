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


def init_sor_to_dv_mappings():
    mappings = []

    return mappings
