import threading
import queue
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


def washer(dishes, dish_queue):
    for dish in dishes:
        time.sleep(1)
        dish_queue.put(dish)

        if dish == "exit":
            log.debug("Washer done...")
        else:
            log.debug("Wash: {}".format(dish))


def dryer(dish_queue):
    while True:
        time.sleep(2)
        dish = dish_queue.get()

        if dish == "exit":
            log.debug("Dryer done...")
            dish_queue.task_done()
            break

        log.debug("Dry: {}".format(dish))
        dish_queue.task_done()


def main():
    dish_queue = queue.Queue()
    thread = threading.Thread(target=dryer, args=(dish_queue,))
    thread.start()

    washer(["salad", "bread", "entee", "desert", "exit"], dish_queue)
    dish_queue.join()

    log.debug("Done...")


if __name__ == "__main__":
    main()
