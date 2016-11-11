from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference
from domainmodel_fhir.identity_domain import Organization

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

##### PATIENT MANAGEMENT #####

class EpisodeOfCare(DvEntity):
    class Default(Sat):
        status = Columns.TextColumn()
        type = Columns.TextArrayColumn()
        period = Columns.FHIR.PeriodColumn()

    class Identifier(HybridSat):
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary (If known)'
        use = Columns.TextColumn(default_value=Types.official)
        id_type = Columns.FHIR.CodeableConceptColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()

    class Statushistory(HybridSat):
        class Types(HybridSat.Types):
            planned = 'planned'
            waitlist = 'waitlist'
            active = 'active'
            onhold = 'onhold'
            finished = 'finished'
            cancelled = 'cancelled'
        status = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn

    #careteam
    class EpisodeOfCareOrganizationLink(Link):
        episodeofcare = LinkReference(EpisodeOfCare)
        organization = LinkReference(Organization)

        class Default(Sat):
            role = Columns.FHIR.CodeableConceptColumn()
            period = Columns.FHIR.PeriodColumn

