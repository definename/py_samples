from collections import namedtuple

# One of the ways of namedtuple initialization
Duck = namedtuple("Duck", "bill tail")
duck = Duck("wide orange", "long")
print(duck)
print(duck.bill)
print(duck.tail)

# Another way to initialize namedtuple
Element = namedtuple("Element", "name, symbol, number")
data = { "name": "Hydrogen", "symbol": "H", "number": 1 }
hydrogen = Element(**data)
print(hydrogen)