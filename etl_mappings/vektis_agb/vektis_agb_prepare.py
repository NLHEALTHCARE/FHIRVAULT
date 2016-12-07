import csv
import glob
import os
import zipfile
import io

from etl_mappings.vektis_agb.vektis_agb_importdef import vektis_import_def

def download_and_replace_zips(path):
    pass
    #todo: automatisch download vanaf vektis site. Hoe moet dat met login?
    # op 2016-12-06 gelden de volgende urls
    # https://www.zorgprisma.nl/Cognos/docs/032_AGB/FAGBX_759_VQI!.zip
    # https://www.zorgprisma.nl/Cognos/docs/032_AGB/FAGBX_All_P!Q0.zip

def convert_vektis_zips_to_csv(path):
    """convert alle zip files in path met fixed length naar losse csv-files.

    zip-files (FAGBX_759 en FAGBX_All) zijn te vinden op www.zorgprisma.nl
    """

    fixed_length_file_defs = vektis_import_def
    os.chdir(path)
    for zip_file_name in (glob.glob('*.zip') or glob.glob('*.ZIP')):
        with zipfile.ZipFile(zip_file_name, 'r') as archive:
            file_names = archive.namelist()

            file_name_list = []
            for file_name in file_names:
                if '__MACOSX' in file_name:
                    continue
                try:
                    raw_file = archive.open(file_name, 'r')
                    binary_str = raw_file.read()
                    if not binary_str:
                        continue
                    if file_name.endswith('A-en.csv'):
                        #alleen ABbestanden meenemen
                        #AB bestanden hebben alle wijzigingen; A bestanden alleen laatste versies, zie vektis doc
                        continue
                    def_name = file_name.split('.')[0].replace('-en', '')
                    if not def_name in fixed_length_file_defs:
                        continue
                    import_def = fixed_length_file_defs[def_name]
                    file_wrapper = io.TextIOWrapper(io.BytesIO(binary_str), encoding='utf8')
                    file_name_list.append(file_name)
                    data_list = []
                    csv_column_names = []
                    i = 0
                    for line in file_wrapper:
                        try:
                            data_row = []
                            start_pos = 0
                            line = line.replace(";", ":").replace("|", ":")  # dit voorkomt een error wanneer een veld een ";" bevat in de de veldwaarde
                            for field_def in import_def:
                                field_name = field_def[0]
                                if len(csv_column_names) < len(import_def):
                                    csv_column_names.append(field_name)
                                field_len = field_def[1]
                                end_pos = start_pos + field_len
                                data_row.append(line[start_pos:end_pos].strip())
                                start_pos = end_pos
                            data_list.append(data_row)
                        except Exception as ex:
                            print(i)
                        i += 1

                    with open(path + def_name + '.csv', 'w', newline='', encoding='utf8') as fp:
                        csv_file = csv.writer(fp, delimiter=';')
                        csv_file.writerow(csv_column_names)
                        #eerste rij bevat alleen file info, geen data
                        del data_list[0]
                        csv_file.writerows(data_list)
                finally:
                    pass

def get_fixed_length_indices(csv_column_names, def_name, fixed_length_file_defs):
    """haal uit de dict met file_defs (vektis_import_def) de list met betreffende vaste velden posities. Deze posities geven aan waar een veld begint."""
    for key in fixed_length_file_defs:
        if key == def_name:
            fixed_lengths = [0]
            for i in range(len(fixed_length_file_defs[key])):
                fixed_lengths.append(fixed_length_file_defs[key][i][1])
                csv_column_names.append(fixed_length_file_defs[key][i][0])

            fixed_length_indices = [fixed_lengths[0]]
            for i in range(len(fixed_lengths)):
                if i == len(fixed_lengths) - 1:
                    break
                else:
                    temp = fixed_length_indices[i] + fixed_lengths[(i + 1)]
                    fixed_length_indices.append(temp)
    return fixed_length_indices

# def convert_vektis_zips_to_csv_old(path):
#     # path = vektis_agb_config['data_path']
#     """convert zip files met fixed length naar losse csv-files"""
#     print(" vektis zips to csv converter actief") ##
#     fixed_length_file_defs = vektis_import_def
#     os.chdir(path)
#     for zip_file_name in (glob.glob('*.zip') or glob.glob('*.ZIP')):
#         with zipfile.ZipFile(zip_file_name, 'r') as archive:
#             file_names = archive.namelist()
#
#             file_name_list = []
#             for file_name in file_names:
#                 if '__MACOSX' in file_name:
#                     continue
#                 try:
#                     raw_file = archive.open(file_name, 'r')
#                     binary_str = raw_file.read()
#                     if not binary_str:
#                         continue
#
#                     def_name = file_name.split('.')[0]
#                     if not def_name in fixed_length_file_defs:
#                         continue
#                     import_def = fixed_length_file_defs[def_name]
#                     file_wrapper = io.TextIOWrapper(io.BytesIO(binary_str), encoding='cp1252')
#                     csv_file = open(path + file_name + '.csv', 'w', encoding='utf8')
#                     file_name_list.append(file_name)
#                     data_list = []
#                     csv_column_names = []
#                     fixed_length_indices = get_fixed_length_indices(csv_column_names, def_name, fixed_length_file_defs)
#                     for line in file_wrapper:
#                         # alternatief HJ
#                         data_row = []
#                         start_pos = 0
#                         line = line.replace(";", ":").replace("|", ":")  # dit voorkomt een error wanneer een veld een ";" bevat in de de veldwaarde
#                         for field_def in import_def:
#                             field_name = field_def[0]
#                             field_len = field_def[1]
#                             end_pos = start_pos + field_len
#                             data_row.append(line[start_pos:end_pos].strip())
#                             start_pos = end_pos
#                         # end alternatief
#                         # for i in range(len(fixed_length_indices)):
#                         #     if i == len(fixed_length_indices) - 1:
#                         #         break
#                         #     else:
#                         #         data_row.append(line[fixed_length_indices[i]: fixed_length_indices[i+1]].strip())
#                         data_list.append(data_row)
#
#                     with open(path + file_name + '.csv', 'w', newline='', encoding='utf8') as fp:
#                         csv_file = csv.writer(fp, delimiter=';')
#                         csv_file.writerow(csv_column_names)
#                         csv_file.writerows(data_list)
#
#                         # source_file = FixedLengthFile(path + file_name, import_def)
#                         # sor_mapping = SourceToSorMapping(source_file, def_name + '_hstage', auto_map=True)
#                         # mappings.append(sor_mapping)
#
#                 finally:
#                     pass
#
#
#                     # for name, file_def in fixed_length_file_defs.items():
#                     #     file_name = pipe.source_layer.path + name + '.s01'
#                     #     raw_file = open(file_name, 'r')
#                     #     binary_str = raw_file.read()
#                     #     if not binary_str: continue
#                     #     # file_wrapper = io.TextIOWrapper(io.BytesIO(binary_str))
#                     #     file = FixedLengthSourceFile(name, file_name, file_def)
#                     #     file.load()
#                     #     pipe.source_layer.files[name] = file
