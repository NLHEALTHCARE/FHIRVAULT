from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, DvValuesetEntity, Link, LinkReference


class Zorgproductgroep(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        code = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()

class Tarief(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        code = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        declaratiecode = Columns.TextColumn()
        omschrijving_declaratiecode = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        specialisme_code = Columns.RefColumn('specialismen')
        agb_uitvoerder= Columns.TextColumn()
        productgroepcode= Columns.TextColumn()
        tarief= Columns.FloatColumn()
        kostensoort= Columns.RefColumn('kostensoorten')
        tarieftype= Columns.RefColumn('tarieftypes')
        declaratie_eenheid= Columns.RefColumn('declaratie_eenheden')
        tariefsoort= Columns.RefColumn('tariefsoorten')
        segment_aanduiding= Columns.TextColumn()
        honorarium_soort= Columns.RefColumn('honorarium_soorten')
        declaratie_regel= Columns.TextColumn()


class Zorgactiviteit(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        code = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        omschrijving_consument = Columns.TextColumn()
        op_nota = Columns.BoolColumn()
        extra = Columns.JsonColumn()

class DiagnoseCombinatie(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        dbc1 = Columns.TextColumn()
        dbc2 = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        indicatie = Columns.TextColumn()
        specialisme_code = Columns.RefColumn('specialismen')

class AfsluitRegel(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        code = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        specialisme_code = Columns.RefColumn('specialismen')
        component_types = Columns.RefColumn('afsluitregel_component_types')
        component_code = Columns.TextColumn()
        groepsnummer = Columns.TextColumn()

class AfsluitReden(DvEntity):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    class Default(Sat):
        code = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        omschrijving_kort = Columns.TextColumn()
        ingangsdatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()

###########################
#LINKS
###########################
class ZorgproductgroepTariefLink(Link):
    _schema_name = 'valset'
    zorgproductgroep = LinkReference(Zorgproductgroep)
    tarief = LinkReference(Tarief)