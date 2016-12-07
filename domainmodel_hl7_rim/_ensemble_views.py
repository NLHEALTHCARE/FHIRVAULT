from domainmodels.role_domain import Zorgverlener, Zorgaanbieder, ZorgverlenerZorgaanbiederLink, Medewerker
from pyelt.datalayers.dv import EnsembleView


# from _unit_tests.unit_tests_rob._domain_rob import *


class ZorgaanbiederEnsemble(EnsembleView):
    zorginstelling = Zorgaanbieder
    huisarts = Zorgverlener
    fysio = Zorgverlener
    link = ZorgverlenerZorgaanbiederLink


    def __init__(self):
        EnsembleView.__init__(self, name='', entity_and_link_list=[])
        self.name = 'test_view'  # naam van de ensemble_view
        self.add_entity_or_link(Zorgaanbieder)  # alleen entiteit aangegeven, alias is niet verplicht
        self.add_entity_or_link(Zorgverlener, 'huisarts')  # hier wordt het alias 'huisarts' aangemaakt
        self.add_entity_or_link(Zorgverlener, 'fysio')
        self.add_entity_or_link(ZorgverlenerZorgaanbiederLink, 'link')


