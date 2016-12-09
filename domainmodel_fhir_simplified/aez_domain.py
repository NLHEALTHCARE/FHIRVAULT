from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference


#########################################################################################################
#                                                                                                       #
# Eerstelijns domein model, gebasseerd op FHIR-standaard (hl7.org.fhir).                                #
#                                                                                                       #
#########################################################################################################


# https://www.hl7.org/fhir/patient.html
class Patient(DvEntity):

    class Default(Sat):
        actief = Columns.BoolColumn(fhir_name='active')
        geslacht = Columns.TextColumn(fhir_name='gender')
        geboortedatum = Columns.DateColumn(fhir_name='birthDate')
        overleden = Columns.BoolColumn(fhir_name='deceasedBoolean')
        burgerlijke_staat = Columns.TextColumn(fhir_name='maritalStatus')
        meerling = Columns.BoolColumn(fhir_name='multipleBirthBoolean')

    class Identificatie(HybridSat): #Identifier

        class Types(HybridSat.Types):
            official = 'official'
            secondary = 'secondary'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')

    class Naam(Sat):
        volledig = Columns.TextColumn(fhir_name='text')
        achternaam = Columns.TextArrayColumn(fhir_name='family')
        partnernaam = Columns.TextArrayColumn()
        voornaam = Columns.TextArrayColumn(fhir_name='given')
        voorvoegsel_achternaam = Columns.TextArrayColumn(fhir_name='prefix')
        voorvoegsel_partnernaam = Columns.TextArrayColumn()
        achtervoegsel = Columns.TextArrayColumn(fhir_name='suffix')

    class Telecom(HybridSat):

        class Types(HybridSat.Types):
            phone = 'phone'
            mobile = 'mobile'
            fax = 'fax'
            email = 'email'
            other = 'other'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')
        volgorde = Columns.IntColumn(fhir_name='order')

    class Adres(HybridSat): #Address

        class Types(HybridSat.Types):
            huis = 'huis'
            werk = 'werk'

        straatnaam = Columns.TextColumn(fhir_name='line')
        huisnummer = Columns.TextColumn(fhir_name='line')
        toevoeging = Columns.TextArrayColumn(fhir_name='line')
        plaats = Columns.TextColumn(fhir_name='city')
        postcode = Columns.TextColumn(fhir_name='postalcode')
        land = Columns.TextColumn(fhir_name='country')

# https://www.hl7.org/fhir/practitioner.html
class Behandelaar(DvEntity):

    class Default(Sat):
        actief = Columns.BoolColumn(fhir_name='active')
        geslacht = Columns.TextColumn(fhir_name='gender')
        geboortedatum = Columns.DateColumn(fhir_name='birthdate')
        kwalificatie = Columns.TextColumn(fhir_name='qualification')

    class Identificatie(HybridSat): #Identifier

        class Types(HybridSat.Types):
            official = 'official'
            secondary = 'secondary'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')

    class Naam(Sat):
        volledig = Columns.TextColumn(fhir_name='text')
        achternaam = Columns.TextArrayColumn(fhir_name='family')
        partnernaam = Columns.TextArrayColumn()
        voornaam = Columns.TextArrayColumn(fhir_name='given')
        voorvoegsel_achternaam = Columns.TextArrayColumn(fhir_name='prefix')
        voorvoegsel_partnernaam = Columns.TextArrayColumn()
        achtervoegsel = Columns.TextArrayColumn(fhir_name='suffix')

    class Telecom(HybridSat):
        class Types(HybridSat.Types):
            phone = 'phone'
            mobile = 'mobile'
            fax = 'fax'
            email = 'email'
            other = 'other'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')
        volgorde = Columns.IntColumn(fhir_name='order')

    class Adres(HybridSat):  # Address

        class Types(HybridSat.Types):
            huis = 'huis'
            werk = 'werk'

        straatnaam = Columns.TextColumn(fhir_name='line')
        huisnummer = Columns.TextColumn(fhir_name='line')
        toevoeging = Columns.TextArrayColumn(fhir_name='line')
        plaats = Columns.TextColumn(fhir_name='city')
        postcode = Columns.TextColumn(fhir_name='postalcode')
        land = Columns.TextColumn(fhir_name='country')

