#!/usr/bin/python3

import requests
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="{asctime} {name} {levelname} - {message}", style="{")

# url = "http://google.com"
# url = "http://172.30.227.84:8000/scritps/Config_0"
url = "http://127.0.0.1:8001"
resp = requests.get(url)

log.debug(f"Status code:{resp.status_code}")
log.debug(f"Reason:{resp.reason}")

for key, value in resp.headers.items():
    log.info(f"Header:{key}:{value}")