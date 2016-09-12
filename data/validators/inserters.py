import csv
import os
from datetime import datetime, timedelta

import data.validators.util as util_validators
from django.core.exceptions import ObjectDoesNotExist
from pytz import timezone, utc

from data.models import Game, Player, DailyFantasySportsSite, PlayerSalary
from data.translators.utils import draftkings_salary_team_abbreviation_converter, fanduel_salary_team_abbreviation_converter, draftkings_player_name_converter, fanduel_player_name_converter


def insert_games(games):
    for game in games:
        if not util_validators.is_valid_game(game=game):
            raise ValueError('invalid game')
        else:
            Game.objects.update_or_create(home_team=game['home_team'],
                                          away_team=game['away_team'],
                                          start_time=game['start_time'],
                                          season=game['season'])


def insert_players(players):
    for player in players:
        if not util_validators.is_valid_player(player=player):
            raise ValueError('player is missing team, position, first name, or last name')
        else:
            Player.objects.update_or_create(name=player['first_name'] + player['last_name'],
                                            team=player['team'],
                                            position=player['position'])


def insert_draftkings_salaries(day):
    draftkings_file_name = os.path.join(os.path.dirname(__file__), "static/salaries/draftkings/{0}.csv".format(day.strftime("%Y-%m-%d")))
    draftkings_log_file_name = os.path.join(os.path.dirname(__file__), "static/salaries/draftkings.log")
    if os.path.isfile(draftkings_file_name):
        log_file = open(draftkings_log_file_name, "a+")
        with open(draftkings_file_name) as file:
            reader = csv.reader(file)
            salaries = list(reader)[1:]
            site = DailyFantasySportsSite.objects.get(name="DraftKings")
            for salary in salaries:
                names_list = salary[1].split(" ")
                first_name = names_list[0]
                last_name = names_list[1]
                converted_names = draftkings_player_name_converter(first_name, last_name)
                first_name = converted_names['first_name']
                last_name = converted_names['last_name']
                game_info_list = salary[3].split(" ")
                team_abbreviation_list = game_info_list[0].split("@")
                away_team_abbreviation = draftkings_salary_team_abbreviation_converter(team_abbreviation_list[0])
                home_team_abbreviation = draftkings_salary_team_abbreviation_converter(team_abbreviation_list[1])
                start_time = game_info_list[1]
                utc_start_time = timezone("US/Eastern").localize(datetime.strptime("{0}-{1}-{2}-{3}".format(day.year, day.month, day.day, start_time), "%Y-%m-%d-%I:%M%p")).astimezone(utc)
                player_team_abbreviation = draftkings_salary_team_abbreviation_converter(salary[5].upper())
                try:
                    player = Player.objects.get(first_name=first_name, last_name=last_name, team__abbreviation=player_team_abbreviation)
                    game = Game.objects.get(home_team__abbreviation=home_team_abbreviation, away_team__abbreviation=away_team_abbreviation, start_time=utc_start_time)
                    salary_value = salary[2]
                    PlayerSalary.objects.update_or_create(site=site, player=player, game=game, salary=salary_value)
                except ObjectDoesNotExist:
                    log_message = "{0} - {1} - {2} - {3}\n".format(first_name, last_name, player_team_abbreviation, utc_start_time)
                    log_file.write(log_message)
        log_file.close()


def insert_fanduel_salaries(day):
    fanduel_file_name = os.path.join(os.path.dirname(__file__), "static/salaries/fanduel/{0}.csv".format(day.strftime("%Y-%m-%d")))
    fanduel_log_file_name = os.path.join(os.path.dirname(__file__), "static/salaries/fanduel.log")
    if os.path.isfile(fanduel_file_name):
        log_file = open(fanduel_log_file_name, "a+")
        with open(fanduel_file_name) as file:
            reader = csv.reader(file)
            salaries = list(reader)[1:]
            site = DailyFantasySportsSite.objects.get(name="FanDuel")
            for salary in salaries:
                first_name = salary[2]
                last_name = salary[3]
                converted_names = fanduel_player_name_converter(first_name, last_name)
                first_name = converted_names['first_name']
                last_name = converted_names['last_name']
                game_info_list = salary[7].split("@")
                away_team_abbreviation = fanduel_salary_team_abbreviation_converter(game_info_list[0])
                home_team_abbreviation = fanduel_salary_team_abbreviation_converter(game_info_list[1])
                player_team_abbreviation = fanduel_salary_team_abbreviation_converter(salary[8].upper())
                day_start_est = timezone('US/Eastern').localize(datetime(year=day.year, month=day.month, day=day.day, hour=0, minute=0, second=0, microsecond=0))
                day_end_est = day_start_est + timedelta(hours=24)
                try:
                    player = Player.objects.get(first_name=first_name, last_name=last_name, team__abbreviation=player_team_abbreviation)
                    game = Game.objects.get(home_team__abbreviation=home_team_abbreviation, away_team__abbreviation=away_team_abbreviation, start_time__gte=day_start_est, start_time__lte=day_end_est)
                    salary_value = salary[6]
                    PlayerSalary.objects.update_or_create(site=site, player=player, game=game, salary=salary_value)
                except ObjectDoesNotExist:
                    log_message = "{0} - {1} - {2} - {3} - {4}\n".format(first_name, last_name, player_team_abbreviation, day_start_est, day_end_est)
                    log_file.write(log_message)
        log_file.close()


def insert_dfs_salaries(start_date, end_date):
    day = start_date
    while day <= end_date:
        insert_draftkings_salaries(day)
        insert_fanduel_salaries(day)
        day = day + timedelta(days=1)