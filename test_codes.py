# this file is only for testing some codes
import app.utils as utils
import pytz
from app import models, constants
import datetime
import calendar
from app.calendars.gregoriancalendar import GregorianCalendar


if __name__ == "__main__":
    md=GregorianCalendar.month_days(2020,9)

    for d in md:
        print(d.weekday())
    print('main')
