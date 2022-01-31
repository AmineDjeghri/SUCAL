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

from .utils import *


def create_data_calendar(masters):
    """
    Return the comming events of an ics file 
    Parameters:
        masters: list of masters name

    Returns:
        data_calendar (DataCalendar): 

    """
    # TO DO: arrange the code to remove duplicate lines
    # HORRIBLE CODE

    utc = pytz.timezone(constants.TIMEZONE)
    min_date = datetime.datetime.strptime(constants.MIN_DATE, "%d-%m-%Y").date()
    min_datetime = datetime.datetime.combine(min_date, datetime.time.min)
    min_datetime = min_datetime.replace(tzinfo=utc)

    events = []
    
    for master in masters: 
        cal = _load_calendar(master)

        if cal is not None:
            for component in cal.walk():
                event = CalendarEvent()
                if component.get('dtstart') :
                    component_dt = component.get('dtstart').dt

                    # events with date & time like courses
                    if  type(component_dt) is datetime.datetime and component_dt.replace(tzinfo=utc) >= min_datetime:
                        event.start = component.get('dtstart').dt.replace(tzinfo=utc)
                        if component.get('dtend') :
                            event.end = component.get('dtend').dt.replace(tzinfo=utc)

                        exdates = component.get('exdate')
                        if component.get('rrule'):
                            reoccur = component.get('rrule').to_ical().decode('utf-8')
                            for dtstart, dtend in zip(get_recurrent_datetimes(reoccur, event.start, exdates, utc),get_recurrent_datetimes(reoccur, event.end, exdates, utc)):
                                event = CalendarEvent()
                                event.type = "Normal" 
                                event.title = str(component.get('summary'))
                                event.location = str(component.get('location'))
                                event.start=dtstart
                                event.end=dtend
                                events.append(event)
                        else:
                            event.type = "Normal" 
                            event.title = str(component.get('summary'))
                            event.location = str(component.get('location'))
                            events.append(event) 

                    # events without time like holidays
                    elif type(component_dt) is datetime.date and component_dt >= min_date:
                        event.type = "Special" 
                        event.start = component.get('dtstart').dt
                        event.start = datetime.datetime.combine(event.start, datetime.datetime.min.time()) #for sorting we will convert it to datetime
                        event.start = event.start.replace(tzinfo=utc)
                        if component.get('dtend') :
                            event.end = component.get('dtend').dt

                        event.title = str(component.get('summary'))
                        event.location = str(component.get('location'))
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
                print("download a new file of ", ics_file, " last time downloaded: ", time.ctime(os.path.getmtime(ics_file)),
                      " today: ", time.ctime(time.time()))
                ics_file_.write(requests.get(constants.CALDAV_URL + MASTERS[master] + "/" + master, auth=(constants.CALDAV_USERNAME, constants.CALDAV_PASSWORD)).text)


def _load_calendar(master):
    cal = None

    _update_calendar(master, if_older_than=0)

    ics_file = constants.DIR_ICS + master + ".ics"
    with open(ics_file, 'r', encoding=constants.ENCODING) as f:
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


