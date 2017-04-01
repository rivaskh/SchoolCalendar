import pandas as pd

ColumnTemplate = {'Teacher':[], 'Subject':[], 'StudentGroups':[], 'Classrooms':[]}

class ResourceCalendarException(Exception):
    pass

class ResourceCalendar:
    def __init__(self, **kwargs):
        if "start_date" not in kwargs:
            raise ResourceCalendarException("expecting start_date")
        if "end_date" not in kwargs:
            raise ResourceCalendarException("expecting end_date")

        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.daily_freq = 1
        if "daily_freq" in kwargs:
            self.daily_freq = kwargs['daily_freq']

        self.calendar_filters = []
        if "calendar_filters" in kwargs:
            print (kwargs['calendar_filters'])
            self.calendar_filters = kwargs['calendar_filters'] 

        self.calendar = pd.DataFrame()

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

    def append_value(self, **kwargs):
        if 'resource_name' not in kwargs:
            raise ResourceCalendarException("expecting resource_name")
        if 'date' not in kwargs:
            raise ResourceCalendarException("expecting date")
        if 'resource_value' not in kwargs:
            raise ResourceCalendarException("expecting resource_value")
        if self.calendar.empty:
            raise ResourceCalendarException("need to call calendar_create()")
            
        res_name = kwargs['resource_name']
        res_value = kwargs['resource_value']
        append_date = kwargs['date']
        self.calendar.at[pd.Timestamp(append_date),res_name].append(res_value)
        return self.calendar.at[pd.Timestamp(append_date), res_name]


    def get_value(self, **kwargs):
        pass
