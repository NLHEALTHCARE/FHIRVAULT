from domainmodel_fhir import test_domain

from domainmodel_fhir.test_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings
from pyelt.pipeline import Pipeline

# pipeline = Pipeline(config=test_configs)
# pipe = pipeline.get_or_create_pipe('test')
# pipe.register_domain(test_domain)
# pipeline.run()

def define_test_pipe(pipeline, test_config):
    pipe = pipeline.get_or_create_pipe('sor_test', test_config)
    pipe.register_domain(test_domain)

    mappings = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(mappings)


    pipe.mappings.extend(init_sor_to_dv_mappings(pipe))


def test_main(*args):
    # from pipelines.general_clinical_configs import general_config, test_config
    from domainmodel_fhir.test_config import test_configs, test_config
    pipeline = Pipeline(test_configs)

    define_test_pipe(pipeline, test_config)

    pipeline.run()


if __name__ == '__main__':
    test_main()