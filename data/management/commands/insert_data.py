from django.core.management.base import BaseCommand

from data.inserters.inserters import insert_positions, insert_teams, insert_schedules, insert_players, insert_box_scores, insert_daily_fantasy_sports_sites, insert_draftkings_salaries, insert_fanduel_salaries
from datetime import datetime
from pytz import utc


class Command(BaseCommand):
    def handle(self, *args, **options):
        # insert_positions()
        # insert_teams('data/inserters/static/nba_team_name_mapping.csv')
        # insert_schedules(2015, 2015)
        # insert_players(2015)
        # insert_box_scores(datetime(year=2015, month=10, day=1, tzinfo=utc), datetime.now(utc))
        insert_daily_fantasy_sports_sites()
        insert_draftkings_salaries(datetime(year=2015, month=12, day=28))
        insert_fanduel_salaries(datetime(year=2015, month=12, day=30))