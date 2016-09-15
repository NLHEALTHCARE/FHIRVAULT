import csv

from pyelt.sources.files import CsvFile

from pipelines.general_clinical_configs import vektis_uzovi_config


def convert_source_file_concerns(data_path):
    source_file = CsvFile(data_path + '/20160419_UZOVI_concerns.csv', delimiter=';', encoding='LATIN1')

    file_name = data_path + '/20160419_UZOVI_concerns.csv'
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        fields = next(reader, None)
        idx = 0
        start_concerns, end_concerns = 0, 0
        start_ic_concerns, end_ic_concerns = 0, 0

        for field in fields:
            if field == 'Concern':
                start_concerns = idx
            elif field == 'Inkoopconcern':
                end_concerns = idx - 1
                start_ic_concerns = idx
            idx += 1
        end_ic_concerns = idx

        #############################
        # volgende regel
        fields = next(reader, None)
        concerns = []
        for field in fields[start_concerns: end_concerns]:
            concern = {'naam': field, 'uzovis': []}
            concerns.append(concern)
        ic_concerns = []
        for field in fields[start_ic_concerns: end_ic_concerns]:
            ic_concerns.append(field)
        print(concerns)

        print(ic_concerns)

        ##############################
        fields = next(reader, None)
        while fields:
            uzovi = fields[0]
            naam = fields[1]
            rol = fields[2]
            idx = 0
            for col in fields[start_concerns: end_concerns]:
                if col == 'x':
                    concerns[idx]['uzovis'].append(uzovi)
                idx += 1

            idx = 0
            for col in fields[start_concerns: end_concerns]:
                if col == 'x':
                    concerns[idx]['uzovis'].append(uzovi)
                idx += 1

            fields = next(reader, None)
        print(concerns)


convert_source_file_concerns(vektis_uzovi_config['data_path'])
