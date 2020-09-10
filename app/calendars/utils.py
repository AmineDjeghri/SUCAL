import datetime
import pytz
from dateutil.rrule import *
from app import constants


def get_recurrent_datetimes(recur_rule, start, exclusions, utc):
    rules = rruleset()
    first_rule = rrulestr(recur_rule, dtstart=start)
    rules.rrule(first_rule)

    if not isinstance(exclusions, list): # this isn't a list when there is only one EXDATE
        exclusions = [exclusions]

    for xdt in exclusions:
        try:
            rules.exdate(xdt.dts[0].dt.replace(tzinfo=utc))
        except AttributeError:
            pass

    dates = []
    min_dt = str_to_datetime(constants.MIN_DATE, utc)
    max_dt = str_to_datetime(constants.MAX_DATE, utc)

    for d in rules.between(min_dt, max_dt):
        dates.append(d)
    return dates


def str_to_datetime(min_date, utc):
    """convert str date from %d-%m-%Y to an aware datime """

    min_date = datetime.datetime.strptime(min_date, "%d-%m-%Y").date()
    min_date_with_time = datetime.datetime.combine(min_date, datetime.time.min)
    min_date_with_time = min_date_with_time.replace(tzinfo=utc)
    return min_date_with_time