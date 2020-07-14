import datetime as dt
import time as tm

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())

# Convert the timestamp to datetime.

date_now = dt.datetime.fromtimestamp(tm.time())

print(date_now)

print(date_now.day)

print(date_now.month)

print(date_now.year)

print(dt.timedelta(days=100))

# todays date
delta = dt.timedelta(days=100)

today = dt.date.today()

print(today)

print(today - delta)

print(today < today - delta)

print(today > today - delta)