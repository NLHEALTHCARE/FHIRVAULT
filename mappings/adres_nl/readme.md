### Proces inladen adres_nl data

Periodiek (ongeveer maandelijks, periodiciteit is niet consequent) ontvangen wij updates van postcode.nl.
Deze data wordt in een zipfile aangeleverd. Na het openen zijn er twee bestanden te zien:

![bestanden](https://github.com/NLHEALTHCARE/FHIRVAULT/blob/2.0.1-zomerwendesprint-test/mappings/adres_nl/images/folder_adresnl.png)

In de titel van de zipfile is de periode zichtbaar voor welke de update geldig is. Deze gebruik je later om de csv te hernoemen, aangezien het csv-bestand altijd een generieke naam (mut_pcdata.csv) heeft.  

0. Preparen

(Laatste keer moest ik de file nog preparen: headers misten, en het was komma separated ipv ; -> open in excel, voeg header toe en sla op als csv)

1. Verplaatsen csv naar juiste folder op server

Verplaats de csv nu naar de juiste folder op Shannon-dev (10.249.1.143). Dit kan middels FTP (bv. Filezilla) of door vanuit de Terminal het bestand te kopiëren. De betreffende folder (filesystem) is /var/dwh2_data/adres_nl/.

2. Hernoemen bestand

Hernoem het bestand mut_pcdata.csv naar 'adresnl_update_[yyyymmdd-yyyymmdd].csv' (o.b.v. bovenstaand voorbeeld zou het dus 'adresnl_update_20170501-20170605' worden). 

*LET WEL:* er dient update in de bestandsnaam voor te komen (geen hoofdletters).

3. De eerst volgende keer dat pyelt runt zal die een nieuw bestand herkennen en zal het bestand worden ingelezen.
