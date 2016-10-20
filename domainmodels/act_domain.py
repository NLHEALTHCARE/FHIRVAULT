from domainmodels.hl7rim_base_domain import *
from domainmodels.hl7rim_enums import *
from domainmodels.entity_domain import *
from domainmodels.role_domain import *
from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import DvEntity, Link, Sat, LinkReference



########################################################################################################################
#
# Financiele Acts, ActRelationships en Particpations
#
########################################################################################################################


class Subtraject(DvEntity, Act):
    """Implementatiehandleiding HL7v3 Grouper v4.0.1, aangevuld met LBZ

    Business key: AGB-code zorgaanbieder + subtrajectnummer
    """

    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.account)
        act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)

    class Default(Sat):
        behandelend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        diagnose_code = Columns.RefColumn(RefTypes.dbc_diagnoses)
        zorgtype = Columns.RefColumn(RefTypes.dbc_zorgtypes)
        zorgvraag = Columns.RefColumn(RefTypes.dbc_zorgvraag_codes)
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        verwijscode = Columns.RefColumn(RefTypes.dbc_verwijscodes)
        afsluitreden = Columns.RefColumn(RefTypes.dbc_afsluitredenen)
        zorgproduct_code = Columns.RefColumn(RefTypes.dbc_zorgproducten)
        declaratie_code = Columns.RefColumn(RefTypes.dbc_declaraties)
        icd10_diagnose = Columns.TextColumn()
        behandeling_naam = Columns.TextColumn()
        behandeling_zijde = Columns.TextColumn()
        status = Columns.TextColumn(RefTypes.subtraject_status)
        disdatum = Columns.DateColumn()
        uzovinummer = Columns.TextColumn()

    #overleg met HJ deze even deze naamgeving omdat het anders inconsistent is met Role_patient (identificatie_SAT). Alle
    # hubs krijgen een sleutel Sat
    class Sleutels(Sat):
        patient_nr = Columns.TextColumn()
        vestiging_agb = Columns.TextColumn()
        nummer = Columns.TextColumn()  # uniek subtrajectnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        code = Columns.TextColumn()
        bron_id = Columns.TextColumn()


    class Kenmerken(Sat):
        "Kenmerken die worden achteraf afgeleid op basis van aanwezigheid zorgactiviteiten"
        type = Columns.RefColumn("subtraject_types")  # bijvoorbeeld dbc zorgproduct of add on zorg activiteit
        is_aanspraak_zvw = Columns.BoolColumn()
        is_aanspraak_zvw_toegepast = Columns.BoolColumn()
        heeft_za_machtiging = Columns.BoolColumn()
        heeft_oranje_za = Columns.BoolColumn()
        is_za_vertaling_toegepast = Columns.BoolColumn()
        is_dagbehandeling = Columns.BoolColumn()
        is_klinisch_tot_3_dagen = Columns.BoolColumn()
        is_klinisch_meer_3_dagen = Columns.BoolColumn()


    class Zorgtraject(Sat):
        "Zorgtraject als Sat opnemen, pragmatische oplossing afgekeken van timeff"
        nummer = Columns.TextColumn()           # uniek zorgtrajectnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()    # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()


class Zorgactiviteit(DvEntity, Act):
    """Implementatiehandleiding HL7v3 Grouper v4.0.1 en https://zibs.nl/wiki/OverdrachtVerrichting

    Voor discussie:
        - Grouper definieert zorgactiviteit als ActClass.account: het doel is financiele declaratie
        - In lijn met HL7 RIM en ZIBS is ActClass [Procedure, Patient encounter] meer op zijn plek

    Gaan we deze splitsen, zodat we expliciet ruimte maken voor meer klinische informatie uit het dossier?
      --> waarschijnlijk wel, zodat we ook flexibel aantal participanten in b.v. een operatie kunnen vastleggen

    Business key: AGB-code zorgaanbieder + subtrajectnummer
    """

    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.account)
        act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)

    class Sleutels(Sat):
        nummer = Columns.TextColumn()  # uniek zorgactiviteitnummer zoals in bronsysteem voorkomt
        extern_nummer = Columns.TextColumn()  # gereserveerd om secundair, extern nummer te registreren, b.v. na migratie
        bron_id = Columns.TextColumn()
        zorgtrajectnummer = Columns.TextColumn()

    class Default(Sat):

        zorgactiviteitcode = Columns.RefColumn(RefTypes.dbc_zorgactiviteiten)
        interne_verrichtingcode = Columns.TextColumn()
        begindatumtijd = Columns.DateTimeColumn()
        einddatumtijd = Columns.DateTimeColumn()
        aantal = Columns.FloatColumn()
        aanvragend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        uitvoerend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        cbv_code = Columns.RefColumn(RefTypes.cbv_codes)  # CBV verrichtingcodes zijn veel uitgebreider dan DBC Zorgactiviteitcodes
        anatomische_locatie = Columns.TextColumn()


    #Todo: JVL naamgeving? wat doen we met OZP dan ook seperate SAT?
    class AddOn(Sat):
        "Kenmerken wanneer zorgactiviteit een los te declareren add-on betreft"
        declaratiecode = Columns.RefColumn(RefTypes.dbc_declaraties)
        add_on_informatie = Columns.TextColumn()


