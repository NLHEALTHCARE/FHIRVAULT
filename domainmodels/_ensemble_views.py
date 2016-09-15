from pyelt.datalayers.dv import Ensemble_view


# from _unit_tests.unit_tests_rob._domain_rob import *


class TestEnsemble(Ensemble_view):
    def __init__(self):
        Ensemble_view.__init__(self, name='', entity_and_link_list=[])
        self.name = 'test_view'  # naam van de ensemble_view
        self.add_entity_or_link(Zorginstelling)  # alleen entiteit aangegeven, alias is niet verplicht
        self.add_entity_or_link(Zorgverlener, 'huisarts')  # hier wordt het alias 'huisarts' aangemaakt
        self.add_entity_or_link(Zorgverlener, 'fysio')
        self.add_entity_or_link(Zorgverlener_Zorginstelling_Link, 'link')


