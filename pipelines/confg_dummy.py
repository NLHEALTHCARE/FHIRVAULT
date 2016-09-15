# KOPIEER DEZE FILE EN HERNOEM NAAR ...._configs
# MAAK EVENTUEEL DE DATABASE AAN IN DE POSTGRES DB MANAGER
# MAAK EVENTUEEL DE LOGS FOLDER AAN
# PAS ONDERSTAANDE WAARDEN AAN IN DE CONFIG


general_config = {
    'log_path': '/logs/',
    'ddl_log_path': '/logs/ddl/',
    'sql_log_path': '/logs/sql/',
    'conn_dwh': 'postgresql://user:pwd@localhost:5432/dwh2',
    'debug': False,  # Zet debug op true om een gelimiteerd aantal rijen op te halen
    'datatransfer_path': '/tmp/pyelt/datatransfer',  # voor linux server: datatransfer pad mag niet in /home folder zijn, want anders kan postgres er niet bij
    'on_errors': 'log',
# vul 'throw' in als je wilt dat het programma stopt zodra er een error optreedt, zodat je die kunt afvangen. Kies log voor als je wilt dat de error gelogt wordt en doorgaat met de volgende stap
    'datatransfer_path': 'c:/tmp/',
    'data_root': 'C:/data/',
    'ask_confirm_on_db_changes': False
}

pipe_dummy1_config = {
    'sor_schema': 'sor_dummy',
    'data_path': general_config['data_root'] + '/dummy/',
    'active': True,
    'connection_string': '',
    'other_configs': None
}

pipe_dummy2_config = {
    'sor_schema': 'sor_dummy',
    'data_path': general_config['data_root'] + '/dummy/',
    'active': True,
    'connection_string': '',
    'other_configs': None
}
