import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class SeqNum():
    __seq_num = None
    __mutex = threading.Lock()

    @classmethod
    def get(cls):
        with cls.__mutex:
            if cls.__seq_num is None:
                cls.__seq_num = 1
            else:
                cls.__seq_num += 1

            time.sleep(2)
            return cls.__seq_num


def do_handle():
    log.debug(SeqNum.get())


def main():
    try:
        thread_list = []
        for index in range(2):
            t = threading.Thread(target=do_handle, name="thread" + str(index))
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join(timeout=0.5)

    except KeyboardInterrupt as e:
        pass
    except Exception as e:
        log.error("Error occurrend: {}".format(e))


if __name__ == "__main__":
    main()
