import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

# particular range usage
log.debug(sum(range(1, 10)))

# custom range generator
def my_range_gen(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

my_range_it = my_range_gen()
my_value_list = [my_value for my_value in my_range_it]
log.debug(my_value_list)
my_value_list = [my_value for my_value in my_range_gen()]
log.debug(my_value_list)
log.debug(list(my_range_gen()))