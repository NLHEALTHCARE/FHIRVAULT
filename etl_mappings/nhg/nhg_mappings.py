import os
import re

from domainmodels.role_domain import *
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile, File
from nhg_fileparser import *


__author__ = 'cmesu'


def init_source_to_sor_mappings(path):
    mappings = []
    decoded_file = parse_txt(path + 'NHG-Tabel 2-Proef-versie-14-koppeltabel.txt', skiplines=1, delimiter='\t', encoding='utf16')
    source_file = CsvFile(decoded_file, delimiter=';', encoding='utf8')
    source_file.set_primary_key(parse_key(source_file))
    target_tbl=parse_name(source_file)
    sor_mapping = SourceToSorMapping(source_file, target_tbl, auto_map=True)
    mappings.append(sor_mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    return mappings