class SubtrajectZorgactiviteitLink(Link, ActRelationship):
    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActRelationshipType.has_debit)
        act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)

    subtraject = LinkReference(Subtraject)
    zorgactiviteit = LinkReference(Zorgactiviteit)


class Zorgverzekering(DvEntity, Act):
    """
    Zorgverzekering c.q. polis

    Business key: UZOVI + verzekerdenummer
    """
    class Hl7(Sat):
        act_class = Columns.TextColumn(ActClass.coverage)

    class Default(Sat):
        verzekerdenummer = Columns.TextColumn()
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        soort = Columns.TextColumn()


class Verkoopprijs(DvEntity, Act):
    """
    Business key: AGB-code + Zorginkoopcombinatiecode
    """
    class Hl7 (Sat):
        act_class = Columns.TextColumn(default_value=ActClass.contract)

    class Default(Sat):
        declaratie_code = Columns.RefColumn(RefTypes.dbc_declaraties)
        prijs_integraal = Columns.FloatColumn()                 # to do: decimal?!
        prijs_ziekenhuis = Columns.FloatColumn()                # to do: decimal?!
        prijs_honorarium_poorter = Columns.FloatColumn()        # to do: decimal?!
        prijs_honorarium_ondersteuner = Columns.FloatColumn()   # to do: decimal?!
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()


#todo: JVL aanvliegwijze bespreken m.b.t. het vullen van de entiteiten. Nu de focus wat we hebben terwijl dit andersom wenselijk is

class Afspraak(DvEntity,Act):

    class Default(Sat):
        afspraak_omschrijving = Columns.TextColumn()
        eigenaar = Columns.TextColumn()
        begindatumtijd = Columns.DateTimeColumn()
        einddatumtijd = Columns.DateTimeColumn()
        createdatumtijd = Columns.DateTimeColumn()
        status = Columns.TextColumn()



    #todo: jvl bespreken Actclasses
    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.act)
        act_mood = Columns.TextColumn(default_value=ActMood.appointment)


    class Sleutels(Sat):
        bron_id = Columns.TextColumn()
        extern_nummer = Columns.TextColumn()
        afspraak_omschrijving_code = Columns.TextColumn()
        afspraak_nummer = Columns.TextColumn()


#todo: aparte tabel voor medewerkers bij personen?
class Afspraak_deelnemer(DvEntity,Act):

    class Default(Sat):
        agb = Columns.TextColumn()
        big = Columns.TextColumn()
        naam = Columns.TextColumn()
        functie = Columns.TextColumn()
        hoedanigheid = Columns.TextColumn()
        eigenaar_type = Columns.TextColumn()


    class Sleutels(Sat):
        medewerker_id = Columns.TextColumn()
        medewerker_code = Columns.TextColumn()
        afspraak_nummer = Columns.TextColumn()


