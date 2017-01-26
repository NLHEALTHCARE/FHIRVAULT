from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *


class Enquete(HubEntity):

    class Default(Sat):
        enquete_id = Columns.TextColumn()
        enquete_label = Columns.TextColumn()
        label_sbg = Columns.TextColumn()
        label_sbg_totaal = Columns.TextColumn()
        omschrijving = Columns.TextColumn()
        omschrijving_uitgebreid = Columns.TextColumn()
        omschrijving_copyright = Columns.TextColumn()
        omschrijving_rapport = Columns.TextColumn()
        normgroup_id = Columns.TextColumn()
        normgroup_label = Columns.TextColumn()


class EnqueteInzet(HubEntity):

    class Default(Sat):

        meetmoment = Columns.TextColumn()
        anatomie = Columns.TextColumn()
        zijde  = Columns.TextColumn()
        geen_reactie_type = Columns.TextColumn()
        benchmark_type = Columns.TextColumn()
        rom_type = Columns.TextColumn()
        referentie_datum = Columns.DateTimeColumn() # reference_date
        aangemaakt = Columns.DateTimeColumn()
        kompleet = Columns.TextColumn()  # completed

    class Identificatie(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()  # test_id
        enquete_inzet_id = Columns.TextColumn()  # test_deployment_id
        gebruiker_id = Columns.TextColumn()  # uid
        traject_id = Columns.TextColumn()
        norm_groep_id = Columns.TextColumn()
        test_groep_id = Columns.TextColumn()
        automatische_test_groep_id = Columns.TextColumn()  # atgid
        behandeling_id = Columns.TextColumn()  # treatment_id


class Antwoord(HubEntity):

    class Default(Sat):
        vraag = Columns.TextColumn()
        antwoord = Columns.TextColumn()
        score = Columns.TextColumn()
        datum = Columns.DateTimeColumn()


    class Identificatie(Sat):
        patient_id = Columns.TextColumn()
        enquete_id = Columns.TextColumn()
        enquete_inzet_id = Columns.TextColumn()
        vraag_id = Columns.TextColumn()



class Score(HubEntity):
    class Default(Sat):
        pass

    class Identificatie(Sat):
        pass

class Notificatie(HubEntity):  # notificatie = indications in Telepsy proms (get_indications)
    class Default(Sat):
        pass

    class Identificatie(Sat):
        pass


#########################
# LINKS
#########################

class EnqueteEnqueteInzetLinkEntity(LinkEntity):
    class Link(Link):
        enquete = LinkReference(Enquete)
        enquete_inzet = LinkReference(EnqueteInzet)