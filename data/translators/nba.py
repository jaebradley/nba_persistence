from basketball_reference_web_scraper.readers import return_all_player_season_statistics
from data.models import Position, Team, Season, Game, Player, BoxScore, DailyFantasySportsSite, PlayerSalary
from data.inserters.inserters import is_valid_player


def translate_position(position):
    if position == 'G':
        return 'PG'
    elif position == 'F':
        return 'SF'
    elif '-' in position:
        return 'PG'
    else:
        return position


def translate_players(season_start_year):
    filtered_players = []
    for player in return_all_player_season_statistics(season_start_year=season_start_year):
        if not is_valid_player(player):
            raise ValueError('player is missing team, position, first name, or last name')
        else:
            team = Team.objects.get(abbreviation=player.team)
            position = Position.objects.get(abbreviation=translate_position(player.position))
            filtered_players.append({
                'position': position,
                'team': team,
                'first_name': player.first_name,
                'last_name': player.last_name
            })

    return filtered_players

