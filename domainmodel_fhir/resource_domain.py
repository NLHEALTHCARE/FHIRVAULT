from domainmodel_fhir.element_domain import CodeableConcept, Coding, Period, HumanName, ContactPoint, Address, \
    Attachment, BackBoneElement
from domainmodels.entity_domain import RefTypes  # todo: RefTypes in fhir_domain.py zelf definieren?
from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

# todo: "base_domain" , reftypes-achtigs toevoegen

""" Resource classes (Patient is een DomainResource) http://hl7.org/fhir/patient.html """

class AbstractPerson:
    class GenderTypes:
        male = 'male'
        female = 'female'
        other = 'other'
        unknown = 'unknown'

class Patient(DvEntity, Entity):   # FHIR type: DomainResource (http://hl7.org/fhir/domainresource.html#1.20)


    class Default(Sat):
        active = Columns.BoolColumn()  # patient record active?
        # gender = Columns.RefColumn(RefTypes.geslacht_types)
        birthdate = Columns.DateColumn()
        gender = Columns.TextColumn(default_value=AbstractPerson.GenderTypes.unknown)
        # deceased + deceased_date voorbeeld van "type[x]" , meer dan 1 datatype voor content. (=polymorphic in OO)
        # voor meer info zie http://hl7.org/fhir/formats.html#choice
        deceased_boolean = Columns.BoolColumn()
        deceased_datetime = Columns.DateTimeColumn()
        extra = Columns.JsonColumn()

        # type[x]
        multiple_birth_boolean = Columns.BoolColumn()
        multiple_birth_integer = Columns.IntColumn()



    class Identifier(HybridSat):      #FHIR type: Element (http://hl7.org/fhir/element.html#1.21.0)
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary (If known)'

        use = Columns.TextColumn(default_value='official')
        # text = CodeableConcept.text
        system = Coding.system   #system heeft FIHR type: uri; Uniform Resource Identifier ( http://hl7.org/fhir/datatypes.html#uri)
        version = Coding.version
        code = Coding.code  # symbool in syntax gedefinieerd door het systeem (http://hl7.org/fhir/datatypes.html#code)
        # display = Coding.display  # weergave gedefinieerd door het systeem
        # user_selected = Coding.user_selected  # indien deze codering door de user zelf was gekozen

        start = Period.start
        period_end = Period.end
        extra = Columns.JsonColumn()
        # assigner = ??? # todo: assigner heeft FHIR type: Reference(Organization); Je referereert hier dus naar een
                    # andere DomainResource (hier is dat "Organization"; Patient is ook een DomainResource) Hoe implementeren?

    class Name(HybridSat):      # naar JSONB
        #todo mag in json
        class Types(HybridSat.Types):     # zie ook utility class HumanName; #todo wat is de meest logische plaats voor deze hybridsat?
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            nickname = 'nickname'
            anonymous = 'anonymous'
            old = 'old'
            maiden = 'maiden'
            none = ''
        use = Columns.TextColumn(default_value=Types.none)
        #todo: in json veld
        text = HumanName.text
        family = HumanName.family   # family name (or surname)
        given = HumanName.given
        prefix = HumanName.prefix
        suffix = HumanName.suffix
        start = HumanName.start
        end = HumanName.end

    class Telecom(HybridSat):
        #todo mag in json
        class Systems: # todo: FHIR remark: ContactPointSystem(Required); verwijst naar een valueset http://hl7.org/fhir/ValueSet/contact-point-system
            phone = 'phone'
            fax = 'fax'
            email = 'email'
            pager = 'pager'
            other = 'other'
        value = ContactPoint.value
        #todo mag in json
        class Types(HybridSat.Types):     # todo: FHIR remark: ContactPointUse(Required); verwijst naar een valueset http://hl7.org/fhir/valueset-contact-point-use.html
            home = 'home'
            work = 'work'
            temp = 'temp'
            old = 'old'
            mobile = 'mobile'
        use = Columns.TextColumn()
        rank = ContactPoint.rank     # moet positieve integer zijn!; specify preferred order of use (1 = highest)
        start = ContactPoint.start
        end = ContactPoint.end
    class address(HybridSat):
        #todo mag in json
        class use(HybridSat.Types):  # hoe wordt dit adres gebruikt; todo: AddressUse(Required): verwijst naar http://hl7.org/fhir/valueset-address-use.html
            home = 'home'
            work = 'work'
            temp = 'temp'
            old = 'old'
        #todo mag in json
        class type(HybridSat.Types):    # todo: AddressType(Required): verwijst naar http://hl7.org/fhir/ValueSet/address-type
            postal = 'postal'
            physical = 'physical'
            both = 'both'

        text = Address.text         # text representation of the address
        line = Address.line         # street name, number, direction & P.O. Box etc.
        city = Address.city
        district = Address.district     # district name (aka county)
        state = Address.state        # sub_unit of country (abbreviations ok)
        postalcode = Address.postalcode
        country = Address.country
        # Country(can be ISO 3166 3 letter code)
        start = Address.start
        end = Address.end

    class marital_status:
        # todo: wordt veld
        #  Marital (civil status of a patient; todo: Marital Status Codes (Required): verwijst naar 	http://hl7.org/fhir/ValueSet/marital-status
        text = CodeableConcept.text
        system = Coding.system   #system heeft FIHR type: uri; Uniform Resource Identifier ( http://hl7.org/fhir/datatypes.html#uri)
        version = Coding.version
        code = Coding.code  # symbool in syntax gedefinieerd door het systeem (http://hl7.org/fhir/datatypes.html#code)
        display = Coding.display  # weergave gedefinieerd door het systeem
        user_selected = Coding.user_selected

    #todo: foto mag weg
    class photo(Attachment):
        content_type = Attachment.content_type     # Mime type of the content, with charset etc. ; todo: MimeType (Required) http://www.rfc-editor.org/bcp/bcp13.txt
        language = Attachment.language          # Human language of the content (BPC-47) ; todo: Language (Required) https://tools.ietf.org/html/bcp47
        data = Attachment.data             # Data inline, base64ed
        url = Attachment.url              # Uri(Uniform Resource Identifier) where the data can be found
        size = Attachment.size              # positieve integer; number of bytes of content (if url provided)
        hash = Attachment.hash            # hash of the data (sha-1, base64ed)
        title = Attachment.title            # label to display instead of the data
        creation = Attachment.creation

