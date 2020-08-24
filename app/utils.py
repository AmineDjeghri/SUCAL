from icalendar import Calendar,Event
from datetime import datetime, date, timedelta
import pytz
import yaml


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
    ########
    ###############################################
    utc=pytz.UTC
    dt_today=datetime.today().date()
    dt_1hour_ago=datetime.now()
    print(type(dt_today))
    print(type(dt_1hour_ago))

    events=[]
    events_without_time=[]
    with open(ics_file,'r', encoding='utf-8') as f:
        cal = Calendar.from_ical(f.read())
        for component in cal.walk():
            event=dict()
            if component.get('dtstart') :
                component_dt=component.get('dtstart').dt
                if  type(component_dt) is datetime and component_dt.replace(tzinfo=utc) > dt_1hour_ago.replace(tzinfo=utc):
                    event['dtstart']=str(component.get('dtstart').dt)
                    event['summary']=str(component.get('summary'))
                    event['location']=str(component.get('location'))
                    if type(component.get('DTEND')) != type(None):
                        event['DTEND']=str(component.get('DTEND').dt)
                    events.append(event)    
                    print(event)                
                elif type(component_dt) is date and component_dt > dt_today-timedelta(days=800):
                    if type(component.get('DTEND')) != type(None):
                        event['DTEND']=str(component.get('DTEND').dt)
                    event['dtstart']=str(component.get('dtstart').dt)
                    event['summary']=str(component.get('summary'))
                    event['location']=str(component.get('location'))
                    print(event)
                    events_without_time.append(event)


    return events,events_without_time


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
            with open(ics_file, "w+", encoding='utf8') as ics_file_:
                ics_file_.write(requests.get(CALDAV_URL + MASTERS[master] + "/" + master, auth=(CALDAV_USERNAME, CALDAV_PASSWORD)).text)