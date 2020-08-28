from flask import Blueprint, render_template, current_app
from . import db
from flask_login import login_required, current_user
from .gregorian_calendar import GregorianCalendar
from .calendar_data import CalendarData

import os
import sys
import time
import requests
import yaml
from . import utils
import timeit
import calendar

main = Blueprint('main', __name__)


@main.route('/')
def index():
    with open(utils.DIR_DATA + "masters.yml", "r") as yml_file:
        masters = yaml.safe_load(yml_file)
        print(masters.keys())
    return render_template('index.html',masters=masters)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/search')
def search():
    return render_template('search.html', results="Hi")

@main.route('/masters/<masters>')
def masters_events(masters):
    events = []
    events_without_time=[]
    print(masters)
    for master in list(set(masters.split("+"))):
        utils.update_ics_file(master, 3600 * 2)
        ics_file = utils.DIR_ICS + master + ".ics"
        event,event_without_time=utils.get_coming_events(ics_file)
        events += event
        events.sort(key=lambda e: e["dtstart"])
        events_without_time += event_without_time
        events_without_time.sort(key=lambda e: e["dtstart"])
        
    return render_template('masters.html', events=events,events_without_time=events_without_time)
    # return render_template('calendar.html', events=events,events_without_time=events_without_time)

@main.route('/calendar/<masters>')
def show_calendar(masters):
    #### NEED to change this func to handle only one master
    events = []
    events_without_time=[]
    for master in list(set(masters.split("+"))):
        utils.update_ics_file(master, 3600 * 2)
        ics_file = utils.DIR_ICS + master + ".ics"
        event,event_without_time=utils.get_coming_events(ics_file)
        events += event
        events.sort(key=lambda e: e["dtstart"])
        events_without_time += event_without_time
        events_without_time.sort(key=lambda e: e["dtstart"])

    GregorianCalendar.setfirstweekday(current_app.config["WEEK_STARTING_DAY"])

    current_day, current_month, current_year = GregorianCalendar.current_date()
    # year = int(request.args.get("y", current_year))
    year=2020
    year = max(min(year, current_app.config["MAX_YEAR"]), current_app.config["MIN_YEAR"])
    # month = int(request.args.get("m", current_month))
    month=9
    month = max(min(month, 12), 1)
    month_name= calendar.month_name[month]

    calendar_data = CalendarData(events,events_without_time, current_app.config["WEEK_STARTING_DAY"])

    events = calendar_data.events_from_calendar(year, month, events, events_without_time)


    weekdays_headers =[day for day in calendar.day_abbr]


    return  render_template(
            "calendar.html",
            year=year,
            month=month,
            month_name=month_name,
            current_year=current_year,
            current_month=current_month,
            current_day=current_day,
            month_days=GregorianCalendar.month_days(year, month),
            previous_month_link=utils.previous_month_link(year, month),
            next_month_link=utils.next_month_link(year, month),
            tasks=events,
            display_view_past_button=current_app.config["SHOW_VIEW_PAST_BUTTON"],
            weekdays_headers=weekdays_headers,
        
    )  


