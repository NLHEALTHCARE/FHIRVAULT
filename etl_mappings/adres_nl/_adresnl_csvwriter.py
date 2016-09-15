import csv
import os

from pipelines.general_clinical_configs import adresnl_config

"""De database is ter download te verkrijgen op: https://retrieve.postcode.nl/retrieve.php?hash=fde151728040ad8cad2498583a8492f1 """
"""Doel: oorspronkelijke csv file van AdresNL bevat geen header-rij. In onderstaande code worden de juiste headers toegevoegd."""

data_path = adresnl_config['data_path']
os.chdir(data_path)
# os.chdir("""c:/!OntwikkelDATA/AdresNL""")

"""headers voor het complete postcode.nl bestand (+ 8 miljoen regels)"""
# headers = ["perceelid", "perceeltype", "huisnr", "huisnr_bag_letter", "huisnr_bag_toevoeging", "bag_nummeraandingid", "bag_adresseerbaarobjectid", "breedtegraad", "lengtegraad", "rdx", "rdy","oppervlakte", "gebruiksdoel", "reeksid", "wijkcode", "lettercombinatie", "huisnr_van", "huisnr_tm", "reeksindicatie", "straatid", "straatnaam", "straatnaam_nen", "plaatsid", "plaatsnaam", "plaatsnaam_nen", "plaatscode", "gemeentecode", "gemeentenaam", "gemeentenaam_nen", "cebucocode", "provinciecode", "provincielevel", "provincienaam"]

""" headers voor een update bestand van postcode.nl; de update bevat een extra column met beschrijving van type update (delete, update, downdate, insert)"""
headers = ["update_type", "perceelid", "perceeltype", "huisnr", "huisnr_bag_letter", "huisnr_bag_toevoeging", "bag_nummeraandingid", "bag_adresseerbaarobjectid", "breedtegraad", "lengtegraad", "rdx",
           "rdy", "oppervlakte", "gebruiksdoel", "reeksid", "wijkcode", "lettercombinatie", "huisnr_van", "huisnr_tm", "reeksindicatie", "straatid", "straatnaam", "straatnaam_nen", "plaatsid",
           "plaatsnaam", "plaatsnaam_nen", "plaatscode", "gemeentecode", "gemeentenaam", "gemeentenaam_nen", "cebucocode", "provinciecode", "provincielevel", "provincienaam"]

"""code om deel van adresnl data in te lezen"""
# with open('pcdata.csv', newline='', encoding='utf-8') as f:
with open('mut_pcdata_augsep2016.csv', newline='', encoding='utf-8') as f:
    r = csv.reader(f)
    data = []
    index = 0
    for line in r:
        if index > 0:
            data.append(line)
        index += 1
        if index > 1000:
            break

"""code om volledig adresnl bestand in te lezen, pas file naam aan naar nieuw bronbestand"""
# with open('adresnl_1000.csv', newline='', encoding='utf-8') as f:
#     r = csv.reader(f, delimiter=';')
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
#             # templine = 'insert;' + line[0]
#             # line[0] = templine
#
#         if index > 0:
#             data.append(line)
#
#         index +=1
#         if index > 10:
#             break

# print(data[1])


# data.append(line)



"""schrijf naar nieuwe file; pas filenaam aan naar nieuw bron bestand:"""
with open('adresnl_1000b.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(headers)
    w.writerows(data)

print("done")
