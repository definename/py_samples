# function definition

def echo(anything):
    return anything + " " + anything

print(echo("quack"))

# None

def is_none(thing):
    if thing is None:
        print("It's nothing")
    elif thing:
        print("It's True")
    else:
        print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none({})

# function default value

def do_it(one, two, three=10):
    return {"one": one, "two": two, "three": three}

print(do_it(1, two=2))

# container as function argument

def buggy(arg, result=[]):
    result.append(arg)
    return result

print("Python buggy:", buggy("a"))
result = buggy("b")
result.append("c")
print("Python buggy:", buggy("d"))

def no_buggy(arg):
    result = []
    result.append(arg)
    return result

no_buggy("no-a")
no_buggy("no-b")
print("Python no buggy:", no_buggy("no-c"))

# positional args

def do_args(*args):
    print("Here is list of params passed to the function:", args)

do_args(1, 2, 3, 4, 5, 123, "sdfdfg")

# keyword args

def do_kwargs(**kwargs):
    print("Keyword args (aka dictionary):", kwargs)

do_kwargs(qwe1="asd", qwe2="sdf", qwe3="qwe")

# function description

def do_help(anything, check):
    '''
    Function description...
    1. This function accepts only one argument.
    2. Only ane argument is accepted by this function
    '''
    if check:
        print(anything)

do_help("any", True)
help(do_help)
print(do_help.__doc__)

# function as params

def do_add(*args):
    return sum(args)

def do_add_args(func, *args):
    return func(*args)

print("The sum is:", do_add_args(do_add, 1, 2, 3, 4, 5))

# inner function

def outer(say):
    def inner(text):
        return "Hey! %s" % text
    return inner(say + "!!!")

print(outer("MatherFucka"))

# closure

def talk(subject):
    def inner():
        print("We are talking on '%s'" % subject)
    return inner

a = talk("Subject1")
b = talk("Subject2")

print(type(a))
print(type(b))
a()
b()

# lambda
words = ["word1", "word2", "word3"]

def edit_story(to_edit, func):
    for word in to_edit:
        print(func(word))

edit_story(words, lambda word: word.capitalize() + "!")
