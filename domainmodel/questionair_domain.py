from domainmodel.identity_domain import Patient
from domainmodel.workflow_domain import Afspraak, Subtraject
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *

class EnqueteMeettraject(HubEntity):
    class Default(Sat):
        anatomie = Columns.TextColumn()
        episode_omschrijving_globaal = Columns.TextColumn() #episode_general
        episode_omschrijving_specifiek = Columns.TextColumn() #episode_specific
        zijde = Columns.TextColumn()
        datum_aanmaak = Columns.DateTimeColumn()  # reference_date
        datum_afgerond = Columns.DateTimeColumn()

    class Telepsy(Sat):
        anatomie = Columns.TextColumn()
        episode = Columns.TextColumn()
        zijde = Columns.TextColumn()
        datum_aanmaak = Columns.DateTimeColumn()

    class Identificatie(Sat):
        patient_nummer = Columns.TextColumn()
        meettraject_volgnummer = Columns.IntColumn()
        zorgtraject_nummer= Columns.TextColumn()
        subtraject_nummer = Columns.TextColumn()
        eerste_afspraak_nummer = Columns.TextColumn()
        kliniek_code = Columns.TextColumn()
        specialisme_code = Columns.TextColumn()
        diagnose_code = Columns.TextColumn()


class EnqueteMeetmoment(HubEntity):
    class Default(Sat):
        label = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        zijde = Columns.TextColumn()
        episode_algemeen = Columns.TextColumn()
        episode_specifiek = Columns.TextColumn()
        datum_aanmaak = Columns.DateTimeColumn()

    class Telepsy(Sat):
        anatomie = Columns.TextColumn()
        episode = Columns.TextColumn()
        moment = Columns.TextColumn()
        zijde = Columns.TextColumn()
        testgroup_id = Columns.TextColumn()
        datum_aanmaak = Columns.DateTimeColumn()
        datum_afgerond = Columns.DateTimeColumn()

    class Afspraak(Sat):
        afspraak_nummer = Columns.TextColumn()
        afspraak_omschrijving = Columns.TextColumn()
        afspraak_status_code = Columns.TextColumn()
        afspraak_status_omschrijving = Columns.TextColumn()
        afspraak_datum = Columns.DateTimeColumn()
        zorgactiviteit_code = Columns.TextColumn()
        zorgactiviteit_omschrijving = Columns.TextColumn()

    class Verzending(Sat):
        datum_verstuur = Columns.DateTimeColumn()
        trigger_na_dagen = Columns.IntColumn()
        datum_verzonden = Columns.DateColumn()
        status = Columns.TextColumn()
        status_bericht = Columns.TextColumn()
        heeft_feedback = Columns.BoolColumn()

    class TestInfo(Sat):
        testgroup_id = Columns.TextColumn()
        testgroup = Columns.TextColumn()


    class Identificatie(Sat):
        patient_nummer = Columns.TextColumn()
        meettraject_volgnummer = Columns.IntColumn()
        meetmoment = Columns.TextColumn()
        meetmoment_volgnummer = Columns.IntColumn()
        subtraject_nummer = Columns.TextColumn()
        afspraak_nummer = Columns.TextColumn()
        specialist_code = Columns.TextColumn()

class Enquete(HubEntity):
    class Default(Sat):
        label = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        omschrijving_uitgebreid = Columns.TextColumn()
        soap_client = Columns.TextColumn()

    class ExterneGegevens(Sat):
        enquete_id = Columns.TextColumn()
        externe_id = Columns.TextColumn()  #
        extra_data = Columns.JsonColumn()

        # label_sbg = Columns.TextColumn()  # wat is dit?
        # label_sbg_totaal = Columns.TextColumn()
        # omschrijving_copyright = Columns.TextColumn()
        # omschrijving_rapport = Columns.TextColumn()
        # normgroup_id = Columns.TextColumn()
        # normgroup_label = Columns.TextColumn()



class Enqueteafname(HubEntity):
    class Default(Sat):
        meetmoment = Columns.TextColumn()
        anatomie = Columns.TextColumn()
        zijde  = Columns.TextColumn()
        uitnodingsdatum = Columns.DateTimeColumn()
        referentie_datum = Columns.DateTimeColumn() # reference_date
        aangemaakt = Columns.DateTimeColumn()
        compleet = Columns.TextColumn()

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


class EnqueteafnameAntwoord(HubEntity): # deze class bevat gegevens met antwoorden en (totaal)scores
    class Default(Sat):
        vraag = Columns.TextColumn()
        antwoord = Columns.TextColumn()
        score = Columns.FloatColumn()
        score_type = Columns.TextColumn()
        datum = Columns.DateTimeColumn()

    class ExterneGegevens(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()
        enquete_meting_id = Columns.TextColumn()
        vraag_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()

# class EnqueteMetingScore(EnqueteMetingAntwoord):
#     pass


class EnqueteafnameNotificatie(HubEntity):  # notificatie = indications in Telepsy proms (get_indications)
    class Default(Sat):
        score_beschrijving = Columns.TextColumn()
        notificatie_type = Columns.TextColumn()
        datum = Columns.DateTimeColumn()

    class ExterneGegevens(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()
        enquete_meting_id = Columns.TextColumn()
        vraag_id = Columns.TextColumn()
        extra_data = Columns.JsonColumn()


#########################
# LINKS
#########################

class EnqueteMeetmomentAfspraakLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meetmoment = LinkReference(EnqueteMeetmoment)
        afspraak = LinkReference(Afspraak)

class EnqueteMeetmomentSubtrajectLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meetmoment = LinkReference(EnqueteMeetmoment)
        subtraject = LinkReference(Subtraject)


class EnqueteafnameMeetmomentLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meettraject = LinkReference(EnqueteMeettraject)
        meetmoment = LinkReference(EnqueteMeetmoment)
        enquete = LinkReference(Enquete)
        enquete_meting = LinkReference(Enqueteafname)

class EnqueteafnameAntwoordLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        # meettraject = LinkReference(Meettraject)
        # meetmoment = LinkReference(Meetmoment)
        enquete_meting = LinkReference(Enqueteafname)
        enquete_meting_resultaat = LinkReference(EnqueteafnameAntwoord)

# class EnqueteMetingEnqueteLinkEntity(LinkEntity):
#     class Link(Link):
#         enquete = LinkReference(Enquete)
#         enquete_meting = LinkReference(EnqueteMeting)

# class ScoreEnqueteInzetLinkEntity(LinkEntity):
#     class Link(Link):
#         score = LinkReference(EnqueteMetingScore)
#         enquete_inzet = LinkReference(EnqueteMeting)
#
#         patient = LinkReference(Patient)

class EnqueteNotificatieMeettrajectLinkEntity(LinkEntity):
    class Link(Link):
        patient = LinkReference(Patient)
        meettraject = LinkReference(EnqueteMeettraject)
        enquete_meting_notificatie = LinkReference(EnqueteafnameNotificatie)