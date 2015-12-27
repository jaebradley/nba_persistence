from django.core.management.base import BaseCommand

from data.inserters.inserters import insert_positions, insert_teams, insert_schedules, insert_players, insert_box_scores
from datetime import datetime
from pytz import utc


class Command(BaseCommand):
    def handle(self, *args, **options):
        insert_positions()
        insert_teams('data/inserters/static/nba_team_name_mapping.csv')
        insert_schedules(2015, 2015)
        insert_players(2015)
        insert_box_scores(datetime(year=2015, month=10, day=1, tzinfo=utc), datetime.now(utc))