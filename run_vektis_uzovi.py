import sys
sys.path.insert(0, '/home/costiaan/PYELT')
sys.path.insert(0, '/home/costiaan/CLINICAL_DATAVAULT')

from etl_mappings.vektis_uzovi.vektis_uzovi_proces import run

if __name__ == '__main__':
    run()