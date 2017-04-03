import pandas as pd

def HolidayList(*args):
    calendar = args[0]
    holidayList = [pd.Timestamp(x).date() for x in args[1]]
    cal = pd.DataFrame({'date':calendar.index, 'holiday':pd.Series(calendar.index.date).isin(holidayList)}).set_index(['date'])
    cal = cal[cal.holiday == True]
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

def WeeklyRecurring(*args):
    calendar = args[0]
    days = args[1]
    cal = pd.DataFrame({'date':calendar.index,'day':pd.Series(calendar.index).dt.weekday_name}).set_index(['date'])
    for day in days:
        dates_to_be_removed = cal[cal['day'] == day]
        calendar = calendar.drop(dates_to_be_removed.index)
    return calendar
