import pytest
from source.resourcecalendar import ResourceCalendar, ResourceCalendarException

class TestCalendarResource:
    def test_AppendValue_Raise_Exception_When_No_ResourceName(self):
        res = ResourceCalendar(start_date='1/1/2017', end_date='31/1/2017', daily_freq=6)
        with pytest.raises(ResourceCalendarException) as excinfo:
            res.append_value()
        excinfo.match("expecting resource_name")

    def test_AppendValue_Raise_Exception_When_No_Date(self):
        res = ResourceCalendar(start_date='1/1/2017', end_date='31/1/2017', daily_freq=6)
        with pytest.raises(ResourceCalendarException) as excinfo:
            res.append_value(resource_name='Teacher')
        excinfo.match("expecting date")

    def test_AppendValue_Raise_Exception_When_No_ResourceValue(self):
        res = ResourceCalendar(start_date='1/1/2017', end_date='31/1/2017', daily_freq=6)
        with pytest.raises(ResourceCalendarException) as excinfo:
            res.append_value(resource_name='Teacher', date='5/1/2017')
        excinfo.match("expecting resource_value")

    def test_AppendValue_Raises_Exception_When_Calendar_Not_Created(self):
        res = ResourceCalendar(start_date='1/1/2017', end_date='31/1/2017', daily_freq=6)
        with pytest.raises(ResourceCalendarException) as excinfo:
            res.append_value(resource_name='Teacher', date='5/1/2017', resource_value='A')
        excinfo.match("need to call calendar_create()")

    def test_set_resource_to_a_particular_date_in_calendar(self):
        res = ResourceCalendar(start_date='1/1/2017', end_date='31/1/2017', daily_freq=6)
        res.create_calendar()
        new_value = res.append_value(date='1/5/2017 01:00:00', resource_name='Teacher', resource_value='A')
        assert new_value == ['A']

