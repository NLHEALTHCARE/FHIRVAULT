from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

########################################################################################################################
#
# Alle referentie typen en classes gebaseerd op HL7 RIM Entity
#
########################################################################################################################


class RefTypes:
    """Referentie types omvatten alle code systems en value sets die binnen het NL Healthcare domein model worden gebruikt.

    De codes worden gebruikts in de SATs. Door de joinen op de referentie tabellen kunnen omschrijvingen, hierachieen
    etc. worden gebruikt. In HL7 RIM wordt dit aangeduid als Coded No Exceptions (CNE).
    """

    # ISO 5218, https://nl.wikipedia.org/wiki/ISO_5218,
    # hetzelfde als COD046-NEN zoals aanbevolen door Vektis http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD046&Co_Or_Code=NEN

    geslacht_types = 'geslacht_types'

    # ISO 3166-2, https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2,
    # hetzelfde als COD032-NEN zoals aanbevolen gebruikt door Vektis http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD032&Co_Or_Code=NEN
    land_codes = 'land_codes'

    # ZIBS / Nictiz naamgebruik codelijst
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    naamgebruik_codes = 'naamgebruik_codes'

    # ZIBS / Nictiz organisatietype codelijst. NB: alleen zorginstellingen, geen generieke organisatie types!?
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    organisatie_types = 'organisatie_types'


    # ZIBS / Nictiz producttype codelijst gebaseerd op UNSPSC
    # https://www.unspsc.org/  Nederlandse versie te koop voor USD 100,-
    product_type_codes = 'product_type'

    # Codelijst voor (familiare) relaties
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    relatie_codes = 'relatie_codes'

    # Codelijst voor rollen van contactpersonen in relatie tot andere personen c.q. patienten
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    rol_codes = 'rol_codes'

    # Codelijst Vektis AGB medische specialismen
    # COD016-VEKT http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD016&Co_Or_Code=VEKT
    specialisme_codes = 'specialisme_codes'

    # Alle DBC codelijsten conform http://werkenmetdbcs.nza.nl/werken-met-dbcs/frontpage/menu-ID-2350
    # Verschillende codestelsels voor Ziekenhuiszorg (RZ), GGZ (RG), Geriatrische Revalidatiezorg (GRZ) en Forensische Zorg (RF)
    # Technisch zijn de ziekenhuiszorg en grz hetzelfde
    
    # Ziekenhuiszorg met prefix DBC
    dbc_afsluitredenen = 'dbc_afsluitredenen'
    dbc_declaraties = 'dbc_declaraties'
    dbc_diagnoses = 'dbc_diagnoses'
    dbc_zorgactiviteiten = 'dbc_zorgactiviteiten'
    dbc_zorgproducten = 'dbc_zorgproducten'
    dbc_zorgtypes = 'dbc_zorgtypes'
    dbc_zorgvraag_codes = 'dbc_zorgvraag_codes'
    dbc_verwijscodes = 'dbc_verwijscodes'

    # DHD
    cbv_codes = 'cbv_codes'

    # GGZ met prefix ggz
    ggz_activiteiten = 'ggz_activiteiten'
    ggz_beroepen = 'ggz_beroepen'
    ggz_hoofdberoepen = 'ggz_hoofdberoepen'
    ggz_circuits = 'ggz_circuits'
    ggz_diagnoses = 'ggz_diagnoses'
    ggz_redenensluiten = 'ggz_redenensluiten'
    ggz_zorgtypes = 'ggz_zorgtypes'
    ggz_productgroepen = 'ggz_productgroepen'
    ggz_prestatiecodes = 'ggz_prestatiecodes'
    ggz_tarief_code = 'ggz_tarief_code'
    ggz_activiteit_tarief_codes = 'ggz_activiteit_tarief_codes'

    # zorginkoopcombinatie
    zorginkoopcombinatie_codes = 'zorginkoopcombinatie_codes'


    # welke zijn dit? Nog op te zoeken
    academische_titels = 'academische_titels'
    adelijke_titels = 'adelijke_titels'
    traject_status_codes = 'traject_status_codes'
    gebeurtenis_status_codes = 'gebeurtenis_status_codes'
    vektis_praktijk_statussen = 'vektis_praktijk_statussen'
    vektis_verbijzonderingscodes = 'vektis_verbijzonderingscodes'
    subtraject_status = 'subtraject_status_codes'



