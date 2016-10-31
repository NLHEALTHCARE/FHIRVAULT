from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference
from domainmodels.hl7rim_base_domain import *

class Gewoon(DvEntity, Entity):
    """ gemaakt voor testen van "gewone data"
    """

    class HL17(Sat):
        pass

    class Default(Sat):
        id = Columns.TextColumn()
        waarde1 = Columns.TextColumn()
        waarde2 = Columns.TextColumn()
        waarde3 = Columns.TextColumn()



class JsonbVariant(DvEntity, Entity):
    """ gemaakt voor testen met JsonB data
    """

    class HL17(Sat):
        pass

    class Default(Sat):
        id = Columns.TextColumn()
        details = Columns.JsonColumn()  # bevat waarde1, waarde2 en waarde3; net zoals de "gewone variant"