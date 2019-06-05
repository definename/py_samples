import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


stop = False

def handler():
    global stop
    log.debug("Do...")
    stop = True

tm = threading.Timer(interval=1.0, function=handler)

def main():
    try:
        tm.start()

        while stop == False:
            time.sleep(0.5)

        tm.join()

    except KeyboardInterrupt as e:
        pass
    except Exception as e:
        log.error("Error occurred: {}".format(e))


if __name__ == "__main__":
    main()
