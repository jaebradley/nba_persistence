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
from data.views import TeamViewSet, PositionViewSet, SeasonViewSet, GameViewSet, PlayerView, BoxScoreViewSet
import settings

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'games', GameViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'box_scores', BoxScoreViewSet)

urlpatterns = [
    url(r'^players/$', PlayerView.as_view()),
    url(r'^players/(?P<id>.+)/$', PlayerView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
