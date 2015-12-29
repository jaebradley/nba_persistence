from data.models import Position, Team, Season, Game, Player, BoxScore
import csv
from basketball_reference_web_scraper.readers import return_schedule, return_all_player_season_statistics, return_box_scores_for_date
from pytz import timezone, utc
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta


def insert_positions():
    positions = [
        {
            'name': 'Point Guard',
            'abbreviation': 'PG'
        },
        {
            'name': 'Shooting Guard',
            'abbreviation': 'SG'
        },
        {
            'name': 'Small Forward',
            'abbreviation': 'SF'
        },
        {
            'name': 'Power Forward',
            'abbreviation': 'PF'
        },
        {
            'name': 'Center',
            'abbreviation': 'C'
        }
    ]
    for position in positions:
        Position.objects.get_or_create(name=position['name'], abbreviation=position['abbreviation'])


def insert_teams(team_name_csv):
    with open(team_name_csv) as file:
        reader = csv.reader(file)
        nba_team_name_list = list(reader)[1:]
        for team in nba_team_name_list:
            Team.objects.get_or_create(name=team[2], abbreviation=team[1])


def insert_schedules(first_season_start_year, last_season_start_year):
    for season_start_year in range(first_season_start_year, last_season_start_year + 1):
        season, created = Season.objects.get_or_create(start_year=season_start_year)
        season_schedule = return_schedule(season_start_year)
        for event in season_schedule.parsed_event_list:
            home_team = Team.objects.get(name=event.home_team_name)
            away_team = Team.objects.get(name=event.visiting_team_name)
            Game.objects.get_or_create(home_team=home_team, away_team=away_team, start_time=event.start_time, season=season)


def insert_players(season_start_year):
    player_season_statistics = return_all_player_season_statistics(season_start_year=season_start_year)
    for player_season in player_season_statistics:
        team = Team.objects.get(abbreviation=player_season.team)
        if player_season.position == 'G':
            player_position = 'PG'
        elif player_season.position == 'F':
            player_position = 'SF'
        elif '-' in player_season.position:
            player_position = 'PG'
        else:
            player_position = player_season.position
        position = Position.objects.get(abbreviation=player_position)
        Player.objects.get_or_create(first_name=player_season.first_name, last_name=player_season.last_name, team=team, position=position)


def insert_box_score(box_score):
    day_start_est = timezone('US/Eastern').localize(datetime(year=box_score.date.year, month=box_score.date.month, day=box_score.date.day, hour=0, minute=0, second=0, microsecond=0))
    day_end_est = day_start_est + timedelta(hours=24)
    day_start_utc = day_start_est.astimezone(utc)
    day_end_utc = day_end_est.astimezone(utc)
    try:
        team = Team.objects.get(abbreviation=box_score.team)
        opponent = Team.objects.get(abbreviation=box_score.opponent)
        player = Player.objects.filter(first_name=box_score.first_name).filter(last_name=box_score.last_name).get(team=team)
        game = Game.objects.filter((Q(home_team=team) & Q(away_team=opponent)) | (Q(home_team=opponent) & Q(away_team=team))).filter(start_time__gte=day_start_utc).get(start_time__lte=day_end_utc)
        BoxScore.objects.get_or_create(
            player=player,
            game=game,
            seconds_played=box_score.seconds_played,
            field_goals=box_score.field_goals,
            field_goal_attempts=box_score.field_goal_attempts,
            three_point_field_goals=box_score.three_point_field_goals,
            three_point_field_goal_attempts=box_score.three_point_field_goal_attempts,
            free_throws=box_score.free_throws,
            free_throw_attempts=box_score.free_throw_attempts,
            offensive_rebounds=box_score.offensive_rebounds,
            defensive_rebounds=box_score.defensive_rebounds,
            total_rebounds=box_score.total_rebounds,
            assists=box_score.assists,
            steals=box_score.steals,
            blocks=box_score.blocks,
            turnovers=box_score.turnovers,
            fouls_committed=box_score.personal_fouls,
            points=box_score.points,
            draftkings_points=float(box_score.points) + float(box_score.three_point_field_goals) * 0.5 + float(box_score.total_rebounds) * 1.25 + float(box_score.assists) * 1.5 + float(box_score.steals) * 2 + float(box_score.blocks) * 2 - float(box_score.turnovers) * 0.5
        )
    except ObjectDoesNotExist:
        pass


def insert_box_scores(minimum_date, maximum_date):
    games = Game.objects.filter(start_time__gte=minimum_date).filter(start_time__lte=maximum_date).filter(boxscore__isnull=True)
    distinct_start_days = set()
    for game in games:
        distinct_start_days.add(game.start_time.replace(tzinfo=timezone('US/Eastern')).date())
    for start_day in distinct_start_days:
        box_scores = return_box_scores_for_date(start_day)
        for box_score in box_scores:
            insert_box_score(box_score)
