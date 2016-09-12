from django.core.management.base import BaseCommand

from data.inserters.position_inserter import PositionInserter
from data.inserters.season_inserter import SeasonInserter
from data.inserters.team_inserter import TeamInserter


class Command(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(Command, self).__init__(stdout, stderr, no_color)

    def handle(self, *args, **options):
        Command.insert_data()

    @staticmethod
    def insert_data():
        PositionInserter.insert_positions()
        SeasonInserter.insert_seasons()
        TeamInserter.insert_teams()