class Factuurregel(DvEntity,Act):

    class Default(Sat):
        omzet_totaal = Columns.FloatColumn()
        omzet_kostendeel = Columns.FloatColumn()
        omzet_honorarium_poort = Columns.FloatColumn()
        omzet_honorarium_ondersteuners = Columns.FloatColumn()
        factuurdatum = Columns.DateColumn()
        is_credit = Columns.TextColumn()

    class Hl7(Sat):
        act_class = Columns.TextColumn(default_value=ActClass.account)
        act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)

    class Subtraject(Sat):
        behandelend_specialisme = Columns.RefColumn(RefTypes.specialisme_codes)
        diagnose_code = Columns.RefColumn(RefTypes.dbc_diagnoses)
        zorgtype = Columns.RefColumn(RefTypes.dbc_zorgtypes)
        zorgvraag = Columns.RefColumn(RefTypes.dbc_zorgvraag_codes)
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()
        verwijscode = Columns.RefColumn(RefTypes.dbc_verwijscodes)
        afsluitreden = Columns.RefColumn(RefTypes.dbc_afsluitredenen)
        zorgproduct_code = Columns.RefColumn(RefTypes.dbc_zorgproducten)
        declaratie_code = Columns.RefColumn(RefTypes.dbc_declaraties)
        icd10_diagnose = Columns.TextColumn()
        behandeling_naam = Columns.TextColumn()
        behandeling_zijde = Columns.TextColumn()
        subtrajectnummer = Columns.TextColumn()
        subtrajectnummer = Columns.TextColumn()
        uzovinummer = Columns.TextColumn()
        verwijzer = Columns.TextColumn()

    class Zorgtraject(Sat):
        zorgtrajectnummer = Columns.TextColumn()
        begindatum = Columns.DateColumn()
        einddatum = Columns.DateColumn()

    class Sleutels(Sat):
        patient_nr = Columns.TextColumn()
        vestiging_agb = Columns.TextColumn()
        nummer = Columns.TextColumn()
        extern_nummer = Columns.TextColumn()
        code = Columns.TextColumn()
        bron_id = Columns.TextColumn()
        factuurnummer = Columns.TextColumn()
        factuurregelnummer = Columns.TextColumn()

    class Grouper(Sat):
        grouper_versie = Columns.TextColumn()
        groupercertificaatversie = Columns.TextColumn()
        hashzpzv = Columns.TextColumn()

    class Verzekering(Sat):
        assurantiepolis = Columns.TextColumn()
        debiteurnaam = Columns.TextColumn()





#  OUDE MEUK, TZT BEKIJKEN OF WE DIT UBERHAUPT GAAN GEBRUIKEN
#
# class Handeling(DvEntity, Act):
#     "Handeling als Nederlandse vertaling van Act. Base class"
#
#     class Hl7(Sat):
#         act_class = Columns.TextColumn(default_value=ActClass.care_provision)
#         act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)
#
#     class Default(Sat):
#         datum = Columns.DateTimeColumn()
#         eindtijd = Columns.DateTimeColumn()
#         status = Columns.RefColumn(RefTypes.gebeurtenis_status)
#
#     class Keys(Sat):
#         bronsysteem = Columns.TextColumn()
#         patientnummer = Columns.TextColumn()
#         nummer = Columns.TextColumn()
#
#
# class HandelingHandelingLink(Link, ActRelationship):
#     Types = ActRelationshipType
#     source = LinkReference(Handeling)
#     target = LinkReference(Handeling)
#
#
# class Traject(DvEntity, Act):
#     class Hl7(Sat):
#         act_class = Columns.TextColumn(default_value=ActClass.care_provision)
#         act_mood = Columns.TextColumn(default_value=ActMood.event_occurrence)
#
#     class Default(Sat):
#         code = Columns.TextColumn()
#         naam = Columns.TextColumn()
#         omschrijving = Columns.TextColumn()
#         start = Columns.DateTimeColumn()
#         eind = Columns.DateTimeColumn()
#         status = Columns.RefColumn(RefTypes.traject_status)
#
#
#
# class TrajectTrajectLink(Link, ActRelationship):
#     """Class voor hierarchie van trajecten, zoals b.v. zorgtraject en subtraject.
#
#     The target Acts do not have an existence independent of the source Act.
#     UsageNote: In UML 1.1, this is a "composition" defined as:
#         "A form of aggregation with strong ownership and coincident lifetime as part of the whole.
#         Parts with non-fixed multiplicity may be created after the composite itself,
#         but once created they live and die with it (i.e., they share lifetimes).
#         Such parts can also be explicitly removed before the death of the composite.
#         Composition may be recursive."
#     """
#     Types = ActRelationshipType
#     source = LinkReference(Traject)
#     target = LinkReference(Traject)
#
#
#
# class Traject_Handeling_Link(Link, ActRelationship):
#     """Class voor aggregatie van trajecten uit handelingen, zoals zorgactiviteiten in een subtraject
#
# 	The target Acts are aggregated by the source Act. Target Acts may have independent existence,
# 	participate in multiple ActRelationships, and do not contribute to the meaning of the source.
#
#     UsageNotes: This explicitly represents the conventional notion of aggregation.
#     The target Act is part of a collection of Acts (no implication is made of cardinality,
#     a source of Acts may contain zero, one, or more member target Acts).
#     """
#
#     class Hl7(Sat):
#         act_relationship_type = Columns.TextColumn(default_value=ActRelationshipType.has_member)
#
#
#
# # Vanaf hier afgeleide classes van Handeling en Traject
# class Zorgcontactmoment(Handeling):
#     "https://zibs.nl/wiki/Contact Alternatieve naam om onderscheid te maken tussen reguliere (CRM) contactmomenten"
#
#     class Hl7(Sat):
#         act_class = Columns.TextColumn(default_value=ActClass.encounter)  # Andere act_class dan Handeling; meer specifiek
#         act_mood = ActMood.event_occurrence


