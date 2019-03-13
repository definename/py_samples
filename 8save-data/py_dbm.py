import dbm
db = dbm.open("definitions", "c")

db["mustard"] = "yellow"
db["ketchup"] = "red"
db["pesto"] = "green"

len(db)

print("pesto key: {}".format(db["pesto"]))