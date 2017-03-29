import pandas as pd

ColumnTemplate = {'Teacher':[], 'Subject':[], 'StudentGroups':[], 'Classrooms':[]}

class ResourceCalendarException(Exception):
    pass

class ResourceCalendar:
    def __init__(self, **kwargs):
        if "start_date" not in kwargs:
            raise ResourceCalendarException("No Start Date")
        if "end_date" not in kwargs:
            raise ResourceCalendarException("No End Date")

        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.daily_freq = 1
        if "daily_freq" in kwargs:
            self.daily_freq = kwargs['daily_freq']

        self.calendar_filters = []
        if "calendar_filters" in kwargs:
            print (kwargs['calendar_filters'])
            self.calendar_filters = kwargs['calendar_filters'] 

        self.calendar = []

    def __len__(self):
        return len(self.calendar.index)

    def create_calendar(self):
        days = pd.date_range(self.start_date, self.end_date) 
        list_of_days = []
        for day in days:
            list_of_days += pd.date_range(day, periods=self.daily_freq, freq='H')
        self.calendar = pd.DataFrame([ColumnTemplate for i in range(len(list_of_days))], index=list_of_days)
        for fltrdict in self.calendar_filters:
            for fltr in fltrdict:
                self.calendar = fltr(self.calendar, fltrdict[fltr])
        return self.calendar


