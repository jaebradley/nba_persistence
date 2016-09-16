from nba_data.client import Client
from data.models import Team, Season, Game
from data.objects.team import Team as TeamEnum


class GameInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_games_for_season(season):
        for team in TeamEnum:
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

