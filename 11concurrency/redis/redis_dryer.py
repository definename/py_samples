import redis
import os
import time
import multiprocessing

conn = redis.Redis()

# pop dishes from the redis.
def dryer():
    pid = os.getpid()
    print("Dryer process: {} is being started...".format(pid))

    while True:
        msg = conn.blpop("dishes", 20)

        if not msg:
            print("No msg")
            break

        val = msg[1].decode("utf-8")

        if val == "quit":
            print("Dryer {} is done".format(pid))
            break

        print("Dryer pid {} dried: {}".format(pid, val))
        time.sleep(0.1)

def main():
    for index in range(3):
        p = multiprocessing.Process(target=dryer)
        p.start()

if __name__ == "__main__":
    main()