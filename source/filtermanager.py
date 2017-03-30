import pandas as pd

def ApplyHolidayList(*args):
    calendar = args[0]
    holidayList = args[1]
    cal = calendar[calendar.index.isin(holidayList)]
    return calendar.drop(cal.index)

def MonthlyRecurring(*args):
    calendar = args[0]
    recurring = args[1]
    cal = pd.DataFrame({'date':calendar.index,'day':pd.Series(calendar.index).dt.weekday_name, 'week':pd.Series(calendar.index).dt.week, 'month':pd.Series(calendar.index).dt.month}).set_index(['date'])
    for recur in recurring:
        week = recur['week']
        day  = recur['day']
        for month in pd.unique(cal['month']):
            cal1 = cal[(cal['month'] == month) & (cal['day'] == day)]
            date_to_be_removed = pd.unique(cal1.index.date)[week - 1]  
            cal1 = cal1[cal1.index.date == date_to_be_removed]
            calendar = calendar.drop(cal1.index)
    return calendar
