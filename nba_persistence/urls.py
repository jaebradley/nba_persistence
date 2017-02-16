"""dfs_site_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from data.views import team_detail, teams_list, players_list, games_list, player_detail, game_detail, seasons_list, \
    season_detail, positions_list, position_detail, game_player_box_scores_list, game_player_box_score_detail, \
    team_player_detail, team_players_list, game_dates_list

# Create a router and register our viewsets with it.
router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^teams/$', teams_list, name='teams_list'),
    url(r'^teams/(?P<pk>[0-9]+)/$', team_detail, name='team_detail'),
    url(r'^teams/(?P<team_id>[0-9]+)/players/$', team_players_list, name='team_players_list'),
    url(r'^teams/(?P<team_id>[0-9]+)/players/(?P<player_id>[0-9]+)/$', team_player_detail, name='team_player_detail'),

    url(r'^players/$', players_list, name='players_list'),
    url(r'^players/(?P<player_id>[0-9]+)$', player_detail, name='player_detail'),

    url(r'^games/$', games_list, name='games_list'),
    url(r'^games/(?P<game_id>[0-9]+)/$', game_detail, name='game_detail'),

    url(r'^seasons/$', seasons_list, name='seasons_list'),
    url(r'^seasons/(?P<season_id>[0-9]+)/$', season_detail, name='season_detail'),

    url(r'^positions/$', positions_list, name='positions_list'),
    url(r'^positions/(?P<position_id>[0-9]+)/$', position_detail, name='position_detail'),

    url(r'^box-scores/$', game_player_box_scores_list, name='game_player_box_scores_list'),
    url(r'^box-scores/(?P<box_score_id>[0-9]+)/$', game_player_box_score_detail, name='game_player_box_score_detail'),

    url(r'^game-dates/$', game_dates_list, name='game_dates_list'),
]
