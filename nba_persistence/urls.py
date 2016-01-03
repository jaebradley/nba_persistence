"""nba_persistence URL Configuration

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
from django.contrib import admin
from rest_framework import routers

import settings
from data.views import TeamViewSet, PositionViewSet, SeasonViewSet, GameViewSet, BoxScoreViewSet, PlayerViewSet, DailyFantasySportsSiteViewSet, PlayerSalaryViewSet

team_list = TeamViewSet.as_view({
    'get': 'list'
})

team_detail = TeamViewSet.as_view({
    'get': 'retrieve'
})

position_list = PositionViewSet.as_view({
    'get': 'list'
})

position_detail = PositionViewSet.as_view({
    'get': 'retrieve'
})

season_list = SeasonViewSet.as_view({
    'get': 'list'
})

season_detail = SeasonViewSet.as_view({
    'get': 'retrieve'
})

player_list = PlayerViewSet.as_view({
    'get': 'list',
})
player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
})

game_list = GameViewSet.as_view({
    'get': 'list'
})

game_detail = GameViewSet.as_view({
    'get': 'retrieve'
})

box_score_list = BoxScoreViewSet.as_view({
    'get': 'list'
})

box_score_detail = BoxScoreViewSet.as_view({
    'get': 'retrieve'
})

daily_fantasy_sports_site_list = DailyFantasySportsSiteViewSet.as_view({
    'get': 'list'
})

daily_fantasy_sports_site_detail = DailyFantasySportsSiteViewSet.as_view({
    'get': 'retrieve'
})

player_salary_list = PlayerSalaryViewSet.as_view({
    'get': 'list'
})

player_salary_detail = PlayerSalaryViewSet.as_view({
    'get': 'retrieve'
})

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^players/$', player_list, name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', player_detail, name='player-detail'),
    url(r'^teams/$', team_list, name='team-list'),
    url(r'^teams/(?P<pk>[0-9]+)/$', team_detail, name='team-detail'),
    url(r'^positions/$', position_list, name='position-list'),
    url(r'^positions/(?P<pk>[0-9]+)/$', position_detail, name='position-detail'),
    url(r'^seasons/$', season_list, name='season-list'),
    url(r'^seasons/(?P<pk>[0-9]+)/$', season_detail, name='season-detail'),
    url(r'^games/$', game_list, name='game-list'),
    url(r'^games/(?P<pk>[0-9]+)/$', game_detail, name='game-detail'),
    url(r'^box_scores/$', box_score_list, name='box_score-list'),
    url(r'^box_scores/(?P<pk>[0-9]+)/$', box_score_detail, name='box_score-detail'),
    url(r'^daily_fantasy_sports_sites/$', daily_fantasy_sports_site_list, name='daily_fantasy_sports_site-list'),
    url(r'^daily_fantasy_sports_sites/(?P<pk>[0-9]+)/$', daily_fantasy_sports_site_detail, name='daily_fantasy_sports_site-detail'),
    url(r'^player_salaries/$', player_salary_list, name='player_salary-list'),
    url(r'^player_salaries/(?P<pk>[0-9]+)/$', player_salary_detail, name='player_salary-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
