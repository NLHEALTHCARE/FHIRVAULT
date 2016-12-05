from domainmodel_fhir.identity_domain import *
from domainmodels.act_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, HybridSat, LinkReference


class Zorgverzekering(DvEntity, Zorgverzekering):

    class Default(Sat):
        begindatum= Columns.DateColumn() #coverage.period
        einddatum = Columns.DateColumn() #coverage.period
        soort = Columns.TextColumn() #coverage.type
        verzekerdenummer = Columns.TextColumn() #coverage.subscriberId
        bin = columns.TextColumn()

# LINKS
class ZorgverzekeringVerzekeraar(Link):
    zorverzekering = LinkReference(Zorgverzekering) #coverage.bin
    Zorgverzekeraar = LinkReference(Zorgverzekeraar) #coverage.Issuer


class ZorgverzekeringPatient(Link):
    zorverzekering = LinkReference(Zorgverzekering) #coverage.bin
    patient = LinkReference(Patient) #coverage.subscriber