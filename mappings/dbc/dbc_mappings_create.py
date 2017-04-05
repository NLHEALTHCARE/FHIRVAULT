from domainmodel.ref_domain import *
from pyelt.datalayers.database import Table
from pyelt.helpers.mappingcreator import MappingWriter
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.pipeline import Pipeline
from pyelt.sources.files import CsvFile


def create_mappings(pipe):
    tbl = Table('zorgproductgroepen_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, Zorgproductgroep)
    tbl = Table('zorgactiviteiten_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, Zorgactiviteit)
    tbl = Table('tarieven_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, Tarief)
    tbl = Table('diagnose_combinatie_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, DiagnoseCombinatie)
    tbl = Table('afsluitregels_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, AfsluitRegel)
    tbl = Table('afsluitreden_hstage', pipe.sor)
    MappingWriter.create_python_code_mappings(tbl, AfsluitReden)

from domainmodel.test_configs import general_config
from domainmodel import ref_domain
pipeline = Pipeline(general_config)
pipe = pipeline.get_or_create_pipe('sor_dbc', {'sor_schema': 'sor_dbc'})
pipe.register_domain(ref_domain)



create_mappings(pipe)


