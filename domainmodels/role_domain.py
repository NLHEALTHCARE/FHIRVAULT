from domainmodels.hl7rim_base_domain import *
from domainmodels.hl7rim_enums import *
from domainmodels.entity_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, HybridSat, LinkReference


########################################################################################################################
#
# Alle referentie typen en classes gebaseerd op HL7 RIM Role en RoleLink
#
# Een Rol wordt gedefinieerd door een Playing Entity en een Scoping Entity.
# Implementatie in datavault met patroon van link tussen
#   - Rol
#   - Playing entity
#   - Scoping entity
########################################################################################################################





class BasePersoon():
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
            idkaart = 'idkaart'  # staat niet in nictiz

        nummer = Columns.TextColumn()
        geldig_tot = Columns.DateColumn()  #staat niet in nictiz


class NaamgegevensSat(Sat):
    """Container voor naamgegevens"""
    initialen = Columns.TextColumn()
    voornamen = Columns.TextColumn()
    roepnaam = Columns.TextColumn()
    naamgebruik_code = Columns.RefColumn(RefTypes.naamgebruik_codes)
    geslachtsnaam = Columns.TextColumn()
    geslachtsnaam_voorvoegsels = Columns.TextColumn()
    partner_geslachtsnaam = Columns.TextColumn()
    partner_voorvoegsels = Columns.TextColumn()


class AdresSat(HybridSat):
    class Types(HybridSat.Types):
        woonadres = 'woonadres'  # HP
        postadres = 'postadres'  # PST
        officieel_adres = 'officieel adres'  # HP ?? staat niet in nictiz
        tijdelijk_adres = 'tijdelijk adres'  # TMP
        bezoek_adres = 'bezoek_adres adres'  # PHYS
        werkadres = 'werkadres'  # WP
        vakantieadres = 'vakantieadres'  # HV
        factuuradres = 'factuuradres'  # staat niet in nictiz

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


class EmailSat(HybridSat):
    """EmailSoortCodeLijst
    https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.4"""

    class Types(HybridSat.Types):
        prive = 'prive'
        werk = 'zakelijk'

    adres = Columns.TextColumn()




class TelefoonSat(HybridSat):
    """NummerSoortCodeLijst
    https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.3"""

    class Types(HybridSat.Types):
        thuis = 'thuis'
        tijdelijk = 'tijdelijk'
        zakelijk = 'zakelijk'
        mobiel = 'mobiel'
        pieper = 'pieper'

    nummer = Columns.TextColumn()



class Tarieven(DvEntity,Role):
    class Default(Sat):
        agb = Columns.TextColumn()
        declaratie_code = Columns.TextColumn()
        inkoopconcern = Columns.TextColumn()
        begintijd = Columns.DateColumn()
        eindtijd = Columns.DateColumn()
        totaal_tarief = Columns.FloatColumn()
        ziekenhuis_tarief = Columns.FloatColumn()
        honorarium_poort_tarief = Columns.FloatColumn()
        honorarium_ondersteuners_tarief = Columns.FloatColumn()

    class Sleutels(Sat):
        bron_id = Columns.TextColumn()



