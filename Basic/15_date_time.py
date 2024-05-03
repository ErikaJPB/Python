# Date Time

import datetime
print(dir(datetime))  # ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


# Getting datetime information

from datetime import datetime

now = datetime.now()
print(now) # 2024-05-02 11:21:09.004062

day = now.day
print(day) # 2

month = now.month
print(month) # 5

year = now.year
print(year) # 2024

hour = now.hour
print(hour) # 11

minute = now.minute
print(minute) # 24

second = now.second
print(second) # 22

timestamp = now.timestamp()
print('timestamp: ', timestamp) # 1651312909.004062

print(f'{day}/{month}/{year}, {hour}:{minute}') # 2/5/2024, 11:26


# strftime 

from datetime import datetime

new_year = datetime(2024, 1, 1)
print(new_year) # 2024-01-01 00:00:00

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 1 1 2024 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}') # 1/1/2024, 0:0


from datetime import datetime

now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time: ',  t) # time: 15:24:00

time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time_one: ', time_one) # time_one: 05/03/2024, 15:25:38

time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print('time_two: ', time_two) # time_two: 03/05/2024, 15:26:38


# strptime

from datetime import datetime

date_string = '3 May, 2024'
print("date_string =", date_string) # date_string =  3 May, 2024
date_object = datetime.strptime(date_string, '%d %B, %Y')
print("date_object =", date_object) # date_object =  2024-05-03 00:00:00



# Date from datetime

from datetime import datetime
from datetime import date

d = date(2024, 5, 3 )
print(d) # 2024-05-03
print('Current date:', d.today()) # Current date: 2024-05-03

today = date.today()
print("Current year:", today.year) # Current year: 2024
print("Current month:", today.month) # Current month: 5
print("Current day:", today.day) # Current day: 3


# Time objects to represent time

from datetime import time

a = time()
print("a:", a) # a: 2024-05-03 15:26:38.004062

b = time(11, 34, 56)
print("b:", b) # b: 11:34:56

c = time(hour=11, minute=34, second=56)
print("c:", c) # c: 11:34:56

d = time(11, 34, 56, 234566)
print("d:", d) # d: 11:34:56.234566



# Difference between two points in time using

today = date(year=2024, month=5, day=3)
new_year = date(year=2025, month=1, day=1)
time_left_for_new_year = new_year - today
print('Time left for new year: ', time_left_for_new_year) # Time left for new year:  243 days, 0:00:00

t1 = datetime(year= 2024, month=5, day=3, hour=0, minute = 59, second=0)
t2 = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print("Time left for new year:", diff) # Time left for new year:  242 days, 23:01:00


# Difference between two points in time using timedelta

from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3:", t3) # t3: 86 days, 22:56:50