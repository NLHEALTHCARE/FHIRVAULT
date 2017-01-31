from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *
from pyelt.datalayers.valset import *


class ValueSetsEnum:
    """Referentie types omvatten alle code systems en value sets die binnen het NL Healthcare domein model worden gebruikt.

    De codes worden gebruikts in de SATs. Door de joinen op de referentie tabellen kunnen omschrijvingen, hierachieen
    etc. worden gebruikt. In HL7 RIM wordt dit aangeduid als Coded No Exceptions (CNE).
    """

    # ISO 5218, https://nl.wikipedia.org/wiki/ISO_5218,
    # hetzelfde als COD046-NEN zoals aanbevolen door Vektis http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD046&Co_Or_Code=NEN

    geslacht_types = 'geslacht_types'

    # ISO 3166-2, https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2,
    # hetzelfde als COD032-NEN zoals aanbevolen gebruikt door Vektis http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD032&Co_Or_Code=NEN
    land_codes = 'land_codes'

    # ZIBS / Nictiz naamgebruik codelijst
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    naamgebruik_codes = 'naamgebruik_codes'

    # ZIBS / Nictiz organisatietype codelijst. NB: alleen zorginstellingen, geen generieke organisatie types!?
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    organisatie_types = 'organisatie_types'

    # ZIBS / Nictiz producttype codelijst gebaseerd op UNSPSC
    # https://www.unspsc.org/  Nederlandse versie te koop voor USD 100,-
    product_type_codes = 'product_type'

    # Codelijst voor (familiare) relaties
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    relatie_codes = 'relatie_codes'

    # Codelijst voor rollen van contactpersonen in relatie tot andere personen c.q. patienten
    # https://decor.nictiz.nl/art-decor/decor-valuesets--zib1bbr-?id=2.16.840.1.113883.2.4.3.11.60.40.2.3.1.1&effectiveDate=2015-04-01T00:00:00
    rol_codes = 'rol_codes'

    # Codelijst Vektis AGB medische specialismen
    # COD016-VEKT http://ei.vektis.nl/WespCodelijstenDetail.aspx?Co_Ge_Code=COD016&Co_Or_Code=VEKT
    specialisme_codes = 'specialisme_codes'
    specialisme_details_codes = 'specialisme_details_codes'

    # Alle DBC codelijsten conform http://werkenmetdbcs.nza.nl/werken-met-dbcs/frontpage/menu-ID-2350
    # Verschillende codestelsels voor Ziekenhuiszorg (RZ), GGZ (RG), Geriatrische Revalidatiezorg (GRZ) en Forensische Zorg (RF)
    # Technisch zijn de ziekenhuiszorg en grz hetzelfde

    # Ziekenhuiszorg met prefix DBC
    dbc_afsluitredenen = 'dbc_afsluitredenen'
    dbc_declaraties = 'dbc_declaraties'
    dbc_diagnoses = 'dbc_diagnoses'
    dbc_zorgactiviteiten = 'dbc_zorgactiviteiten'
    dbc_zorgproducten = 'dbc_zorgproducten'
    dbc_zorgtypes = 'dbc_zorgtypes'
    dbc_zorgvraag_codes = 'dbc_zorgvraag_codes'
    dbc_verwijscodes = 'dbc_verwijscodes'

    # DHD
    cbv_codes = 'cbv_codes'

    # GGZ met prefix ggz
    ggz_activiteiten = 'ggz_activiteiten'
    ggz_beroepen = 'ggz_beroepen'
    ggz_hoofdberoepen = 'ggz_hoofdberoepen'
    ggz_circuits = 'ggz_circuits'
    ggz_diagnoses = 'ggz_diagnoses'
    ggz_redenensluiten = 'ggz_redenensluiten'
    ggz_zorgtypes = 'ggz_zorgtypes'
    ggz_productgroepen = 'ggz_productgroepen'
    ggz_prestatiecodes = 'ggz_prestatiecodes'
    ggz_tarief_code = 'ggz_tarief_code'
    ggz_activiteit_tarief_codes = 'ggz_activiteit_tarief_codes'

    # zorginkoopcombinatie
    zorginkoopcombinatie_codes = 'zorginkoopcombinatie_codes'

    # welke zijn dit? Nog op te zoeken
    academische_titels = 'academische_titels'
    adelijke_titels = 'adelijke_titels'
    traject_status_codes = 'traject_status_codes'
    gebeurtenis_status_codes = 'gebeurtenis_status_codes'
    vektis_praktijk_statussen = 'vektis_praktijk_statussen'
    vektis_verbijzonderingscodes = 'vektis_verbijzonderingscodes'
    subtraject_status = 'subtraject_status_codes'



class Valueset(DvValueset):
    valueset_naam = Columns.TextColumn()
    code = Columns.TextColumn()
    omschrijving = Columns.TextColumn()


class Zorgproduct(DvValueset):
    omschrijving_latijn = Columns.TextColumn()
    omschrijving_consument = Columns.TextColumn()
    declaratie_code_verzekerde_zorg = Columns.TextColumn()
    declaratie_code_onverzekerde_zorg = Columns.TextColumn()
    wbmv_code = Columns.TextColumn()
    zorgproductgroep_code = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()

