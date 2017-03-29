import pandas as pd

def ApplyHolidayList(*args):
    calendar = args[0]
    holidayList = args[1]
    cal = calendar[calendar.index.isin(holidayList)]
    return calendar.drop(cal.index)

