import time
from domainmodels import role_domain
from mappings.performances.performance_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings, \
    create_jsonb_variants
from pyelt.pipeline import Pipeline


def define_performance_pipe(pipeline, test_config):
    pipe = pipeline.get_or_create_pipe('performance', test_config)
    # pipe.register_domain(role_domain)
    #
    source_to_sor_mappings = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(source_to_sor_mappings)

    create_jsonb_variants()  # genereert de jsonb varianten van de "gewone tabellen" voor testen van performance

    #
    # sor_to_ref_mappings = init_sor_to_dv_mappings(pipe)
    # pipe.mappings.extend(sor_to_ref_mappings)
    # #
    # sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    # pipe.mappings.extend(sor_to_dv_mappings)


def performance_main(*args):
    from pipelines.general_clinical_configs import general_config, test_config
    start = time.time()
    pipeline = Pipeline(general_config)
    define_performance_pipe(pipeline, test_config)
    pipeline.run()

if __name__ == '__main__':
    performance_main()

