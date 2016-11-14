from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference
from domainmodel_fhir.identity_domain import Organization, Practitioner, Patient

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

##### PATIENT MANAGEMENT #####

# https://www.hl7.org/fhir/episodeofcare.html
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


class EpisodeOfCarePatientLink(Link):
    episodeofcare = LinkReference(EpisodeOfCare)
    patient = LinkReference(Patient)


class EpisodeOfCareManagingOrganizationLink(Link):
    episodeofcare = LinkReference(EpisodeOfCare)
    organization = LinkReference(Organization)


class EpisodeOfCarePCareManagerLink(Link):
    episodeofcare = LinkReference(EpisodeOfCare)
    practitioner = LinkReference(Practitioner)


class EpisodeOfCareCareTeamLink(Link):
    episodeofcare = LinkReference(EpisodeOfCare)
    organization = LinkReference(Organization)
    practitioner = LinkReference(Practitioner)

    class Default(Sat):
        role = Columns.FHIR.CodeableConceptColumn()
        period = Columns.FHIR.PeriodColumn

# class EpisodeOfCareConditionLink(Link):
#     episodeofcare = LinkReference(EpisodeOfCare)
#     condition = LinkReference(Condition)
#
# class EpisodeOfCareReferralRequestLink(Link):
#     episodeofcare = LinkReference(EpisodeOfCare)
#     referralrequest = LinkReference(ReferralRequest)

# Contact : https://www.hl7.org/fhir/encounter.html
# Afspraak: https://www.hl7.org/fhir/appointment.html
# Labresult: https://www.hl7.org/fhir/observation.html
#

