from datetime import datetime

from django.core.management.base import BaseCommand
from pytz import utc

from data.inserters.inserters import insert_positions, insert_teams, insert_players, insert_games
from data.teams.nba import teams as nba_teams
from data.positions.nba import positions as nba_positions
from data.translators.nba import translate_players, translate_seasons_to_games
import data.inserters.nba.inserters as nba_inserters


class Command(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(Command, self).__init__(stdout, stderr, no_color)
        self.season_start_year = 2015
        self.season_start_date = datetime(year=2015, month=10, day=1, tzinfo=utc)

    def handle(self, *args, **options):
        self.insert_nba_data()

    def insert_nba_data(self):
        # insert_positions(positions=nba_positions)
        # insert_teams(teams=nba_teams)
        # players = translate_players(season_start_year=self.season_start_year)
        # insert_players(players=players)
        # games = translate_seasons_to_games(self.season_start_year, self.season_start_year)
        # insert_games(games=games)
        nba_inserters.insert_box_scores(self.season_start_date, datetime.now(utc))


