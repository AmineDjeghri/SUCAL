from icalendar import Calendar,Event
from datetime import datetime, date, timedelta
import pytz
import calendar

print([day for day in calendar.day_abbr])
with open('app/data/ics/M2_DAC.ics','r', encoding='utf-8') as f:
    cal = Calendar.from_ical(f.read())
