import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

cv =  threading.Condition()
done_list = {}

def do(done_id):
    log.debug("Do... {}".format(done_id))
    with cv:
        while done_list[done_id] != True:
            cv.wait()
        log.debug("Done... {}".format(done_id))

def main():
    t_list = []
    for index in range(2):
        done_list[index] = False
        t = threading.Thread(target=do, args=(index,))
        t.start()
        t_list.append(t)
        time.sleep(1)
    
    while True:
        time.sleep(0.5)

    # for t in t_list:
    #     t.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.debug("Stop...")
        with cv:
            for key in done_list.keys():
                done_list[key] = True
                cv.notify_all()

    except Exception as e:
        log.error("Error occurred: {}".format(e))
