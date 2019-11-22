#!/usr/bin/python3
import logging
import urllib.request as ur

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="{asctime} {name} {levelname} - {message}", style="{")

# url = "http://google.com"
# url = "http://172.30.227.84:8000"
# url = "http://172.30.227.84:8000/scripts/Config_0"
url = "http://127.0.0.1:8001"
conn = ur.urlopen(url)

log.debug(f"Status code:{conn.status}")
for key, value in conn.getheaders():
    log.debug(f"{key}:{value}")