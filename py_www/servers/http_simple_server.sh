#!/bin/sh

python3 -u -m http.server | tee log
# python3 -u -m http.server |& tee httpserver.log