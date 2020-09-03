from icalendar import Calendar,Event
import datetime
import pytz
import yaml
import requests
import os
import time
from .datacalendar import CalendarEvent, DataCalendar
import calendar
from app import constants
import traceback


def create_data_calendar(masters):
    """
    Return the comming events of an ics file 
    Parameters:
        masters: list of masters name
        min_date: minimum date to get events
        utc: timzeone
    Returns:
        events (list): events that have a date and a time (datetime.datetime)
        events_without_time(list): events that have only a date (datetime.date)
    """

    utc = pytz.timezone(constants.TIMEZONE)

    min_date = datetime.datetime.strptime(constants.MIN_DATE, "%d-%m-%Y").date()
    min_date_with_time = datetime.datetime.combine(min_date, datetime.time.min)
    min_date_with_time = min_date_with_time.replace(tzinfo=utc)

    events = []
    
    for master in masters: 
        cal = _load_calendar(master)

        if cal is not None:
            for component in cal.walk():

                event = CalendarEvent()
                if component.get('dtstart') :
                    component_dt = component.get('dtstart').dt
                    if  type(component_dt) is datetime.datetime and component_dt.replace(tzinfo=utc) >= min_date_with_time:
                        event.start = component.get('dtstart').dt
                        event.title = str(component.get('summary'))
                        event.location = str(component.get('location'))
                        event.type = "Normal" # events with date & time like courses
                        if type(component.get('dtend')) != type(None):
                            event.end = component.get('dtend').dt
                        events.append(event)  

                    elif type(component_dt) is datetime.date and component_dt >= min_date:
                        if type(component.get('dtend')) != type(None):
                            event.end = component.get('dtend').dt

                        #for sorting (need to be datetime)
                        event.start = component.get('dtstart').dt
                        event.start = datetime.datetime.combine(event.start,datetime.datetime.min.time())
                        event.start = utc.localize(event.start)

                        event.title = str(component.get('summary'))
                        event.location = str(component.get('location'))
                        event.type = "Special" # events without time like holidays
                        events.append(event)

    data_calendar = DataCalendar(events, constants.FIRST_WEEKDAY)
    return data_calendar


def _update_calendar(master, if_older_than=0):
    with open(constants.DIR_DATA + "masters.yml", "r") as yml_file:
        MASTERS = yaml.safe_load(yml_file)
    if master in MASTERS.keys():
        ics_file = constants.DIR_ICS + master + ".ics"

        if not os.path.isfile(ics_file) or os.path.getmtime(ics_file) + if_older_than < time.time():
            with open(ics_file, "w+", encoding='utf8') as ics_file_:
                ics_file_.write(requests.get(constants.CALDAV_URL + MASTERS[master] + "/" + master, auth=(constants.CALDAV_USERNAME, constants.CALDAV_PASSWORD)).text)


def _load_calendar(master):
    cal= None

    _update_calendar(master, if_older_than=1800)

    ics_file = constants.DIR_ICS + master + ".ics"
    with open(ics_file,'r', encoding=constants.ENCODING) as f:
        try:
            cal = Calendar.from_ical(f.read())
        except:
            print("---------failed reading the calendar-------------")

    if cal is None:
        print("-----> redownloading ", master, ".ics")
        _update_calendar(master)
        with open(ics_file,'r', encoding=constants.ENCODING) as f:
            try:
                cal = Calendar.from_ical(f.read())
                print("----------- SUCCEEDED TO READ THE CALENDAR----")
            except:
                traceback.print_exc()
                print("----------- FAILED TO READ THE CALENDAR-------")

    return cal