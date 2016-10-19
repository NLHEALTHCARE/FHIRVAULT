test_configs = {
    'log_path': '/logs/',
    'ddl_log_path': '/logs/ddl/',
    'sql_log_path': '/logs/sql/',
    'conn_dwh': 'postgresql://postgres:Welkomnlhc2016@localhost:5432/dwh2a',
    'debug': False,
    'ask_confirm_on_db_changes': False,
    'on_errors': 'log',
    'datatransfer_path': 'c:/tmp/',
    'data_root': 'C:/!OntwikkelDATA',
    'email_settings': {
        'send_log_mail_after_run': True,
        'from': 'server <henk-jan.van.reenen@nlhealthcareclinics.com>',
        'to': 'henk-jan.van.reenen@nlhealthcareclinics.com',
        'subject': 'blablaa',
        'msg': 'Hierbij de pyelt log\n\n\n(deze mail niet beantwoorden)\n\n'
    }
}

test_config = {
    'sor_schema': 'sor_test',
    'data_path': test_configs['data_root'] + '/jsontest/',

    'active': True
}