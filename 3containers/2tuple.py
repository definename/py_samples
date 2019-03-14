empy_tuple = ()
print(empy_tuple)

tuple1 = "one",
print(tuple1)

tuple2 = "one", "two"
print(tuple2)

tuple3 = ("1", "2", "3")
print(tuple3)

t1, t2, t3 = tuple3
print(t1, t2, t3, sep="-")

t1, t2 = t2, t1
print(t1, t2, t3, sep="-")

originList = ["list1", "list2", "list3"]
print("originList:", originList)
originTuple = (1, 2, 3, originList)
print("originTuple:", originTuple)

try:
    originTuple[0] = 999
except TypeError as e:
    print("Unbale to change tuple container: {}".format(e))

originTuple[3][0] = "changed"
print("But we can change list which was passed to the tuple: {}".format(originTuple))
