import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        output.put(dish)

        if (dish == "finish"):
            print("\tWasher done...")
        else:
            print("Wash: {}".format(dish))

def dryer(input):
    while True:
        dish = input.get()

        if (dish == "finish"):
            print("\tDryer done...")
            input.task_done()
            break

        print("Dry: {}".format(dish))
        input.task_done()

# entry point
if __name__ == "__main__":
    dish_queue = mp.JoinableQueue()
    proc = mp.Process(target=dryer, args=(dish_queue,))
    proc.deamon = True
    proc.start()

    washer(["salad", "bread", "entee", "dessert", "finish"], dish_queue)
    dish_queue.join()
