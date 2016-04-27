def is_valid_player(player):
    return 'team' in player and \
            'position' in player and \
            'first_name' in player and \
            'last_name' in player


def is_valid_game(game):
    return 'away_team' in game and \
           'home_team' in game and \
           'start_time' in game and \
           'season' in game