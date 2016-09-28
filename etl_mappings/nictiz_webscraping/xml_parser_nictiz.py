import csv
import os
import urllib
import urllib.request
import xml.etree.ElementTree as ET

from etl_mappings.nictiz_webscraping.html_parser_nictiz import html_to_string, NicTizParser


class Valuesets:
    def __init__(self, root):
        self.root = root
        self.headers = []
        self.rows = []
        self.counter = 0

    def get_only_unique(self, seq):
        # order preserving
        checked = []
        for e in seq:
            if e not in checked:
                checked.append(e)
        return checked

    def get_headers_and_rows(self):

        for valueset in self.root.iter('valueSet'):
            for conceptlist in self.root.iter('conceptList'):  # deze regel localiseert in het document (alle knopen met de
                # naam: ) 'conceptList, ongeacht waar deze zich bevinden

                for concept in conceptlist:
                    # onderstaande regel zorgt dat er een vaste volgorde van de kolommen ontstaat
                    rows_temp = [concept.attrib.get('level')] + [concept.attrib.get('type')] + [concept.attrib.get('code')] + [concept.attrib.get('displayName')] + [concept.attrib.get('codeSystem')] \
                    + [valueset.attrib.get('id')] + [valueset.attrib.get('displayName')] + [valueset.attrib.get('effectiveDate')] + [valueset.attrib.get('statusCode')]
                    if len(rows_temp) == 9:  # de gelezen rij wordt alleen mee genomen indien de lengte gelijk is aan het
                        # aantal kolommen; let op is nu nog hardgecodeerd!
                        self.rows.append(rows_temp)
                    if self.counter == 0:
                        headers_temp = ['level', 'type', 'code', 'displayName', 'codeSystem', 'id', 'valueset', 'ingangsdatum', 'codestatus']

                        self.headers.append(headers_temp)
                        self.counter += 1
                headers = self.headers

                rows = self.get_only_unique(self.rows)  # verbruikt veel tijd indien alle xml bestanden worden gelezen!
                return headers, rows


class NictizCSVWriter:
    def __init__(self, data_path, file_name):
        self.file_name = file_name
        self.data_path = data_path

    def save_as_csv(self, rows):
        """
        door het aanroepen van deze functie wordt aan een csv file nieuwe regels toegevoegd (writer setting = 'a')
        """
        os.chdir(self.data_path)

        with open(self.file_name, 'a', newline='', encoding='utf-8') as f:  # als het stukje met newline weggelaten wordt
            # komt er tussen iedere regel een lege regel te staan.
            # Als encoding=utf-8 wordt weggelaten leidt dit voor sommige xml bestanden tot een encoding error.

            f_csv = csv.writer(f, delimiter=';')  # als de delimiter niet specifiek gedefinieerd wordt, wordt
            # als default een komma als delimiter gebruikt.
            for row in rows:
                if "Administrative Gender (HL7 V3)" not in row:
                    f_csv.writerow(row)

                if "Administrative Gender (HL7 V3)" in row:
                    print(
                        """'Administrative Gender (HL7 V3)' is niet opgenomen in 'valuesets.csv'. Reden: Deze oid (2.16.840.1.113883.1.11.1) wordt ook door 'AdministrativeGender' gebruikt. Deze laatste bevat precies dezelfde values en is bovendien van een recentere datum.""")

    def save_csv_headers(self, headers):
        """
        door het aanroepen van deze functie wordt de oude csv-file overschreven  (writer setting = 'w') door een bestand
        met alleen een row met kolomnamen.

        """
        os.chdir(self.data_path)

        with open(self.file_name, 'w', newline='', encoding='utf-8') as f:  # als het stukje met newline weggelaten wordt
            # komt er tussen iedere regel een lege regel te staan.
            # Als encoding=utf-8 wordt weggelaten leidt dit voor sommige xml bestanden tot een encoding error.

            f_csv = csv.writer(f, headers, delimiter=';') # als de delimiter niet specifiek gedefinieerd wordt, wordt
            # als default een komma als delimiter gebruikt.
            f_csv.writerows(headers)


