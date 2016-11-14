from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference
from domainmodel_fhir.identity_domain import Organization, Practitioner, Patient
from domainmodel_fhir.clinical_domain import Condition, ReferralRequest

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

# https://www.hl7.org/fhir/encounter.html
class Encounter(DvEntity):
    class Default:
        status = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()
        Encounterclass = Columns.TextColumn()
        type = Columns.FHIR.CodeableConceptColumn()
        priority = Columns.FHIR.CodeableConceptColumn()
        period = Columns.FHIR.CodeableConceptColumn()
        length = Columns.IntColumn()
        reason = Columns.FHIR.CodeableConceptColumn()

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
            arrived = 'arrived'
            in_progress = 'in-progress'
            onleave = 'onleave'
            finished = 'finished'
            cancelled = 'cancelled'
        status = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn

    class Extra(Sat):
        hospitalization = Columns.JsonColumn()


class EncounterEncounter(Link):
    encounter = LinkReference(Encounter)
    part_of = LinkReference(Encounter)


class EncounterPatient(Link):
    encounter = LinkReference(Encounter)
    patient = LinkReference(Patient)


class EncounterEpisodeOfCare(Link):
    encounter = LinkReference(Encounter)
    episodeofcare = LinkReference(EpisodeOfCare)


class EncounterReferralRequest(Link):
    encounter = LinkReference(Encounter)
    referralrequest = LinkReference(ReferralRequest)


class EncounterIndication(Link):
    encounter = LinkReference(Encounter)
    condition = LinkReference(Condition)
    # procedure = LinkReference(Procedure)


class EncounterParticipantLink(Link):
    encounter = LinkReference(Encounter)
    # relatedperson = LinkReference(RelatedPerson)
    practitioner = LinkReference(Practitioner)

    class Default(Sat):
        type = Columns.FHIR.CodeableConceptColumn()
        period = Columns.FHIR.PeriodColumn


# class EncounterAppointment(Link):
#     encounter = LinkReference(Encounter)
#     Appointment = LinkReference(Appointment)


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

