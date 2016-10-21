import csv
import glob
import io
import os
import time
import zipfile

from pyelt.pipeline import Pipeline

import domainmodels
from etl_mappings.vektis_agb.vektis_agb_importdef import vektis_import_def
from etl_mappings.vektis_agb.vektis_agb_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings

__author__ = 'hvreenen'


def define_vektis_agb_pipe(pipeline, vektis_agb_config):
    pipe = pipeline.get_or_create_pipe('vektis_agb', vektis_agb_config)
    pipe.register_domain(domainmodels.role_domain)
    #
    source_to_sor_mappings = init_source_to_sor_mappings(vektis_agb_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)
    #
    sor_to_ref_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_ref_mappings)
    #
    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def vektis_main(*args):
    print('running vektis_agb through general_clinical_configs.py')
    from pipelines.general_clinical_configs import general_config, vektis_agb_config
    start = time.time()
    if vektis_agb_config['convert_vektis_zips_to_csv']:
            convert_vektis_zips_to_csv(vektis_agb_config)
    else:
        print(" vektis zips to csv converter inactief")
    pipeline = Pipeline(general_config)
    define_vektis_agb_pipe(pipeline, vektis_agb_config)
    pipeline.run()


def convert_vektis_zips_to_csv(vektis_agb_config):
    path = vektis_agb_config['data_path']
    """convert zip files met fixed length naar losse csv-files"""
    print(" vektis zips to csv converter actief")

    fixed_length_file_defs = vektis_import_def

    os.chdir(path)
    for zip_file_name in glob.glob("*.zip"):
        with zipfile.ZipFile(zip_file_name, 'r') as archive:
            file_names = archive.namelist()

            file_name_list = []
            for file_name in file_names:
                if '__MACOSX' in file_name: continue
                try:
                    raw_file = archive.open(file_name, 'r')
                    binary_str = raw_file.read()
                    if not binary_str: continue

                    def_name = file_name.split('.')[0]
                    if not def_name in fixed_length_file_defs: continue
                    import_def = fixed_length_file_defs[def_name]
                    file_wrapper = io.TextIOWrapper(io.BytesIO(binary_str))
                    csv_file = open(path + file_name + '.csv', 'w')
                    file_name_list.append(file_name)
                    data_list = []
                    csv_column_names = []

                    fixed_length_indices = get_fixed_length_indices(csv_column_names, def_name, fixed_length_file_defs)

                    for line in file_wrapper:
                        # alternatief HJ
                        data_row = []
                        start_pos = 0
                        line = line.replace(";", "_")  # dit voorkomt een error wanneer een veld een ";" bevat in de de veldwaarde
                        for field_def in import_def:
                            field_name = field_def[0]
                            field_len = field_def[1]
                            end_pos = start_pos + field_len
                            data_row.append(line[start_pos:end_pos].strip())
                            start_pos = end_pos
                        # end alternatief
                        # for i in range(len(fixed_length_indices)):
                        #     if i == len(fixed_length_indices) - 1:
                        #         break
                        #     else:
                        #         data_row.append(line[fixed_length_indices[i]: fixed_length_indices[i+1]].strip())
                        data_list.append(data_row)

                    with open(path + file_name + '.csv', 'w', newline='', encoding='utf8') as fp:
                        csv_file = csv.writer(fp, delimiter=';')
                        csv_file.writerow(csv_column_names)
                        csv_file.writerows(data_list)

                        # source_file = FixedLengthFile(path + file_name, import_def)
                        # sor_mapping = SourceToSorMapping(source_file, def_name + '_hstage', auto_map=True)
                        # mappings.append(sor_mapping)

                finally:
                    pass


                    # for name, file_def in fixed_length_file_defs.items():
                    #     file_name = pipe.source_layer.path + name + '.s01'
                    #     raw_file = open(file_name, 'r')
                    #     binary_str = raw_file.read()
                    #     if not binary_str: continue
                    #     # file_wrapper = io.TextIOWrapper(io.BytesIO(binary_str))
                    #     file = FixedLengthSourceFile(name, file_name, file_def)
                    #     file.load()
                    #     pipe.source_layer.files[name] = file


def get_fixed_length_indices(csv_column_names, def_name, fixed_length_file_defs):
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


if __name__ == '__main__':
    vektis_main()

# for filename, file in pipe.source_layer.files.items():
#     for row in file.rows:
#         print(row)
