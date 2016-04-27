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


def is_valid_box_score(box_score):
    return 'seconds_played' in box_score and \
            'field_goals' in box_score and \
            'three_point_field_goals' in box_score and \
            'three_point_field_goal_attempts' in box_score and \
            'free_throws' in box_score and \
            'fhree_throw_attempts' in box_score and \
            'offensive_rebounds' in box_score and \
            'defensive_rebounds' in box_score and \
            'total_rebounds' in box_score and \
            'assists' in box_score and \
            'steals' in box_score and \
            'blocks' in box_score and \
            'turnovers' in box_score and \
            'personal_fouls' in box_score and \
            'points' in box_score

def translate_box_score_to_draftkings_points(boxscore):
    