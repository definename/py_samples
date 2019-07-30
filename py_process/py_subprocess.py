#! /usr/bin/python3.6

import subprocess

ret = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
print("Exit code: {}".format(ret.returncode))
