"""prepare CBS gegevens"""
import csv


def prepare_cbs_data(path, from_file = 'Gebieden_in_Nederland_CBS.csv', to_file = 'prepared_gebieden_in_nederland.csv'):

    """    #BRON:     # http://statline.cbs.nl/

    Cbs download heeft 4 titel kolommen. Deze moeten worden samengevoegd"""
    file_name = '{}{}'.format(path, 'Gebieden_in_Nederland_CBS.csv')
    new_file_name = '{}{}'.format(path, 'prepared_gebieden_in_nederland.csv')
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        i = 0
        titles = {}
        content = []
        for row in reader:
            if i<= 4:
                titles[i] = row

            else:
                content.append(row)
            i += 1


        new_title_row = []
        for i in range(len(titles[1])):
            new_title = titles[1][i] + '_' + titles[2][i] + '_' + titles[3][i]
            if titles[2][i] == titles[3][i]:
                new_title = titles[1][i] + '_' + titles[2][i]
            new_title = titles[2][i] + '_' + titles[3][i]
            if titles[2][i] == titles[3][i]:
                new_title = titles[2][i]
            new_title = new_title.replace(' ', '_').lower()
            new_title = new_title.replace('(', '').replace(')', '').replace('-', '_').replace("'", '')
            new_title = new_title.replace('_van_gemeenten_', '_')
            if new_title in new_title_row:
                print('ERROR', new_title)
            new_title_row.append(new_title)

    #csv scrijven naar nieuw bestand
    with open(new_file_name, 'w', newline='', encoding='UTF-8') as new_file:
        writer = csv.writer(new_file, delimiter=';')
        #nieuwe titel aan content rijen toevoegen
        content.insert(0, new_title_row)
        #laatste rij is copyright info. Deze moet eraf
        content = content[:len(content)-1]
        writer.writerows(content)

if __name__ == '__main__':
    prepare_cbs_data('C:/!OntwikkelDATA/cbs/')
