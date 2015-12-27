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
from data.views import TeamViewSet, PositionViewSet, SeasonViewSet, GameViewSet, BoxScoreView, PlayerViewSet
import settings

player_list = PlayerViewSet.as_view({
    'get': 'list',
})
player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
})

router = routers.SimpleRouter()
router.register(r'teams', TeamViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'games', GameViewSet)
router.register(r'positions', PositionViewSet)

urlpatterns = [
    url(r'^players/$', player_list, name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', player_detail, name='player-detail'),
    url(r'^box_scores/$', BoxScoreView.as_view()),
    url(r'^box_scores/(?P<id>.+)/$', BoxScoreView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
