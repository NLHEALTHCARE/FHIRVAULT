
from domainmodel.identity_domain import Patient, Zorgverlener, Zorgverzekeraar
from domainmodel.workflow_domain import Subtraject, Zorgaanbieder
from domainmodel.valueset_domain import ValueSetsEnum
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, HybridSat, LinkReference

"""Alle resources die te maken hebben met de zorg, zoals zorgactiviteit, diagnose"""

class Zorgactiviteit(DvEntity):
    """Business key: AGB-code zorgaanbieder + subtrajectnummer
    """

    class Identificatie(Sat):
        nummer = Columns.TextColumn()  # uniek zorgactiviteitnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        bron_id = Columns.TextColumn()
        zorgtrajectnummer = Columns.TextColumn()

    class Default(Sat):
        zorgactiviteitcode = Columns.RefColumn(ValueSetsEnum.dbc_zorgactiviteiten)
        interne_verrichtingcode = Columns.TextColumn()
        begindatumtijd = Columns.DateTimeColumn()
        einddatumtijd = Columns.DateTimeColumn()
        aantal = Columns.FloatColumn()
        aanvragend_specialisme = Columns.RefColumn(ValueSetsEnum.specialisme_codes)
        uitvoerend_specialisme = Columns.RefColumn(ValueSetsEnum.specialisme_codes)
        cbv_code = Columns.RefColumn(ValueSetsEnum.cbv_codes)  # CBV verrichtingcodes zijn veel uitgebreider dan DBC Zorgactiviteitcodes
        anatomische_locatie = Columns.TextColumn()


    #Todo: JVL naamgeving? wat doen we met OZP dan ook seperate SAT?
    class AddOn(Sat):
        "Kenmerken wanneer zorgactiviteit een los te declareren add-on betreft"
        declaratiecode = Columns.RefColumn(ValueSetsEnum.dbc_declaraties)
        add_on_informatie = Columns.TextColumn()

class Diagnose(DvEntity):
    class Identificatie(Sat):
        nummer = Columns.TextColumn()

    class Default(Sat):
        naam = Columns.TextColumn()

##############################
# LINKS
##############################

class SubtrajectZorgactiviteitLink(Link):
    patient = LinkReference(Patient)
    subtraject = LinkReference(Subtraject)
    zorgactiviteit = LinkReference(Zorgactiviteit)

class SubtrajectDiagnoseLink(Link):
    subtraject = LinkReference(Subtraject)
    diagnose = LinkReference(Diagnose)

class ZorgactviteitDeelnemersLink(Link):
    """
    Definitie van Grouper heeft 1..1 relaties voor participanten, vandaar in vaste kolommen
    """
    zorgactiviteit = LinkReference(Zorgactiviteit)
    patient = LinkReference(Patient)
    aanvragende_zorgaanbieder = LinkReference(Zorgaanbieder)
    aanvragende_zorgverlener = LinkReference(Zorgverlener)
    uitvoerende_zorgaanbieder = LinkReference(Zorgaanbieder)
    uitvoerende_zorgverlener = LinkReference(Zorgverlener)
    betaler = LinkReference(Zorgverzekeraar)
#

