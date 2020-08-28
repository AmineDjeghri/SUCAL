import json
import os
import time
from datetime import datetime
from typing import Dict, List, Optional, cast
import timeit
from . import constants 
from flask import current_app
from .gregorian_calendar import GregorianCalendar

KEY_TASKS = "tasks"
KEY_USERS = "users"
KEY_NORMAL_TASK = "normal"
KEY_REPETITIVE_TASK = "repetition"
KEY_REPETITIVE_HIDDEN_TASK = "hidden_repetition"


class CalendarData:

    REPETITION_TYPE_WEEKLY = "w"
    REPETITION_TYPE_MONTHLY = "m"
    REPETITION_SUBTYPE_WEEK_DAY = "w"
    REPETITION_SUBTYPE_MONTH_DAY = "m"

    def __init__(self, events,events_without_time, first_weekday: int = constants.WEEK_START_DAY_MONDAY) -> None:
        self.events = events
        self.events_without_time=events_without_time
        self.gregorian_calendar = GregorianCalendar
        self.gregorian_calendar.setfirstweekday(first_weekday)

    @staticmethod
    def is_past(year: int, month: int, current_year: int, current_month: int) -> bool:
        if year < current_year:
            return True
        elif year == current_year:
            if month < current_month:
                return True
        return False

    def events_from_calendar(self, year: int, month: int, events,events_without_time) -> Dict:
        #### THIS CODE IS HORRIBLE, PLZ CONTRIBUTE TO CORRECT IT
        a=timeit.default_timer()
        month_events = {}
        for day in self.gregorian_calendar.month_days(year, month):
            month_events[str(day.month)]=dict()

        for day in self.gregorian_calendar.month_days(year, month):
            month_events[str(day.month)][str(day.day)]=list()
            for event in events:
                if event['dtstart'].year==day.year and event['dtstart'].month==day.month and event['dtstart'].day==day.day:
                    month_events[str(day.month)][str(day.day)].append(event)
        print(month_events)
        b=timeit.default_timer()
        print('time taken ',b-a)
        return month_events


    def event_by_id(self, id):
        return 'not coded yet'

