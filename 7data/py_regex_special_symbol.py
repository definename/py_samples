# special symbols
import re
import string
print("{}".format(len(string.printable)))

print("Numbers only: {}".format(re.findall("\\d", string.printable)))
print("Letters, numbers and underscore only: {}".format(re.findall("\\w", string.printable)))