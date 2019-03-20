import urllib.request as ur
url = "http://google.com"
conn = ur.urlopen(url)

print("Status code: {}".format(conn.status), end="\n\n")
for key, value in conn.getheaders():
    print(key, value)