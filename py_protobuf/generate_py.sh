#!/bin/sh

NUMBER_OF_EXPECTED_ARGS=1
if [ $# -eq $NUMBER_OF_EXPECTED_ARGS ]; then
    echo "[*] About to run py protobuf generator"
    find $1 -name '*.proto' -type f -print -exec protoc --proto_path=$1 --python_out=$1 '{}' \;
else
    echo "[*] Usage: $0 <directory_with_protofiles>"
fi