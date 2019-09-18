import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

mutex = threading.RLock()


def do_lock2():
    with mutex:
        log.debug(do_lock2.__name__)


def do_lock1():
    with mutex:
        log.debug(do_lock1.__name__)
        do_lock2()


def main():
    do_lock1()


if __name__ == "__main__":
    main()
