from .gregoriancalendar import GregorianCalendar

class CalendarEvent():
    def __init__(self, title=None, start=None, end=None, location=None,type=None):
        self.start = start
        self.end = end
        self.location = location
        self.title = title
        self.type=type

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join('{}={!r}'.format(k, v) for k, v in self.__dict__.items())
        )


class DataCalendar:
    def __init__(self, events, first_weekday: int = 0) -> None:
        """
        Parameters:
            events(list of CalendarEvent)
            events_without_time(list of CalendarEvent)
        """
        self.events = events
        self.gregorian_calendar = GregorianCalendar
        self.gregorian_calendar.setfirstweekday(first_weekday)

    def get_month_data(self, year: int, month: int):
        """ return a single calendar page (contains at maxiumu 3 months, the actual month and some days from
        the previous and next month
        Return : two dics, both :dic["month"]["day"]
        """
        #### THIS CODE IS HORRIBLE, PLZ CONTRIBUTE TO MAKE IT BETTER
        month_events = {}


        for day in self.gregorian_calendar.month_days(year, month):
            for event in self.events:
                if event.start.year == day.year and event.start.month == day.month and event.start.day == day.day:
                    month_events=_check_month_dict(month_events, day)
                    month_events[str(day.month)][str(day.day)].append(event)
                    month_events[str(day.month)][str(day.day)]
        
        for key in month_events.keys():
            for key2 in month_events[key].keys():
                month_events[key][key2]=sorted(month_events[key][key2], key=lambda x: x.start)

        return month_events

    def get_events(self):
        return sorted(self.events, key=lambda x: x.start)


    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join('{}={!r}'.format(k, v) for k, v in self.__dict__.items())
        )


def _check_month_dict(month_events, day):
    """ create a dictionnary key for the month and the day if they do not already exist """
    if str(str(day.month)) not in month_events:
        month_events[str(day.month)] = dict()
    if str(day.day) not in month_events[str(day.month)]:
        month_events[str(day.month)][str(day.day)]=list()
    return month_events