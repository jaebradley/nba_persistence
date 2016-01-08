def draftkings_salary_team_abbreviation_converter(draftkings_team_abbreviation):
    if draftkings_team_abbreviation.upper() == "NY":
        return "NYK"

    if draftkings_team_abbreviation.upper() == 'CHA':
        return 'CHO'

    if draftkings_team_abbreviation.upper() == 'SA':
        return 'SAS'

    if draftkings_team_abbreviation.upper() == 'BKN':
        return 'BRK'

    if draftkings_team_abbreviation.upper() == 'GS':
        return 'GSW'

    return draftkings_team_abbreviation.upper()


def fanduel_salary_team_abbreviation_converter(fanduel_team_abbreviation):
    if fanduel_team_abbreviation.upper() == "GS":
        return "GSW"

    if fanduel_team_abbreviation.upper() == 'CHA':
        return 'CHO'

    if fanduel_team_abbreviation.upper() == 'SA':
        return 'SAS'

    if fanduel_team_abbreviation.upper() == 'BKN':
        return 'BRK'

    return fanduel_team_abbreviation.upper()


def draftkings_player_name_converter(first_name, last_name):
    first_name_upper = first_name.upper()
    last_name_upper = last_name.upper()

    if first_name_upper == 'PATTY' and last_name_upper == 'MILLS':
        return {
            'first_name': 'Patrick',
            'last_name': 'Mills'
        }

    if first_name_upper == 'LUC' and last_name_upper == 'RICHARD':
        return {
            'first_name': 'Luc',
            'last_name': 'Mbah'
        }

    return {
        'first_name': first_name,
        'last_name': last_name
    }
