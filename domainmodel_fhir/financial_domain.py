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

    class Ruleset(Sat):
        system = Columns.TextColumn()
        version = Columns.TextColumn()
        code = Columns.TextColumn()
        display = Columns.TextColumn()
        userselected = Columns.BoolColumn()

    class originalRuleset(Sat):
        system = Columns.TextColumn()
        version = Columns.TextColumn()
        code = Columns.TextColumn()
        display = Columns.TextColumn()
        userselected = Columns.BoolColumn()

    type = Columns.TextColumn()
    created = Columns.DateTimeColumn

