from pyelt.pipeline import Pipeline

from domainmodels import role_domain
from etl_mappings.manual_data.manual_data_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings


def define_manual_data_pipe(pipeline, manual_data_config):
    """in manual data staan voorlopig alleen nog de klinieken, kvknummers en agbcodes"""
    pipe = pipeline.get_or_create_pipe('manual_data', manual_data_config)
    pipe.register_domain(role_domain)

    source_to_sor_mappings = init_source_to_sor_mappings(manual_data_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)

    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def manual_data_proces_main(*args):
    from pipelines.general_clinical_configs import general_config
    pipeline = Pipeline(general_config)
    define_manual_data_pipe(pipeline)
    pipeline.run()


if __name__ == '__main__':
    manual_data_proces_main()