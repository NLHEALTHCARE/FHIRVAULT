from pipelines.general_clinical_configs import vektis_uzovi_config
from pipelines.general_clinical_configs import general_config
from domainmodels import role_domain
from pyelt.pipeline import Pipeline
from etl_mappings.vektis_uzovi.vektis_uzovi_mappings import init_sor_to_dv_mappings, init_source_to_sor_mappings


def run():
    pipeline = Pipeline(general_config)
    pipe = pipeline.get_or_create_pipe('vektis_uzovi', vektis_uzovi_config)
    pipe.register_domain(role_domain)
    pipe.mappings.extend(init_source_to_sor_mappings(pipe.source_db))
    pipe.mappings.extend(init_sor_to_dv_mappings(pipe))
    pipeline.run()


if __name__ == '__main__':
    run()
