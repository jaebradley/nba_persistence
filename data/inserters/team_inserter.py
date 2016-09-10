from data.objects.team import Team as TeamEnum
from data.models import Team as TeamModel


class TeamInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_teams():
        for team in TeamEnum.members:
            TeamModel.update_or_create(name=team.name)