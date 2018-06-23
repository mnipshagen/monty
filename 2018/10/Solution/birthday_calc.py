"""
This module contains the BirthdayCalc class.

Uses the datetime module.
"""

import datetime
from datetime import datetime as dt

class BirthdayCalc:
    """
    This class defines a BirthdayCalc object which can return the difference between
    a birthday and the current date in seconds, minutes, hours, days, months
    and yearsself.

    Attributes:
        bday: Birthday
        today: Date of today
    """

    def __init__(self,day,month,year):
        """
        Creates a new BirthdayCalc object.

        Args:
            day: day (of the month) of the birthday
            month: month (of the year) of the birthday
            year: year of the birthday
        """

        # save birthday and today at datetime objects
        self.bday = dt(year,month,day)
        self.today = dt.today()

        # to make the results more accurate, we will get the total seconds that
        # have passed since the day of the birth to this very second
        # it was not necessary to do this, using the time difference in days
        # would have sufficed :)
        # to compute the total amount of seconds since birth, we first convert
        # the days from the timedelta object diff into seconds and then add
        # the seconds difference on top
        diff = (self.today - self.bday)
        self._diff_seconds = diff.days * 24 * 60 * 60 + diff.seconds

    def seconds_since_birth(self):
        """ Returns the seconds that have passed since birth. """
        return self._diff_seconds

    def minutes_since_birth(self):
        """ Returns the minutes that have passed since birth. """
        return int(self.seconds_since_birth() / 60)

    def hours_since_birth(self):
        """ Returns the hours that have passed since birth. """
        return int(self.minutes_since_birth() / 60)

    def days_since_birth(self):
        """ Returns the days that have passed since birth. """
        return int(self.hours_since_birth() / 24)

    def _years_since_birth_float(self):
        """ Returns the years that have passed since birth as a float. """
        # we include this method because the months would be too inaccurate
        # if we just worked with the integer years
        return self.days_since_birth() / 365.25

    def years_since_birth(self):
        """ Returns the seconds that have passed since birth. """
        return int(self._years_since_birth_float())

    def months_since_birth(self):
        """ Returns the months that have passed since birth. """
        return int(self._years_since_birth_float() * 12)

    def next_birthday(self):
        """ Returns the days left until the next birthday """
        # get the date of the birthday this year
        bday_this_year = dt(self.today.year, self.bday.month, self.bday.day)

        # rounding up
        day_difference = (bday_this_year - self.today).days + 1

        # if birthday has not already passed this year
        if (day_difference >= 0):
            return day_difference # just return how many days left

        # day_difference was negative, so birthday is next year
        # we cannot use 365 + day_difference as this would deliver wrong results
        # in case of a gap year
        # therefore, we calculate the difference again
        bday_next_year = dt(self.today.year + 1, self.bday.month, self.bday.day)
        return (bday_next_year - self.today).days + 1 # again, round up
