import locale
from datetime import date

bday = date(1987, 12, 24)

locale.setlocale(locale.LC_TIME,"uk-UA")
fout = open("locale.txt", "wt")
redable = bday.strftime("%A %B %d")
fout.write(redable)

# todo: test printing on console