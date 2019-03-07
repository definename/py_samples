import unicodedata

def unicode_test(origin):
    try:
        name = unicodedata.name(origin)
        found = unicodedata.lookup(name)
        print("\nName:", name, "\nOrigin:", origin, "\nFound:", found)
    except Exception as e:
        print("Unicode test failed:", e)

unicode_test("A")
unicode_test("\u20ac")
unicode_test("\u2603")

unicode_test("\u00e9")
place_via_code = "caf\u00e9"
print("place via code:", place_via_code)

place_via_name = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
print("place via name:", place_via_name)

print(len("1"))
print(len("\u00e9"))