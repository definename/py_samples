#!/bin/sh

python3 -u -m http.server |&tee ./httpserver.log