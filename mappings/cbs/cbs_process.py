from mappings.cbs.cbs_mappings import init_source_to_sor_mappings





def define_cbs_pipe(pipeline, adresnl_config):
    pipe = pipeline.get_or_create_pipe('cbs', config=adresnl_config)

    mappings = init_source_to_sor_mappings(pipe)
    pipe.mappings.extend(mappings)

    # pipe.mappings.extend(init_sor_to_valset_mappings(pipe))


