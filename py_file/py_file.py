#! /usr/bin/python3

import os
import glob
import shutil
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def line_func(line_type): return log.debug("{:=^50s}".format(line_type))

w_poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

try:
    fout = open("relativity", "wt")
except OSError as e:
    print("Unable to open file {} for writing".format(e))

line_func("write via file object")
print("{} bytes were written".format(fout.write(w_poem)))

line_func("write via print function")
print(w_poem, sep="", end="", file=fout, flush=True)
fout.close()

line_func("read chunk")
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

line_func("read lines")
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

line_func("read with iterator")
it_poem = ""
fread3 = open("relativity", "rt")
for line in fread3:
    it_poem += line

fread3.close()
print("{} bytes have been read".format(len(l_poem)), end="\n\n")

line_func("context manager")
ls_poem = ""
with open("relativity", "rt") as fread4:
    lines = fread4.readlines()

print("{} lines have been read".format(len(lines)), end="\n\n")
for line in lines:
    print(line, end="")

files = os.listdir(os.curdir)
for f in files:
    if os.path.isfile(f) and os.path.splitext(f)[1] == ".txt":
        print("\tFile {} is being removed".format(f))
        os.remove(f)

line_func("files")
fpath = "./oops.txt"
fout = open(fpath, "wt")
print("Oops, I created a file.", file=fout)
fout.close()

line_func("file type")
print("File {} has been created: {}".format(fpath, os.path.exists(fpath)))
print("{} has file type: {}".format(fpath, os.path.isfile(fpath)))
print("{} has dir type: {}".format(fpath, os.path.isdir(fpath)))
print("{} has link type: {}".format(fpath, os.path.islink(fpath)))

line_func("copy, rename, hardlink")
fcopy = "./ohno.txt"
print("Origin {} was copied into {}".format(fpath, shutil.copy(fpath, fcopy)))
os.replace(fcopy, "./ooops.txt")

fhardlink = "./hardlink.txt"
os.link(fpath, fhardlink)
print("Hard link was created: {}".format(os.path.isfile(fhardlink)))

line_func("directories")
dirlist = glob.glob("./*")
for dl in dirlist:
    print("\tFile found in current dir{}".format(dl))