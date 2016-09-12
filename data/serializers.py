from rest_framework.serializers import ModelSerializer

from data.models import Team, Position, Season, Game, Player, TraditionalBoxScore, PlayerSalary, DailyFantasySportsSite


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position()
        fields = ('name', 'abbreviation')


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team()
        fields = ('name', 'abbreviation')


class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season()
        fields = ('start_year',)


class GameSerializer(ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    season = SeasonSerializer()

    class Meta:
        model = Game()
        fields = ('home_team', 'away_team', 'start_time', 'season')


class PlayerSerializer(ModelSerializer):
    team = TeamSerializer()
    position = PositionSerializer()

    class Meta:
        model = Player()
        fields = ('first_name', 'last_name', 'team', 'position')


class BoxScoreSerializer(ModelSerializer):
    player = PlayerSerializer()
    game = GameSerializer()

    class Meta:
        model = TraditionalBoxScore
        fields = ('player', 'game', 'seconds_played', 'field_goals', 'field_goal_attempts', 'three_point_field_goals',
                  'three_point_field_goal_attempts', 'free_throws', 'free_throw_attempts', 'offensive_rebounds',
                  'defensive_rebounds', 'total_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'fouls_committed',
                  'points', 'draftkings_points')


class DailyFantasySportsSiteSerializer(ModelSerializer):
    class Meta:
        model = DailyFantasySportsSite
        fields = ('name',)


class PlayerSalarySerializer(ModelSerializer):
    site = DailyFantasySportsSiteSerializer()
    game = GameSerializer()
    player = PlayerSerializer()

    class Meta:
        model = PlayerSalary
        fields = ('site', 'game', 'player', 'salary')