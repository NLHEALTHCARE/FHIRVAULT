from domainmodels import role_domain
from etl_mappings.vektis_uzovi.vektis_uzovi_mappings import init_sor_to_dv_mappings, init_source_to_sor_mappings
from pyelt.pipeline import Pipeline


def define_nhg_pipe(pipeline, nhg_config):
    pipe = pipeline.get_or_create_pipe('nhg', nhg_config)
    pipe.register_domain(role_domain)
    #
    source_to_sor_mappings = init_source_to_sor_mappings(nhg_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)
    #
    sor_to_ref_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_ref_mappings)
    #
    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def nhg_main(*args):
    from pipelines.general_configs import general_config, nhg_config
    pipeline = Pipeline(general_config)
    define_nhg_pipe(pipeline, nhg_config)
    pipeline.run()


if __name__ == '__main__':
    nhg_main()



