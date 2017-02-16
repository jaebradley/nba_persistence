# Create your views here.

from datetime import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from data.models import Team, Position, Season, Player, Game, GamePlayerBoxScore, TeamPlayer
from data.serializers import TeamSerializer, PositionSerializer, SeasonSerializer, PlayerSerializer, GameSerializer, \
    GamePlayerBoxScoreSerializer, TeamPlayerSerializer


class QuerySetReadOnlyViewSet(ReadOnlyModelViewSet):
    def build_response(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PositionViewSet(ReadOnlyModelViewSet):
    serializer_class = PositionSerializer

    def get_queryset(self):
        return Position.objects.all().order_by('name')


class TeamViewSet(ReadOnlyModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all().order_by('name')


class SeasonViewSet(ReadOnlyModelViewSet):
    serializer_class = SeasonSerializer

    def get_queryset(self):
        return Season.objects.all().order_by('start_time')


class PlayerViewSet(ReadOnlyModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        result = Player.objects.all().order_by('name')

        name = self.request.query_params.get('name', None)
        source_id = self.request.query_params.get('source_id', None)

        if name is not None:
            result = result.filter(name=name)

        if source_id is not None:
            result = result.filter(source_id=source_id)

        return result


class TeamPlayerViewSet(QuerySetReadOnlyViewSet):
    serializer_class = TeamPlayerSerializer
    queryset = TeamPlayer.objects.all().order_by('team__name', 'player__name')

    def list_team_players(self, request, *args, **kwargs):
        result = self.queryset.filter(team__id=kwargs.get('team_id'))
        return self.build_response(queryset=result)

    def retrieve_team_player(self, request, *args, **kwargs):
        result = self.queryset.filter(team__id=kwargs.get('team_id')).filter(player__id=kwargs.get('player_id'))
        return self.build_response(queryset=result)


class GameViewSet(ReadOnlyModelViewSet):
    serializer_class = GameSerializer

    def get_queryset(self):
        result = Game.objects.all().order_by('start_time')

        home_team_id = self.request.query_params.get('home_team_id', None)
        away_team_id = self.request.query_params.get('away_team_id', None)
        season_id = self.request.query_params.get('season_id', None)
        source_id = self.request.query_params.get('source_id', None)

        if home_team_id is not None:
            result = result.filter(home_team__id=home_team_id)

        if away_team_id is not None:
            result = result.filter(away_team__id=away_team_id)

        if season_id is not None:
            result = result.filter(season__id=season_id)

        if source_id is not None:
            result = result.filter(source_id=source_id)

        return result


class GamePlayerBoxScoreViewSet(ReadOnlyModelViewSet):
    serializer_class = GamePlayerBoxScoreSerializer

    def get_queryset(self):
        result = GamePlayerBoxScore.objects.all().order_by('game__start_time')

        home_team_id = self.request.query_params.get('home_team_id', None)
        away_team_id = self.request.query_params.get('away_team_id', None)
        season_id = self.request.query_params.get('season_id', None)
        game_source_id = self.request.query_params.get('game_source_id', None)
        player_name = self.request.query_params.get('player_name', None)
        player_source_id = self.request.query_params.get('player_source_id', None)
        start_time_gte = self.request.query_params.get('start_time_gte', None)
        start_time_lte = self.request.query_params.get('start_time_lte', None)

        if home_team_id is not None:
            result = result.filter(game__home_team__id=home_team_id)

        if away_team_id is not None:
            result = result.filter(game__away_team__id=away_team_id)

        if season_id is not None:
            result = result.filter(game__season__id=season_id)

        if game_source_id is not None:
            result = result.filter(game__source_id=game_source_id)

        if player_name is not None:
            result = result.filter(player__name=player_name)

        if player_source_id is not None:
            result = result.filter(player_source_id=player_source_id)

        if start_time_gte is not None:
            result = result.filter(game__start_time__gte=datetime.fromtimestamp(timestamp=start_time_gte))

        if start_time_lte is not None:
            result = result.filter(game__start_time__lte=datetime.fromtimestamp(timestamp=start_time_lte))

        return result


class GameDatesViewSet(ViewSet):
    queryset = Game.objects.filter(start_time__lte=datetime.now()).datetimes('start_time', 'day', order='ASC')

    def list(self, request):
        return Response(self.queryset)
