import threading
import queue
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

is_running = True
dish_queue = queue.Queue()

def washer(dishes, dish_queue):
    for dish in dishes:
        time.sleep(0.5)
        dish_queue.put(dish)

        if dish is None:
            log.debug("Washer done...")
        else:
            log.debug(f"Wash:{dish}")


def dryer():
    try:
        while is_running:
            try:
                dish = dish_queue.get(timeout=1)
                dish_queue.task_done()
                if dish is None:
                    break
                log.debug(f"Dry dish:{dish} is running:{is_running}")
            except queue.Empty:
                log.warning("Dryer queue is empty...")
        log.debug("Dryer done...")
    except Exception as e:
        log.error(f"Dryer error:{e}")


def main():
    try:

        thread = threading.Thread(target=dryer)
        thread.start()

        washer(["salad", "bread", "entee", "desert", None], dish_queue)

        dish_queue.join()
        log.debug("Queue joined...")
        thread.join()
        log.debug("Thread joined...")
    except KeyboardInterrupt:
        log.debug("Keyboard interrupted...")
        global is_running
        is_running = False

        dish_queue.join()
        log.debug("Queue joined...")
        thread.join()
        log.debug("Thread joined...")
    except Exception as e:
        log.error(f"Error occurred:{e}")

if __name__ == "__main__":
    main()
