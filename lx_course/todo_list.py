import datetime
import pickle

todoList = {}

def validateDate(func):
    def wrapper(date, *args):
        try:
            datetime.datetime.strptime(date, r"%d.%m.%y")
        except ValueError:
            raise ValueError("Incorrect date")
        return func(date, *args)
    return wrapper

def add():
    dt = input("\tEnter date in format 01.01.99: ")
    desc = input("\tEnter task description: ")
    addTask(dt, desc)

@validateDate
def addTask(dt, desc):
    try:
        if dt in todoList:
            todoList[dt].append(desc)
        else:
            todoList[dt] = [desc]
    except ValueError as e:
        print("Unable to add task: {}".format(e))
    else:
        print("Task has been successfully added to the task list")

def enum():
    dt = input("\tEnter date in format 01.01.99: ")
    enumTasks(dt)

@validateDate
def enumTasks(dt):
    try:
        if dt in todoList:
            print("\tDate: {}\n\tTask list: {}".format(dt, todoList[dt]))
        else:
            print("Timestamp: {} was not found".format(dt))
    except ValueError as e:
        print("Unable to enumerate tasks: {}".format(e))
    else:
        print("Task list has been successfully enumerated")

def saveList():
    try:
        fout = open("todoList.dat", "wb")
        pickle.dump(todoList, fout)
    except OSError as e:
        print("Unbale to save: {}".format(e))
    else:
        print("Task list has been successfully saved")


def loadList():
    try:
        fin = open("todoList.dat", "rb")
        todoList.update(pickle.load(fin))
    except OSError as e:
        print("Unable to open database: {}".format(e))
    else:
        print("Task list has been successfully loaded")

desc = """Usage:
'a' - add task to list,
'e' - enumerate task,
'x' - to exit.
"""

loadList()

while True:
    v = input(desc)

    if v == 'a':
        add()
    elif v == 'e':
        enum()
    elif v == 'x':
        break
    else:
        continue

saveList()