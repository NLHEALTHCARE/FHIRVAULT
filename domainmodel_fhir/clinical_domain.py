from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference
from domainmodel_fhir.identity_domain import Organization, Practitioner, Patient

#########################################################################################################
#                                                                                                       #
# Domeinmodel volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

##### GENERAL #####


# https://www.hl7.org/fhir/condition.html
class Condition(DvEntity):
    class Default(Sat):

        class CategoryTypes:
            complaint = 'Complaint'
            symptom = 'Symptom'
            finding = 'Finding'
            diagnosis = 'Diagnosis'

        class ClinicalStatusTypes:
            active = 'Active'
            relapse = 'Relapse'
            remission = 'Remission'
            resolved = 'Resolved'

        class VerificationStatusTypes:
            provisional = 'Provisional'
            differential = 'Differential'
            confirmed = 'Confirmed'
            refuted = 'Refuted'
            entered_in_error = 'Entered in error'
            unknown = 'Unknown'

        dateRecorded = Columns.DateColumn()
        code = Columns.FHIR.CodeableConceptColumn()
        category = Columns.FHIR.CodeableConceptColumn()
        clinicalStatus = Columns.TextColumn()
        verificationStatus = Columns.TextColumn()
        severity = Columns.FHIR.CodeableConceptColumn()

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

    class Bodysite(Sat):
        bodysite = Columns.FHIR.CodeableConceptColumn()

    class Extra(Sat):
        onset = Columns.JsonColumn()
        abatement = Columns.JsonColumn()
        evidence = Columns.JsonColumn()
        notes = Columns.JsonColumn


# CAREPROVISION
class ReferralRequest(DvEntity):
    class Default (Sat):
        class StatusTypes():
            draft = 'draft'
            requested = 'requested'
            active = 'active'
            cancelled = 'cancelled'
            accepted = 'accepted'
            rejected = 'rejected'
            completed = 'completed'

        status = Columns.TextColumn()
        date = Columns.DateTimeColumn()
        type = Columns.FHIR.CodeableConceptColumn()
        specialty = Columns.FHIR.CodeableConceptColumn()
        priority = Columns.FHIR.CodeableConceptColumn()
        dateSent = Columns.DateTimeColumn
        reason = Columns.FHIR.CodeableConceptColumn()
        description = Columns.TextColumn()
        serviceRequested = Columns.FHIR.CodeableConceptColumn()
        fulfillmentTime = Columns.FHIR.PeriodColumn()

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


class ReferralRequestPatientLink(Link):
    referralrequest = LinkReference(ReferralRequest)
    patient = LinkReference(Patient)


class ReferralRequestRequesterLink(Link):
    referralrequest = LinkReference(ReferralRequest)
    practitioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)


class ReferralRequestRecipientLink(Link):
    referralrequest = LinkReference(ReferralRequest)
    practitioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)


# class ConditionAssessmentLink(Link)
#     condition = LinkReference(condition)
#     clinicalimpression = LinkReference(ClinicalImpression)
#     diagnosticreport = LinkReference(DiagnosticReport)
#
#     class Default:
#         summary = Columns.TextColumn


