from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference


class Organization(DvEntity):
    class Default(Sat):
        active = Columns.BoolColumn()
        name = Columns.TextColumn()

    class Identifier(HybridSat):
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary (If known)'

        use = Columns.TextColumn(default_value=Types.official)
        org_type = Columns.FHIR.CodeableConceptColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()

    #todo: afmaken mat andere sats

class OrganizationOrganizationLink(Link):
    organization = LinkReference(Organization)
    linked_to_organization = LinkReference(Organization)
