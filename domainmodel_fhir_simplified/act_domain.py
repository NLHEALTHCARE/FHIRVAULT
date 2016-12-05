from domainmodels.role_domain import *
from domainmodel_fhir.financial_domain import *
from domainmodel_fhir.identity_domain import *

from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, LinkReference


class Zorgverzekering(Coverage):

    class Default(Sat):
        verzekerdenummer = Coverage.subscriberId()
        begindatum = Coverage.begindate()
        einddatum = Coverage.enddate()
        soort = Columns.TextColumn()


