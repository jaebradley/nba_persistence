from data.objects.season import Season as SeasonEnum
from data.models import Season as SeasonModel


class SeasonInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_seasons():
        for season in SeasonEnum.members:
            SeasonModel.update_or_create(name=season.name)