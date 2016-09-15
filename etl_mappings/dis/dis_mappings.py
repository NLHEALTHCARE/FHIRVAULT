from domainmodels.role_domain import Zorgverzekeraar
from etl_mappings.dis.dis_configs import dis_config
from etl_mappings.dis.dis_domain import *
from pyelt.datalayers.database import Table
from pyelt.helpers.mappingcreator import MappingWriter
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping, SorToLinkMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.sources.databases import SourceTable, SourceQuery
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(source_db):
    mappings = []

    ###############################
    # Account
    ###############################
    source_tbl = SourceTable('accountBase', source_db.default_schema, source_db)
    source_tbl.set_primary_key(['AccountId'])
    sor_mapping = SourceToSorMapping(source_tbl, 'account_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ###############################
    # Declaratietarief
    ###############################
    source_tbl = SourceTable('gz_declaratietariefExtensionBase', source_db.default_schema, source_db)
    source_tbl.set_primary_key(['gz_declaratietariefId'])
    sor_mapping = SourceToSorMapping(source_tbl, 'declaratietarief_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ###############################
    # Declaratieprestatie
    ###############################
    source_qry = SourceQuery(source_db, """
    select ext.*, OrganizationId, statecode, statuscode
    from Zorg_MSCRM.dbo.gz_declaratieprestatieExtensionBase ext
    inner join Zorg_MSCRM.dbo.gz_declaratieprestatieBase base on ext.gz_declaratieprestatieId=base.gz_declaratieprestatieId
    where year(gz_0408_Begindatumprestatie)=2016 and month(gz_0408_Begindatumprestatie)=7
    """, 'view_1')
    source_qry.set_primary_key(['gz_declaratieprestatieId'])
    sor_mapping = SourceToSorMapping(source_qry, 'declaratieprestatie_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ###############################
    # Declaratie
    ###############################
    source_qry = SourceQuery(source_db, """
    select ext.*, OrganizationId, statecode, statuscode
    from Zorg_MSCRM.dbo.gz_declaratieExtensionBase ext
    inner join Zorg_MSCRM.dbo.gz_declaratieBase base on ext.gz_declaratieId=base.gz_declaratieId
    inner join Zorg_MSCRM.dbo.gz_declaratieprestatieExtensionBase restraint on ext.gz_declaratieId=restraint.gz_declaratieId
    where year(gz_0408_Begindatumprestatie)=2016 and month(gz_0408_Begindatumprestatie)=7
    """, 'view_2')
    source_qry.set_primary_key(['gz_declaratieId'])
    sor_mapping = SourceToSorMapping(source_qry, 'declaratie_hstage', auto_map=True)
    mappings.append(sor_mapping)

    return mappings


# def create_python_code_mappings(pipe):
#     tbl = Table('uzovi_hstage', pipe.sor)
#     str=MappingWriter.create_python_code_mappings(tbl, Zorgverzekeraar)
#     print(str)

def init_sor_to_dv_mappings(pipe):
    sor = pipe.sor
    mappings = []
    return mappings
