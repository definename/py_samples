import calendar
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

log.debug("is leap: {}".format(calendar.isleap(1987)))
log.debug("is leap: {}".format(calendar.isleap(2020)))

# date
from datetime import date

someDate = date.today()
log.debug("Some date: {}".format(someDate.isoformat()))

# timedelta
from datetime import timedelta

oneDay = timedelta(days=1)
tomorrow = someDate + oneDay
log.debug("+1 day: {}".format(tomorrow.isoformat()))

yesterday = someDate - oneDay
log.debug("-1 day: {}".format(yesterday.isoformat()))

# time
from datetime import time
someTime = time(23, 12, 31)
log.debug("{}".format(someTime.isoformat()))

from datetime import datetime
some = datetime.combine(someDate, someTime)
log.debug("Some datetime {}".format(some.isoformat()))

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

log.debug("\tWritten: {}".format(today_string))

# parse isoformat
dt = datetime.fromisoformat(today_string)
log.debug("\tParsed: {}".format(dt.isoformat()))

# bday week day
bday = date(1987, 12, 24)
log.debug("Week day: {}".format(bday.weekday()))

# 10 000 day from bday
log.debug("10 000 day was born: {}".format(bday + timedelta(days=10000)))

log.debug("=== parse datetime string")

yymd_raw = "201733"
try:
    yymd_date = datetime.strptime(yymd_raw, r"%Y%m%d")
    log.info("yy({}) m({}) d({})".format(yymd_date.year, yymd_date.month, yymd_date.day))
except ValueError as e:
    log.error("Failed to parse date: {}".format(e))

log.debug("=== parse time string")

tm_raw = "163710"
try:
    tm_date = datetime.strptime(tm_raw, r"%H%M%S")
    log.info("h({}) m({}) s({})".format(tm_date.hour, tm_date.minute, tm_date.second))
except ValueError as e:
    log.error("Failed to parse date: {}".format(e))