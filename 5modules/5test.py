import sys
print("Arguments: ", sys.argv)

# Here is places where python looks for modules
for place in sys.path:
    print("-", place)

# Python packages
from sources import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:", weekly.forecast())