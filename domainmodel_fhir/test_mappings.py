import glob, os, io, zipfile

from domainmodel_fhir.test_domain import Patient

from pyelt.mappings.base import ConstantValue
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping, SorToRefMapping, EntityViewToEntityMapping, EntityViewToLinkMapping, \
    SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.mappings.transformations import FieldTransformation
from pyelt.mappings.validations import Validation
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []
    path = pipe.config['data_path']
    source_file = CsvFile('{}{}'.format(path, 'test.csv'), delimiter=';')



    source_file.reflect()
    source_file.set_primary_key(['patient_nummer'])
    sor_mapping = SourceToSorMapping(source_file, 'patient_hstage', auto_map=True)
    mappings.append(sor_mapping)

    return mappings


def init_sor_to_dv_mappings(pipe):

    mappings = []
    sor = pipe.sor

    mapping = SorToEntityMapping('patient_hstage', Patient, sor)
    mapping.map_bk('patient_nummer')
    mapping.map_field("patient_nummer", Patient.Default.patient_nummer)
    # mapping.map_field("active::boolean", Patient.Default.active)

    # mapping.map_field("gender", Patient.Default.gender)

    mapping.map_field("extra::jsonb", Patient.Default.extra)


    mapping.map_field("deceased_boolean::boolean", Patient.Default.extra2, json_field='overleden')
    mapping.map_field("deceased_datetime::date", Patient.Default.extra2, json_field = 'datum_overleden')
    mapping.map_field("birthdate::date", Patient.Default.birthdate)
    mapping.map_field("multiple_birth_boolean::boolean", Patient.Default.extra2)
    mapping.map_field("multiple_birth_integer::integer", Patient.Default.extra2)


    mappings.append(mapping)

    return mappings
