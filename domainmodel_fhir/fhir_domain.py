from domainmodels.entity_domain import RefTypes  # todo: RefTypes in fhir_domain.py zelf definieren?
from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################


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
        class type(HybridSat.Types):    # type heeft FHIR type: CodeableConcept (http://hl7.org/fhir/datatypes.html#codeableconcept)
            text = Columns.TextColumn() # plain text weergave van het concept
            class coding(HybridSat.Types.Coding):  # coding heeft FHIR type: Element; todo: hoe om te gaan met deze extra laag? HybridSat.Types.Coding bestaat nog niet
                system = Columns.TextColumn()   #system heeft FIHR type: uri; Uniform Resource Identifier ( http://hl7.org/fhir/datatypes.html#uri)
                text = Columns.TextColumn() # string that represents the concept; identiteit van terminologie systeem
                version = Columns.TextColumn()
                code = Columns.TextColumn()  # symbool in syntax gedefinieerd door het systeem (http://hl7.org/fhir/datatypes.html#code)
                display = Columns.TextColumn()  # weergave gedefinieerd door het systeem
                user_selected = Columns.BoolColumn()  # indien deze codering door de user zelf was gekozen



