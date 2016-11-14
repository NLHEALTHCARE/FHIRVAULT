from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, Link, HybridSat, HybridLink, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################

##### INDIVIDUALS #####


# https://www.hl7.org/fhir/patient.html
class Patient(DvEntity):
    class Default(Sat):
        class GenderTypes:
            """enum met codes"""
            male = 'male'
            female = 'female'
            other = 'other'
            unknown = 'unknown'
        active = Columns.BoolColumn()
        gender = Columns.TextColumn(default_value=GenderTypes.unknown)
        birthdate = Columns.DateColumn()
        deceased_boolean = Columns.BoolColumn()
        deceased_datetime = Columns.DateTimeColumn()
        marital_status = Columns.FHIR.CodeableConceptColumn()
        multiple_birth_boolean = Columns.BoolColumn()
        multiple_birth_integer = Columns.IntColumn()

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

    # https: // www.hl7.org / fhir / datatypes.html  # HumanName
    # https://simplifier.net/NL-BasicComponents/nl-core-humanname
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

        class AddressTypes:
            postal = 'postal'
            physical = 'physical'
            both = 'both'

        use = Columns.TextColumn()
        add_type = Columns.TextColumn()
        text = Columns.TextColumn()
        line = Columns.TextArrayColumn()
        city = Columns.TextColumn()
        district = Columns.TextColumn()
        state = Columns.TextColumn()
        postalcode = Columns.TextColumn()
        country = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()

    class Communication(Sat):
        language = Columns.FHIR.CodeableConceptColumn()
        preffered = Columns.BoolColumn()

    class Extra(Sat):
        #contactpersoon
        contact = Columns.JsonColumn()

# https://www.hl7.org/fhir/practitioner.html
# https://simplifier.net/Nictiz/bgz-Practitioner
class Practitioner(DvEntity):
    class Default(Sat):
        class GenderTypes:
            """enum met codes"""
            male = 'male'
            female = 'female'
            other = 'other'
            unknown = 'unknown'
        active = Columns.BoolColumn()
        gender = Columns.TextColumn(default_value=GenderTypes.unknown)
        birthdate = Columns.DateColumn()

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

    class Name(Sat):
        class Types():
            usual = 'usual'
            official = 'official'
            temp = 'temp'
            nickname = 'nickname'
            anonymous = 'anonymous'
            old = 'old'
            maiden = 'maiden'

        use = Columns.TextColumn()
        text = Columns.TextColumn()
        family = Columns.TextArrayColumn()
        given = Columns.TextArrayColumn()
        prefix = Columns.TextArrayColumn()
        suffix = Columns.TextArrayColumn()
        period = Columns.FHIR.PeriodColumn()

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

        use = Columns.TextColumn()
        add_type = Columns.TextColumn()
        text = Columns.TextColumn()
        line = Columns.TextArrayColumn()
        city = Columns.TextColumn()
        district = Columns.TextColumn()
        state = Columns.TextColumn()
        postalcode = Columns.TextColumn()
        country = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()

    class Communication(Sat):
        language = Columns.FHIR.CodeableConceptColumn()

    class Extra(Sat):
        qualification = Columns.JsonColumn()

##### GROUPS #####


# https://www.hl7.org/fhir/organization.html
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
        org_type = Columns.FHIR.CodeableConceptColumn()
        system = Columns.TextColumn()
        value = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()

    class Telecom(HybridSat):
        class Types(HybridSat.Types):
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
            work = 'work'
            temp = 'temp'
            old = 'old'

        class AddressTypes():
            postal = 'postal'
            physical = 'physical'
            both = 'both'

        use = Columns.TextColumn()
        add_type = Columns.TextColumn()
        text = Columns.TextColumn()
        line = Columns.TextArrayColumn()
        city = Columns.TextColumn()
        district = Columns.TextColumn()
        state = Columns.TextColumn()
        postalcode = Columns.TextColumn()
        country = Columns.TextColumn()
        period = Columns.FHIR.PeriodColumn()


class OrganizationOrganizationLink(Link):
    organization = LinkReference(Organization)
    part_of_organization = LinkReference(Organization)


class PatientManagingOrganizationLink(Link):
    patient = LinkReference(Patient)
    organization = LinkReference(Organization)


class PatientCareProviderLink(Link):
    patient = LinkReference(Patient)
    practitioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)


class PractitionerOrganizationLink(Link):
    practitioner = LinkReference(Practitioner)
    organization = LinkReference(Organization)
    # location = LinkReference(Location)
    # healthcareServices = LinkReference(HealthcareServices)

    class Default(Sat):
        role = Columns.FHIR.CodeableConceptColumn()
        speciality = Columns.FHIR.CodeableConceptColumn()
        period = Columns.FHIR.PeriodColumn

# Zorgaanbieder: https://simplifier.net/Nictiz/bgz-CareProvider
#
# Zorgverzekeraar : https://www.hl7.org/fhir/coverage.html
# Afdeling : https://simplifier.net/Nictiz/bgz-DepartmentType
#
# Zorgactiviteit : https://www.hl7.org/fhir/episodeofcare.html

# https://simplifier.net/NL-BasicComponents/nl-core-humanname
