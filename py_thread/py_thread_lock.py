import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()
do_exit = False


def do(mutex):
    t = threading.current_thread()
    while True:
        time.sleep(0.5)
        with mutex:
            if do_exit == True:
                print("{} is being stopped...".format(t.name))
                break

            print("{}".format(t.name))


def main():
    global do_exit
    try:
        mutex = threading.Lock()
        thread_list = []
        for i in range(5):
            t = threading.Thread(target=do, name="thread" + str(i), args=(mutex, ))
            t.start()
            thread_list.append(t)

        while threading.active_count() > 0:
            for t in thread_list:
                t.join(timeout=0.5)

    except KeyboardInterrupt:
        log.debug("Program is being stopped...")
        with mutex:
            do_exit = True
    except Exception as e:
        log.error("Error occurrend: {}".format(e))


if __name__ == "__main__":
    main()
