import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

cv =  threading.Condition()
done = False

def do():
    cv.acquire()
    log.debug("Do...")
    while done != True:
        cv.wait()
    log.debug("Done...")
    cv.release()

def main():
    do()
    do()


if __name__ == "__main__":
    main()
