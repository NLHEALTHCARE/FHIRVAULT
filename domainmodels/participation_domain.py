from domainmodels.entity_domain import *
from domainmodels.role_domain import *
from domainmodels.act_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, HybridSat, LinkReference, DynamicLinkReference


class SubtrajectParticipationLink(Link, Participation):
    """
    Definitie van Grouper heeft 1..1 relaties voor participanten, vandaar in vaste kolommen
    """
    subtraject = LinkReference(Subtraject)  # type = object
    patient = LinkReference(Patient)  # type = subject
    hoofdbehandelaar = LinkReference(Zorgverlener)  # type = performer, eindverantwoordelijke
    verwijzer = LinkReference(Zorgverlener)  # type = referrer
    verwijzende_instelling = LinkReference(Zorgaanbieder)  # type = referrer
    betaler = LinkReference(Zorgverzekeraar)  # type = guarantor party
    huisarts = LinkReference(Zorgverlener)  # type = primary information recipient
    instelling = LinkReference(Zorgaanbieder)


class ZorgactviteitParticipationLink(Link, Participation):
    """
    Definitie van Grouper heeft 1..1 relaties voor participanten, vandaar in vaste kolommen
    """
    zorgactiviteit = LinkReference(Zorgactiviteit)  # type = object
    patient = LinkReference(Patient)  # type = subject
    aanvragende_zorgaanbieder = LinkReference(Zorgaanbieder)  # type = referrer by
    aanvragende_zorgverlener = LinkReference(Zorgverlener)  # type = referrer by
    uitvoerende_zorgaanbieder = LinkReference(Zorgaanbieder)  # type = performer
    uitvoerende_zorgverlener = LinkReference(Zorgverlener)  # type = performer
    betaler = LinkReference(Zorgverzekeraar)  # type = guarantor party
#
class ZorgverzekeringParticipatieLink(Link, Participation):
    patient = LinkReference(Patient)  # type = subject
    verzekeraar = LinkReference(Zorgverzekeraar)  # type = guarantor party


class VerkoopprijsParticipatieLink(Link, Participation):
    zorgaanbieder = LinkReference(Zorgaanbieder)
    inkoopcombinatie = LinkReference(Zorginkoopcombinatie)

class AfspraakParticipationLink(Link,Participation):
    patient = LinkReference(Patient)
    afspraak = LinkReference(Afspraak)



#
# # Partipcaties
# # PatientEncounter: patient(subject), ToegewezenEntiteit(performer), Medewerker(encounter_participant), Locatie(locatie)
# # Traject: patient(subject), Betaler(guarantor),
#
# class ParticipatiePatientHandelingLink(Link, Participation):
#     """Generieke Link voor alle verschillende Participanten in Handeling
#     waarbij een Patient als ParticipatonType.subject"""
#     class Types():
#         """
#         Alle types van Rollen die mogelijk kunnen voorkomen in deze Link tabel
#         """
#         zorgverlener = Zorgverlener
#
#         # is dit nodig, of is dit niet besloten in scoper van zorgverlenerrol
#         # zorgaanbiederrol = ZorgaanbiederRol
#
#         locatierol = Locatie
#         betalerrol = Betaler
#         begunstigderol = Begunstigde
#
#     class Default(Sat):
#         participation_type = Columns.TextColumn(default_value=ParticipationType.subject)
#
#     patient = LinkReference(PatientRol)
#     handeling = LinkReference(Handeling)
#     rol = DynamicLinkReference()                # verwijst naar een Rol, waarbij per record ParticipationType wordt aangegeven tijdens mappins
#
#
#
# class ParticipatieTrajectLink(Link, Participation):
#     """Generiek, voor... (hetzelfde als hierboven, maar dan voor Traject"""
#     class Types():
#         """
#         Alle types van Rollen die mogelijk kunnen voorkomen in deze Link tabel
#         """
#         zorgverlenerrol = ZorgverlenerRol
#
#         # is dit nodig, of is dit niet besloten in scoper van zorgverlenerrol
#         # zorgaanbiederrol = ZorgaanbiederRol
#
#         locatierol = LocatieRol
#         betalerrol = BetalerRol
#         begunstigderol = BegunstigdeRol
#
#
#
#     class Default(Sat):
#         participation_type = Columns.TextColumn(default_value=ParticipationType.subject)
#
#     patient = LinkReference(PatientRol)
#     handeling = LinkReference(Handeling)
#
# class ParticipatieZorgverlenerTraject_Link(Link, Participation):
#
#     class Verwijzer(Sat):
#         participation_type = Columns.TextColumn(default_value=ParticipationType.referrer)
#
#     # hier moet komen: verwijzer ZorgverlenerRol, daarmee meteen Zorgverlener (player) en Zorginstelling (scoper) gedekt
#
#
# # Partipcation zijn letterlijk links in DV
# # Vraag: kunnen/willen we verschillende Participations combineren?!
# class LinkZorgactviteitPartipication(Participation):
#     pass
#     # weet niet hoe ik dit in code moet uitschrijven
#     # maar idee is dat voor elke rol die deelneemt een ParticipationType wordt gedefinieerd
#
#     # def map_roles_participation(self, role_class):
#     #     map = {
#     #         RoleClass.PAT: ParticipationType.SBJ,               # Patient is subject
#     #         RoleClass.PROV: ParticipationType.PRF,              # Provider is performer
#     #         # maar kan ook ParticipationType.ATND, ParticipationType.DIS, ParticipationType.REF zijn
#     #         RoleClass.PAYOR: ParticipationType.GUAR,            # Payor is Guarantor
#     #         RoleClass.EMP:   ParticipationType._ParticipationAncillary # Employees vervullen ancillary rol
#     #         }
#     #     return map[role_class]
#     #
#     # def __init__(self, role_class):
#     #     self.participation_type = self.map_roles_participation(role_class)