class Patient(DvEntity, Role):
    """https://zibs.nl/wiki/Patient

    Playing Entity = Persoon
    Scoping Entity = Zorgaanbieder

    Business Key: naam_bronsysteem + relatienummer/inschrijvingsnummer
    Business Key (alternatief): AGB-code zorgaanbieder (8) + BSN (9) + geboortedatum (ISO, 8) + geslachtcode (1)  (26 cijfers)
    """


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
            idkaart = 'idkaart'  # staat niet in nictiz

        nummer = Columns.TextColumn()
        geldig_tot = Columns.DateColumn()  # staat niet in nictiz


    class Hl7(Sat):
        role_class = Columns.TextColumn(default_value=RoleClass.patient)

    class Naamgegevens(Sat):
        """Container voor naamgegevens"""
        initialen = Columns.TextColumn()
        voornamen = Columns.TextColumn()
        roepnaam = Columns.TextColumn()
        naamgebruik_code = Columns.RefColumn(RefTypes.naamgebruik_codes)
        geslachtsnaam = Columns.TextColumn()
        geslachtsnaam_voorvoegsels = Columns.TextColumn()
        partner_geslachtsnaam = Columns.TextColumn()
        partner_voorvoegsels = Columns.TextColumn()

    class Adres(HybridSat):
        class Types(HybridSat.Types):
            woonadres = 'woonadres'  # HP
            postadres = 'postadres'  # PST
            officieel_adres = 'officieel adres'  # HP ??
            tijdelijk_adres = 'tijdelijk adres'  # TMP
            bezoek_adres = 'bezoek_adres adres'  # PHYS
            werkadres = 'werkadres'  # WP
            vakantieadres = 'vakantieadres'  # HV
            factuuradres = 'factuuradres'  # staat niet in nictiz

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

    class Email(HybridSat):
        """EmailSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.4
        """

        class Types(HybridSat.Types):
            prive = 'prive'
            werk = 'zakelijk'

        adres = Columns.TextColumn()

    class Telefoon(HybridSat):
        """NummerSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.3
        """

        class Types(HybridSat.Types):
            thuis = 'thuis'
            tijdelijk = 'tijdelijk'
            zakelijk = 'zakelijk'
            mobiel = 'mobiel'
            pieper = 'pieper'

        nummer = Columns.TextColumn()

    class Inschrijving(Sat):
        # hj hernoemt naar inschrijving, zodat zorgaanbieder (later) gaat verwijzen naar de zorgaanbieder entiteit via de link
        """Registratie van patient bij een zorgaanbieder"""
        agb_code_zorgaanbieder = Columns.TextColumn()
        inschrijfnummer = Columns.TextColumn()
        bronsysteem = Columns.TextColumn()  # bronsysteem specificiek toevoegen om nummer uniek te maken
        inschrijfdatum = Columns.DateColumn()
        uitschrijfdatum = Columns.DateColumn()

    class Bankgegevens(Sat):
        naam = Columns.TextColumn()
        code = Columns.TextColumn()
        rekeningnummer = Columns.TextColumn()

    #begin aanpassing Jan
    class Sleutels(Sat):
        extern_nummer = Columns.TextColumn()
        nummer = Columns.TextColumn()
        bron_id = Columns.TextColumn()
    #einde aanpassing Jan

class ContactPersoon(DvEntity, Role):
    pass


class PatientContactpersoonLink(Link):
    patient = LinkReference(Patient)
    contactpersoon = LinkReference(ContactPersoon)


