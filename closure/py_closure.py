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

# change closure
def f(x):
    def g(y):
        return x * y
    def set_x(a):
        nonlocal x
        x = a
    g.set_x = set_x
    return g

g = f(2)
print(g(10))

g.set_x(4)
print(g(10))

