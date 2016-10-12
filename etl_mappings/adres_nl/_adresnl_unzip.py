"""Unzippen van postcodenl update bestanden bijvoorbeeld van https://retrieve.postcode.nl/retrieve.php?hash=63e7fad64879ff12bd87e18bfac71b2c
   en de bestandsnamen aanpassen zodat de periode waarvoor die update goldt terug te zien is in de bestandsnaam"""

import os
import zipfile
import glob


# from pipelines.clinics import adresnl_config
from pipelines.general_clinical_configs import general_config, adresnl_config


class PostcodesNL:
    def __init__(self):
        self.download_path = adresnl_config['download_path']
        self.zip_name = ''
        self.zip_date = '' # hierin komt te staan voor welke data de update geldt.

    def set_URL(self, URL):
        self.URL = URL
        return self.URL

    def get_zip_name(self):
        os.chdir(self.download_path)
        zip_name = glob.glob('mut*.zip')
        assert len(zip_name) == 1, 'Er zijn geen zip files die starten met "mut" of er zijn er meerdere. Er zou maar 1 zip file startend met "mut" moeten zijn (oude varianten worden na unzippen verwijderd'

        self.zip_name = zip_name[0]

        #todo: Nadat de postcodenl_update zip uitgepakt is mag deze zip file niet meer in de downloads folder staan.dus verwijderen of verplaatsen
        # print('{} is now removed from download folder'.format(self.zip_name))
        # os.remove(self.zip_name)
        return self.zip_name

    def unzip_file(self):

        zip_ref = zipfile.ZipFile('{}{}'.format(self.download_path, self.zip_name), 'r')
        zip_ref.extractall(adresnl_config['data_path'])
        zip_ref.close()

    def get_zip_date(self):
        self.zip_date = self.zip_name[3:21] # dit heeft als result een string dat er min of meer als volgt uitziet: "_20160801-20160905". Deze string geeft dus aan over welke periode het gaat (jaar maand dag - jaar maand dag)
        return self.zip_date

    def rename_csv_and_schema(self):
        os.chdir(adresnl_config['data_path'])
        if os.path.exists('adresnl_update{}.csv'.format(self.zip_date)):
            pass
        else:
            os.rename('mut_pcdata.csv','adresnl_update{}.csv'.format(self.zip_date))
        if os.path.exists('adresnl_update{}.schema'.format(self.zip_date)):
            pass
        else:
            os.rename('mut_pcdata.schema','adresnl_update{}.schema'.format(self.zip_date))

    def get_csv_name(self):
        self.csv_name = 'adresnl_update{}.csv'.format(self.zip_date)
        return self.csv_name


    def postcodenl_run(self):

        pcnl = PostcodesNL()
        pcnl.set_URL('https://retrieve.postcode.nl/retrieve.php?hash=63e7fad64879ff12bd87e18bfac71b2c') #todo: deze url verandert waarschijnlijk bij iedere nieuwe update. Moet waarschijnlijk dus handmatig aangepast gaan worden iedere keer.
        pcnl.get_zip_name()
        pcnl.unzip_file()
        pcnl.get_zip_date()
        # pcnl.rename_csv_and_schema()
        pcnl.get_csv_name()

        print(pcnl.csv_name)



if __name__ == '__main__':

    pcnl = PostcodesNL()
    pcnl.postcodenl_run()



    # pcnl = PostcodesNL()
    # pcnl.set_URL('https://retrieve.postcode.nl/retrieve.php?hash=89bf575f699daba0c46c53493f63ac3b') #todo: deze url verandert waarschijnlijk bij iedere nieuwe update. Moet waarschijnlijk dus handmatig aangepast gaan worden iedere keer.
    # pcnl.get_zip_name()
    # pcnl.unzip_file()
    # pcnl.get_zip_date()
    # # pcnl.rename_csv_and_schema()
    # pcnl.get_csv_name()
    #
    # print(pcnl.csv_name)











