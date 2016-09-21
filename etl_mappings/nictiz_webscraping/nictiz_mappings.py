from pyelt.mappings.sor_to_dv_mappings import SorToRefMapping
from pyelt.mappings.source_to_sor_mappings import SourceToSorMapping
from pyelt.mappings.validations import SorValidation
from pyelt.sources.files import CsvFile


def init_source_to_sor_mappings(pipe):
    mappings = []
    validations = []

    ###############################
    # valuesets
    ###############################
    data_path = pipe.config['data_path']
    source_file = CsvFile(data_path + '/valuesets.csv', delimiter=';')

    source_file.reflect()
    source_file.set_primary_key(['id', 'code', 'ingangsdatum', 'level'])
    sor_mapping = SourceToSorMapping(source_file, 'valuesets_hstage', auto_map=True)
    mappings.append(sor_mapping)

    validation = SorValidation(tbl='valuesets_hstage', schema=pipe.sor)
    validation.msg = 'Dubbel codes'
    validation.set_check_for_duplicate_keys(['code', 'valueset', 'level'])
    validations.append(validation)

    return mappings, validations


def init_sor_to_dv_mappings():
    mappings = []

    ###############################
    # valuesets
    ###############################
    ref_mapping = SorToRefMapping('valuesets_hstage')
    ref_mapping.map_code_field('code')
    ref_mapping.map_descr_field('displayName')
    ref_mapping.map_type_field('valueset', 'id')
    ref_mapping.map_level_field('level')
    ###
    ref_mapping.map_leveltype_field('type')
    ###
    mappings.append(ref_mapping)
    return mappings
