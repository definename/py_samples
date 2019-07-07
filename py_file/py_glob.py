#! /usr/bin/python3

import glob
dirlist = glob.glob("./*")
for dl in dirlist:
    print("\tFile found in current dir{}".format(dl))