import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

# lambda
words = ["word1", "word2", "word3"]


def edit_story(to_edit, func):
    for word in to_edit:
        print(func(word))


edit_story(words, lambda word: word.capitalize() + "!")

ls = [1, 2, 3]
mo = map(lambda v: v * 2, ls)
print("Double values in list: {}".format(list(mo)))

# sort list of tuples with lambda
ls1 = [(1, 3), (3, 1), (2, 2)]
ls1.sort()
print("x[0] by default {}".format(ls1))

ls1.sort(key=lambda x: x[1])
print("x[1]: {}".format(ls1))

def init_action():
    action = []
    for i in range(3):
        action.append(lambda x, i=i: i ** x)
    return action

def main():
    # Namespace and default params in cycles
    action = init_action()
    for i in range(len(action)):
        log.debug(action[i](2))

if __name__ == "__main__":
    main()