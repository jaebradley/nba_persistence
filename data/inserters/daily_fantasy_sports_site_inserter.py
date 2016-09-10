from data.objects.daily_fantasy_sports_site import DailyFantasySportsSite
from data.models import DailyFantasySportsSite as DailyFantasySportsSiteModel


class DailyFantasySportsSiteInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_daily_fantasy_sports_sites():
        for site in DailyFantasySportsSite.members:
            DailyFantasySportsSiteModel.update_or_create(name=site.name)