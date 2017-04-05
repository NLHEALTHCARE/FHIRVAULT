from mappings.nictiz_webscraping.nictiz_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings
from mappings.nictiz_webscraping.xml_parser_nictiz import scrape_from_web
from pyelt.pipeline import Pipeline


def define_nictiz_pipe(pipeline, nictiz_config):
    pipe = pipeline.get_or_create_pipe('nictiz', nictiz_config)
    mappings, validations = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(mappings)
    pipe.validations.extend(validations)
    pipe.mappings.extend(init_sor_to_dv_mappings())


def nictiz_main():
    from pipelines.general_clinical_configs import general_config, nictiz_config

    pipeline = Pipeline(general_config)
    define_nictiz_pipe(pipeline, nictiz_config)
    if nictiz_config['use_scraping']:
        scrape_from_web(nictiz_config)
    pipeline.run()


if __name__ == '__main__':
    nictiz_main()
