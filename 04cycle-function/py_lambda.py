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

ls1.sort(key = lambda x: x[1])
print("x[1]: {}".format(ls1))