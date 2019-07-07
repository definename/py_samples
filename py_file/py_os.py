#! /usr/bin/python3

import os
import shutil

files = os.listdir(os.curdir)
for f in files:
    if os.path.isfile(f) and os.path.splitext(f)[1] == ".txt":
        print("\tFile {} is being removed".format(f))
        os.remove(f)

fpath = "./oops.txt"
fout = open(fpath, "wt")
print("Oops, I created a file.", file=fout)
fout.close()

print("File {} has been created: {}".format(fpath, os.path.exists(fpath)))
print("{} has file type: {}".format(fpath, os.path.isfile(fpath)))
print("{} has dir type: {}".format(fpath, os.path.isdir(fpath)))
print("{} has link type: {}".format(fpath, os.path.islink(fpath)))

fcopy = "./ohno.txt"
print("Origin {} was copied into {}".format(fpath, shutil.copy(fpath, fcopy)))
os.replace(fcopy, "./ooops.txt")

fhardlink = "./hardlink.txt"
os.link(fpath, fhardlink)
print("Hard link was created: {}".format(os.path.isfile(fhardlink)))