import logging
import logging.config
import os

from data.models import Team as TeamModel, Position as PositionModel, Season as SeasonModel
from data.objects import Team as TeamObject, Position as PositionObject, Season as SeasonObject

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '../../logging.conf'))
logger = logging.getLogger('inserter')


def insert_positions():
    for position in PositionObject:
        logger.info('Get/Creating position: %s' % position)
        PositionModel.objects.get_or_create(name=position.value)


def insert_seasons():
    for season in SeasonObject:
        logger.info('Get/Creating season: %s' % season)
        SeasonModel.objects.get_or_create(start_time=season.get_start_time(), end_time=season.get_end_time())


def insert_teams():
    for team in TeamObject:
        logger.info('Get/Creating team: %s' % team)
        TeamModel.objects.get_or_create(name=team.get_name())
