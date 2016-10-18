
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
# humanname = HumanName()
# print(type(humanname))
# print(type(humanname.use))
# print(type(humanname.use.maiden))
# print(type(Period.start))
# print(type(humanname.start))

class Reference:
    reference = Columns.TextColumn()    # Relative, internal or absolute URL reference
    display = Columns.TextColumn()      # Text alternative for the resource

class ContactPoint(HybridSat):
    class system(HybridSat.Types): # todo: FHIR remark: ContactPointSystem(Required); verwijst naar een valueset http://hl7.org/fhir/ValueSet/contact-point-system
        phone = 'phone'
        fax = 'fax'
        email = 'email'
        pager = 'pager'
        other = 'other'
    value = Columns.TextColumn()    # the actual contact point details
    class use(HybridSat.Types):     # todo: FHIR remark: ContactPointUse(Required); verwijst naar een valueset http://hl7.org/fhir/valueset-contact-point-use.html
        home = 'home'
        work = 'work'
        temp = 'temp'
        old = 'old'
        mobile = 'mobile'
    rank = Columns.IntColumn()      # moet positieve integer zijn!; specify preferred order of use (1 = highest)
    start = Period.start
    end = Period.end

class Address(HybridSat):
    class use(HybridSat.Types):  # hoe wordt dit adres gebruikt; todo: AddressUse(Required): verwijst naar http://hl7.org/fhir/valueset-address-use.html
        home = 'home'
        work = 'work'
        temp = 'temp'
        old = 'old'

    class type(HybridSat.Types):    # todo: AddressType(Required): verwijst naar http://hl7.org/fhir/ValueSet/address-type
        postal = 'postal'
        physical = 'physical'
        both = 'both'

    text = Columns.TextColumn()         # text representation of the address
    line = Columns.TextColumn()         # street name, number, direction & P.O. Box etc.
    city = Columns.TextColumn()
    district = Columns.TextColumn()     # district name (aka county)
    state = Columns.TextColumn()        # sub_unit of country (abbreviations ok)
    postalcode = Columns.TextColumn()
    country = Columns.TextColumn()      # Country(can be ISO 3166 3 letter code)
    start = Period.start
    end = Period.end


class Attachment:
    content_type = Columns.TextColumn()     # Mime type of the content, with charset etc. ; todo: MimeType (Required) http://www.rfc-editor.org/bcp/bcp13.txt -> soort RefType?
    language = Columns.TextColumn()          # Human language of the content (BPC-47) ; todo: Language (Required) https://tools.ietf.org/html/bcp47
    data = Columns.TextColumn()             # Data inline, base64ed
    url = Columns.TextColumn()              # Uri(Uniform Resource Identifier) where the data can be found
    size = Columns.IntColumn()              # positieve integer; number of bytes of content (if url provided)
    hash = Columns.TextColumn()             # hash of the data (sha-1, base64ed)
    title = Columns.TextColumn()            # label to display instead of the data
    creation = Columns.DateTimeColumn()     # date attachement was first created

class value_x:      # FHIR name: value[x]
                    # dit is een voorbeeld van een FHIR OpenTypeElement: deze hebben geen gespecificeerd
                    # type en worden weergegeven met de wilcard '*'.
                    # lijst van OpenTypeElements: http://hl7.org/fhir/datatypes.html#open
                    # de elementnaam [x] wordt vervangen door de Title cased name of the data type
    value = Columns.TextColumn()

class Extension:
    url = Columns.TextColumn()  # indentifies the meaning of the extension
    value = value_x.value

class BackBoneElement:
    modifier_extension = Extension()

# print(type(BackBoneElement.modifier_extension.url))






