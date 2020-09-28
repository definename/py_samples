#! /usr/bin/python3

import dbus
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    bus = dbus.SessionBus()
    try:
        remote_object = bus.get_object(
                        "com.example.SampleService",
                        "/SomeObject")
        reply_list = remote_object.HelloWorld(
                        "Hello from dbus client!",
                        dbus_interface="com.example.SampleInterface")

        for entry in reply_list:
            log.debug(entry)

    except dbus.DBusException:
        log.exception("dbus error occured")

if __name__ == "__main__":
    main()