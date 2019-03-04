import sys
print("Arguments: ", sys.argv)

# Here is places where python looks for modules
for place in sys.path:
    print("-", place)