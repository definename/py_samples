import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

empty_dict = {}
print(empty_dict)

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
    test = dict(aa=1, bb=2)
    for k in test:
        log.debug(f"key11: {k} value: {test[k]}")

    for k, v in test.items():
        log.debug(f"key22: {k} value: {v}")

def main():
    iteration()

if __name__ == "__main__":
    main()