from data.objects.position import Position as PositionEnum
from data.models import Position as PositionModel


class PositionInserter:

    def __init__(self):
        pass

    @staticmethod
    def insert_positions():
        for position_name in [position.value for position in PositionEnum]:
            PositionModel.objects.update_or_create(name=position_name)