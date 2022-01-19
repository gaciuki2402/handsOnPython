from datetime import datetime, date, time
import calendar
current_time=datetime.now()
print(current_time)

todays_date=datetime.today()
print(todays_date)

day=date.today()
print(day)

t=datetime.now()
print(
    "year:",t.year,
    "month:",t.month,
    "day:",t.day,
    "hour:",t.hour,
    "minute:",t.minute,
    "second:",t.second

                    )
# gettingdatetime as input
my_date="19-01-2022-23:00:08"
i=datetime.strptime(my_date,"%d-%m-%Y-%H:%M:%S")
print(i)
print(calendar.month(2022,6))

