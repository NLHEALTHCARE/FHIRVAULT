from etl_mappings.timeff.timeff_proces import define_timeff_pipe

from etl_mappings.adres_nl.adresnl_process import define_adres_nl_pipe
from etl_mappings.dbc.dbc_proces import define_dbc_pipe
from etl_mappings.manual_data.manula_data_proces import define_manual_data_pipe
from etl_mappings.nictiz_webscraping.nictiz_process import define_nictiz_pipe
from etl_mappings.nictiz_webscraping.xml_parser_nictiz import scrape_from_web
from etl_mappings.vektis_agb.vektis_agb_proces import define_vektis_agb_pipe, convert_vektis_zips_to_csv
from pipelines.general_clinical_configs import *

# from etl_mappings.vektis_uzovi.vektis_uzovi_proces import create_vektis_uzovi_pipe
from pyelt.pipeline import Pipeline


def create_vektis_uzovi_pipe(pipeline):
    pass


def main_pipeline_run():
    #

    pipeline = Pipeline(general_config)

    if nictiz_config['active']:
        define_nictiz_pipe(pipeline, nictiz_config)
        if nictiz_config['use_scraping']:
            scrape_from_web(nictiz_config)

    if manual_data_config['active']:
        define_manual_data_pipe(pipeline, manual_data_config)

    if vektis_agb_config['active']:
        if vektis_agb_config['convert_vektis_zips_to_csv']:
            convert_vektis_zips_to_csv()
        define_vektis_agb_pipe(pipeline, vektis_agb_config)

    if vektis_uzovi_config['active']:
        create_vektis_uzovi_pipe(pipeline, vektis_uzovi_config)

    if adresnl_config['active']:
        define_adres_nl_pipe(pipeline, adresnl_config)

    if dbc_config['active']:
        define_dbc_pipe(pipeline, dbc_config)

    pipeline.run()


if __name__ == '__main__':
    main_pipeline_run()
