from flask import Blueprint, render_template, current_app, request, abort
from . import db
from flask_login import login_required, current_user
import os
import sys
import time
import requests
import yaml
from . import utils
import timeit
import calendar
from . import constants
from .calendars import factory
from .calendars.gregoriancalendar import GregorianCalendar

main = Blueprint('main', __name__)


@main.route('/')
def index():
    try:
        with open(constants.DIR_DATA + "masters.yml", "r") as yml_file:
            masters = yaml.safe_load(yml_file)
    except:
        abort(404)
    return render_template('index.html',masters=masters)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/search')
def search():
    return render_template('search.html', results="Not Implemented yet")


@main.route('/calendar/<masters>')
def show_calendar(masters):
    masters = list(set(masters.split("+")))
    
    if 'M1'not in masters and 'M1' in '\t'.join(masters):
        masters.append('M1') 
    if 'M2' not in masters and 'M2' in '\t'.join(masters):
        masters.append('M2')
    
    print(masters)

    current_day, current_month, current_year = GregorianCalendar.current_date()
    year = int(request.args.get("y", current_year))
    month = int(request.args.get("m", current_month))
    year, month, month_name = utils.preprocess_year_and_month(year,month)

    weekdays_headers = [day for day in calendar.day_abbr][:5] # Only weekdays
    print(weekdays_headers)
    month_days = GregorianCalendar.month_weekdays(year, month)
    month_days = list(month_days)

    data_calendar = factory.create_data_calendar(masters)
    month_events = data_calendar.get_month_data(year, month)

    return  render_template(
            "calendar.html",
            year=year,
            month=month,
            month_name=month_name,
            current_year=current_year,
            current_month=current_month,
            current_day=current_day,
            month_days=month_days,
            previous_month_link=utils.previous_month_link(year, month),
            next_month_link=utils.next_month_link(year, month),
            tasks=month_events,
            weekdays_headers=weekdays_headers,
        
    )  


