#! /usr/bin/python3

import pickle
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class Tiny():
    def __str__(self):
        return "Tiny"

tiny1 = Tiny()
print("tiny1 object: {}".format(str(tiny1)), end="\n\n")

# Serialize/Deserialize python class object.
pickled = pickle.dumps(tiny1)
tiny2 = pickle.loads(pickled)
print("tiny2 object: {}".format(str(tiny2)))

# Pickle/Unpickle python dict.
fname = "pickled.dat"
with open(file=fname, mode="wb") as f:
    obj = dict(a=1, b=2, c=3)
    log.debug(f"dict object is being pickled {obj}")
    pickle.dump(obj=obj, file=f)

with open(file=fname, mode="rb") as f:
    obj = pickle.load(file=f)
    log.debug(f"dict object has been unpickled {obj}")