# print(type(Patient.photo.content_type))
# print(type(Patient.photo.creation))

    class contact:      # FHIR type: BackBoneElement
        #todo mag helemaal in json
        modifier_extension = BackBoneElement.modifier_extension
        url = BackBoneElement.modifier_extension.url
        value = BackBoneElement.modifier_extension.value

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

        class telecom(HybridSat):
            class system(HybridSat.Types): # todo: FHIR remark: ContactPointSystem(Required); verwijst naar een valueset http://hl7.org/fhir/ValueSet/contact-point-system
                phone = 'phone'
                fax = 'fax'
                email = 'email'
                pager = 'pager'
                other = 'other'
            value = ContactPoint.value
            class use(HybridSat.Types):     # todo: FHIR remark: ContactPointUse(Required); verwijst naar een valueset http://hl7.org/fhir/valueset-contact-point-use.html
                home = 'home'
                work = 'work'
                temp = 'temp'
                old = 'old'
                mobile = 'mobile'
            rank = ContactPoint.rank     # moet positieve integer zijn!; specify preferred order of use (1 = highest)
            start = ContactPoint.start
            end = ContactPoint.end
        class address(HybridSat):
            class use(HybridSat.Types):  # hoe wordt dit adres gebruikt; todo: AddressUse(Required): verwijst naar http://hl7.org/fhir/valueset-address-use.html
                home = 'home'
                work = 'work'
                temp = 'temp'
                old = 'old'

        class type(HybridSat.Types):    # todo: AddressType(Required): verwijst naar http://hl7.org/fhir/ValueSet/address-type
            postal = 'postal'
            physical = 'physical'
            both = 'both'

        text = Address.text         # text representation of the address
        line = Address.line         # street name, number, direction & P.O. Box etc.
        city = Address.city
        district = Address.district     # district name (aka county)
        state = Address.state        # sub_unit of country (abbreviations ok)
        postalcode = Address.postalcode
        country = Address.country
        # Country(can be ISO 3166 3 letter code)
        start = Address.start
        end = Address.end

        class Gender(HybridSat):
            class gender(HybridSat.Types):  # FHIR: AdministrativeGender(Required) 	http://hl7.org/fhir/ValueSet/administrative-gender
                male = 'male'
                female = 'female'
                other = 'other'
                unknown = 'unknown'

        # organization = ??  # Reference(Organization)

        start = Period.start  # The period during which this contact person or organization is valid to be contacted with regard to this patient
        end = Period.end

# print(type(Patient.contact.country))

        class communication:      # FHIR type: BackBoneElement
            modifier_extension = BackBoneElement.modifier_extension
            url = BackBoneElement.modifier_extension.url
            value = BackBoneElement.modifier_extension.value

            # language = ??             # FHIR: Language(Required) https://tools.ietf.org/html/bcp47
            preferred = Columns.BoolColumn  # language preference indicator

        # careprovider + ??     # FHIR: Reference(Organization| Practioner); patients nominated primary care provider

        # managingOrganization  # FHIR: Reference(Organization) Organization that is the custodian of the patient record

    class link(HybridSat):      # FHIR type: BackBoneElement; Link to another patient resource that concerns the same actual person
        modifier_extension = BackBoneElement.modifier_extension
        url = BackBoneElement.modifier_extension.url
        value = BackBoneElement.modifier_extension.value

        # other = ??      # Reference(Patient);   the other patient resource that the link refers to
        class type(HybridSat.Types):    # LinkType(Required): http://hl7.org/fhir/ValueSet/link-type
            replace = 'replace'
            refer = 'refer'
            seealso = 'seealso'















