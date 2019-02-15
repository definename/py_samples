things = ["mozzarella", "cinderella", "cinderella"]
print(things[1].capitalize())

things[1] = things[1].upper()
print(things[1])

del things[2]
print(things)

surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
print(surprise[-1])
surprise[-1] = surprise[-1].capitalize()
print(surprise[-1])

e2f = {
	"dog": "chien",
	"cat": "chat",
	"walrus": "morse"
	}
print("e2f dictionary:", e2f)
print("French version of 'walrus':", e2f["walrus"])

f2e = dict()
for eng, fr in e2f.items():
	f2e[fr] = eng
print("f2e dictionary:", f2e)
print("English version of 'chien':", f2e["chien"])

eset = set(e2f.keys())
print("Set of english words:", eset)