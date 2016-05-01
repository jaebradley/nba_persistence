import datetime

import pytz


def translate_day_start_from_est_to_utc(year, month, day):
    day_start_est = pytz.timezone('US/Eastern')\
                        .localize(datetime.datetime(year=year,
                                                    month=month,
                                                    day=day,
                                                    hour=0,
                                                    minute=0,
                                                    second=0,
                                                    microsecond=0))
    return day_start_est.astimezone(pytz.utc)


def translate_day_end_from_est_to_utc(year, month, day):
    day_start_utc = translate_day_start_from_est_to_utc(year=year, month=month, day=day)
    return day_start_utc + datetime.timedelta(hours=24)