import datetime

todoList = {}

while True:
    v = input("type: 'a' - add task to list, 'l' - list task, 'x' - to exit: ")

    if v == 'a':
        dt = datetime.datetime.strptime(input("-- enter date in format 01.01.99: "), r"%d.%m.%y").date()
        task = input("-- enter task description: ")
        if dt in todoList:
            todoList[dt].append(task)
        else:
            todoList[dt] = [task]
    elif v == 'l':
        dt = datetime.datetime.strptime(input("-- enter date in format 01.01.99: "), r"%d.%m.%y").date()
        if dt in todoList:
            print("-- date: {}\n-- task list: {}".format(dt, todoList[dt]))
    elif v == 'x':
        break
    else:
        continue