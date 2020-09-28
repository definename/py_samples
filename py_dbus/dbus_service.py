#! /usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib

class SomeObject(dbus.service.Object):

    @dbus.service.method("com.example.SampleInterface",
                         in_signature='s',
                         out_signature='as')
    def HelloWorld(self, hello_message):
        log.debug(hello_message)
        return ["Hello",
                "from dbus service",
                "with unique name",
                name.get_bus().get_unique_name()]


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    name = dbus.service.BusName("com.example.SampleService", dbus.SessionBus())
    log.debug(name.get_name())
    object = SomeObject(name.get_bus(), '/SomeObject')

    mainloop = GLib.MainLoop()
    log.debug("Running example service")
    mainloop.run()
