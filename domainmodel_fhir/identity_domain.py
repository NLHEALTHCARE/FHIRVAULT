from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

##### GROUPS #####

class Organization(DvEntity):
    class Default(Sat):
        active = Columns.BoolColumn()
        name = Columns.TextColumn()

    class Identifier(HybridSat):
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            secondary = 'secondary (If known)'

        use = Columns.TextColumn(default_value=Types.official)
#        org_type = Columns.FHIR.CodeableConceptColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
#        period = Columns.FHIR.PeriodColumn()

    #todo: afmaken mat andere sats

class OrganizationOrganizationLink(Link):
    organization = LinkReference(Organization)
    linked_to_organization = LinkReference(Organization)




##### INDIVIDUALS #####

class GenderTypes:
    """enum met codes"""
    male = 'male'
    female = 'female'
    other = 'other'
    unknown = 'unknown'

class Patient(DvEntity):
    class Default(Sat):
        active = Columns.BoolColumn()
        birthdate = Columns.DateColumn()
        gender = Columns.TextColumn(default_value=GenderTypes.unknown)
        deceased_boolean = Columns.BoolColumn()
        deceased_datetime = Columns.DateTimeColumn()

        multiple_birth_boolean = Columns.BoolColumn()
        multiple_birth_integer = Columns.IntColumn()
        material_status = Columns.FHIR.CodeableConceptColumn()

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
#        period = Columns.FHIR.PeriodColumn()


    class Name(HybridSat):
        class Types(HybridSat.Types):
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            nickname = 'nickname'
            anonymous = 'anonymous'
            old = 'old'
            maiden = 'maiden'
            none = ''
        use = Columns.TextColumn(default_value=Types.none)
        text = Columns.TextColumn()
        family = Columns.TextArrayColumn()
        given = Columns.TextArrayColumn()
        prefix = Columns.TextArrayColumn()
        suffix = Columns.TextArrayColumn()
        period = Columns.FHIR.PeriodColumn()

    class Extra(Sat):
        # contactpersoon
        contact = Columns.JsonColumn()
        # mag weg
        animal = Columns.JsonColumn()
        photo = Columns.TextColumn()

    class Communication(Sat):
        language = Columns.FHIR.CodeableConceptColumn()
        preffered = Columns.BoolColumn()

    class Telecom(HybridSat):
        class Types(HybridSat.Types):
            home = 'home'
            work = 'work'
            temp = 'temp'
            old = 'old'
            mobile = 'mobile'
        class Systems():
            phone = 'phone'
            fax = 'fax'
            email = 'email'
            pager = 'pager'
            other = 'other'

        use = Columns.TextColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
        rank = Columns.IntColumn()
        period = Columns.FHIR.PeriodColumn()


    class Address(HybridSat):

        class Types(HybridSat.Types):
            home = 'home'
            work = 'work'
            temp = 'temp'
            old = 'old'

        class AddressTypes():
            postal = 'postal'
            physical = 'physical'
            both = 'both'

        use= Columns.TextColumn()
        add_type = Columns.TextColumn()
        text = Columns.TextColumn()
        line = Columns.TextArrayColumn()
        city = Columns.TextColumn()
        district = Columns.TextColumn()
        state = Columns.TextColumn()
        postalcode = Columns.TextColumn()
        country = Columns.TextColumn()
#        period = Columns.FHIR.PeriodColumn()




# class PatientManagingOrganizationLink(Link):
#     patient = LinkReference(Patient)
#     organization = LinkReference(Organization)



class Practitioner(DvEntity):
    pass

class RelatedPerson(DvEntity):
    pass

class PatientOrganizationLink(Link):
    patient = LinkReference(Patient)
    organization = LinkReference(Organization)

class PatientCareProfiderLink(Link):
    patient = LinkReference(Patient)
    practioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)

class PatientPatientLink(HybridLink):
    class Types(HybridLink.Types):
        replace  = 'replace'
        refer = 'refer'
        seealso = 'seealso'

    patient = LinkReference(Patient)
    linked_to = LinkReference(Patient)
