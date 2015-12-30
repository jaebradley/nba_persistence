def draftkings_salary_team_abbreviation_converter(draftkings_team_abbreviation):
    if draftkings_team_abbreviation.upper() == "NY":
        return "NYK"

    return draftkings_team_abbreviation.upper()


def fanduel_salary_team_abbreviation_converter(fanduel_team_abbreviation):
    if fanduel_team_abbreviation.upper() == "GS":
        return "GSW"

    return fanduel_team_abbreviation.upper()
