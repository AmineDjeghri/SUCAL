
from .calendars.gregoriancalendar import GregorianCalendar
from . import constants
import calendar

def previous_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.previous_month_and_year(year=year, month=month)
    return (
        ""
        if year < constants.MIN_YEAR or year > constants.MAX_YEAR
        else "?y={}&m={}".format(year, month)
    )

def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    
    return (
        ""
        if year < constants.MIN_YEAR or year > constants.MAX_YEAR
        else "?y={}&m={}".format(year, month)
    )

def preprocess_year_and_month(year,month):
    year = max(min(year, constants.MAX_YEAR), constants.MIN_YEAR)
    month = max(min(month, 12), 1)
    month_name= calendar.month_name[month]

    return year, month, month_name

def check_month_dict(month_events, day):
    """ create a dictionnary key for the month and the day if they do not already exist """
    if str(str(day.month)) not in month_events:
        month_events[str(day.month)] = dict()
    if str(day.day) not in month_events[str(day.month)]:
        month_events[str(day.month)][str(day.day)]=list()
    return month_events