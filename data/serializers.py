from rest_framework.serializers import ModelSerializer

from data.models import Team, Position, Season, Player, Game, GamePlayerBoxScore, TeamPlayer


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position()
        fields = ('id', 'name')


class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season()
        fields = ('id', 'start_time', 'end_time')


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team()
        fields = ('id', 'name')


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player()
        fields = ('id', 'name', 'source_id')


class TeamPlayerSerializer(ModelSerializer):
    team = TeamSerializer()
    player = PlayerSerializer()

    class Meta:
        model = TeamPlayer()
        fields = ('id', 'team', 'player')


class GameSerializer(ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    season = SeasonSerializer()

    class Meta:
        model = Game()
        fields = ('id', 'home_team', 'away_team', 'season', 'start_time', 'source_id')


class GamePlayerBoxScoreSerializer(ModelSerializer):
    game = GameSerializer()
    team_player = TeamPlayerSerializer()

    class Meta:
        model = GamePlayerBoxScore()
        fields = ('id', 'game', 'team_player', 'status', 'explanation', 'seconds_played', 'field_goals_made',
                  'field_goals_attempted', 'three_point_field_goals_made', 'three_point_field_goals_attempted',
                  'free_throws_made', 'free_throws_attempted', 'offensive_rebounds', 'defensive_rebounds',
                  'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'plus_minus')
