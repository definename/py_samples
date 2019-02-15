empty_dict = {}
print(empty_dict)

dictOrigin = {
    "seconds": "1",
    "minutes": "2",
    "hour": "3",
    "day": "4",
    "month": "5",
    "year": "5"
}
print(dictOrigin)

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

dictOrigin["year"] = 2019
print(dictOrigin)

others = {
    "century": "6",
    "millennium": "7",
    "month":"February"
}

dictOrigin.update(others)
print("Update:", dictOrigin)

del dictOrigin["seconds"]
print("Delete element:", dictOrigin)

print("Checks whether 'seconds' key was deleted from collection:", "seconds" in dictOrigin)

print("Current month:", dictOrigin.get("month", "January"))

print(dictOrigin.keys())
print(dictOrigin.values())
print(dictOrigin.items())

dictCopy = dictOrigin.copy()
dictCopy["minutes"] = "47"
dictCopy["hours"] = "17"
print("Origin:", dictOrigin)
print("Copy:", dictCopy)
