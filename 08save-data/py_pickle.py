class Tiny():
    def __str__(self):
        return "Tiny"

tiny1 = Tiny()
print("tiny1 object: {}".format(str(tiny1)), end="\n\n")

# serialize/deserialize python object
import pickle
pickled = pickle.dumps(tiny1)
tiny2 = pickle.loads(pickled)
print("tiny2 object: {}".format(str(tiny2)))
