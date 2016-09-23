from nba_data.client import Client
from data.models import Team, Season, Game, TraditionalBoxScore, Player
from data.objects.season import Season as SeasonEnum
from django.core.exceptions import ObjectDoesNotExist


class BoxScoreInserter:
    def __init__(self):
        pass

    @staticmethod
    def insert_traditional_box_scores():
        for season in SeasonEnum:
            BoxScoreInserter.insert_traditional_box_scores_for_season(season=season)

    @staticmethod
    def insert_traditional_box_scores_for_season(season):
        for game in Game.objects.filter(season=Season.objects.get(name=season.value)):
            BoxScoreInserter.insert_traditional_box_scores_for_game(game_id=str(game.nba_id))

    @staticmethod
    def insert_traditional_box_scores_for_game(game_id):
        box_score = Client.get_traditional_box_score(game_id=game_id)
        for player_box_score in box_score.player_box_scores:
            team = Team.objects.get(name=player_box_score.player.team.value)
            try:
                player = Player.objects.get(name=player_box_score.player.name,
                                            team=team,
                                            nba_id=player_box_score.player.id)
                game = Game.objects.get(nba_id=box_score.game_id)
                TraditionalBoxScore.objects.get_or_create(
                    player=player,
                    game=game,
                    seconds_played=player_box_score.seconds_played,
                    field_goals=player_box_score.field_goals_made,
                    field_goal_attempts=player_box_score.field_goal_attempts,
                    three_point_field_goals=player_box_score.three_point_field_goals_made,
                    three_point_field_goal_attempts=player_box_score.three_point_field_goal_attempts,
                    free_throws=player_box_score.free_throws_made,
                    free_throw_attempts=player_box_score.free_throws_attempts,
                    offensive_rebounds=player_box_score.offensive_rebounds,
                    defensive_rebounds=player_box_score.defensive_rebounds,
                    assists=player_box_score.assists,
                    steals=player_box_score.steals,
                    blocks=player_box_score.blocks,
                    turnovers=player_box_score.turnovers,
                    fouls_committed=player_box_score.personal_fouls,
                    plus_minus=player_box_score.plus_minus,
                )
            except ObjectDoesNotExist:
                continue
