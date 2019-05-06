import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class RepeatingTimer():
    def __init__(self, interval, callback, *args, **kwargs):
        super().__init__()
        self.__timer = None
        self.__interval = interval
        self.__callback = callback
        self.__args = args
        self.__kwargs = kwargs

    def callback(self):
        self.__callback(*self.__args, **self.__kwargs)
        self.start()

    def start(self):
        self.__timer = threading.Timer(self.__interval, self.callback)
        self.__timer.start()

    def join(self):
        self.__timer.join()

    def cancel(self):
        self.__timer.cancel()


def timeout_handler():
    log.debug("Expired!!!")


def main():
    try:
        tm = RepeatingTimer(1, timeout_handler)
        log.debug("Timer has been started")
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
