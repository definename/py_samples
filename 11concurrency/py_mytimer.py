import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class MyTimer(threading.Thread):
    def __init__(self, timeout, callback, args=None, kwargs=None):
        super().__init__()
        self.__is_running = True
        self.__timeout = timeout
        self.__cv =  threading.Condition()
        self.__callback = callback
        self.__args = args if args is not None else []
        self.__kwargs = kwargs if kwargs is not None else {}

    def run(self):
        while self.__is_running:
            with self.__cv:
                if self.__cv.wait(self.__timeout) and not self.__is_running:
                    break
            self.__callback(*self.__args, **self.__kwargs)

    def stop(self):
        self.__is_running = False
        with self.__cv:
            self.__cv.notify_all()

def do(one, two):
    log.debug(f"Done!!! {one} {two}")

def main():
    try:
        param1 = 1
        param2 = 2
        timer = MyTimer(timeout=1.0, callback=do, args=(param1, param2))
        timer.start()

        run = True
        while run:
            time.sleep(1)

    except KeyboardInterrupt:
        timer.stop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.error(f"{e}", exc_info=True)