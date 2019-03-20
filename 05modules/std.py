table = {
    "Hidrogen": 1,
    "Helium": 2
}

print(table)
table.setdefault("Carbon", 12)
print(table)


# collections module, test defaultdict
def no_idea():
    return 99

from collections import defaultdict as dd
# def_table = dd(int)
# def_table = dd(no_idea)
def_table = dd(lambda: "Huh?")

def_table["Hidrogen"] = 1
def_table["Helium"]
print(def_table)

# collections module, test counter
from collections import Counter
breakfast = ["spam", "spam", "eggs", "spam"]
breakfast_count = Counter(breakfast)
print(breakfast_count)

lunch = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch)
print(lunch_counter)

print("+", breakfast_count + lunch_counter)
print("-", breakfast_count - lunch_counter)

# collections module, test ordereddict
quotes = {
    'Curly': 'Nyuk nyuk!',
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
}
for q in quotes:
    print("dict", q)

from collections import OrderedDict
order_quotes = OrderedDict(quotes)
order_quotes.move_to_end("Curly")

for oq in order_quotes:
    print("order", oq)

# collections module, test deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome("ab1ba"))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome("radar"))

# itertools module

from itertools import accumulate as ac

multiply = lambda a, b : a * b
for item in ac([1, 2, 3, 4], multiply):
    print(item, end=" ")
print()

# pprint module

import pprint

pp = pprint.PrettyPrinter(1, 30)
pp.pprint(quotes)