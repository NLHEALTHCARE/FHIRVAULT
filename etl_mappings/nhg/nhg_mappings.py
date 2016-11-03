from domainmodels.role_domain import *
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile, File
import csv

__author__ = 'cmesu'


def convert_txt_csv(filename, **args):
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


def init_source_to_sor_mappings(path):
    mappings = []
    file = convert_txt_csv(path + 'NHG-Tabel 2-Proef.txt', skiplines=1, delimiter='\t', encoding='utf16')
    source_file = CsvFile(file, delimiter=';', encoding='utf8')
    source_file.set_primary_key(['Code'])
    sor_mapping = SourceToSorMapping(source_file, 'nhg2_proef_hstage', auto_map=True)
    mappings.append(sor_mapping)
    return mappings

def init_sor_to_dv_mappings(pipe):
    mappings = []
    return mappings


