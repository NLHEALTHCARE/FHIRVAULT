from domainmodel import identity_domain
from etl_mappings.vektis_agb.vektis_agb_mappings import init_source_to_sor_mappings, init_sor_to_valuesets_mappings, init_sor_to_dv_mappings

__author__ = 'hvreenen'

"""vektis agb_codes komen van https://www.zorgprisma.nl  """



def define_vektis_agb_pipe(pipeline, vektis_agb_config):
    pipe = pipeline.get_or_create_pipe('vektis_agb', vektis_agb_config)
    pipeline.register_domain(identity_domain)

    source_to_sor_mappings = init_source_to_sor_mappings(vektis_agb_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)
    #todo refs van vektis
    sor_to_valueset_mappings = init_sor_to_valuesets_mappings(pipe)
    pipe.mappings.extend(sor_to_valueset_mappings)

    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def vektis_main(*args):
    pass



if __name__ == '__main__':
    vektis_main()

