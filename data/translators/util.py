import pytz
import datetime


def translate_day_start_and_end_from_est_to_utc(year, month, day):
    day_start_est = pytz.timezone('US/Eastern')\
                        .localize(datetime.datetime(year=year,
                                                    month=month,
                                                    day=day,
                                                    hour=0,
                                                    minute=0,
                                                    second=0,
                                                    microsecond=0))
    day_end_est = day_start_est + datetime.timedelta(hours=24)
    return {
        'day_start_utc': day_start_est.astimezone(pytz.utc),
        'day_end_utc': day_end_est.astimezone(pytz.utc)
    }