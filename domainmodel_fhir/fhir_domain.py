from domainmodels.entity_domain import RefTypes  # todo: RefTypes in fhir_domain.py zelf definieren?
from domainmodels.hl7rim_base_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Sat, HybridSat, Link, LinkReference

#########################################################################################################
#                                                                                                       #
# Domein model volgens FHIR-standaard (hl7.org.fhir). Iedere Entiteit heeft als type "DomainResource"   #
#                                                                                                       #
#########################################################################################################


class Patient(DvEntity, Entity):   # FHIR: DomainResource (http://hl7.org/fhir/domainresource.html#1.20)

    class Default(Sat):
        active = Columns.BoolColumn()  # patient record active?
        gender = Columns.RefColumn(RefTypes.geslacht_types)
        birthdate = Columns.DateColumn()
        # deceased + deceased_date voorbeeld van "type[x]" , meer dan 1 datatype voor content. (=polymorphic in OO)
        # voor meer info zie http://hl7.org/fhir/formats.html#choice
        deceased_boolean = Columns.BoolColumn()
        deceased_datetime = Columns.DateTimeColumn()
        # type[x}
        multiple_birth_boolean = Columns.BoolColumn()
        multiple_birth_integer = Columns.IntColumn()


