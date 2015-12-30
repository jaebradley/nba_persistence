def draftkings_salary_team_abbreviation_converter(draftkings_team_abbreviation):
    if draftkings_team_abbreviation.upper() == "NY":
        return "NYK"

    if draftkings_team_abbreviation.upper() == 'CHA':
        return 'CHO'

    if draftkings_team_abbreviation.upper() == 'SA':
        return 'SAS'

    if draftkings_team_abbreviation.upper() == 'BKN':
        return 'BRK'

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
