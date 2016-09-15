import os

from dbfread import DBF

""" gedownload van: https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/gemeente/herindelingen-en-grenswijzigingen via
de link onderaan de pagina waar de Bronnen vermeld staan inclusief de "relatietabel postcode huisnummer buurt wijk gemeente
2015. download verwijst naar: https://www.cbs.nl/-/media/_excel/2016/19/2015-cbs-pc6huisnummer-buurt.zip"""

os.chdir("""c:/!ontwikkel/ondersteundebestanden""")

# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#         return i +1
#
# print(file_len('cbs_buurten_utf8.txt'))


"""unzip"""
# fh = open('2015-cbs-pc6huisnummer-buurt.zip', 'rb')
# z = zipfile.ZipFile(fh)
# for name in z.namelist():
#     outpath = "C:/!ontwikkel/ondersteundebestanden"
#     z.extract(name, outpath)
# fh.close()

counter2 = 0
for a in DBF('cbs_buurten.dbf', encoding='latin-1'):
    if counter2 < 1:
        keys = a.keys
        templist = list(a.keys())
        templine = (';'.join(map(str, templist)))

        file = open('cbs_buurten.txt', 'a')
        file.write('{0}\n'.format(templine))
        file.close()

        values = a.values
        templist = list(a.values())
        if len(templine) > 10:  # this should avoid adding empty lines (at the end of the doc for example))
            templine = (';'.join(map(str, templist)))

        file = open('cbs_buurten.txt', 'a')
        file.write('{0}\n'.format(templine))
        file.close()

        counter2 += 1
    else:
        values = a.values
        templist = list(a.values())  # maak een list van de values in de ordered dictionary
        # print(';'.join(map(str,templist))) #verander mbv "map()" alle items in de list in een string en voeg ze daarna samen tot 1 string
        templine = (';'.join(map(str, templist)))  # verander mbv "map()" alle items in de list in een string en voeg ze daarna samen tot 1 string

        file = open('cbs_buurten.txt', 'a')
        file.write('{0}\n'.format(templine))
        file.close()

print(" Latin-1 encoded cbs_buurten.txt klaar")

"Volgende blok  zet encoding van cbs_buurten.txt van Latin1 om in UTF8 en is een noodzakelijke stap om errors later tijdens het wegschrijven naar de dv te voorkomen.  "
BLOCKSIZE = 1024 * 1024
with open('cbs_buurten.txt', 'rb') as inf:
    with open('cbs_buurten_utf8.txt', 'wb') as ouf:
        while True:
            data = inf.read(BLOCKSIZE)
            if not data: break
            converted = data.decode('latin1').encode('utf-8')
            ouf.write(converted)

print('done. Controleer of er geen empty lines aan het eind van het document zijn. Pas eventueel naamgeving aan en kopieer dit dan naar AdresNl folder in !Ontwikkeldata')
