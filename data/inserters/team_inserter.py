from data.objects.team import Team as TeamEnum
from data.models import Team as TeamModel


class TeamInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_teams():
        for team_name in [team_name.name for team_name in TeamEnum]:
            TeamModel.objects.update_or_create(name=team_name)