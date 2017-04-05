from domainmodel.identity_domain import Zorgverlener
from mappings.dbc.dbc_transformations import DbcTransformations
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToValueSetMapping
from domainmodel.valueset_domain import *
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.files import CsvFile

"""Nieuwe versie van dbc-dis bestanden op open dis data
http://www.opendisdata.nl/downloads

* REF ZPD: zorgproducten
* REF ZAT: zorgactiviteiten
* REF SPC: specialisme
* REF DNG: diagnosen
* DBC: met relaties ??
* DBC_PROFIEL: met relaties ??

"""
def init_source_to_sor_mappings(pipe):
    mappings = []
    path = pipe.config['data_path']
    source_file = CsvFile('{}{}'.format(path, '05_REF_ZPD.csv'), delimiter=',', encoding='latin1', quote='"')
    source_file.reflect()
    source_file.set_primary_key(['zorgproduct_cd'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgproduct_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '03_REF_ZAT.csv'), delimiter=',', encoding='latin1', quote='"')
    source_file.reflect()
    source_file.set_primary_key(['zorgactiviteit_cd'])
    sor_mapping = SourceToSorMapping(source_file, 'zorgactiviteit_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '04_REF_DGN.csv'), delimiter=',', encoding='latin1', quote='"')
    source_file.reflect()
    source_file.set_primary_key(['diagnose_cd'])
    sor_mapping = SourceToSorMapping(source_file, 'diagnose_hstage', auto_map=True)
    mappings.append(sor_mapping)

    source_file = CsvFile('{}{}'.format(path, '06_REF_SPC.csv'), delimiter=',', encoding='latin1', quote='"')
    source_file.reflect()
    source_file.set_primary_key(['specialisme_cd'])
    sor_mapping = SourceToSorMapping(source_file, 'specialisme_hstage', auto_map=True)
    mappings.append(sor_mapping)
    return mappings



def init_sor_to_valset_mappings(pipe):

    mappings = []
    s = 'versie,datum_bestand,peildatum,zorgproduct_cd,latijn_oms,consument_oms,declaratie_verzekerd_cd,declaratie_onverzekerd_cd'
    # mapping = SorToValueSetMapping('zorgproducten_hstage', Zorgproduct)
    # mapping.map_field("zorgproduct_cd", Zorgproduct.code)
    # mapping.map_field("consument_oms", Zorgproduct.omschrijving)
    # mapping.map_field("latijn_oms", Zorgproduct.omschrijving_latijn)
    # mapping.map_field("consument_oms", Zorgproduct.omschrijving_consument)
    # mapping.map_field("declaratie_verzekerd_cd", Zorgproduct.declaratie_code_verzekerde_zorg)
    # mapping.map_field("declaratie_onverzekerd_cd", Zorgproduct.declaratie_code_onverzekerde_zorg)
    # mappings.append(mapping)

    # Beschikbare velden ZORGACTIVITEITEN_HSTAGE:
    s = 'versie,datum_bestand,peildatum,zorgactiviteit_cd,omschrijving,zorgprofielklasse_cd,zorgprofielklasse_oms'
    # mapping = SorToValueSetMapping('zorgactiviteiten_hstage', Zorgactiviteit)
    # mapping.map_field("zorgactiviteit_code", Zorgactiviteit.code)
    # mapping.map_field("omschrijving", Zorgactiviteit.omschrijving)
    # mapping.map_field("zorgprofielklasse_cd", Zorgactiviteit.omschrijving_consument)
    # mapping.map_field("zorgprofielklasse_oms", Zorgactiviteit.groep_code)
    # mappings.append(mapping)

    # Beschikbare velden DIAGNOSE_HSTAGE:
    s = 'versie,datum_bestand,peildatum,diagnose_cd,specialisme_cd,diagnose_omschrijving'
    mapping = SorToValueSetMapping('diagnose_hstage', Diagnose)
    mapping.map_field("LPAD(diagnose_cd, 4, '0')", Diagnose.code)
    mapping.map_field("diagnose_omschrijving", Diagnose.omschrijving)
    mapping.map_field("specialisme_cd", Diagnose.specialisme_code)
    mappings.append(mapping)

    # Beschikbare velden SPECIALISMEN_HSTAGE:
    s = 'versie,datum_bestand,peildatum,specialisme_cd,omschrijving	'
    mapping = SorToValueSetMapping('specialisme_hstage', Specialisme)
    mapping.map_field("specialisme_cd", Specialisme.code)
    mapping.map_field("omschrijving", Specialisme.omschrijving)
    mappings.append(mapping)
    return  mappings
