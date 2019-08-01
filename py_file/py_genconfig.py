#! /usr/bin/python3.6

import logging
import configparser

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def io_decorator(func):
    def inner(*args, **kwargs):
        log.debug(f"Generate config with: {func.__name__}")
        func(*args, **kwargs)
    return inner

@io_decorator
def generate_config1(filename):
    with open(file=filename + "1.cfg", mode="wt") as ofile:
        ofile.write("[rmcp]\n")
        ofile.write("resend = 5\n")
        ofile.write("request_timeout = 5\n")
        ofile.write("identify_timeout = 1\n")
        ofile.write("is_heartbeat = True\n")
        ofile.write("heatbeat_timeout = 1\n")

        ofile.write("\n[uart]\n")
        ofile.write("port = ~/serial2\n")

@io_decorator
def generate_config2(filename):
    config = configparser.ConfigParser()
    config["rmcp"] =  { "resend": 5,
                        "request_timeout": 5,
                        "identify_timeout": 1,
                        "is_heartbeat": True,
                        "heatbeat_timeout": 1 }
    config["uart"] = { "port": "~/serial2" }
    with open(file=filename + "2.cfg", mode="wt") as ofile:
        config.write(ofile)


def main():
    filename = "config"
    generate_config1(filename)
    generate_config2(filename)

if __name__ == "__main__":
    main()
