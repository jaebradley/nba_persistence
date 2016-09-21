from nba_data.client import Client
from data.models import Team, Season, Game
from data.objects.team import Team as TeamEnum


class GameInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_games_for_season(season):
        for team in TeamEnum:
            team_obj = Team.objects.get(name=team.value)
            home_game_counts = Game.objects.filter(home_team=team_obj, season=Season.objects.get(name=season.value)).count()
            away_game_counts = Game.objects.filter(away_team=team_obj, season=Season.objects.get(name=season.value)).count()
            if home_game_counts < 41 or away_game_counts < 41 or home_game_counts + away_game_counts < 82:
                GameInserter.insert_games_for_team(season=season, team=team)

    @staticmethod
    def insert_games_for_team(season, team):
        for game in Client.get_games_for_team(season=season, team=team):
            home_team = Team.objects.get(name=game.matchup.home_team.value)
            away_team = Team.objects.get(name=game.matchup.away_team.value)
            Game.objects.get_or_create(
                home_team=home_team,
                away_team=away_team,
                start_date=game.date,
                season=Season.objects.get(name=season.value))

