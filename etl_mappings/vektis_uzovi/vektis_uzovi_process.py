from pipelines.general_clinical_configs import vektis_uzovi_config

from domainmodels import role_domain
from etl_mappings.vektis_uzovi.vektis_uzovi_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings
from pipelines.general_clinical_configs import general_config
from pyelt.pipeline import Pipeline


def run():
    pipeline = Pipeline(general_config)
    pipe = pipeline.get_or_create_pipe('vektis', vektis_config)
    pipe.register_domain(role_domain)
    pipe.mappings.extend(init_source_to_sor_mappings(pipe.source_db))
    pipe.mappings.extend(init_sor_to_dv_mappings(pipe))
    pipeline.run()


if __name__ == '__main__':
    run()
