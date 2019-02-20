origin_set = set([1, 2, 3, 4])
print(origin_set)

origin_set1 = {'a', 'b', 'c', 'd', 'e'}
print(origin_set1)

origin_set2 = set({
	'apple': 'red',
	'orange': 'orange',
	'cherry': 'red'})
print(origin_set2)

drinks = {
	'martini': {'vodka', 'vermouth'},
	'black russian': {'vodka', 'kahlua'},
	'white russian': {'cream', 'kahlua', 'vodka'},
	'manhattan': {'rye', 'vermouth', 'bitters'},
	'screwdriver': {'orange juice', 'vodka'}
	}
print(drinks)

drinkVodka = []
for name, contents in drinks.items():
	if "vodka" in contents:
		drinkVodka.append(name)

print("Drink vodka:", drinkVodka)

drinkNoVodka = []
for name, contents in drinks.items():
	if "vodka" not in contents:
		drinkNoVodka.append(name)

print("Drink no vodka:", drinkNoVodka)

a = {1, 2}
b = {2, 3}

print("Intersection:", a & b)
print("Union:", a | b)
print("Difference:", a - b)
print("Or:", a ^ b)
print("Subset:", a <= b, a <= a)
