
import os
import re

from domainmodels.role_domain import *
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile, File

__author__ = 'cmesu'


def parse_txt(filename, **args):
    delimiter = ';'
    encoding = 'utf8'
    skiplines = 0
    for k, v in args.items():
        if k == 'skiplines':
            skiplines = range(v)
        elif k == 'delimiter':
            delimiter = v
        elif k == 'encoding':
            encoding = v
    file_in = open(filename, 'r', encoding=encoding)
    file_in.close()
    file_in = open(file_in.name, 'r', encoding=file_in.encoding)
    file_out = open(file_in.name.replace(file_in.name[-4:], '.csv'), 'w', encoding='utf8')
    for _ in skiplines:
        next(file_in)
    for line in file_in:
        file_out.write(str(line.replace(delimiter, ';')))
    file_in.close()
    file_out.close()
    return file_out.name

def parse_key(source_file):
    source_file.reflect()
    key = []
    for col in source_file.columns:
        key.append(col.name)
    return key

def parse_name(source_file):
    name = os.path.splitext(source_file.name)[0]
    name = name.lower()
    name = name.split('-versie-')[0]+re.sub('[1234567890_]', '', name.split('-versie-')[1])
    name = name.replace('-tabel ', '').replace(' ', '_').replace('-', '_')
    name = name+'_hstage'
    return name


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


