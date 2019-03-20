import multiprocessing
import os
import time

def do_this(what):
    while True:
        print("Process: {} says: {}".format(os.getpid(), what))
        time.sleep(1)

if __name__ == "__main__":
    processList = []
    for i in range(2):
        p = multiprocessing.Process(
            target=do_this,
            args=("I'm function {}".format(i),),
            name="NAME{}".format(i))
        processList.append(p)

    for p in processList:
        print("\tProcess: {} is being started".format(p.name))
        p.start()

    time.sleep(5)

    for p in processList:
        print("\tProcess: {} is being terminated".format(p.name))
        p.terminate()