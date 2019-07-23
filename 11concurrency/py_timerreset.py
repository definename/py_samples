import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class Timer(threading.Thread):
    def __init__(self, timeout, callback, args=None, kwargs=None):
        super().__init__()
        self.__is_running = True
        self.__timeout = timeout
        self.__trigger = threading.Event()
        self.__callback = callback
        self.__args = args if args is not None else []
        self.__kwargs = kwargs if kwargs is not None else {}

    def run(self):
        try:
            while self.is_running:
                self.__trigger.clear()
                log.debug(f"Timeout: {self.timeout}")
                if self.__trigger.wait(self.timeout):
                    continue
                self.__kwargs["timer"] = self
                self.__callback(*self.__args, **self.__kwargs)
        except Exception as e:
            log.debug(f"Timer error: {e}", exc_info=True)

    @property
    def is_set(self):
        return self.__trigger.is_set()

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, is_running):
        self.__is_running = is_running

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout):
        self.__timeout = timeout

    def stop(self):
        self.is_running = False
        self.__trigger.set()

    def reset(self, timeout):
        self.timeout = timeout
        self.__trigger.set()

def do(timer):
    log.debug("Done!!!")
    # timer.timeout = None

def main():
    try:
        timer = Timer(timeout=None, callback=do)
        timer.start()

        while True:
            time.sleep(2)
            timer.reset(timeout=1)
    except KeyboardInterrupt:
        log.debug("Keyboard interrupted")
        timer.stop()
    except Exception as e:
        log.error(f"{e}", exc_info=True)


if __name__ == "__main__":
    main()