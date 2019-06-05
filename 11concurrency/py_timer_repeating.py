import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class RepeatingTimer():
    def __init__(self, interval, callback, repeat=-1, args=None, kwargs=None):
        super().__init__()
        self.__timer = None
        self.__interval = interval
        self.__callback = callback
        self.__args = args if args is not None else []
        self.__kwargs = kwargs if kwargs is not None else {}
        self.__repeat = repeat

    def function(self, *args, **kwargs):
        self.__callback(*args, **kwargs)

        if self.__repeat < 0:
            self.start()
        if self.__repeat > 0:
            self.__repeat -= 1
            self.start()

    def start(self):
        self.__timer = threading.Timer(
            interval=self.__interval,
            function=self.function,
            args=self.__args,
            kwargs=self.__kwargs)

        self.__timer.start()

    def join(self):
        self.__timer.join()

    def cancel(self):
        self.__timer.cancel()

def timeout_handler(param1, param2):
    log.debug("Expired!!! {} {}".format(param1, param2))

def main():
    try:
        log.debug("Timer has been started")
        tm = RepeatingTimer(interval=1, callback=timeout_handler, args=(123, 321))
        tm.start()

        while True:
            time.sleep(0.5)

    except KeyboardInterrupt as e:
        pass
    except Exception as e:
        log.error("Error occurred: {}".format(e))

    tm.cancel()


if __name__ == "__main__":
    main()
