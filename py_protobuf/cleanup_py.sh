#!/bin/sh

echo "[*] About to cleanup py protobuf generated files"
find . -name '*_pb2.py' -type f -print -exec rm '{}' \;