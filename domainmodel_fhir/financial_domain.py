from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference
from domainmodel_fhir.identity_domain import Organization, Practitioner, Patient
from domainmodel_fhir.clinical_domain import Condition, ReferralRequest
from domainmodel_fhir.workflow_domain import  EpisodeOfCare, Encounter

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################


### BILLING ###

# https://www.hl7.org/fhir/claim.html
class Claim(DvEntity):
    class Default(Sat):

        class ClaimTypes:
            institutional = 'Institutional'
            oral = 'Oral'
            pharmacy = 'Pharmacy'
            professional = 'Professional'
            vision = 'Vision'

        class Uses:
            complete = 'Complete'
            proposed = 'Proposed'
            exploratory = 'exploratory'
            other = 'Other'

        ruleset = Columns.FHIR.CodingColumn()
        originalruleset = Columns.FHIR.CodingColumn()
        type = Columns.TextColumn()
        created = Columns.DateTimeColumn()
        use = Columns.TextColumn()
        priority = Columns.TextColumn()
        fundsReserve = Columns.TextColumn()
        school = Columns.TextColumn()
        accident = Columns.DateTimeColumn()
        accidentType = Columns.FHIR.CodingColumn()

    class Identifier(HybridSat):
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary'

        use = Columns.TextColumn(default_value=Types.official)
        id_type = Columns.FHIR.CodeableConceptColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()


##CODING elementen (0 *)
# condition (coding)
# exception (coding)
# interventionException (coding)
# additionalMaterials (coding)

## ITEM (0 *)
# sequence	positiveInt
# type	Coding
# provider	Reference(Practitioner)
# diagnosisLinkId	positiveInt
# service	Coding
# serviceDate	date
# quantity	SimpleQuantity
# unitPrice	Money
# factor	decimal
# points	decimal
# net	Money
# udi	Coding
# bodySite	Coding
# subSite	Coding
# modifier	Coding
    ## DETAIL (0 *)
    # sequence	positiveInt
    # type	Coding
    # service	Coding
    # quantity	SimpleQuantity
    # unitPrice	Money
    # factor	decimal
    # points	decimal
    # net	Money
    # udi	Coding
        # SUBDETAIL (0 *)
        # sequence	positiveInt
        # type	Coding
        # service	Coding
        # quantity	SimpleQuantity
        # unitPrice	Money
        # factor	decimal
        # points	decimal
        # net	Money
        # udi	Coding
    # prosthesis	BackboneElement
    # initial	boolean
    # priorDate	date
    # priorMaterial	Coding
# missingTeeth	BackboneElement
# tooth	Coding
# reason	Coding
# extractionDate	date

# diagnosis
# sequence
# diagnosis

## COVERAGE
# sequence
# focal
# coverage
# businessArrangement
# relationship
# preAuthRef
# claimResponse
# originalRuleset


# LINKS
class ClaimPayeeLink(Link):
    claim = LinkReference(Claim)
    practitioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)
    patient = LinkReference(Patient)

    class Default(Sat):

        class Types(HybridLink.Types):
            subscriber = 'subscriber'
            provider = 'provider'
            other = 'other'
        type = Columns.TextColumn(default_value=Types.other)


class ClaimTargetOrganizationLink(Link):
    claim = LinkReference(Claim)
    organization = LinkReference(Organization)


class ClaimProviderLink(Link):
    claim = LinkReference(Claim)
    practitioner = LinkReference(Practitioner)


class ClaimOrganizationLink(Link):
    claim = LinkReference(Claim)
    organization = LinkReference(Organization)


class ClaimEntererLink(Link):
    claim = LinkReference(Claim)
    practitioner = LinkReference(Practitioner)


class ClaimReferralRequestLink(Link):
    claim = LinkReference(Claim)
    referralrequest = LinkReference(ReferralRequest)


class ClaimPatientLink(Link):
    claim = LinkReference(Claim)
    patient = LinkReference(Patient)


class ClaimProviderLink(Link):
    claim = LinkReference(Claim)
    practitioner = LinkReference(Practitioner)


# class ClaimFacilityLink(Link):
#     claim = LinkReference(Claim)
#     location = LinkReference(Location)
# prescription	Reference(MedicationOrder|VisionPrescription)
# originalPrescription	Reference(MedicationOrder)



