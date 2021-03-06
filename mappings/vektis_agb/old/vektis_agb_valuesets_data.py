from domainmodel.valueset_domain import ValueSetsEnum

vektis_valuesets_data = {ValueSetsEnum.specialisme_codes: {'01': 'Huisartsen',
                                                '02': 'Apothekers',
                                                '03': 'Medisch specialisten',
                                                '04': 'Fysiotherapeuten',
                                                '05': 'Logopedisten',
                                                '07': 'Oefentherapeuten',
                                                '08': 'Verloskundigen',
                                                           '11': 'Tandarts-specialisten mondziekten en kaakchirurgie)',
                                                           '12': 'Tandartsen',
                                                           '13': 'Tandarts-specialisten dento-maxillaire orthopedie)',
                                                           '14': 'Arts arbeid en gezondheid/bedrijfsgeneeskunde',
                                                           '17': 'Rechtspersonen',
                                                           '24': 'Dietisten',
                                                           '26': 'Podotherapeuten',
                                                           '44': 'Optometristen',
                                                           '57': 'Physician assistant',
                                                           '76': 'Leveranciers hulpmiddelen',
                                                           '84': 'Overige artsen',
                                                           '85': 'Taxivervoerders',
                                                           '87': 'Mondhygienisten',
                                                           '88': 'Ergotherapeuten',
                                                           '89': 'Schoonheidsspecialistes',
                                                           '90': 'Genezers',
                                                           '91': 'Verpleegkundigen',
                                                           '93': 'Tandtechnici / tandprothetici',
                                                           '94': 'Psychologische zorgverleners',
                                                           '96': 'Pedicuren',
                                                           '98': 'Declaranten'},

                         ValueSetsEnum.academische_titels: {'bc': 'Baccalaureus',
                                                 'dr': 'Doctor',
                                                 'drs': 'Doctorandus',
                                                 'ing': 'Ingenieur HBO',
                                                 'ir': 'Ingenieur WO',
                                                 'm': 'Master',
                                                 'mr': 'Meester in de rechten WO'},

                         ValueSetsEnum.adelijke_titels: {'B': 'Baron',
                                              'BS': 'Barones',
                                              'G': 'Graaf',
                                              'GI': 'Gravin',
                                              'H': 'Hertog',
                                              'HI': 'Hertogin',
                                              'JH': 'Jonkheer',
                                              'JV': 'Jonkvrouw',
                                              'M': 'Markies',
                                              'MI': 'Markiezin',
                                              'P': 'Prins',
                                              'PS': 'Prinses',
                                              'R': 'Ridder',
                                              'PR': 'Professor'},

                         ValueSetsEnum.geslacht_types: {'0': 'Onbekend',
                                             '1': 'Man',
                                             '2': 'Vrouw',
                                             '9': 'Niet gespecificeerd'},

                         ValueSetsEnum.vektis_praktijk_statussen:
                       {'1': 'vrijgevestigd',
                        '2': 'vrijgevestigd medisch specialist, toelatingsovereenkomst getekend',
                        '3': 'in loondienst',
                        '4': 'vrijgevestigd medisch specialist, toelatingsovereenkomst getekend'},

                         ValueSetsEnum.vektis_verbijzonderingscodes:
                       {'01-01': 'Niet apotheekhoudend',
                        '01-10': 'Apotheekhoudend',
                        '01-20': 'Alternatieve huisarts',
                        '03-01': 'Oogheelkunde medisch specialist)',
                        '03-02': 'Keel-,neus- en oorheelkunde',
                        '03-03': 'Chirurgie',
                        '03-04': 'Plastische chirurgie',
                        '03-05': 'Orthopedie',
                        '03-06': 'Urologie',
                        '03-07': 'Verloskunde en gynaecologie',
                        '03-08': 'Neurochirurgie',
                        '03-09': 'Zenuw - en zielsziekten',
                        '03-10': 'Dermatologie',
                        '03-13': 'Inwendige geneeskunde',
                        '03-16': 'Kindergeneeskunde',
                        '03-18': 'Gastro-enterologie',
                        '03-20': 'Cardiologie',
                        '03-22': 'Longziekten',
                        '03-24': 'Reumatologie',
                        '03-26': 'Allergologie',
                        '03-27': 'Revalidatie',
                        '03-28': 'Cardio-pulmonale chirurgie',
                        '03-29': 'Psychiatrie',
                        '03-30': 'Neurologie',
                        '03-35': 'Geriatrie',
                        '03-61': 'Radiotherapie',
                        '03-62': 'Radiologie',
                        '03-63': 'Nucleaire geneeskunde',
                        '03-86': 'Klinische chemie',
                        '03-87': 'Medische microbiologie',
                        '03-88': 'Pathologische anatomie',
                        '03-89': 'Anesthesiologie',
                        '03-90': 'Klinische Genetica',
                        '04-01': 'Fysiotherapie',
                        '04-02': 'Heilgymnastiek/massage',
                        '05-01': 'Logopedie',
                        '05-02': 'Foniatrie',
                        '07-01': 'Methode Cesar',
                        '07-02': 'Methode Mensendieck',
                        '08-01': 'Bevoegdheid echoscopie',
                        '84-01': 'Chiropractici',
                        '84-02': 'Orthomanuele geneeskunde',
                        '84-03': 'Acupunctuur',
                        '84-04': 'Iriscopie',
                        '84-05': 'Homeopathie',
                        '84-06': 'Natuurgeneeskunde',
                        '84-07': 'Antroposofische geneeskunde',
                        '84-08': 'Moermantherapie',
                        '84-09': 'Enzymtherapie',
                        '84-10': 'Manuele geneeskunde',
                        '84-11': 'Haptonomie',
                        '84-12': 'Osteopathie geneeswijze',
                        '84-13': 'Flebologie/proctologie',
                        '84-14': 'Orthomoleculair',
                        '84-15': 'Neuraal therapeut',
                        '84-16': 'Sportgeneeskunde/sportarts',
                        '84-17': 'EHBO-arts',
                        '84-18': 'Verpleeghuisarts',
                        '84-19': 'Schoolarts',
                        '84-20': 'Consultatieburoarts',
                        '84-21': 'SCEN-arts',
                        '89-01': 'Acn�',
                        '89-02': 'Camouflage',
                        '89-03': 'Elektrisch epileren',
                        '90-01': 'Chiropratici',
                        '90-02': 'Orthomanuele geneeskunde',
                        '90-03': 'Acupunctuur',
                        '90-04': 'Iriscopie',
                        '90-05': 'Homeopathie',
                        '90-06': 'Natuurgeneeskunde',
                        '90-07': 'Antroposofische geneeskunde',
                        '90-08': 'Moermantherapie',
                        '90-09': 'Enzymtherapie',
                        '90-10': 'Manuele geneeskunst',
                        '90-11': 'Haptonomie',
                        '90-12': 'Osteopathie geneeswijze',
                        '90-13': 'Huidtherapie',
                        '90-14': 'Kunstzinnig therapeuten',
                        '90-15': 'Podotherapie',
                        '90-16': 'Orthomoleculair',
                        '93-01': 'Tandprothetici',
                        '93-02': 'Tandtechnici',
                        '94-01': 'Eerste lijns psychologen',
                        '94-02': 'Psychotherapeuten',
                        '94-03': 'Seksuologen',
                        '94-04': 'Kinder- en jeugd psycholoog',
                        '94-05': 'Klinisch psycholoog',
                        '94-06': 'Gezondheidszorgpsycholoog'}}

if __name__ == '__main__':
    print('source_valueset;source_code;source_code;target_valueset;target_code;target_descr')

    for valset, dict in vektis_valuesets_data.items():
        for code, descr in dict.items():
            print('{0};{1};{2};{0};{1};{2}'.format(valset, code, descr))