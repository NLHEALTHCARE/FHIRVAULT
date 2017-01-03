from domainmodel.identity_domain import *
from domainmodel.valueset_domain import ValueSetsEnum
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, LinkReference

"""Workflow resources zoals traject, subtraject, afspraak"""


class Zorgtraject(DvEntity):
    class Default(Sat):
        nummer = Columns.TextColumn()  # uniek zorgtrajectnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()

class Subtraject(DvEntity):
    """FHIR Resource = EisodeOfCare
    """
    class Default(Sat):
        behandelend_specialisme = Columns.RefColumn(ValueSetsEnum.specialisme_codes)
        diagnose_code = Columns.RefColumn(ValueSetsEnum.dbc_diagnoses)
        zorgtype = Columns.RefColumn(ValueSetsEnum.dbc_zorgtypes)
        zorgvraag = Columns.RefColumn(ValueSetsEnum.dbc_zorgvraag_codes)
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        verwijscode = Columns.RefColumn(ValueSetsEnum.dbc_verwijscodes)
        zorgproduct_code = Columns.RefColumn(ValueSetsEnum.dbc_zorgproducten)
        declaratie_code = Columns.RefColumn(ValueSetsEnum.dbc_declaraties)
        icd10_diagnose = Columns.TextColumn()
        behandeling_naam = Columns.TextColumn()
        behandeling_zijde = Columns.TextColumn()
        disdatum = Columns.DateColumn()
        uzovinummer = Columns.TextColumn()

    class Status(Sat):
        status = Columns.TextColumn(ValueSetsEnum.subtraject_status)
        afsluitreden = Columns.RefColumn(ValueSetsEnum.dbc_afsluitredenen)

    # Sat met keys
    class Identificatie(Sat):
        patient_nr = Columns.TextColumn()
        vestiging_agb = Columns.TextColumn()
        nummer = Columns.TextColumn()  # uniek subtrajectnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        code = Columns.TextColumn()
        bron_id = Columns.TextColumn()


    class Kenmerken(Sat):
        "Kenmerken die worden achteraf afgeleid op basis van aanwezigheid zorgactiviteiten"
        type = Columns.RefColumn("subtraject_types")  # bijvoorbeeld dbc zorgproduct of add on zorg activiteit
        is_aanspraak_zvw = Columns.BoolColumn()
        is_aanspraak_zvw_toegepast = Columns.BoolColumn()
        heeft_za_machtiging = Columns.BoolColumn()
        heeft_oranje_za = Columns.BoolColumn()
        is_za_vertaling_toegepast = Columns.BoolColumn()
        is_dagbehandeling = Columns.BoolColumn()
        is_klinisch_tot_3_dagen = Columns.BoolColumn()
        is_klinisch_meer_3_dagen = Columns.BoolColumn()


    class Zorgtraject(Sat):
        "Zorgtraject als Sat opnemen, pragmatische oplossing afgekeken van timeff"
        nummer = Columns.TextColumn()           # uniek zorgtrajectnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()    # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()


#todo: JVL aanvliegwijze bespreken m.b.t. het vullen van de entiteiten. Nu de focus wat we hebben terwijl dit andersom wenselijk is

class Afspraak(DvEntity):
    class Default(Sat):
        afspraak_omschrijving = Columns.TextColumn()
        eigenaar = Columns.TextColumn()
        begindatumtijd = Columns.DateTimeColumn()
        einddatumtijd = Columns.DateTimeColumn()
        createdatumtijd = Columns.DateTimeColumn()
        status = Columns.TextColumn()

    class Identificatie(Sat):
        bron_id = Columns.TextColumn()
        extern_nummer = Columns.TextColumn()
        afspraak_omschrijving_code = Columns.TextColumn()
        afspraak_nummer = Columns.TextColumn()

##############################
# LINKS
##############################

class ZorgTrajectSubtrajectLink(Link):
    patient = LinkReference(Patient)
    zorgtraject = LinkReference(Zorgtraject)
    subtraject = LinkReference(Subtraject)

class SubtrajectDeelnemersLink(Link):
    subtraject = LinkReference(Subtraject)
    patient = LinkReference(Patient)
    hoofdbehandelaar = LinkReference(Zorgverlener)
    verwijzer = LinkReference(Zorgverlener)
    verwijzende_instelling = LinkReference(Zorgaanbieder)
    betaler = LinkReference(Zorgverzekeraar)
    huisarts = LinkReference(Zorgverlener)
    instelling = LinkReference(Zorgaanbieder)
    vestiging = LinkReference(Vestiging)


class AfspraakDeelnemersLink(Link):
    patient = LinkReference(Patient)
    afspraak = LinkReference(Afspraak)
    instelling = LinkReference(Zorgaanbieder)
    medewerker = LinkReference(Medewerker)

