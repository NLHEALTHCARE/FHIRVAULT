from domainmodels.entity_domain import RefTypes  # todo: RefTypes in fhir_domain.py zelf definieren?
from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################



class Coding:
    system = Columns.TextColumn()   #system heeft FIHR type: uri; Uniform Resource Identifier ( http://hl7.org/fhir/datatypes.html#uri)
    version = Columns.TextColumn()
    code = Columns.TextColumn()  # symbool in syntax gedefinieerd door het systeem (http://hl7.org/fhir/datatypes.html#code)
    display = Columns.TextColumn()  # weergave gedefinieerd door het systeem
    user_selected = Columns.BoolColumn()  # indien deze codering door de user zelf was gekozen

class CodeableConcept(Coding):  # todo: overerving nodig?
    text = Columns.TextColumn() # plain text weergave van het concept

class Period:    # FHIR type: Element; de class Period wordt niet alleen door de class Identifier (van de class Patient) gebruikt maar ook door andere classes
    start = Columns.DateTimeColumn() # Starting time with inclusive boundary
    end = Columns.DateTimeColumn()  # 	End time with inclusive boundary, if not ongoing

class HumanName:    #FHIR type: Element
    class use(HybridSat.Types):
        usual = 'usual'
        official = 'official'
        temp = 'temp'
        nickname = 'nickname'
        anonymous = 'anonymous'
        old = 'old'
        maiden = 'maiden'
    text = Columns.TextColumn()     # text representation of the full name
    family = Columns.TextColumn()   # family name (or surname)
    given = Columns.TextColumn()    # given names (not always 'first'); includes middle names
    prefix = Columns.TextColumn()   # Parts that come before the name
    suffix = Columns.TextColumn()   # Part that come after the name
    # period_start = Columns.DateTimeColumn(Period.start)
    start = Period.start
    end = Period.end

# todo: mag weg na testen:
# humanname = HumanName()
# print(type(humanname))
# print(type(humanname.use))
# print(type(humanname.use.maiden))
# print(type(Period.start))
# print(type(humanname.start))


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







