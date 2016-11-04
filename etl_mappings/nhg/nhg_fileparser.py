import os
import re
from colorama import Fore, Back, Style

def parse_txt(filename, **args):
    delimiter = ';'
    skiplines = 0
    for k, v in args.items():
        if k == 'delimiter':
            delimiter = v
    for encoding in 'utf_16', 'utf_16_le', 'utf_16_be', 'utf_8_sig', 'utf-8', 'cp1250', 'cp1252':
        try:
            file_in = open(filename, 'r', encoding=encoding)
            next(file_in)
            break
        except:
            pass
    if file_in:
        file_out = open(file_in.name.replace(file_in.name[-4:], '.csv'), 'w', encoding='utf8')
        file_in.seek(0)
        header = next(file_in).lower()
        if 'nhg' in header:
            header = next(file_in).lower()
        header = str(re.sub('[1234567890-]', '', header).replace(delimiter, ';').replace(' ', '_'))
        file_out.write(header)
        for line in file_in:
            file_out.write(str(line.replace(';', ':').replace(delimiter, ';')))
        file_in.close()
        file_out.close()
        return file_out.name
    else:
        print(Fore.RED, 'Onbekende file-encoding: '+filename)
        return None

def parse_key(source_file):
    source_file.reflect()
    key = []
    for col in source_file.columns:
        for search in 'id', 'code', 'mnem', 'num', 'nr', 'memo', 'icpc':
            if search in col.name.lower():
                key.append(col.name)
                break
    return key

def parse_name(source_file):
    name = os.path.splitext(source_file.name)[0]
    name = name.lower()
    name = name.split('-versie-')[0]+re.sub('[1234567890_]', '', name.split('-versie-')[1])
    name = name.replace('-tabel ', '').replace(' ', '_').replace('-', '_')
    name = name+'_hstage'
    return name
