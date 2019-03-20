import unicodedata

# 1

mystery = "\U0001f4a9"
print(mystery)

try:
    print("unicode name is: {}".format(unicodedata.name(mystery)))
except ValueError as e:
    print("Failed to lookup unicode name for {}, error occurred: {}, ".format(mystery, e))

# 2

pop_bytes = mystery.encode("utf-8")
print(f"pop_bytes: {pop_bytes}")

# 3
pop_string = pop_bytes.decode("utf-8")
print(f"pop_string: {pop_string}")

# 4

old = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.""" % ("roast beef", "ham", "head", "clam")
print(old)

# 5

letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

print(letter, end="\n\n")

# 6
response = {
    "salutation": "Colonel",
    "name": "Hackenbush",
    "product": "duck blind",
    "verbed": "imploded",
    "room": "conservatory",
    "animals": "emus",
    "amount": "$1.38",
    "percent": "1",
    "spokesman": "Edgar Schmeltz",
    "job_title": "Licensed Podiatrist" }

print(letter.format(**response), end="\n\n")

# 7
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon."""

print(mammoth, end="\n\n")

# 8
import re
print("All words which starts from 'c': {}".format(re.findall(r"\bc\w*", mammoth)), end="\n\n")

# 9
print("All (4 letter) words which starts from 'c': {}".format(re.findall(r"\bc\w{3}\b", mammoth)), end="\n\n")

# 10
print("All words which ends with 'r': {}".format(re.findall(r"\b[\w\']*r\b", mammoth)), end="\n\n")

