import app.models as models
from app.calendars import factory, gregoriancalendar
import datetime
import calendar
import pytest
import pytz
from app import constants,utils
import os

# IMPORTANT :
# THESE ARE NOT REAL TESTS, THEY ONLY HELP TO SEE IF EVERYTHING WORKS
# FINE WHEN I UPDATE THE IMPORTS & THE STRUCTURE OF THE APP


def test_create_calendar():

    factory._update_calendar("M1")
    data_calendar = factory.create_data_calendar(["M1"])
    
    events = data_calendar.events

    print(data_calendar.events)

    assert len(events) != 0
    month_events = data_calendar.get_month_data(2020, 1)
    print(month_events)

    print('---------Androide-------')

    data_calendar = factory.create_data_calendar(["M1_ANDROIDE"])
    month_events= data_calendar.get_month_data(2020, 9)
    print(month_events)


def test_create_calendar3():

    data_calendar = factory.create_data_calendar(["M1"])
    
    events = data_calendar.events

    # print(data_calendar.events)

    assert len(events) != 0

    month_events = data_calendar.get_month_data(2020, 9)
    print(month_events)


def test_create_calendar2():

    data_calendar = factory.create_data_calendar(["M1","M1_ANDROIDE"])
    
    events = data_calendar.events


    # print(data_calendar.events)


    assert len(events) != 0

    month_events = data_calendar.get_month_data(2020, 9)
    print(month_events)
    
def test_create_empty_calendar():
    data_calendar = factory.create_data_calendar(masters=[])
    # print(data_calendar)

    print(data_calendar.get_month_data(2020,8))

def test_main_views():
    masters=['M1','M1_DAC']

    if 'M1'not in masters and 'M1' in '\t'.join(masters):
        masters.append('M1') 
    if 'M2' not in masters and 'M2' in '\t'.join(masters):
        masters.append('M2')
    
    print(masters)

    current_day, current_month, current_year = gregoriancalendar.GregorianCalendar.current_date()
    year = 2020
    month = 9
    year, month, month_name = utils.preprocess_year_and_month(year,month)

    weekdays_headers = [day for day in calendar.day_abbr][:5] # Only weekdays
    print(weekdays_headers)
    month_days = gregoriancalendar.GregorianCalendar.month_weekdays(year, month)
    month_days = list(month_days)

    data_calendar = factory.create_data_calendar(masters)
    month_events = data_calendar.get_month_data(year, month)
    print(month_events)