# old style
print("Old style:")

print("%s %s" % ("Richard", "Gere"))

print("%20s %-20s" % ("Richard", "Gere"))

print("%20.1s. %-20s" % ("Richard", "Gere"))

print("%*.*s. %-*.*s" % (20, 1, "Richard", 20, 4, "Gere"))

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

try:
    print("{r:20s} {g:^20s} {n:^20.1d}".format(r="Richard", g="Gere", n=100))
except Exception as e:
    print("Fromatting error occurred: {}".format(e))

print("{0:=^100s}".format("BIG SALE"))

# string interpolation interpolation
name = "Oleh"
age = 21
print(f"Name: {name}, age: {age}")