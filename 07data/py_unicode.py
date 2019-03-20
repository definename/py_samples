import unicodedata

# unicode
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

# encode/decode
origin_str = "\u2603"
print("origin:", origin_str, type(origin_str), len(origin_str))
encoded_bytes = origin_str.encode("utf-8")
print("encoded:", encoded_bytes, type(encoded_bytes), len(encoded_bytes))

decoded_str = encoded_bytes.decode("utf-8")
print("decoded:", decoded_str, type(decoded_str), len(decoded_str))
