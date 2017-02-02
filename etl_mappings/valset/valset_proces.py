from domainmodel import valueset_domain
from etl_mappings.dis.dis_mappings import init_source_to_sor_mappings, init_sor_to_valset_mappings
from pyelt.pipeline import Pipeline

__author__ = 'hvreenen'


def define_dis_pipe(pipeline, dis_config):
    pipe = pipeline.get_or_create_pipe('sor_dis', dis_config)
    pipeline.register_valset_domain(valueset_domain, 'valset')

    source_to_sor_mappings = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(source_to_sor_mappings)

    sor_to_valset_mappings = init_sor_to_valset_mappings(pipe)
    pipe.mappings.extend(sor_to_valset_mappings)



def dis_main(*args):
    from pipelines.general_clinical_configs import general_config, dis_config
    pipeline = Pipeline(general_config)

    define_dis_pipe(pipeline, dis_config)

    pipeline.run()


if __name__ == '__main__':
    dis_main()


