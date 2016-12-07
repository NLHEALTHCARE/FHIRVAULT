import csv
import glob
import io
import os
import time
import zipfile
from chardet import detect

from domainmodel_fhir_simplified import identity_domain
from etl_mappings.vektis_agb.vektis_agb_importdef import vektis_import_def
from etl_mappings.vektis_agb.vektis_agb_mappings import init_source_to_sor_mappings, init_sor_to_dv_mappings, \
    init_sor_to_ref_mappings
from pyelt.pipeline import Pipeline

__author__ = 'hvreenen'

"""vektis agb_codes komen van https://www.zorgprisma.nl  """



def define_vektis_agb_pipe(pipeline, vektis_agb_config):
    pipe = pipeline.get_or_create_pipe('vektis_agb', vektis_agb_config)
    pipe.register_domain(identity_domain)

    source_to_sor_mappings = init_source_to_sor_mappings(vektis_agb_config['data_path'])
    pipe.mappings.extend(source_to_sor_mappings)
    #todo refs van vektis
    # sor_to_ref_mappings = init_sor_to_ref_mappings(pipe)
    # pipe.mappings.extend(sor_to_ref_mappings)

    sor_to_dv_mappings = init_sor_to_dv_mappings(pipe)
    pipe.mappings.extend(sor_to_dv_mappings)


def vektis_main(*args):
    pass



if __name__ == '__main__':
    vektis_main()

