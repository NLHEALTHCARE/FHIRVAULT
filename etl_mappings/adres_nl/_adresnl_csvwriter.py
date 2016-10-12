import csv
import os
from etl_mappings.adres_nl._adresnl_unzip import PostcodesNL
from pipelines.general_clinical_configs import adresnl_config

"""De oorspronkelijk database is ter download te verkrijgen op: https://retrieve.postcode.nl/retrieve.php?hash=fde151728040ad8cad2498583a8492f1 """
"""Doel: oorspronkelijke csv file van AdresNL bevat geen header-rij. In onderstaande code worden de juiste headers toegevoegd."""

pcnl = PostcodesNL()
"""verander hier de URL naar de nieuwste update:"""
pcnl.set_URL('https://retrieve.postcode.nl/retrieve.php?hash=63e7fad64879ff12bd87e18bfac71b2c') #todo: deze url verandert waarschijnlijk bij iedere nieuwe update. Moet waarschijnlijk dus handmatig aangepast gaan worden iedere keer.
pcnl.get_zip_name()
pcnl.unzip_file()
pcnl.get_zip_date()
pcnl.get_csv_name()

data_path = adresnl_config['data_path']
os.chdir(data_path)

""" headers voor een update bestand van postcode.nl; de update bevat een extra column met beschrijving van type update (delete, update, downdate, insert)"""
headers = ["update_type", "perceelid", "perceeltype", "huisnr", "huisnr_bag_letter", "huisnr_bag_toevoeging", "bag_nummeraandingid", "bag_adresseerbaarobjectid", "breedtegraad", "lengtegraad", "rdx",
           "rdy", "oppervlakte", "gebruiksdoel", "reeksid", "wijkcode", "lettercombinatie", "huisnr_van", "huisnr_tm", "reeksindicatie", "straatid", "straatnaam", "straatnaam_nen", "plaatsid",
           "plaatsnaam", "plaatsnaam_nen", "plaatscode", "gemeentecode", "gemeentenaam", "gemeentenaam_nen", "cebucocode", "provinciecode", "provincielevel", "provincienaam"]

"""code om (deel van) adresnl data in te lezen"""
with open('mut_pcdata.csv', newline='', encoding='utf-8') as f:

    r = csv.reader(f)
    data = []
    index = 0
    for line in r:

        if index > 0:
            # if 'downdate' not in line: # voorbeeld van mogelijkheid om te filteren op inhoud van iedere line-list
            data.append(line)
        index += 1
        # if index > 1000:
        #     break

"""schrijf naar nieuwe file; pas filenaam aan naar nieuw bron bestand:"""
with open('{}'.format(pcnl.csv_name), 'w', newline='', encoding='utf-8') as f:

    w = csv.writer(f, delimiter=';')
    w.writerow(headers)
    w.writerows(data)

print("done")



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""code om het aanvangsbestand van adresnl bestand (8 miljoen regels) in te lezen, dit is slechts eenmalig. Hierna wordt
 de database telkens aangepast met kleine update bestanden"""
# with open('pcdata.csv', newline='', encoding='utf-8') as f:
#     r = csv.reader(f) # default voor de delimiter is een ',' en dat geeft hier problemen
#     data = []
#     index = 0
#     for line in r:
#         #Vergeleken met het volledige adressenbestand staat in een update bestand afkomstig van postcode.nl een extra
#         # column met daarin update_types.
#         # aan het eerste bestand kan deze kolom worden toegevoegd met de onderstaande 2 regels code die het aantal kolommen
#         # vergelijkt tussen een bestand en het aantal headers, ontbreekt de update_type dan wordt de kolom dus
#         # alsnog gevuld met 'insert'.
#
#         if len(line) != len(headers):
#             line.insert(0, 'insert')
#
#         if index > 0:
#             data.append(line)
#
#         index +=1
#         # if index > 1000:
#         #     break
# """schrijf naar nieuwe file; pas filenaam aan naar nieuw bron bestand:"""
# with open('adresnl_compleet.csv', 'w', newline='', encoding='utf-8') as f:
#     w = csv.writer(f, delimiter=';')
#     w.writerow(headers)
#     w.writerows(data)
#
# print("done")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