class Medewerker(DvEntity, Role):
    """Standaard definitie nog opzoeken.

    Business key: KvK nummer + personeelsnummer
    """
    class Hl7(Sat):
        role_class = Columns.TextColumn(default_value=RoleClass.employee)

    class Default(Sat):
        geboortedatum = Columns.DateColumn()
        geslacht_code = Columns.RefColumn(RefTypes.geslacht_types)

    class Sleutels(Sat):
        medewerker_nummer = Columns.TextColumn()
        medewerker_id = Columns.TextColumn()
        medewerker_code = Columns.TextColumn()


    class Contract(Sat):
        functie = Columns.TextColumn()
        afdeling = Columns.TextColumn()
        voltijd_percentage = Columns.FloatColumn()
        contract_onbepaalde_duur = Columns.BoolColumn()
        salaris = Columns.FloatColumn()

    class Titels(Sat):
        academische_titel = Columns.TextColumn()
        adelijke_titel = Columns.TextColumn()

    class BeroepsGegevens(Sat):
        datum_aanvang_beroep = Columns.DateColumn()
        datum_einde_beroep = Columns.DateColumn()
        is_hoogleraar = Columns.BoolColumn()
        reden_einde_beroep = Columns.TextColumn()

    class Naamgegevens(Sat):
        """Container voor naamgegevens"""
        initialen = Columns.TextColumn()
        voornamen = Columns.TextColumn()
        roepnaam = Columns.TextColumn()
        naamgebruik_code = Columns.RefColumn(RefTypes.naamgebruik_codes)
        geslachtsnaam = Columns.TextColumn()
        geslachtsnaam_voorvoegsels = Columns.TextColumn()
        partner_geslachtsnaam = Columns.TextColumn()
        partner_voorvoegsels = Columns.TextColumn()

    class Adres(HybridSat):
        class Types(HybridSat.Types):
            woonadres = 'woonadres'  # HP
            postadres = 'postadres'  # PST
            officieel_adres = 'officieel adres'  # HP ??
            tijdelijk_adres = 'tijdelijk adres'  # TMP
            bezoek_adres = 'bezoek_adres adres'  # PHYS
            werkadres = 'werkadres'  # WP
            vakantieadres = 'vakantieadres'  # HV
            factuuradres = 'factuuradres'  # staat niet in nictiz

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

    class Email(HybridSat):
        """EmailSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1
        """

        class Types(HybridSat.Types):
            prive = 'prive'
            werk = 'zakelijk'

        adres = Columns.TextColumn()

    class Telefoon(HybridSat):
        """NummerSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.3
        """

        class Types(HybridSat.Types):
            thuis = 'thuis'
            tijdelijk = 'tijdelijk'
            zakelijk = 'zakelijk'
            mobiel = 'mobiel'
            pieper = 'pieper'

        nummer = Columns.TextColumn()


class Zorgverlener(Medewerker):
    """https://zibs.nl/wiki/Zorgverlener

    ZIBS concept van Zorgverlener maakt geen onderscheidt tussen Persoon(Entity), Role en Participation.
    In het domein model van NL Healthcare volgen wij de implementatie van HL7 RIM
    - Een Zorgverlener is Rol, gespeeld door een persoon, en gescoped door de CIBG zijnde autoriteit die zorgverleners licenceert
    - De zorgverlener heeft de RoleClass LicensedEntity
    - ZIBS 'zorgverlenerrol' is gemapped naar PartipcationType (hoofdbehandelaar, verwijzer, huisarts etc.)
    - Relatie tussen Zorgverlener en Zorgaanbieder middels RoleLink: Zorgverlener has part Zorgaanbieder

    zie ook:
    http://corepointhealth.com/resource-center/hl7-resources/r-mim-refined-message-information-model

    Business key = AGB-code zorgverlener of BIG code.
    AGB = 8 cijfers, met prefix 'AGB'
    BIG code = 11 cijfers, met prefix BIG
    """

    class Identificatie(Sat):
        agb_code = Columns.TextColumn()
        big_code = Columns.TextColumn()
        uzi_nummer = Columns.TextColumn()
        specialisme = Columns.RefColumn(RefTypes.specialisme_codes)


