from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from data.models import Team, Position, Season, Game, Player, BoxScore
from data.serializers import TeamSerializer, PositionSerializer, SeasonSerializer, GameSerializer, PlayerSerializer, BoxScoreSerializer


# Create your views here.


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all().order_by('name')
    serializer_class = PositionSerializer


class SeasonViewSet(ModelViewSet):
    queryset = Season.objects.all().order_by('-start_year')
    serializer_class = SeasonSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all().order_by('start_time')
    serializer_class = GameSerializer


class PlayerView(ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all().order_by('first_name').order_by('last_name')
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        team_abbreviation = self.request.query_params.get('team_abbreviation', None)
        position_abbreviation = self.request.query_params.get('position_abbreviation', None)

        if 'id' in self.kwargs:
            queryset = queryset.filter(id=self.kwargs['id'])

        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)

        if team_abbreviation is not None:
            queryset = queryset.filter(team__abbreviation=team_abbreviation)

        if position_abbreviation is not None:
            queryset = queryset.filter(position__abbreviation=position_abbreviation)

        return queryset


class BoxScoreViewSet(ModelViewSet):
    queryset = BoxScore.objects.all().order_by('game__start_time').order_by('-player__last_name').order_by('-player__first_name')
    serializer_class = BoxScoreSerializer