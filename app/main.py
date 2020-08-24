from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

import ics
import os
import sys
import time
import requests
import yaml

import timeit

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/search')
def search():
    return render_template('search.html', results="Hi")

CALDAV_URL = "https://cal.ufr-info-p6.jussieu.fr:443/caldav.php/"
CALDAV_USERNAME = "student.master"
CALDAV_PASSWORD = "guest"

SMSAPI_URL = ""

DIR_DATA = "app/data/"
DIR_ICS = DIR_DATA + "ics/"

with open(DIR_DATA + "masters.yml", "r") as yml_file:
    MASTERS = yaml.safe_load(yml_file)

def update_ics_file(master, if_older_than):
    if master in MASTERS.keys():
        ics_file = DIR_ICS + master + ".ics"

        if not os.path.isfile(ics_file) or os.path.getmtime(ics_file) + if_older_than < time.time():
            with open(ics_file, "w+") as ics_file_:
                ics_file_.writelines(requests.get(CALDAV_URL + MASTERS[master] + "/" + master, auth=(CALDAV_USERNAME, CALDAV_PASSWORD)).text)

# def update_everything():
#     for master in MASTERS:
#         update_ics_file(master, 0)

def get_coming_events(ics_file, gap_before=3600*2):

    with open(ics_file, "r") as ics_file_:
        events = [e for e in ics.Calendar(ics_file_.read()).events if e.begin.timestamp >= time.time() - gap_before]

    return events

@main.route('/masters/<masters>')
def masters_events(masters):
    a=timeit.default_timer()
    events = []
    masters=list(set(masters.split("+")))
    for master in masters:
        print(master)
        update_ics_file(master, 3600 * 2)

        ics_file = DIR_ICS + master + ".ics"
        events += get_coming_events(ics_file)
        
        # events.sort(key=lambda e: e.begin.timestamp)
    b=timeit.default_timer()
    print('time raken ',b-a)
    return render_template('masters.html')