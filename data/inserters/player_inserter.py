from nba_data.client import Client
from data.models import Player, Team, Position, Season


class PlayerInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_players_for_season(season):
        for player in Client.get_players_for_season(season=season):
            player_details = Client.get_player_info(player_id=player.nba_id)

            position_name = ""
            if player_details.position is not None:
                position_name = player_details.position.value.lower()

            team = Team.objects.get(name=player.team.value)
            Player.objects.get_or_create(name=player.name,
                                         position=Position.objects.get(name=position_name),
                                         team=team,
                                         season=Season.objects.get(name=season.value),
                                         jersey_number=player_details.jersey_number)

