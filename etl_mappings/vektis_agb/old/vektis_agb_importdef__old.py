__author__ = 'hvreenen'

"""Met een 'True' value wordt hier aangegeven dat dit veld meegenomen moet worden voor het verkrijgen van de bk."""

vektis_import_def = {
    'instel': (
        ('soort_instelling', 2, True),
        ('instellingsnummer', 6, True),
        ('naam_instelling', 60),
        ('straat', 24),
        ('huisnummer', 5),
        ('huisnummer_toevoeging', 5),
        ('postcode', 6),
        ('plaats', 24),
        ('telefoon', 11),
        ('datum_einde', 8)
    ),
    'fagbx20': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('zorgverlenersnummer', 6, True),
        ('naam', 25),
        ('voorletters', 6),
        ('voorvoegsel', 10),
        ('adellijke_titel', 2),
        ('academische_titel', 3),
        ('straat', 24),
        ('huisnummer', 5),
        ('huisnummer_toevoeging', 5),
        ('postcode', 6),
        ('plaatsnaam', 24),
        ('telefoonnummer', 11),
        ('geboortedatum', 8),
        ('geslacht', 1),
        ('datum_aanvang_beroep', 8),
        ('datum_einde_beroep', 8),
        ('nadere_verbijzondering_zvl_srt', 2),
        ('mutatiesoort', 1),
        ('reserve', 96)
    ),

    'fagbx21': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('zorgverlenersnummer', 6, True),
        ('indicatie_hoogleraar', 1),
        ('reden_einde_beroep', 1),
        ('mutatiesoort', 1),
        ('reserve', 142)
    ),

    'fagbx22': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('zorgverlenersnummer', 6, True),
        ('praktijknummer', 5, True),
        ('datum_toetreding_praktijk', 8),
        ('datum_uittreding_praktijk', 8),
        ('status_in_de_praktijk', 1),
        ('mutatiesoort', 1),
        ('praktijksoort', 2),
        ('reserve', 220)
    ),

    'fagbx23': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('praktijknummer', 5, True),
        ('naam_deel_1', 46),
        ('telefoonnummer', 11),
        ('datum_aanvang_praktijk', 8),
        ('datum_einde_praktijk', 8),
        ('filler', 1),
        ('organisatievorm', 1),
        ('mutatiesoort', 1),
        ('reserve', 142)
    ),

    'fagbx24': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('zorgverlenersnummer', 6, True),
        ('instellingsnummer', 6, True),
        ('datum_toetreding_praktijk', 8),
        ('datum_uittreding_praktijk', 8),
        ('status_in_de_instelling', 1),
        ('mutatiesoort', 1),
        ('reserve', 220)
    ),

    'fagbx25': (
        ('aanduiding_oud', 1),
        ('bestandcode', 2),
        ('zorgverlenersoort', 2, True),
        ('praktijknummer', 5, True),
        ('praktijkadres_volgnummer', 2, True),
        ('straat', 24),
        ('huisnummer', 5),
        ('huisnummer_toevoeging', 5),
        ('postcode', 6),
        ('plaatsnaam', 24),
        ('mutatiesoort', 1),
        ('reserve', 220)
    )
}
