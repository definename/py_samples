import multiprocessing
import os

def do_this(what):
    print("Process: {} says: {}".format(os.getpid(), what))

if __name__ == "__main__":
    for i in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function {}".format(i),))
        p.start()