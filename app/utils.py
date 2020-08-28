from icalendar import Calendar,Event
from datetime import datetime, date, timedelta
import pytz
import yaml
import requests
import os
import time
import re
from .gregorian_calendar import GregorianCalendar
from flask import current_app, request
import config
import calendar
from .calendar_data import CalendarData

CALDAV_URL = "https://cal.ufr-info-p6.jussieu.fr:443/caldav.php/"
CALDAV_USERNAME = "student.master"
CALDAV_PASSWORD = "guest"

SMSAPI_URL = ""

DIR_DATA = "app/data/"
DIR_ICS = DIR_DATA + "ics/"


def get_coming_events(ics_file):
    """
    Return the comming events of an ics file 
    Parameters:
        ics_file: ics file
    Returns:
        events (datetime.datetime): events that have a date and a time 
        events_without_time(datetime.date): events that have only a date
    """

    ###############################################

    ######## NEED TO UPDATE THE CODE TO MAKE IT BETTER READABLE
    ######## USE DECODE FUNCTION OF ICALENDAR
    ######## CODE AGAIN THE DATE PARSING ECT...
    ######## ADD exception handling file not found 
    ###############################################
    utc=pytz.timezone(current_app.config['TIMEZONE'])
    dt_today=datetime.today().date()
    dt_1hour_ago=datetime.now()
    
    events=[]
    events_without_time=[]
    with open(ics_file,'r', encoding='utf-8') as f:
        cal = Calendar.from_ical(f.read())
        for component in cal.walk():
            event=dict()
            if component.get('dtstart') :
                component_dt=component.get('dtstart').dt
                if  type(component_dt) is datetime and component_dt.replace(tzinfo=utc) > dt_1hour_ago.replace(tzinfo=utc):
                    event['dtstart']=component.get('dtstart').dt
                    event['summary']=str(component.get('summary'))
                    event['location']=str(component.get('location'))
                    if type(component.get('dtend')) != type(None):
                        event['dtend']=component.get('dtend').dt
                    events.append(event)                 
                elif type(component_dt) is date and component_dt > dt_today:
                    if type(component.get('dtend')) != type(None):
                        event['dtend']=component.get('dtend').dt
                    event['dtstart']=component.get('dtstart').dt
                    event['summary']=str(component.get('summary'))
                    event['location']=str(component.get('location'))
                    events_without_time.append(event)


    return events,events_without_time


def update_ics_file(master, if_older_than):
    with open(DIR_DATA + "masters.yml", "r") as yml_file:
        MASTERS = yaml.safe_load(yml_file)
    if master in MASTERS.keys():
        ics_file = DIR_ICS + master + ".ics"

        if not os.path.isfile(ics_file) or os.path.getmtime(ics_file) + if_older_than < time.time():
            with open(ics_file, "w+", encoding='utf8') as ics_file_:
                ics_file_.write(requests.get(CALDAV_URL + MASTERS[master] + "/" + master, auth=(CALDAV_USERNAME, CALDAV_PASSWORD)).text)








# see `app_utils` tests for details, but TL;DR is that urls must start with `http://` or `https://` to match
URLS_REGEX_PATTERN = r"(https?\:\/\/[\w/\-?=%.]+\.[\w/\+\-?=%.~&\[\]\#]+)"
DECORATED_URL_FORMAT = '<a href="{}" target="_blank">{}</a>'
def previous_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.previous_month_and_year(year=year, month=month)
    return (
        ""
        if year < current_app.config["MIN_YEAR"] or year > current_app.config["MAX_YEAR"]
        else "?y={}&m={}".format(year, month)
    )

def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    
    return (
        ""
        if year < current_app.config["MIN_YEAR"] or year > current_app.config["MAX_YEAR"]
        else "?y={}&m={}".format(year, month)
    )

def task_details_for_markup(details: str) -> str:
    if not current_app.config["AUTO_DECORATE_TASK_DETAILS_HYPERLINK"]:
        return details

    decorated_fragments = []
    fragments = re.split(URLS_REGEX_PATTERN, details)
    for index, fragment in enumerate(fragments):
        if index % 2 == 1:
            decorated_fragments.append(DECORATED_URL_FORMAT.format(fragment, fragment))
        else:
            decorated_fragments.append(fragment)

    return "".join(decorated_fragments)

