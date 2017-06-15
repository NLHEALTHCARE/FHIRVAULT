### Proces inladen adres_nl data

Periodiek (ongeveer maandelijks, periodiciteit is niet consequent) ontvangen wij van postcode.nl. 
Deze data wordt in een zipfile aangeleverd. Na het openen zijn er twee bestanden te zien:

![](https://github.com/NLHEALTHCARE/FHIRVAULT/blob/2.0.1-zomerwendesprint-test/mappings/adres_nl/images/folder_adresnl.png)

In de titel van de zipfile is de periode zichtbaar voor welke de update geldig is. Deze gebruik je later om de csv te hernoemen, aangezien het csv-bestand altijd een generieke naam (mut_pcdata.csv) heeft.  

1. Verplaatsen csv naar juiste folder op server

Verplaats de csv nu naar de juiste folder op Shannon-dev (10.249.1.143). Dit kan middels FTP (bv. Filezilla) of door vanuit de Terminal het bestand te kopiëren. De betreffende folder (filesystem) is /var/dwh2_data/adres_nl/.

2. Hernoemen bestand

Hernoem het bestand mut_pcdata.csv naar 'adresnl_update_[yyyymmdd-yyyymmdd].csv' (o.b.v. bovenstaand voorbeeld zou het dus 'adresnl_update_20170501-20170605' worden). 

3. Aanpassen config file (evt. hier later geautomatiseerd alternatief voor verzinnen)

Wijzig in de sectie voor adresnl in de config file (vanuit Pycharm, staat onder /CLINICSVAULT/configs/) de naam van het adresnl bestand conform de nieuwe naam, feitelijk hoef je dus enkel de data te wijzen:

![](https://github.com/NLHEALTHCARE/FHIRVAULT/blob/2.0.1-zomerwendesprint-test/mappings/adres_nl/images/wijzig_config_file.png)

4. Draai script om de nieuwe data in te laden

Tot slot dien je nog even het script te draaien waarmee de data daadwerkelijk ingeladen wordt in de adresnl_update tabel. Dit betreft het volgende script: ????
