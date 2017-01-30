from domainmodel.identity_domain import Patient
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *

class Meettraject(HubEntity):
    class Default(Sat):
        anatomie = Columns.TextColumn()
        diagnose_globaal = Columns.TextColumn() #episode_general
        diagnose_specifiek = Columns.TextColumn() #episode_specific
        zijde = Columns.TextColumn()

        datum_aanmaak = Columns.DateTimeColumn()  # reference_date
        datum_afgerond = Columns.DateTimeColumn()

class Meetmoment(HubEntity):
    class Default(Sat):
        label = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        datum_aanmaak = Columns.DateTimeColumn()
        datum_verzonden = Columns.DateColumn()
        soap_response = Columns.TextColumn()

class Enquete(HubEntity):
    class Default(Sat):
        label = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        omschrijving_uitgebreid = Columns.TextColumn()

class Enquete(HubEntity):
    class Default(Sat):
        label = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        omschrijving_uitgebreid = Columns.TextColumn()

    class ExterneGegevens(Sat):
        externe_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()

        # label_sbg = Columns.TextColumn()  # wat is dit?
        # label_sbg_totaal = Columns.TextColumn()
        # omschrijving_copyright = Columns.TextColumn()
        # omschrijving_rapport = Columns.TextColumn()
        # normgroup_id = Columns.TextColumn()
        # normgroup_label = Columns.TextColumn()



class EnqueteMeting(HubEntity):
    class Default(Sat):
        meetmoment = Columns.TextColumn()
        anatomie = Columns.TextColumn()
        zijde  = Columns.TextColumn()

        referentie_datum = Columns.DateTimeColumn() # reference_date
        aangemaakt = Columns.DateTimeColumn()
        compleet = Columns.TextColumn()  # completed #kompleet is toch met een c

    class ExterneGegevens(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()  # test_id
        enquete_meting_id = Columns.TextColumn()  # test_deployment_id
        traject_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()
        # geen_reactie_type = Columns.TextColumn()  # hier eventueel ref kolom van maken
        # benchmark_type = Columns.TextColumn()  # hier eventueel ref kolom van maken
        # rom_type = Columns.TextColumn()  # hier eventueel ref kolom van maken

    # class Identificatie(Sat):
    #     patient_id = Columns.TextColumn()
    #     enquete_id = Columns.TextColumn()  # test_id
    #     enquete_meting_id = Columns.TextColumn()  # test_deployment_id
    #     gebruiker_id = Columns.TextColumn()  # uid
    #     traject_id = Columns.TextColumn()
    #     norm_groep_id = Columns.TextColumn()
    #     test_groep_id = Columns.TextColumn()
    #     automatische_test_groep_id = Columns.TextColumn()  # atgid
    #     behandeling_id = Columns.TextColumn()  # treatment_id


class EnqueteMetingAntwoord(HubEntity):
    class Default(Sat):
        vraag = Columns.TextColumn()
        antwoord = Columns.TextColumn()
        score = Columns.FloatColumn()
        score_type = Columns.TextColumn()
        datum = Columns.DateTimeColumn()

    class ExterneGegevens(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()
        enquete_inzet_id = Columns.TextColumn()
        vraag_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()

# class EnqueteMetingScore(EnqueteMetingAntwoord):
#     pass


class EnqueteMetingNotificatie(HubEntity):  # notificatie = indications in Telepsy proms (get_indications)
    class Default(Sat):
        score_beschrijving = Columns.TextColumn()
        notificatie_type = Columns.TextColumn()
        datum = Columns.DateTimeColumn()

    class ExterneGegevens(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()
        enquete_inzet_id = Columns.TextColumn()
        vraag_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()


#########################
# LINKS
#########################

class EnqueteMetingLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meettraject = LinkReference(Meettraject)
        meetmoment = LinkReference(Meetmoment)
        enquete = LinkReference(Enquete)
        enquete_meting = LinkReference(EnqueteMeting)


class EnqueteAntwoordLinkEntity(LinkEntity):
    class Link(Link):
        # patient = LinkReference(Patient)
        # meettraject = LinkReference(Meettraject)
        # meetmoment = LinkReference(Meetmoment)
        enquete_meting = LinkReference(EnqueteMeting)
        enquete_meting_antwoord = LinkReference(EnqueteMetingAntwoord)



# class ScoreEnqueteInzetLinkEntity(LinkEntity):
#     class Link(Link):
#         score = LinkReference(EnqueteMetingScore)
#         enquete_inzet = LinkReference(EnqueteMeting)
#
#         patient = LinkReference(Patient)

class EnqueteNotificatieMeettrajectLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meettraject = LinkReference(Meettraject)
        enquete_meting_notificatie = LinkReference(EnqueteMetingNotificatie)