# 1 write data to file
wtext = "This is a test of the emergency text system"

filename = "text.txt"
fwrite = open(filename, "wt")
fwrite.write(wtext)
fwrite.close()

# 2 read data from file and compare with origin
rtext = ""
fread = open(filename, "rt")
chunk = 100
while True:
    line = fread.read(chunk)
    if not line:
        fread.close()
        break
    rtext += line

print("Text is equal: {}".format(rtext == wtext))
