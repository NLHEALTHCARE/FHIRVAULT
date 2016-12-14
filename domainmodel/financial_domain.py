from domainmodel.clinical_domain import Zorgactiviteit
from domainmodel.identity_domain import Patient,Zorgaanbieder, Zorginkoopcombinatie, Zorgverzekeraar
from domainmodel.workflow_domain import Subtraject
from domainmodel.reftypes import RefTypes
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#https://www.hl7.org/fhir/coverage.html
class Zorgverzekering(DvEntity): #COVERAGE
    class Default(Sat):
        begindatum= Columns.DateColumn() #coverage.period
        einddatum = Columns.DateColumn() #coverage.period
        soort = Columns.TextColumn() #coverage.type
        verzekerdenummer = Columns.TextColumn() #coverage.subscriberId
        bin = Columns.TextColumn()

class Verkoopprijs(DvEntity):
    """
    Business key: AGB-code + Zorginkoopcombinatiecode
    """

    class Default(Sat):
        declaratie_code = Columns.RefColumn(RefTypes.dbc_declaraties)
        prijs_integraal = Columns.FloatColumn()
        prijs_ziekenhuis = Columns.FloatColumn()
        prijs_honorarium_poorter = Columns.FloatColumn()
        prijs_honorarium_ondersteuner = Columns.FloatColumn()
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()


#https://www.hl7.org/fhir/claim.html
class Declaratie(DvEntity):

    class Default(Sat):
        ruleset = Columns.TextColumn(fhir_name='ruleset')
        type = Columns.TextColumn(fhir_name='type')
        factuurnummer = Columns.TextColumn()
        factuurdatum = Columns.DateColumn()
        is_credit = Columns.TextColumn()

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


#todo kan overerven van declaratie / FHIR=Claim?
class Factuurregel(DvEntity):

    class Default(Sat):
        omzet_totaal = Columns.FloatColumn()
        omzet_kostendeel = Columns.FloatColumn()
        omzet_honorarium_poort = Columns.FloatColumn()
        omzet_honorarium_ondersteuners = Columns.FloatColumn()
        factuurdatum = Columns.DateColumn()
        is_credit = Columns.TextColumn()


    class Subtraject(Sat):
        behandelend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        diagnose_code = Columns.RefColumn(RefTypes.dbc_diagnoses)
        zorgtype = Columns.RefColumn(RefTypes.dbc_zorgtypes)
        zorgvraag = Columns.RefColumn(RefTypes.dbc_zorgvraag_codes)
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        verwijscode = Columns.RefColumn(RefTypes.dbc_verwijscodes)
        afsluitreden = Columns.RefColumn(RefTypes.dbc_afsluitredenen)
        zorgproduct_code = Columns.RefColumn(RefTypes.dbc_zorgproducten)
        declaratie_code = Columns.RefColumn(RefTypes.dbc_declaraties)
        icd10_diagnose = Columns.TextColumn()
        behandeling_naam = Columns.TextColumn()
        behandeling_zijde = Columns.TextColumn()
        subtrajectnummer = Columns.TextColumn()
        subtrajectnummer = Columns.TextColumn()
        uzovinummer = Columns.TextColumn()
        verwijzer = Columns.TextColumn()

    class Zorgtraject(Sat):
        zorgtrajectnummer = Columns.TextColumn()
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()

    class Sleutels(Sat):
        patient_nr = Columns.TextColumn()
        vestiging_agb = Columns.TextColumn()
        nummer = Columns.TextColumn()
        extern_nummer = Columns.TextColumn()
        code = Columns.TextColumn()
        bron_id = Columns.TextColumn()
        factuurnummer = Columns.TextColumn()
        factuurregelnummer = Columns.TextColumn()

    class Grouper(Sat):
        grouper_versie = Columns.TextColumn()
        groupercertificaatversie = Columns.TextColumn()
        hashzpzv = Columns.TextColumn()

    class Verzekering(Sat):
        assurantiepolis = Columns.TextColumn()
        debiteurnaam = Columns.TextColumn()

########################################################
# LINKS
########################################################

class ZorgactiviteitPatient(Link):
    zorgactiviteit = LinkReference(Zorgactiviteit)
    patient = LinkReference(Patient)


class ZorgverzekeringVerzekeraar(Link):
    zorverzekering = LinkReference(Zorgverzekering)  # coverage.bin
    Zorgverzekeraar = LinkReference(Zorgverzekeraar)  # coverage.Issuer


class ZorgverzekeringPatient(Link):
    zorverzekering = LinkReference(Zorgverzekering)  # coverage.bin
    patient = LinkReference(Patient)  # coverage.subscriber


class FactuurregelSubtrajectLink(Link):
    factuurregel = LinkReference(Factuurregel)
    patient = LinkReference(Patient)
    subtraject = LinkReference(Subtraject)


class ZorgverzekeringParticipatieLink(Link):
    patient = LinkReference(Patient)
    verzekeraar = LinkReference(Zorgverzekeraar)


class VerkoopprijsParticipatieLink(Link):
    zorgaanbieder = LinkReference(Zorgaanbieder)
    inkoopcombinatie = LinkReference(Zorginkoopcombinatie)