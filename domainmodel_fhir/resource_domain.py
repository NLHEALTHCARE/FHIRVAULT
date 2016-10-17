from domainmodel_fhir.element_domain import CodeableConcept, Coding, Period, HumanName
from domainmodels.entity_domain import RefTypes  # todo: RefTypes in fhir_domain.py zelf definieren?
from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################



""" Resource classes (Patient is een DomainResource) """


class Patient(DvEntity, Entity):   # FHIR type: DomainResource (http://hl7.org/fhir/domainresource.html#1.20)

    class Default(Sat):
        active = Columns.BoolColumn()  # patient record active?
        gender = Columns.RefColumn(RefTypes.geslacht_types)
        birthdate = Columns.DateColumn()
        # deceased + deceased_date voorbeeld van "type[x]" , meer dan 1 datatype voor content. (=polymorphic in OO)
        # voor meer info zie http://hl7.org/fhir/formats.html#choice
        deceased_boolean = Columns.BoolColumn()
        deceased_datetime = Columns.DateTimeColumn()
        # type[x]
        multiple_birth_boolean = Columns.BoolColumn()
        multiple_birth_integer = Columns.IntColumn()

    class Identifier(HybridSat):      #FHIR type: Element (http://hl7.org/fhir/element.html#1.21.0)
        class use(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary (If known)'

        text = CodeableConcept.text
        system = Coding.system   #system heeft FIHR type: uri; Uniform Resource Identifier ( http://hl7.org/fhir/datatypes.html#uri)
        version = Coding.version
        code = Coding.code  # symbool in syntax gedefinieerd door het systeem (http://hl7.org/fhir/datatypes.html#code)
        display = Coding.display  # weergave gedefinieerd door het systeem
        user_selected = Coding.user_selected  # indien deze codering door de user zelf was gekozen

        start = Period.start
        period_end = Period.end

    class Name(HybridSat):
        class use(HybridSat.Types):     # zie ook utility class HumanName; #todo wat is de meest logische plaats voor deze hybridsat?
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            nickname = 'nickname'
            anonymous = 'anonymous'
            old = 'old'
            maiden = 'maiden'
        text = HumanName.text
        family = HumanName.family   # family name (or surname)
        given = HumanName.given
        prefix = HumanName.prefix
        suffix = HumanName.suffix
        start = HumanName.start
        end = HumanName.end







