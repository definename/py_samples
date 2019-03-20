import calendar

print("is leap: {}".format(calendar.isleap(1987)))
print("is leap: {}".format(calendar.isleap(2020)))


from datetime import date

someDate = date.today()
print("Some date: {}".format(someDate.isoformat()))

from datetime import timedelta

oneDay = timedelta(days=1)
tomorrow = someDate + oneDay
print("+1 day: {}".format(tomorrow.isoformat()))

yesterday = someDate - oneDay
print("-1 day: {}".format(yesterday.isoformat()))

from datetime import time
someTime = time(23, 12, 31)
print("{}".format(someTime.isoformat()))

from datetime import datetime
some = datetime.combine(someDate, someTime)
print("Some datetime {}".format(some.isoformat()))