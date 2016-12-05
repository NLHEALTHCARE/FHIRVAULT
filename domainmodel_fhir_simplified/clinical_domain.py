from domainmodel_fhir.identity_domain import *
from domainmodels.act_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, HybridSat, LinkReference

class Zorgactiviteit(DvEntity, Act): #PROCEDURE

       class Default(Sat):
        zorgactiviteitcode = Columns.RefColumn(RefTypes.dbc_zorgactiviteiten)
        interne_verrichtingcode = Columns.TextColumn()
        begindatumtijd = Columns.DateTimeColumn()
        einddatumtijd = Columns.DateTimeColumn()
        aantal = Columns.FloatColumn()
        aanvragend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        uitvoerend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        cbv_code = Columns.RefColumn(RefTypes.cbv_codes)  # CBV verrichtingcodes zijn veel uitgebreider dan DBC Zorgactiviteitcodes
        anatomische_locatie = Columns.TextColumn()

    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.account)
        act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)

    class Sleutels(Sat):
        nummer = Columns.TextColumn()  # uniek zorgactiviteitnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        bron_id = Columns.TextColumn()
        zorgtrajectnummer = Columns.TextColumn()

    class AddOn(Sat):
        "Kenmerken wanneer zorgactiviteit een los te declareren add-on betreft"
        declaratiecode = Columns.RefColumn(RefTypes.dbc_declaraties)
        add_on_informatie = Columns.TextColumn()


# LINKS
class ZorgactiviteitPatient(Link):
    zorgactiviteit = LinkReference(Zorgactiviteit)
    patient = Link(Patient)


class ZorgverzekeringVerzekeraar(Link):
    zorverzekering = LinkReference(Zorgverzekering)  # coverage.bin
    Zorgverzekeraar = LinkReference(Zorgverzekeraar)  # coverage.Issuer


class ZorgverzekeringPatient(Link):
    zorverzekering = LinkReference(Zorgverzekering)  # coverage.bin
    patient = LinkReference(Patient)  # coverage.subscriber