class Zorgproductgroep(DvValueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'

    code = Columns.TextColumn()
    omschrijving = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()

class Tarief(DvValueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'

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


class Zorgactiviteit(DvValueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'

    code = Columns.TextColumn()
    omschrijving = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()
    omschrijving_consument = Columns.TextColumn()
    op_nota = Columns.BoolColumn()
    extra = Columns.JsonColumn()
    groep_code = Columns.TextColumn()
    groep_omschrijving = Columns.TextColumn()
    wbmv_code = Columns.TextColumn()
    is_addon = Columns.BoolColumn()
    is_landelijke_code=  Columns.BoolColumn()

class Specialisme(DvValueset):
    pass


class Zorgtype(DvValueset):
    omschrijving_lang= Columns.TextColumn()
    subgroep_code= Columns.TextColumn()
    subgroep_omschrijving_kort= Columns.TextColumn()
    subgroep_omschrijving_lang= Columns.TextColumn()
    hoofdgroep_code= Columns.TextColumn()
    hoofdgroep_omschrijving_kort= Columns.TextColumn()
    hoofdgroep_omschrijving_lang= Columns.TextColumn()
    ingangsdatum= Columns.DateColumn()
    einddatum= Columns.DateColumn()

class Zorgvraag(DvValueset):
    omschrijving_lang= Columns.TextColumn()
    subgroep_code= Columns.TextColumn()
    subgroep_omschrijving_kort= Columns.TextColumn()
    subgroep_omschrijving_lang= Columns.TextColumn()
    hoofdgroep_code= Columns.TextColumn()
    hoofdgroep_omschrijving_kort= Columns.TextColumn()
    hoofdgroep_omschrijving_lang= Columns.TextColumn()
    ingangsdatum= Columns.DateColumn()
    einddatum= Columns.DateColumn()

class Behandeling(DvValueset):
    omschrijving_lang= Columns.TextColumn()
    subgroep_code= Columns.TextColumn()
    subgroep_omschrijving_kort= Columns.TextColumn()
    subgroep_omschrijving_lang= Columns.TextColumn()
    hoofdgroep_code= Columns.TextColumn()
    hoofdgroep_omschrijving_kort= Columns.TextColumn()
    hoofdgroep_omschrijving_lang= Columns.TextColumn()
    ingangsdatum= Columns.DateColumn()
    einddatum= Columns.DateColumn()

class Diagnose(DvValueset):
    omschrijving_lang= Columns.TextColumn()
    subgroep_code= Columns.TextColumn()
    subgroep_omschrijving_kort= Columns.TextColumn()
    subgroep_omschrijving_lang= Columns.TextColumn()
    hoofdgroep_code= Columns.TextColumn()
    hoofdgroep_omschrijving_kort= Columns.TextColumn()
    hoofdgroep_omschrijving_lang= Columns.TextColumn()
    ingangsdatum= Columns.DateColumn()
    einddatum= Columns.DateColumn()
    specialisme_code = Columns.RefColumn('specialismen')
    diagnose_groep = Columns.TextColumn()
    


class DiagnoseCombinatie(DvValueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'
    code = Columns.TextColumn()
    dbc1 = Columns.TextColumn()
    dbc2 = Columns.TextColumn()
    omschrijving = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()
    indicatie = Columns.TextColumn()
    specialisme_code = Columns.RefColumn('specialismen')

class AfsluitRegel(Valueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'

    code = Columns.TextColumn()
    omschrijving = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()
    specialisme_code = Columns.RefColumn('specialismen')
    component_types = Columns.RefColumn('afsluitregel_component_types')
    component_code = Columns.TextColumn()
    groepsnummer = Columns.TextColumn()

class AfsluitReden(DvValueset):
    """Standaard definitie nog opzoeken.
    """
    _schema_name = 'valset'

    code = Columns.TextColumn()
    omschrijving = Columns.TextColumn()
    omschrijving_kort = Columns.TextColumn()
    ingangsdatum = Columns.DateColumn()
    einddatum = Columns.DateColumn()

###########################
#LINKS
###########################
# class ZorgproductgroepTariefLink(Link):
#     _schema_name = 'valset'
#     zorgproductgroep = LinkReference(Zorgproductgroep)
#     tarief = LinkReference(Tarief)

class Datum(DvValueset):
    """Zie dim_dag uit dwh1
    """
    datum = Columns.DateColumn()
    iso_week = Columns.IntColumn()
    maand = Columns.IntColumn()
    kwartaal = Columns.TextColumn()
    jaar = Columns.IntColumn()
    jaar_iso_week = Columns.TextColumn()
    jaar_maand = Columns.TextColumn()
    jaar_kwartaal = Columns.TextColumn()
    volgnummer_dag = Columns.IntColumn()
    volgnummer_maand = Columns.IntColumn()
    volgnummer_jaar = Columns.IntColumn()
    label = Columns.TextColumn()

class Buurt(DvValueset):
    """CBS buurten
    postcode, huisnummer, gemeenteco, gemeentena, wijkcode, wijknaam, buurtcode, buurtmnaam
    """
    postcode = Columns.TextColumn()
    huisnummer = Columns.TextColumn()
    gemeente_code = Columns.TextColumn()
    gemeentenaam = Columns.TextColumn()
    wijk_code = Columns.TextColumn()
    buurt_code = Columns.TextColumn()
    buurtnaam = Columns.TextColumn()


###########################
#LINKS
###########################
# class ZorgproductgroepTariefLink(Link):
#     _schema_name = 'valset'
#     zorgproductgroep = LinkReference(Zorgproductgroep)
#     tarief = LinkReference(Tarief)