#
# class Afspraak(Handeling):
#     "Concern conform definitie https://zibs.nl/wiki/OverdrachtConcern"
#     act_class = ActClass.concern
#     act_mood = ActMood.appointment
#
#     class Default(Sat):
#         agb_zorgverlener_code = Columns.TextColumn()
#         afspraaksoort_code = Columns.TextColumn()
#         afspraaksoort_omschrijving = Columns.TextColumn()
#         afspraakstatus_code = Columns.TextColumn()
#         afspraakstatus_omschrijving = Columns.TextColumn()
#         afspraaknummer = Columns.TextColumn()
#
#
# class Meettraject(Traject):
#
#     pass
#
#
# class Concern(Handeling):
#     "Concern conform definitie https://zibs.nl/wiki/OverdrachtConcern"
#     act_class = ActClass.concern
#     act_mood = ActMood.event_occurrence
#
#
#
#
#
#
# class GeplandeZorgActiviteit(Zorgcontactmoment):
#     "https://zibs.nl/wiki/OverdrachtGeplandeZorgActiviteit"
#     act_mood = ActMood.appointment_request  # APT = Appointment
#
#
#
# class Declaratie(Handeling):
#     act_class = ActClass.financial_adjudication_financial_adjudication_results
#     act_mood = ActMood.event_occurrence
#
#
# class Factuurregel(Handeling):
#     act_class = ActClass.financial_transaction  # XACT = financial transaction
#     act_mood = ActMood.event_occurrence
#
#
#
#
#
# # ActRelationship zijn letterlijk links in DV, ActRelationshipType geeft semantische betekenis
# # Vraag: kunnen/willen we verschillende ActRelationships combineren?!
# # class LinkConcernSubtraject(ActRelationship):
# #     pass
# #     # todo act_relationship_type = ActRelationshipType.RSON        # Subtraject has-reason concern
# #
# #
# # class LinkSubtrajectZorgcontactmoment(ActRelationship):
# #     pass
# #     # todo act_relationship_type = ActRelationshipType.PART        # Zorgactiviteit is-part-of Subtraject
# #
# #
# # class LinkSubtrajectVerrichting(ActRelationship):
# #     pass
# #     # todo act_relationship_type = ActRelationshipType.PART        # Verrichting is-part-of Subtraject
# #
# #
# # class LinkSubtrajectDeclaratie(ActRelationship):
# #     pass
# #     # todo act_relationship_type = ActRelationshipType.CHRG        # Subtraject has-charge Declaratie
# #
# #
# # class LinkDeclaratieFactuurregel(ActRelationship):
# #     pass
# #     # todo act_relationship_type = ActRelationshipType.COVBY       # Factuurregels is-covered-by Declaratie (waar polis en declarabel product is gecontroleerd)
#
#
#
# # Unit test
# # def test():§§
# #     e = Subtraject()
# #     assert e.act_class == ActClass.PCPR, print("Subtraject is geen Act-type care provision")
# #     assert e.act_mood == ActMood.EVN, print("Subtraject is geen Mood-type event")