class Zorgaanbieder(DvEntity, Role):
    """https://zibs.nl/wiki/Zorgaanbieder

    Een zorgaanbieder is een organisatie die medische-, paramedische- en/of verpleegkundige zorg aanbiedt,
    en ook daadwerkelijk verleent, aan cliënten/patiënten. Voorbeelden zijn:
    ziekenhuis, verpleeghuis, huisartsenpraktijk.

    Een zorgaanbieder heeft 1 of meerdere vestigingen.

    In DWH2.0 wordt Vektis AGB database met alle zorginstellingen ingelezen

    Business key: AGB-code
    """

    # class Hl7(Sat):
    #     role_class = Columns.TextColumn(default_value=RoleClass.healthcare_provider)


    class Default(Sat):
        naam = Columns.TextColumn()
        extra_naam = Columns.TextColumn()
        organisatie_type = Columns.RefColumn(RefTypes.organisatie_types)
        afdeling_specialisme_code = Columns.RefColumn(RefTypes.specialisme_codes)


    class Identificatie(Sat):
        agb_code = Columns.TextColumn()
        wtzi_code = Columns.TextColumn()
        kvk_nummer = Columns.TextColumn()
        kvk_vestigingsnummer = Columns.TextColumn()

    class ExternalKeys(HybridSat):
        class Types(HybridSat.Types):
            timeff_code = 'timeff_code'
            timeff_pk = 'timeff_pk'

        key = Columns.TextColumn()


    class Adres(HybridSat):
        class Types(HybridSat.Types):
            postadres = 'postadres'  # PST
            officieel_adres = 'officieel adres'  # HP ??
            bezoek_adres = 'bezoek_adres adres'  # PHYS
            factuuradres = 'factuuradres'  # staat niet in nictiz

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

    class Email(HybridSat):
        """EmailSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1"""

        class Types(HybridSat.Types):
            prive = 'prive'
            werk = 'zakelijk'

        adres = Columns.TextColumn()

    class Telefoon(HybridSat):
        """NummerSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.0.1.3"""

        class Types(HybridSat.Types):
            thuis = 'thuis'
            tijdelijk = 'tijdelijk'
            zakelijk = 'zakelijk'
            mobiel = 'mobiel'
            pieper = 'pieper'

        nummer = Columns.TextColumn()


class Vestiging(Zorgaanbieder):
    """
    Identificeerbare vestigingen, zijnde een unieke combinatie van een:
      - zorgaanbieder
      - adres
      - onderneming

    Business key: interne vestiging_code
    """

    class Hl7(Sat):
        role_class = Columns.TextColumn(default_value=RoleClass.service_delivery_location)

    class VestigingIdentificatie(Sat):
        vestiging_code = Columns.TextColumn()
        vestiging_naam = Columns.TextColumn()
        agb_code = Columns.TextColumn()
        administratie_code = Columns.TextColumn()       #verschiillende vestigingen kunnen dezelfde administratie delen
        kvk_nummer = Columns.IntColumn()
        btw_nummer = Columns.TextColumn()  #staat niet in nictiz


class Afdeling(DvEntity, Role):
    """
    Identificeerbare afdelingen, die mogelijjk over verschillende vestigingen verspreid zijn:
      - specifiek domein, b.v. Finance, ICT, Kwaliteit
       - unieke kostenplaats

    Business key: vestigingcode + afdelingscode en/of kostenplaats
    """

    class Default(Sat):
        code = Columns.TextColumn()
        naam = Columns.TextColumn()
        kostenplaats = Columns.TextColumn()


class Zorgverzekeraar(DvEntity, Role):
    """https://zibs.nl/wiki/Betaler

    Betalers zijn organisaties of individuen die betalen voor de aan de patiënt geleverde zorg.
    Deze organisaties of individuen kunnen zijn: instellingen of personen die financieel garant staan
    of verantwoordelijk zijn voor de patiënt (zoals ouders van minderjarigen),
    organisaties met directe financiële verantwoordelijkheid, combinaties van deze of de patiënt zelf.

    NB: de Verzekering is als aparte Act opgenomen, en staat los van de Rol BetalerVerzekeraar.

    Invoice_payor: The role of an organization that undertakes to accept claims invoices,
    assess the coverage or payments due for those invoices and pay to the designated payees for those invoices.
    This role may be either the underwriter or a third-party organization authorized by the underwriter.
    The scoping entity is the organization that underwrites the claimed coverage.
    """

    class Hl7(Sat):
        role_class = Columns.TextColumn(default_value=RoleClass.invoice_payor)

    class Default(Sat):
        uzovi_nummer = Columns.TextColumn()
        naam = Columns.TextColumn()

    class Adres(HybridSat):
        class Types(HybridSat.Types):
            PHYS = 'woonadres'
            PST = 'postadres'
            HP = 'officieel adres'
            TMP = 'tijdelijk adres'
            WP = 'werkadres'
            HV = 'vakantieadres'

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

    class Email(HybridSat):
        """EmailSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1"""

        class Types(HybridSat.Types):
            prive = 'prive'
            werk = 'zakelijk'

        adres = Columns.TextColumn()

    class Telefoon(HybridSat):
        """NummerSoortCodeLijst
        https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1"""

        class Types(HybridSat.Types):
            thuis = 'thuis'
            tijdelijk = 'tijdelijk'
            zakelijk = 'zakelijk'
            mobiel = 'mobiel'
            pieper = 'pieper'

        nummer = Columns.TextColumn()


