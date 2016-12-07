from domainmodel_fhir_simplified import identity_domain
from etl_mappings.vektis_uzovi.vektis_uzovi_mappings import init_sor_to_dv_mappings, init_source_to_sor_mappings


def define_vektis_uzovi_pipe(pipeline, vektis_uzovi_config):
    pipe = pipeline.get_or_create_pipe('vektis_uzovi', vektis_uzovi_config)
    pipe.register_domain(identity_domain)
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
    pass # zie main proces in CLINCS-repo


if __name__ == '__main__':
    vektis_uzovi_main()



