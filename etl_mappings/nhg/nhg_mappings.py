from domainmodels.role_domain import *
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile

__author__ = 'cmesu'


def init_source_to_sor_mappings(path):
    mappings = []
    source_file = CsvFile(path + 'NHG-Tabel 2-Proef.txt', delimiter='\t', encoding='utf8')
    source_file.set_primary_key(['Code'])
    sor_mapping = SourceToSorMapping(source_file, 'nhg2_proef_hstage', auto_map=True)
    mappings.append(sor_mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    return mappings

