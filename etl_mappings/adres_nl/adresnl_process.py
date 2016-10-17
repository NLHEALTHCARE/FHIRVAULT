from pyelt.pipeline import Pipeline

from domainmodels import entity_domain
from etl_mappings.adres_nl import adresnl_db_functions
from etl_mappings.adres_nl.adresnl_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings
# from pipelines.general_clinical_configs import general_config


"""vektis agb_codes komen van https://www.zorgprisma.nl  """

def define_adres_nl_pipe(pipeline, adresnl_config):
    pipe = pipeline.get_or_create_pipe('adresnl', config=adresnl_config)

    pipe.register_domain(entity_domain)
    pipe.register_db_functions(adresnl_db_functions, pipe.sor)

    mappings = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(mappings)

    pipe.mappings.extend(init_sor_to_dv_mappings(pipe))


def adres_nl_main(*args):
    from pipelines.general_clinical_configs import general_config
    pipeline = Pipeline(general_config)

    define_adres_nl_pipe(pipeline, general_config)

    pipeline.run()


if __name__ == '__main__':
    adres_nl_main()