class Persoon(DvEntity, Entity):
    """Een natuurlijk persoon. Gereserveerd voor genereren van Master Person Index.
    Geen adres sat

    Business key: BSN + geboortedatum (ISO) + geslachtcode (18 cijfers)
    """

    class Hl7(Sat):
        entity_class = Columns.TextColumn(default_value=EntityClass.person)
        entity_determiner = Columns.TextColumn(default_value=EntityDeterminer.specific)

    class Default(Sat):
        geboortedatum = Columns.DateColumn()
        geslacht_code = Columns.RefColumn(RefTypes.geslacht_types)
        meerling_indicator = Columns.TextColumn()
        overlijdens_indicator = Columns.TextColumn()
        datum_overlijden = Columns.DateTimeColumn()

    class Identificatie(HybridSat):
        class Types(HybridSat.Types):
            bsn = 'BSN'
            rijbewijs = 'rijbewijs'
            paspoort = 'paspoort'

        nummer = Columns.TextColumn()

    class Naamgegevens(Sat):
        initialen = Columns.TextColumn()
        voornamen = Columns.TextColumn()
        roepnaam = Columns.TextColumn()
        naamgebruik_code = Columns.RefColumn(RefTypes.naamgebruik_codes)
        geslachtsnaam = Columns.TextColumn()
        geslachtsnaam_voorvoegsels = Columns.TextColumn()
        partner_geslachtsnaam = Columns.TextColumn()
        partner_voorvoegsels = Columns.TextColumn()

    class Email(HybridSat):
        """EmailSoortCodeLijst https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00"""

        class Types(HybridSat.Types):
            prive = 'prive'
            werk = 'zakelijk'

        adres = Columns.TextColumn()

    class Telefoon(HybridSat):
        """NummerSoortCodeLijst https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00"""

        class Types(HybridSat.Types):
            thuis = 'thuis'
            tijdelijk = 'tijdelijk'
            zakelijk = 'zakelijk'
            mobiel = 'mobiel'
            pieper =  'pieper'

        nummer = Columns.TextColumn()


class Organisatie(DvEntity, Entity):
    """Een organisatie, uniek identificeerbaar met een KvK nummer.

    ZIBS maakt geen expliciet onderscheid tussen Organization en Role. Binnen het NL Healthcare domein model volgen
    we HL7 RIM, waarbij wel het onderscheid wordt gemaakt.

    Business key = KvK nummer
    """

    class Hl7(Sat):
        entity_class = Columns.TextColumn(default_value=EntityClass.organization)
        entity_determiner = Columns.TextColumn(default_value=EntityDeterminer.specific)

    class Default(Sat):
        kvk_nummer = 'kvk_nummer'
        naam = Columns.TextColumn()

    class Telefoongegevens(HybridSat):
        class Types(HybridSat.Types):
            telefoon = 'telefoon'
            mobiel = 'mobiel'
            telefoon2 = 'telefoon2'
            mobiel2 = 'mobiel2'

        nummer = Columns.TextColumn()

    class Emailgegevens(HybridSat):
        class Types(HybridSat.Types):
            email = 'email'
            email2 = 'email2'

        adres = Columns.TextColumn()

    class Webgegevens(HybridSat):
        class Types(HybridSat.Types):
            email = 'website'
            email2 = 'website2'

        adres = Columns.TextColumn()


class AdresNL(DvEntity, Entity):
    """Adressen in Nederland uniek identificeerbaar met postcode + huisnummer

    In DWH2.0 gaan we landelijke adressen database inlezen"""
    class Hl7(Sat):
        entity_class = Columns.TextColumn(default_value=EntityClass.place)
        entity_determiner = Columns.TextColumn(default_value=EntityDeterminer.specific)

    class Default(Sat):
        straat = Columns.TextColumn()
        huisnummer = Columns.IntColumn()
        huisnummerletter = Columns.TextColumn()
        huisnummertoevoeging = Columns.TextColumn()
        aanduiding_bij_nummer_code = Columns.TextColumn()
        woonplaats = Columns.TextColumn()
        gemeente = Columns.TextColumn()
        land_code = Columns.RefColumn(RefTypes.land_codes)
        postcode = Columns.TextColumn()
        additionele_informatie = Columns.TextColumn()
        provincie = Columns.TextColumn()  # staat niet in nictiz


    ##### Sat voor de deleted adressen (rfw)

    class RecordStatus(Sat):

        status = Columns.TextColumn()
        # bag_nummeraanduiding_del = Columns.TextColumn()
        # bag_adresseerobject_del = Columns.TextColumn()

    #####


   # de extra info in onderstaande sat is gebaseerd op gegevens afkomstig zijn uit landelijk adressen database, maar
        # geen onderdeel zijn van de default sat zoals hierboven gedefinieerd is.
    class ExtraInfo(Sat):

