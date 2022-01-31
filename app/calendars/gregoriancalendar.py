import calendar
from datetime import date, datetime, timedelta
from typing import Iterable, List, Tuple


class GregorianCalendar:
    MONTH_NAMES = [calendar.month_name[i] for i in range(1,13)]

    @staticmethod
    def setfirstweekday(weekday: int) -> None:
        calendar.setfirstweekday(weekday)
    
    @staticmethod
    def firstweekday():
        return calendar.firstweekday()

    @staticmethod
    def previous_month_and_year(year: int, month: int) -> Tuple[int, int]:
        previous_month_date = date(year, month, 1) - timedelta(days=1)
        return previous_month_date.month, previous_month_date.year

    @staticmethod
    def next_month_and_year(year: int, month: int) -> Tuple[int, int]:
        last_day_of_month = calendar.monthrange(year, month)[1]
        next_month_date = date(year, month, last_day_of_month) + timedelta(days=1)
        return next_month_date.month, next_month_date.year

    @staticmethod
    def current_date() -> Tuple[int, int, int]:
        today_date = datetime.now().date()
        return today_date.day, today_date.month, today_date.year

    @staticmethod
    def month_days(year: int, month: int) -> Iterable[date]:
        return calendar.Calendar(calendar.firstweekday()).itermonthdates(year, month)

    @staticmethod
    def month_weekdays(year: int, month: int) -> Iterable[date]:
        md = GregorianCalendar.month_days(year, month)

        md_without_weekends=[day for day in md if day.weekday()<5]
        return md_without_weekends

        