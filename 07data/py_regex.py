import re

# match at the beginning of the string.
source = "Young Frankenstein"
mo1 = re.match("You", source)
if mo1:
    print(mo1.group())

mo2 = re.match("^You", source)
if mo2:
    print(mo2.group())

# find first matching in any position of the given source
mo3 = re.search("Frank", source)
if mo3: print(mo3.group())

# find all occurence of given symbol
mo4 = re.findall("n", source)
if mo4: print("Found {} matches".format(len(mo4)))

mo5 = re.findall("n.", source)
if mo5: print(mo5)

mo6 = re.findall("n.?", source)
if mo6: print(mo6)

# split given source string according to the given pattern
mo7 = re.split("n", source)
if mo7: print(mo7)

# replace matches
mo8 = re.sub("n", "!", source)
if mo8: print(mo8)