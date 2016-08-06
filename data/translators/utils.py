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

    if draftkings_team_abbreviation.upper() == 'NO':
        return 'NOP'

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

    if fanduel_team_abbreviation.upper() == 'NO':
        return 'NOP'

    if fanduel_team_abbreviation.upper() == 'NY':
        return 'NYK'

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

    if first_name_upper == 'JAKARR' and last_name_upper == 'SAMPSON':
        return {
            'first_name': 'JaKarr',
            'last_name': 'Sampson'
        }

    if first_name_upper == 'LOUIS' and last_name_upper == 'AMUNDSON':
        return {
            'first_name': 'Lou',
            'last_name': 'Amundson'
        }

    return {
        'first_name': first_name,
        'last_name': last_name
    }


def fanduel_player_name_converter(first_name, last_name):
    first_name_upper = first_name.upper()
    last_name_upper = last_name.upper()

    if first_name_upper == 'BRAD' and last_name_upper == 'BEAL':
        return  {
            'first_name': 'Bradley',
            'last_name': 'Beal'
        }

    if first_name_upper == 'JOSE JUAN' and last_name_upper == 'BAREA':
        return {
            'first_name': 'Jose',
            'last_name': 'Barea'
        }

    if first_name_upper == 'LOUIS' and last_name_upper == 'WILLIAMS':
        return {
            'first_name': 'Lou',
            'last_name': 'Williams'
        }

    if first_name_upper == 'LARRY' and last_name_upper == 'NANCE JR.':
        return {
            'first_name': 'Larry',
            'last_name': 'Nance'
        }

    if first_name_upper == 'ISHMAEL' and last_name_upper == 'SMITH':
        return {
            'first_name': 'Ish',
            'last_name': 'Smith'
        }

    return {
        'first_name': first_name,
        'last_name': last_name
    }