# https://www.hl7.org/fhir/organisatie.html
class Organisatie(DvEntity):

    class Default(Sat):
        type = Columns.TextColumn(fhir_name='type')
        actief = Columns.BoolColumn(fhir_name='active')
        naam = Columns.TextColumn(fhir_name='org_name')

    class Identificatie(HybridSat): #Identifier

        class Types(HybridSat.Types):
            official = 'official'
            secondary = 'secondary'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')

    class Telecom(HybridSat):

        class Types(HybridSat.Types):
            phone = 'phone'
            mobile = 'mobile'
            fax = 'fax'
            email = 'email'
            other = 'other'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value')
        volgorde = Columns.IntColumn(fhir_name='order')

    class Adres(HybridSat): #Address

        class Types(HybridSat.Types):
            huis = 'huis'
            werk = 'werk'

        straatnaam = Columns.TextColumn(fhir_name='line')
        huisnummer = Columns.TextColumn(fhir_name='line')
        toevoeging = Columns.TextArrayColumn(fhir_name='line')
        plaats = Columns.TextColumn(fhir_name='city')
        postcode = Columns.TextColumn(fhir_name='postalcode')
        land = Columns.TextColumn(fhir_name='country')


#https://www.hl7.org/fhir/claim.html
class Declaratie(DvEntity):
    class Default(Sat):
        ruleset = Columns.TextColumn(fhir_name='ruleset')
        type = Columns.TextColumn(fhir_name='type')
        factuurnummer = Columns.TextColumn()

    class Identificatie(HybridSat): #Identifier

        class Types(HybridSat.Types):
            official = 'official'
            secondary = 'secondary'

        systeem = Columns.TextColumn(fhir_name='system')
        waarde = Columns.TextColumn(fhir_name='value') #declaratieprestatieId

    class Item(Sat):
        prestatie = Columns.TextArrayColumn(fhir_name='service')
        prestatiedatum = Columns.DateColumn(fhir_name='serviceDate')
        aantal = Columns.IntColumn(fhir_name='quantity')
        prijs = Columns.FloatColumn(fhir_name='unitPrice')
        bedrag = Columns.FloatColumn(fhir_name='net')


### LINKS ###


class OrganisatieOrganisatieLink(Link):

    organisatie = LinkReference(Organisatie)
    deel_van = LinkReference(Organisatie)


class PatientManagingOrganisatieLink(Link):

    patient = LinkReference(Patient)
    organisatie = LinkReference(Organisatie)


class BehandelaarOrganisatieLink(Link):

    behandelaar = LinkReference(Behandelaar)
    organisatie = LinkReference(Organisatie)

    class Default(Sat):

        role = Columns.TextColumn()
        speciality = Columns.TextColumn()


class DeclaratieDeclarantLink(Link):
    declaratie = LinkReference(Declaratie)
    behandelaar = LinkReference(Behandelaar)
    organisatie = LinkReference(Organisatie)
    patient = LinkReference(Patient)

    class Default(Sat):

        class Types(HybridLink.Types):
            subscriber = 'subscriber'
            provider = 'provider'
            other = 'other'
        type = Columns.TextColumn(default_value=Types.other)


class DeclaratieVerzekeraarLink(Link):
    declaratie = LinkReference(Declaratie)
    organisatie = LinkReference(Organisatie)


class DeclaratieProviderLink(Link):
    declaratie = LinkReference(Declaratie)
    behandelaar = LinkReference(Behandelaar)


class DeclaratieOrganisatieLink(Link):
    declaratie = LinkReference(Declaratie)
    organisatie = LinkReference(Organisatie)


class DeclaratiePatientLink(Link):
    declaratie = LinkReference(Declaratie)
    patient = LinkReference(Patient)

