import calendar

print("is leap: {}".format(calendar.isleap(1987)))
print("is leap: {}".format(calendar.isleap(2020)))

# date
from datetime import date

someDate = date.today()
print("Some date: {}".format(someDate.isoformat()))

# timedelta
from datetime import timedelta

oneDay = timedelta(days=1)
tomorrow = someDate + oneDay
print("+1 day: {}".format(tomorrow.isoformat()))

yesterday = someDate - oneDay
print("-1 day: {}".format(yesterday.isoformat()))

# time
from datetime import time
someTime = time(23, 12, 31)
print("{}".format(someTime.isoformat()))

from datetime import datetime
some = datetime.combine(someDate, someTime)
print("Some datetime {}".format(some.isoformat()))

# write to file in isoformat
iofile = open("dt.dat", "w+")
print(datetime.now().isoformat(), file=iofile, end="")

# read from file
import io
iofile.seek(0, io.SEEK_SET)

today_string = ""
while True:
    line = iofile.readline()
    if not line:
        break
    today_string += line

print("\tWritten: {}".format(today_string))

# parse isoformat
dt = datetime.fromisoformat(today_string)
print("\tParsed: {}".format(dt.isoformat()))

# bday week day
bday = date(1987, 12, 24)
print("Week day: {}".format(bday.weekday()))

# 10 000 day from bday
print("10 000 day was born: {}".format(bday + timedelta(days=10000)))