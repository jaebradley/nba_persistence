from datetime import datetime

from django.core.management.base import BaseCommand
from pytz import utc

from data.inserters.inserters import insert_positions, insert_teams, insert_schedules, insert_players, insert_box_scores
from data.teams.nba import teams as nba_teams
from data.positions.nba import positions as nba_positions


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.insert_nba_data()

        insert_schedules(2015, 2015)
        insert_players(2015)
        insert_box_scores(datetime(year=2015, month=10, day=1, tzinfo=utc), datetime.now(utc))

    def insert_nba_data(self):
        insert_positions(nba_positions)
        insert_teams(nba_teams)

