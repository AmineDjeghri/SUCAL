# this file is only for testing some codes
import app.utils as utils
import pytz
from app import models, constants
import datetime
import calendar
from app.calendars.gregoriancalendar import GregorianCalendar


if __name__ == "__main__":
    d1=datetime.datetime(2020,2,1)
    print(d1)
    d2=datetime.date(2020,2,1)
    d3=datetime.date(2020,1,5)
    l=[d1,d2,d3]
    print(l)
    l1=sorted(l)
    print(l1)
    # l=sorted(l, key=lambda x: x.rank)

