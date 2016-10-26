from domainmodels import role_domain
from etl_mappings.vektis_uzovi.vektis_uzovi_mappings import init_sor_to_dv_mappings, init_source_to_sor_mappings
from pyelt.pipeline import Pipeline


def define_vektis_uzovi_pipe(pipeline, vektis_uzovi_config):
    pipe = pipeline.get_or_create_pipe('vektis_uzovi', vektis_uzovi_config)
    pipe.register_domain(role_domain)
    #
    source_to_sor_mappings = init_source_to_sor_mappings(vektis_uzovi_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)
    #
    sor_to_ref_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_ref_mappings)
    #
    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def vektis_uzovi_main(*args):
    from pipelines.general_configs import general_config, vektis_uzovi_config
    pipeline = Pipeline(general_config)
    define_vektis_uzovi_pipe(pipeline, vektis_uzovi_config)
    pipeline.run()


if __name__ == '__main__':
    vektis_uzovi_main()



