from data.objects.season import Season as SeasonEnum
from data.models import Season as SeasonModel


class SeasonInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_seasons():
        for season_name in [season.name for season in SeasonEnum]:
            SeasonModel.objects.update_or_create(name=season_name)