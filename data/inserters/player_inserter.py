from nba_data.client import Client
from data.models import Player
from data.objects.position import Position


class PlayerInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_players_for_season(season):
        for player in Client.get_players_for_season(season=season):
            position = Position.from_name(name=player.position.value)
            Player.get_or_create(name=player.name,
                                 position=position.value,
                                 team=player.team.value,
                                 season=player.season.value)

