#! /usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

empty_dict = {}
log.debug(empty_dict)

dict_origin = {
    "seconds": "1",
    "minutes": "2",
    "hour": "3",
    "day": "4",
    "month": "5",
    "year": "5"
}
print(dict_origin)

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

dict_origin["year"] = 2019
print(dict_origin)

others = {
    "century": "6",
    "millennium": "7",
    "month":"February"
}

dict_origin.update(others)
print("Update:", dict_origin)

del dict_origin["seconds"]
print("Delete element:", dict_origin)

print("Checks whether 'seconds' key was deleted from collection:", "seconds" in dict_origin)

print("Current month:", dict_origin.get("month", "January"))

print(dict_origin.keys())
print(dict_origin.values())
print(dict_origin.items(), end="\n\n")

dictCopy = dict_origin.copy()
dictCopy["minutes"] = "47"
dictCopy["hours"] = "17"
print("Origin:", dict_origin)
print("Copy:", dictCopy, end="\n\n")

def iteration():
    test_dict = dict(a=1, c=3, b=2)
    for k in test_dict:
        log.debug(f"key: {k} {test_dict[k]}")

    for k in sorted(test_dict):
        log.debug(f"sorted key: {k} {test_dict[k]}")

def main():
    iteration()

if __name__ == "__main__":
    main()