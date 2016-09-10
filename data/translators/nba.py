# import pytz
# from basketball_reference_web_scraper.readers import return_all_player_season_statistics, return_box_scores_for_date, return_schedule
# from django.db.models import Q
#
# import data.calculators.nba as nba_calculators
# import data.translators.util as util_translators
# from data.models import Position, Team, Season, Game, Player

from nba_data.client import Client
from nba_data.data.season import Season

def test():
    print Client.get_players_for_season(season=Season.season_2015)

test()


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
    box_score.team = team
    box_score.opponent = opponent
    box_score.player = player
    box_score.game = game
    box_score.draftkings_points = draftkings_points
    return box_score


def translate_date_to_box_scores(start_day):
    translated_box_scores = []
    box_scores = return_box_scores_for_date(start_day)
    for box_score in box_scores:
        translated_box_scores.append(translate_box_score(box_score=box_score))
    return translated_box_scores


def translate_date_range_to_distinct_start_days(minimum_date, maximum_date):
    games = Game.objects.filter(start_time__gte=minimum_date)\
                        .filter(start_time__lte=maximum_date)\
                        .filter(boxscore__isnull=True)
    distinct_start_days = set()
    for game in games:
        distinct_start_days.add(game.start_time.replace(tzinfo=pytz.timezone('US/Eastern')).date())
    return distinct_start_days


def translate_seasons_to_games(first_season_start_year, last_season_start_year):
    translated_games = []
    for season_start_year in range(first_season_start_year, last_season_start_year + 1):
        season, created = Season.objects.get_or_create(start_year=season_start_year)
        season_schedule = return_schedule(season_start_year)
        for event in season_schedule.parsed_event_list:
            home_team = Team.objects.get(name=event.home_team_name)
            away_team = Team.objects.get(name=event.visiting_team_name)
            translated_games.append({
              'home_team': home_team,
              'away_team': away_team,
              'start_time': event.start_time,
              'season': season
            })
    return translated_games