def scrape_from_web(configs):

    if configs['use_scraping'] == False:
        print('In de config file staat use_scraping op False. Gevolg: webscraping van nictiz vindt niet plaats.')
    elif configs['use_scraping']:  # indien True dan runt de code, anders niet.

        """Verkrijg alle xml refs waarnaar verwezen wordt op de url: 'https://decor.nictiz.nl/decor/services/ValueSetIndex?prefix=&format=html&language=nl-NL' """

        html_as_string = html_to_string('https://decor.nictiz.nl/decor/services/ValueSetIndex?ref=2.16.840.1.113883.2.4.3.11.60.101')
        parser = NicTizParser()
        parser.feed(html_as_string)
        parser.close()

        """maak hieronder een comment van de xml_refs versie die je niet wil gebruiken   """
        """versie 1: alle xml_refs afkomstig van Nictiz; let op! duurt bijna een uur om beide csv tabellen te verkrijgen, met
                     name de tabel valueset_values duurt lang"""
        # xml_refs = parser.xml_refs
        """versie 2: beperkt aantal xml_refs om programma mee te testen"""
        # xml_refs = ['RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.1.11.2&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.13&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.6&effectiveDate=&prefix=hg-&format=xml&language=nl-NL','RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.11&effectiveDate=&prefix=hg-&format=xml&language=nl-NL']
        """versie 3: selectie van xml_refs afkomstig van Nictiz:"""
        xml_refs = parser.xml_refs[20:30]
        # print(xml_refs)
        """versie 4: 3x adressoort, met als enige verschil naar welk project ze refereren"""
        # xml_refs = ['RetrieveValueSet?id=2.16.840.1.113883.3.88.12.3221.7.4&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.6&effectiveDate=&prefix=naw-&format=xml&language=nl-NL','RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.6&effectiveDate=&prefix=kz-&format=xml&language=nl-NL']
        """ versie 5:  """
        # xml_refs = ['RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.1.11.2&effectiveDate=&prefix=hg-&format=html&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.6&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.13&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.11&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.9&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.8&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.1.11.2&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.7&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.4&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.19890&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.78&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.5&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.101.11.14&effectiveDate=&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.20&effectiveDate=2014-11-19T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.18&effectiveDate=2013-10-01T16:45:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.16&effectiveDate=2013-05-24T15:56:54&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.15&effectiveDate=2013-05-24T15:30:25&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.14&effectiveDate=2013-04-10T14:51:01&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.9&effectiveDate=2011-10-12T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.12&effectiveDate=2011-10-12T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.2&effectiveDate=2011-10-12T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.3&effectiveDate=2011-10-12T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.1&effectiveDate=2011-10-12T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.2.4.3.11.60.103.11.19&effectiveDate=2009-10-01T00:00:00&prefix=hg-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.10609&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.395&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.10878&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.10882&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.19638&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.19358&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.8&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.155&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.159331&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL', 'RetrieveValueSet?id=2.16.840.1.113883.1.11.10317&effectiveDate=&prefix=hl7m-&format=xml&language=nl-NL']
        """
        verzamelen van valuesets:
        """

        scrape_url = configs['scrape_url']
        data_path = configs['data_path']
        counter = 0

        for xml_ref in xml_refs:

            url = scrape_url + str(xml_ref)
            u = urllib.request.urlopen(url)
            tree = ET.parse(u)
            root = tree.getroot()
            valueset_values = Valuesets(root)

            for conceptlist in root.iter('conceptList'):  # deze regel zorgt ervoor dat er alleen headers en rows worden
                # opgehaald indien 'concepList' bestaat in het xml bestand dat nu gelezen wordt.
                headers, rows = valueset_values.get_headers_and_rows()

                new_csv = NictizCSVWriter(data_path, 'valuesets.csv')
                if counter < 1:
                    new_csv.save_csv_headers(headers)
                    counter += 1
                new_csv.save_as_csv(rows)

        print('Data saved to valuesets.csv in {}'.format(data_path))