#         status_temp = Columns.TextColumn() # record_status kan zijn "downdate, update, delete en insert"; komt voor in de update bestanden van postcodeNL.
        perceeltype = Columns.TextColumn() # type perceel (verblijfsobject, standplaats, ligplaats, postbus)
        bag_huisnummertoevoeging = Columns.TextColumn() # verwijst naar actieve BAG (Basisadministratie Adressen en Gebouwen) aanduiding
        gebruiksdoel = Columns.TextColumn()
        # gemeentenaam = Columns.TextColumn()

    class PostcodeDetails(Sat):
        wijkcode = Columns.TextColumn() # nummergedeelte van postcode
        lettercombinatie = Columns.TextColumn() # lettergedeelte van postcode
        huisnr_van = Columns.TextColumn() # laagste huisnummer van postcode range
        huisnr_tm = Columns.TextColumn() # hoogste huisnummer van postcode range
        reeksindicatie = Columns.TextColumn() # postcode range type (0 = oneven, 1 = even)

    class GeoInfo(Sat):
        breedtegraad = Columns.TextColumn()  # indien aanwezig
        lengtegraad = Columns.TextColumn()  # indien aanwezig
        rdx = Columns.TextColumn()  # rijkdriehoekscoordinaat van adres voordeur
        rdy = Columns.TextColumn()
        oppervlakte = Columns.TextColumn()  # indien adres verblijfblijfplaats; woonoppervlak in vierkante meters

    class Identificatie(Sat):
        bag_nummeraandingid = Columns.TextColumn()
        bag_adresseerbaarobjectid = Columns.TextColumn()
        perceelid = Columns.IntColumn()  # Postcode.nl identifier voor "perceel" level
        reeksid = Columns.TextColumn()  # Postcode.nl identifier for 'pcreeks' level.
        straatid = Columns.IntColumn() #postcode.nl identifier for 'straat' level.
        plaatsid = Columns.IntColumn()
        # gemeenteid = Columns.IntColumn() # Postcode.nl identifier for 'gemeente' level

    class Afkortingen(Sat):
        # _nen: duidt op format volgens NEN 5825 conventies: oftewijl Nederlandse standaard om bepaalde namen tot een
        # vaste lengte af te korten. Bijvoorbeeld een plaatsnaam wordt afgekort tot 24 characters volgens deze conventie
        straat_nen = Columns.TextColumn()
        plaats_nen = Columns.TextColumn()
        gemeente_nen = Columns.TextColumn()
        gemeentecode = Columns.IntColumn() # code gebruikt door CBS
        cebucocode = Columns.IntColumn() # code gebruikt door DeBuCo (Centraal Bureau voor Courantenpubliciteit)
        provinciecode = Columns.TextColumn() # Postcode.nl identifier for 'provincie' level
        
    class CBS_buurten(Sat): # let op dit is een ander bronbestand (cbs_buurten) dan de bovenstaande sats.

        wijkcode = Columns.IntColumn()  # let op: niet verwarren met de wijkcode van adres_nl; betekent niet hetzelfde
        wijknaam = Columns.TextColumn()
        buurtcode = Columns.IntColumn()
        buurtnaam = Columns.TextColumn()




class MedischHulpmiddel(DvEntity, Entity):
    """https://zibs.nl/wiki/MedischHulpmiddel

    Medische hulpmiddelen kunnen worden omschreven als de inwendig geïmplanteerde en uitwendige apparatuur
    en/of hulpmiddelen die de patiënt gebruikt of heeft gebruikt om de gevolgen van functionele beperkingen
    van orgaansystemen te verminderen of om de behandeling van een ziekte mogelijk te maken.
    """

    class Hl7(Sat):
        entity_class = Columns.TextColumn(default_value=EntityClass.device)

    class Default(Sat):
        product_id = Columns.TextColumn()
        product_type_code = Columns.RefColumn(RefTypes.product_type_codes)
        begindatum = Columns.DateColumn()
        indicatie_probleem = Columns.TextColumn()       #todo: moet dit eigenlijk niet via link naar Concern?
        toelichting = Columns.TextColumn()
        anatomische_locatie = Columns.TextColumn()
        locatie_zorgaanbieder = Columns.TextColumn()    #todo: moet dit eigenlijk niet via link naar Role zorgaanbieder?
        zorgverlener = Columns.TextColumn()             #todo: moet dit eigenlijk niet via link naar Role zorgverlener?


class Medicijn(DvEntity, Entity):
    pass
