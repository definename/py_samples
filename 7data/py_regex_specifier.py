import re

# specifier using
source ='''I wish I may, I wish I might
Have a dish of fish tonight thisfishisnotfound fishisnotfound thisfish.'''

print("{}".format(source))

print()
print("'wish' only: {}".format(re.findall("wish", source)))
print("'wish or fish': {}".format(re.findall("wish|fish", source)))

print()
print("'wish or fish': {}".format(re.findall("[wf]ish", source)))
print("collocation of 'wsh': {}".format(re.findall("[wsh]+", source)))

print()
print("'I' behind 'wish': {}".format(re.findall("I (?=wish)", source)))
print("'wish' in front of 'I': {}".format(re.findall("(?<=I) wish", source)))

print()
print("r'fish' -> {}".format(re.findall(r"fish", source)))
print("r'\\bfish' -> {}".format(re.findall(r"\bfish", source)))
print("r'\\bfish\\b' -> {}".format(re.findall(r"\bfish\b", source)))
print("r'fish\\b' -> {}".format(re.findall(r"fish\b", source)))

print()
mo1 = re.search(r"(. dish\b).*(\bfish\b)", source)
if mo1:
    print(mo1.group())
    print(mo1.groups())

print()
mo2 = re.search(r"(?P<DISHGROUP>. dish\b).*(?P<FISHGROUP>\bfish\b)", source)
if mo2:
    print(mo2.group())
    print(mo2.groups())
    print("DISHGROUP: {}".format(mo2.group("DISHGROUP")))
    print("FISHGROUP: {}".format(mo2.group("FISHGROUP")))

    mo2_dict = mo2.groupdict()
    print("dict DISHGROUP: {}".format(mo2_dict["DISHGROUP"]))
    print("dict FISHGROUP: {}".format(mo2_dict["FISHGROUP"]))

