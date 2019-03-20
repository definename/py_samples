import requests
url = "http://google.com"
resp = requests.get(url)

print("Status code: {}".format(resp), end="\n\n")

for key, value in resp.headers.items():
    print(key, value)