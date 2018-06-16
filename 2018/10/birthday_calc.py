import datetime



class BirthdayCalc():
    
    def __init__ (self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def bday(self, day, month, year):
        from birthday_fun import get_bday
        year = get_bday.year
        month = get_bday.month
        day = get_bday.day
        return datetime(year, month, day)
    
    def years_since_birth(self, day, month, year):
        now = datetime.datetime.today()
        years_now = now.year()
        year_since = years_now - year
        return year_since
        