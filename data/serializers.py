from data.models import Team, Position, Season, Game, Player, BoxScore
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class PositionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('name', 'abbreviation')


class TeamSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'abbreviation')


class SeasonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('start_year')


class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('home_team', 'away_team', 'start_time', 'season')


class PlayerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'team', 'position')


class BoxScoreSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BoxScore
        fields = ('player', 'game', 'seconds_played', 'field_goals', 'field_goal_attempts', 'three_point_field_goals',
                  'three_point_field_goal_attempts', 'free_throws', 'free_throw_attempts', 'offensive_rebounds',
                  'defensive_rebounds', 'total_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'fouls_committed',
                  'points', 'draftkings_points')