class Zorginkoopcombinatie(DvEntity, Role):
    """http://www.vektis.nl/images/Beheer_en_onderhoud_UZOVI_v1_1.pdf

        cz = 'CZ'
        achmea = 'ACHMEA - AGIS'
        dsw = 'DSW - STAD HOLLAND'
        multizorg = 'MULTIZORG VRZ'
        menzis = 'Menzis'
        vgz = 'COOPERATIE VGZ'
    """
    class Hl7(Sat):
        role_class = Columns.TextColumn(default_value=RoleClass.underwriter)

    class Default(Sat):
        naam = Columns.RefColumn(RefTypes.zorginkoopcombinatie_codes)



########################################################################################################################
#
#  Links tussen rollen, om hierarchieen weer te geven en controles uit te voeren
#
#######################################################################################################################


class PatientZorgaanbiederLink(Link):
    """Link welke patienten bij welke zorgaanbieder patient zijn

    Pragmatisch opgelost, mag strict genomen niet in HL7 RIM
    """
    patient = LinkReference(Patient)
    zorgaanbieder = LinkReference(Zorgaanbieder)


class ZorgverlenerZorgaanbiederLink(Link):
    """Link welke zorgverleners bij welke zorgaanbieder verbonden zijn

    Pragmatisch opgelost, mag strict genomen niet in HL7 RIM
    """
    zorgverlener = LinkReference(Zorgverlener)
    zorgaanbieder = LinkReference(Zorgaanbieder)

    #to do: kenmerken uit Vektis AGB database aan linktabel toevoegen


class ZorgaanbiederZorgaanbiederLink(Link):
    """
    Bedoeld om hierachieen aan te geven tussen zorgaanbieders
    """
    child = LinkReference(Zorgaanbieder)
    parent = LinkReference(Zorgaanbieder)


class ZorgaanbiederAfdelingLink(Link):
    """
    Bedoeld om hierachieen aan te geven tussen zorgaanbieders
    """
    child = LinkReference(Afdeling)
    parent = LinkReference(Zorgaanbieder)


class ZorginkoopcombinatieLink(Link, RoleLink):
    """http://www.vektis.nl/images/Beheer_en_onderhoud_UZOVI_v1_1.pdf"""
    verzekeraar = LinkReference(Zorgverzekeraar)
    inkoopcombinatie = LinkReference(Zorginkoopcombinatie)


class ZorgverzekeraarKoepelLink(Link):
    """
    Bedoeld om hierachieen aan te geven tussen zorgverzekeraars
    """
    child = LinkReference(Zorgverzekeraar)
    parent = LinkReference(Zorgverzekeraar)


#
# class OndernemingLink(Link):
#     child = LinkReference(Onderneming)
#     parent = LinkReference(Onderneming)
#
# class MedewerkerOrganisatieLink(Link):
#     medewerker = LinkReference(Medewerker)
#     werkgever = LinkReference(Zorgaanbieder)






#TO DO: vanaf hieronder nog opschonen







# Je kan RoleClass.part gebruiken om hierachieen in organizaties weer te geven, maar wordt dit wat omslachtig?
# class Zorginkoopcombinatie(DvEntity, Role):
#     class Hl7(Sat):
#         role_class = Columns.TextColumn(default_value=RoleClass.part)


#
#
#
# class Zorgverzekeraar(DvEntity, Role):
#     """http://www.vektis.nl/images/Beheer_en_onderhoud_UZOVI_v1_1.pdf"""
#
#     class Default(Sat):
#         uzovi_code = Columns.TextColumn()



