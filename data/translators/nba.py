from basketball_reference_web_scraper.readers import return_all_player_season_statistics
from data.models import Position, Team, Season, Game, Player, BoxScore, DailyFantasySportsSite, PlayerSalary
from data.inserters.inserters import is_valid_player
import data.translators.util as util_translators
import data.validators.nba as nba_validators
import data.calculators.nba as nba_calculators
from django.db.models import Q


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


def translate_box_score(box_score):
    if not nba_validators.is_valid_box_score(box_score=box_score):
        raise ValueError('invalid box score')
    else:
        day_start_utc = util_translators.translate_day_start_from_est_to_utc(year=box_score.date.year,
                                                                             month=box_score.date.month,
                                                                             day=box_score.date.day)
        day_end_utc = util_translators.translate_day_end_from_est_to_utc(year=box_score.date.year,
                                                                         month=box_score.date.month,
                                                                         day=box_score.date.day)
        team = Team.objects.get(abbreviation=box_score.team)
        opponent = Team.objects.get(abbreviation=box_score.opponent)
        player = Player.objects.filter(first_name=box_score.first_name).filter(last_name=box_score.last_name).get(team=team)
        game = Game.objects.filter((Q(home_team=team) & Q(away_team=opponent)) | (Q(home_team=opponent) & Q(away_team=team)))\
                           .filter(start_time__gte=day_start_utc)\
                           .get(start_time__lte=day_end_utc)
        draftkings_points = nba_calculators.calculate_draftkings_points(box_score=box_score)
        box_score['team'] = team
        box_score['opponent'] = opponent
        box_score['player'] = player
        box_score['game'] = game
        box_score['draftkings_points'] = draftkings_points
        return box_score

