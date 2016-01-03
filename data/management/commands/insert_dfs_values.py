from django.core.management.base import BaseCommand
from datetime import datetime
from data.inserters.inserters import insert_daily_fantasy_sports_sites, insert_dfs_salaries
from pytz import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        insert_daily_fantasy_sports_sites()
        insert_dfs_salaries(start_date=datetime(year=2015, month=12, day=29, tzinfo=timezone("US/Eastern")), end_date=datetime.now(tz=timezone("US/Eastern")))