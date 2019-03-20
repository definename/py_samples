# particular range usage
print(sum(range(1, 10)))

# custom range function
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

r = list(my_range())
print(r)