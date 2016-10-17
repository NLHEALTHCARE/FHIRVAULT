
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import HybridSat

""" Dit domain bevat 'Element' classes. In FHIR kunnen 'Elements' gebruikt worden door meerdere
    FHIR 'Resources' (zie resource_domain.py) """

""" Element classes"""

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

class HumanName(HybridSat):    #FHIR type: Element
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
humanname = HumanName()
print(type(humanname))
print(type(humanname.use))
print(type(humanname.use.maiden))
print(type(Period.start))
print(type(humanname.start))
