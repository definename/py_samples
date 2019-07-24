import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

# old style
print("Old style:")

print("%s %s" % ("Richard", "Gere"))

print("%20s %-20s" % ("Richard", "Gere"))

print("%20.1s. %-20s" % ("Richard", "Gere"))

print("%*.*s. %-*.*s" % (20, 1, "Richard", 20, 4, "Gere"))
name = "SomeName"
surname = "SomeSurname"
log.debug("Name: %(name)s Surname: %(surname)s", {"name":"SomeName", "surname": "SomeSurname"})
log.debug("Name: %(name)s Surname: %(surname)s", vars())

# new style
print("New style:")

print("{} {}".format("Richard", "Gere"))
print("{1} {0}".format("Richard", "Gere"))

print("{r} {g}".format(r="Richard", g="Gere"))

d = { "r": "Richard", "g": "Gere" }
print("{0} {1[r]} {1[g]}".format("Author is", d))

print("{0:s} {1:s}".format("Richard", "Gere"))
print("{r:s} {g:s}".format(r="Richard", g="Gere"))
print("{r:20s} {g:20s}".format(r="Richard", g="Gere"))
print("{r:>20.1s}. {g:<20s}".format(r="Richard", g="Gere"))
print("{r:^20s} {g:^20s}".format(r="Richard", g="Gere"))

print("{one:^20.1s} {two:^20.2s} {three:^20.3s}".format(one="!!!maxstringlength", two="!!!maxstringlength", three="!!!maxstringlength"))

try:
    print("{r:20s} {g:^20s} {n:^20.1d}".format(r="Richard", g="Gere", n=100))
except Exception as e:
    print("Fromatting error occurred: {}".format(e))

print("{0:=^100s}".format("BIG SALE"))
log.debug("It runs {0.platform}, one: {config[one]}, two: {config[two]}".format(sys, config={"one":1, "two":2}))
for i in range(1, 4):
    log.debug("New dynamic precision: {0:.{1}f}".format(1/3.0, i))
    log.debug("Old dynamic precision: %.*f", i, 1 / 3.0)

# string interpolation
name = "Oleh"
age = 21
print(f"Name: {name}, age: {age}")

tuple_id = (1, 2, 3)
log.debug(f"tuple_id {tuple_id}")
log.debug(f"tuple_id {tuple_id[0]} {tuple_id[1]} {tuple_id[2]}")
log.debug("=" * 50)