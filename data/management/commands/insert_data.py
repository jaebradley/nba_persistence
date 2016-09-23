from django.core.management.base import BaseCommand

from data.inserters.position_inserter import PositionInserter
from data.inserters.season_inserter import SeasonInserter
from data.inserters.team_inserter import TeamInserter
from data.inserters.player_inserter import PlayerInserter
from data.inserters.game_inserter import GameInserter
from data.inserters.box_score_inserter import BoxScoreInserter
from data.objects.season import Season


class Command(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super(Command, self).__init__(stdout, stderr, no_color)

    def handle(self, *args, **options):
        Command.insert_static_data()
        Command.insert_dynamic_data()

    @staticmethod
    def insert_static_data():
        PositionInserter.insert_positions()
        SeasonInserter.insert_seasons()
        TeamInserter.insert_teams()

    @staticmethod
    def insert_dynamic_data():
        # PlayerInserter.insert_players_for_season(season=Season.season_2015)
        # GameInserter.insert_games_for_season(season=Season.season_2015)
        BoxScoreInserter.insert_traditional_box_scores()


