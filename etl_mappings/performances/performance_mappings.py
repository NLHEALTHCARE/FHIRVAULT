import glob
import os

import datetime

from pipelines.general_clinical_configs import general_config

from psycopg2.extras import DictCursor
from sqlalchemy import create_engine

from etl_mappings.performances.performance_domain import Gewoon
from pyelt.sources.files import CsvFile
from pyelt.mappings.sor_to_dv_mappings import SorToEntityMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping


def execute_sql(sql):
    engine = create_engine(general_config['conn_dwh'])
    # engine = create_engine('postgresql://postgres:Welkomnlhc2016@localhost:5432/jsontest')
    conn = engine.raw_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)

    cursor.execute(sql)
    conn.commit()
    cursor.close()


def execute_sql2(sql):
    # conn = psycopg2.connect("""host='localhost' dbname='pyelt_unittests' user='postgres' password='{}'""".format(get_your_password()))
    engine = create_engine(general_config['conn_dwh'])
    conn = engine.raw_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()

    return result


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []

    #####################
    # performgewoon_100 #
    #####################

    data_path = pipe.config['data_path']
    source_file = CsvFile(data_path + 'performgewoon_100.csv', delimiter=';')
    source_file.reflect()
    source_file.set_primary_key(['id'])

    sor_mapping = SourceToSorMapping(source_file, 'performgewoon_100_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ##########################
    # performgewoon_1miljoen #
    ##########################

    data_path = pipe.config['data_path']
    source_file = CsvFile(data_path + 'performgewoon_1miljoen.csv', delimiter=';')
    source_file.reflect()
    source_file.set_primary_key(['id'])

    sor_mapping = SourceToSorMapping(source_file, 'performgewoon_1miljoen_hstage', auto_map=True)
    mappings.append(sor_mapping)

    ###########################
    # performgewoon_10miljoen #
    ###########################

    data_path = pipe.config['data_path']
    source_file = CsvFile(data_path + 'performgewoon10mil.csv', delimiter=';')
    source_file.reflect()
    source_file.set_primary_key(['id'])

    sor_mapping = SourceToSorMapping(source_file, 'performgewoon_10miljoen_hstage', auto_map=True)
    mappings.append(sor_mapping)

    return mappings


def create_jsonb_variants():  # De jsonb-tabellen worden op deze manier aangemaakt, want het exporteren van een geldig jsonb bestand werkte niet.

    sql = """
    DROP TABLE if exists sor_test.performjsonb_100_hstage;

    CREATE TABLE sor_test.performjsonb_100_hstage(
	  id SERIAL PRIMARY KEY,
	  details JSON NOT NULL
	);

	insert into sor_test.performjsonb_100_hstage (details)
    select
        row_to_json(t)
    FROM
        (SELECT waarde1, waarde2, waarde3 FROM sor_test.performgewoon_100_hstage) as t;

    ALTER TABLE sor_test.performjsonb_100_hstage ALTER COLUMN details type JSONB using details::text::jsonb;

    """


    sql2 = """
    DROP TABLE if exists sor_test.performjsonb_1miljoen_hstage;

    CREATE TABLE sor_test.performjsonb_1miljoen_hstage(
	  id SERIAL PRIMARY KEY,
	  details JSON NOT NULL
	);

	insert into sor_test.performjsonb_1miljoen_hstage (details)
    select
        row_to_json(t)
    FROM
        (SELECT waarde1, waarde2, waarde3 FROM sor_test.performgewoon_1miljoen_hstage) as t;

    ALTER TABLE sor_test.performjsonb_1miljoen_hstage ALTER COLUMN details type JSONB using details::text::jsonb;"""

    sql3 = """
    DROP TABLE if exists sor_test.performjsonb_10miljoen_hstage;

    CREATE TABLE sor_test.performjsonb_10miljoen_hstage(
	  id SERIAL PRIMARY KEY,
	  details JSON NOT NULL
	);

	insert into sor_test.performjsonb_10miljoen_hstage (details)
    select
        row_to_json(t)
    FROM
        (SELECT waarde1, waarde2, waarde3 FROM sor_test.performgewoon_10miljoen_hstage) as t;

    ALTER TABLE sor_test.performjsonb_10miljoen_hstage ALTER COLUMN details type JSONB using details::text::jsonb;


    """

    execute_sql(sql)
    execute_sql(sql2)
    execute_sql(sql3)


def init_sor_to_dv_mappings(pipe):
    mappings = []
    sor = pipe.sor

    mapping = SorToEntityMapping('performgewoon_100_hstage', Gewoon, sor)
    mapping.map_bk('id')

    mapping.map_field('id', Gewoon.Default.id)
    mapping.map_field('waarde1', Gewoon.Default.waarde1)
    mapping.map_field('waarde2', Gewoon.Default.waarde2)
    mapping.map_field('waarde3', Gewoon.Default.waarde3)

    mappings.append(mapping)

    return mappings
