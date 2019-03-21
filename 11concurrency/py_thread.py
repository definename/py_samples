import threading, queue
import time

def washer(dishes, dish_queue):
    for dish in dishes:
        time.sleep(1)
        dish_queue.put(dish)

        if dish == "exit":
            print("\tWasher done...")
        else:
            print("Wash: {}".format(dish))

def dryer(dish_queue):
    while True:
        time.sleep(2)
        dish = dish_queue.get()

        if dish == "exit":
            print("\tDryer done...")
            dish_queue.task_done()
            break

        print("Dry: {}".format(dish))
        dish_queue.task_done()

# entry point
dish_queue = queue.Queue()
for n in range(1):
    thread = threading.Thread(target=dryer, args=(dish_queue,))
    thread.start()

washer(["salad", "bread", "entee", "desert", "exit"], dish_queue)
dish_queue.join()

print("Done...")

