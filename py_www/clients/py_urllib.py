#!/usr/bin/python3

import urllib.request as ur
# url = "http://google.com"
# url = "http://172.30.227.84:8000"
url = "http://172.30.227.84:8000/scripts/Config_0"
conn = ur.urlopen(url)

print("Status code: {}".format(conn.status), end="\n\n")
for key, value in conn.getheaders():
    print(key, value)