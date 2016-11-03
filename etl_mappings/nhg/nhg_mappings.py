import os
import glob

from domainmodels.role_domain import *
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile, File
from etl_mappings.nhg.nhg_fileparser import parse_txt, parse_key, parse_name

__author__ = 'cmesu'


def init_source_to_sor_mappings(path):
    mappings = []
    os.chdir(path)
    for textfile in glob.glob('*.txt'):
        decoded_file = parse_txt(path + textfile, skiplines=1, delimiter='\t', encoding='utf_16')
        source_file = CsvFile(decoded_file, delimiter=';', encoding='utf8')
        source_file.set_primary_key(parse_key(source_file))
        target_tbl = parse_name(source_file)
        sor_mapping = SourceToSorMapping(source_file, target_tbl, auto_map=True)
        mappings.append(sor_mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    return mappings


