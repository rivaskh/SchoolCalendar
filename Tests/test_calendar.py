import pytest
from source.resourcecalendar import ResourceCalendar, ResourceCalendarException
from source.filtermanager import ApplyHolidayList,MonthlyRecurring

class TestCalendar:
    def test_Initialize_Calendar_Without_StartDate(self):
        with pytest.raises(ResourceCalendarException) as excinfo:
            cal =  ResourceCalendar()
        excinfo.match("No Start Date")
        
    def test_Initialize_Calendar_Without_EndDate(self):
        with pytest.raises(ResourceCalendarException) as excinfo:
            cal = ResourceCalendar(start_date='1/1/2017')
        excinfo.match("No End Date")

    def test_Initalize_Calendar_With_Start_And_EndDate(self):
        res = ResourceCalendar(start_date='1/1/2017',end_date='31/1/2017')
        cal = res.create_calendar()
        assert len(cal) == 31 

    def test_Initalize_Calendar_With_Frequency_In_Day(self):
        res = ResourceCalendar(start_date='1/1/2017',end_date='31/1/2017', daily_freq=6)
        cal = res.create_calendar()
        assert len(cal) == 31*6 

class TestApplyCalendarFilters:
    def test_Apply_Holiday_List_Filter(self):
        holidayList = ['1/5/2017','1/17/2017']
        res = ResourceCalendar(start_date='1/1/2017',end_date='31/1/2017', daily_freq=6, calendar_filters=[{ApplyHolidayList:holidayList}])
        cal = res.create_calendar()
        assert len(cal) == (31*6 - 2) 

    def test_Apply_Monthly_Recurring_Filter(self):
        monthlyRecurring = [{'day':'Saturday','week':2}]
        res = ResourceCalendar(start_date='1/1/2017',end_date='31/1/2017', daily_freq=6, calendar_filters=[{MonthlyRecurring:monthlyRecurring}])
        cal = res.create_calendar()
        assert len(cal) == 180 
        


