import datetime

import pytz
from enum import Enum


class Position(Enum):
    point_guard = 'Point Guard'
    shooting_guard = 'Shooting Guard'
    small_forward = 'Small Forward'
    power_forward = 'Power Forward'
    center = 'Center'


class Season(Enum):
    nba_2017 = {
        'start_time': pytz.timezone('America/New_York').localize(datetime.datetime(2016, 10, 25, 19, 30, 0, 0)),
        'end_time': pytz.timezone('America/New_York').localize(datetime.datetime(2017, 6, 18, 20, 0, 0, 0))
    }
    nba_2016 = {
        'start_time': pytz.timezone('America/New_York').localize(datetime.datetime(2015, 10, 28, 20, 0, 0, 0)),
        'end_time': pytz.timezone('America/New_York').localize(datetime.datetime(2016, 6, 20, 20, 0, 0, 0))
    }
    nba_2015 = {
        'start_time': pytz.timezone('America/New_York').localize(datetime.datetime(2014, 10, 28, 20, 0, 0, 0)),
        'end_time': pytz.timezone('America/New_York').localize(datetime.datetime(2015, 6, 16, 21, 0, 0, 0))
    }
    nba_2014 = {
        'start_time': pytz.timezone('America/New_York').localize(datetime.datetime(2013, 10, 29, 19, 0, 0, 0)),
        'end_time': pytz.timezone('America/New_York').localize(datetime.datetime(2014, 6, 15, 20, 0, 0, 0))
    }
    nba_2013 = {
        'start_time': pytz.timezone('America/New_York').localize(datetime.datetime(2012, 10, 30, 19, 0, 0, 0)),
        'end_time': pytz.timezone('America/New_York').localize(datetime.datetime(2013, 6, 20, 21, 0, 0, 0))
    }

    def get_start_time(self):
        return self.value['start_time']

    def get_end_time(self):
        return self.value['end_time']

    @staticmethod
    def value_of(start_time, end_time):
        assert isinstance(start_time, datetime.datetime)
        assert isinstance(end_time, datetime.datetime)

        for season in Season:
            if season.value['start_time'] == start_time and season.value['end_time'] == end_time:
                return season

        raise ValueError('Unable to identify season')


class Team(Enum):
    atlanta_hawks = {
        'name': 'Atlanta Hawks'
    }
    boston_celtics = {
        'name': 'Boston Celtics'
    }
    brooklyn_nets = {
        'name': 'Brooklyn Nets'
    }
    charlotte_hornets = {
        'name': 'Charlotte Hornets'
    }
    chicago_bulls = {
        'name': 'Chicago Bulls'
    }
    cleveland_cavaliers = {
        'name': 'Cleveland Cavaliers'
    }
    dallas_mavericks = {
        'name': 'Dallas Mavericks'
    }
    denver_nuggets = {
        'name': 'Denver Nuggets'
    }
    detroit_pistons = {
        'name': 'Detroit Pistons'
    }
    golden_state_warriors = {
        'name': 'Golden State Warriors'
    }
    houston_rockets = {
        'name': 'Houston Rockets'
    }
    indiana_pacers = {
        'name': 'Indiana Pacers'
    }
    los_angeles_clippers = {
        'name': 'Los Angeles Clippers'
    }
    los_angeles_lakers = {
        'name': 'Los Angeles Lakers'
    }
    memphis_grizzlies = {
        'name': 'Memphis Grizzlies'
    }
    miami_heat = {
        'name': 'Miami Heat'
    }
    milwaukee_bucks = {
        'name': 'Milwaukee Bucks'
    }
    minnesota_timberwolves = {
        'name': 'Minnesota Timberwolves'
    }
    new_orleans_pelicans = {
        'name': 'New Orleans Pelicans'
    }
    new_york_knicks = {
        'name': 'New York Knicks'
    }
    oklahoma_city_thunder = {
        'name': 'Oklahoma City Thunder'
    }
    orlando_magic = {
        'name': 'Orlando Magic'
    }
    philadelphia_76ers = {
        'name': 'Philadelphia 76ers'
    }
    phoenix_suns = {
        'name': 'Phoenix Suns'
    }
    portland_trail_blazers = {
        'name': 'Portland Trail Blazers'
    }
    sacramento_kings = {
        'name': 'Sacramento Kings'
    }
    san_antonio_spurs = {
        'name': 'San Antonio Spurs'
    }
    toronto_raptors = {
        'name': 'Toronto Raptors'
    }
    utah_jazz = {
        'name': 'Utah Jazz'
    }
    washington_wizards = {
        'name': 'Washington Wizards'
    }

    def get_name(self):
        return self.value['name']

    @staticmethod
    def value_of(name):
        assert isinstance(name, basestring)

        for team in Team:
            if team.value['name'] == name:
                return team

        raise ValueError('Unable to identify team with name: %s', name)
