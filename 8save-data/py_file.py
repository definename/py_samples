w_poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

try:
    fout = open("relativity", "wt")
except OSError as e:
    print("Unable to open file {} for writing".format(e))

# write via file object
print("{} bytes were written".format(fout.write(w_poem)))

# write via print function
print(w_poem, sep="", end="", file=fout, flush=True)

fout.close()

# read chunk
r_poem = ""
fread1 = open("relativity", "rt")
chunk = 100
while True:
    fragment = fread1.read(chunk)
    if not fragment:
        break
    r_poem += fragment

fread1.close()
print("{} bytes have been read".format(len(r_poem)), end="\n\n")

# read lines
l_poem = ""
fread2 = open("relativity", "rt")
line = 100
while True:
    line = fread2.readline()
    if not line:
        break
    l_poem += line

fread2.close()
print("{} bytes have been read".format(len(l_poem)), end="\n\n")

# read with iterator
it_poem = ""
fread3 = open("relativity", "rt")
for line in fread3:
    it_poem += line

fread3.close()
print("{} bytes have been read".format(len(l_poem)), end="\n\n")

# read with lines, this method closes file automaticaly.
ls_poem = ""
with open("relativity", "rt") as fread4:
    lines = fread4.readlines()

print("{} lines have been read".format(len(lines)), end="\n\n")
for line in lines:
    print(line, end="")
