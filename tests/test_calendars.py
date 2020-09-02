import app.models as models
from app.calendars import factory
import datetime
import calendar
import pytest
import pytz
from app import constants
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


# def test_create_calendar2():

#     data_calendar = factory.create_data_calendar(["M1","M1_ANDROIDE"])
    
#     events = data_calendar.events
#     events_without_time = data_calendar.events_without_time

#     # print(data_calendar.events)
#     # print(data_calendar.events_without_time)

#     assert len(events) != 0
#     assert len(events_without_time) != 0

#     month_events, month_events_without_time = data_calendar.get_month_data(2020, 9)
#     print(month_events)
#     print(month_events_without_time)
    
# def test_create_empty_calendar():
#     data_calendar = factory.create_data_calendar(masters=[])
#     # print(data_calendar)

#     print(data_calendar.get_month_data(2020,8))