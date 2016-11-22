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


#condition (coding)
#exception (coding)
#interventionException (coding)
#additionalMaterials (coding)

# item	BackboneElement
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
    # detail	BackboneElement
    # sequence	positiveInt
    # type	Coding
    # service	Coding
    # quantity	SimpleQuantity
    # unitPrice	Money
    # factor	decimal
    # points	decimal
    # net	Money
    # udi	Coding
        # subDetail	BackboneElement
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


# diagnosis (SAT?)
# sequence
# diagnosis


#HYBRIDLINK?
# PAYEE
# Type
# provider	Reference(Practitioner)
# organization	Reference(Organization)
# person	Reference(Patient)

# LINKSAT?
# coverage	Σ	0.*	BackboneElement
# sequence	Σ	0.1	positiveInt
# focal	Σ	0.1	boolean
# coverage	Σ	0.1	Reference(Coverage)
# businessArrangement	Σ	0.1	string
# relationship	Σ	0.1	Coding
# preAuthRef	Σ	0.*	string
# claimResponse	Σ	0.1	Reference(ClaimResponse)
# originalRuleset	Σ	0.1	Coding


# LINKS
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



