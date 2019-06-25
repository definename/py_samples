import logging
import string
import struct
import random
import enum

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


# random.seed(a=3)

log.debug("{:=^100s}{}".format("hexdigits", string.hexdigits))
for index in range(3):
    log.debug(random.choices(string.hexdigits, k=2))


log.debug("{:=^100s}".format("getrandbits"))
for index in range(3):
    random_bits = random.getrandbits(16)
    log.debug("{:016b}".format(random_bits))
    log.debug("{}".format(hex(random_bits)))
    log.debug(format(random_bits, "x"))

log.debug("{:=^100s}{}".format("two digits with replacement", string.digits))
while True:
    pair = random.choices(string.digits, k=2)
    log.debug(f"{pair[0]} {pair[1]}")
    if pair[0] == pair[1]:
        break

log.debug("{:=^100s}".format("corruption probability"))
class Corruption_t(enum.Enum):
    INSERT = 1
    DELETE = 2
    XOR = 3
    COMBINE = 4
    NO_CORRUPTION = 5

class Insert_t(enum.Enum):
    BEFORE = 1
    AFTER = 2
    INSIDE = 3

def make_choice(insert=10, delete=10, xor=10, combine=10):
    no_corruption = 100 - (insert + delete + xor + combine)
    return random.choices(list(Corruption_t), [insert, delete, xor, combine, no_corruption], k=1)

def generate_choice(count):
    in_count = 0
    while in_count < count:
        yield make_choice()[0]
        in_count += 1

choice_gen = generate_choice(count=1000)
choice_res = {}
for choice in choice_gen:
    if choice == Corruption_t.INSERT:
        choice = random.choices(list(Insert_t))[0]

    if choice in choice_res:
        choice_res[choice] += 1
    else:
        choice_res[choice] = 1

for choise, count in choice_res.items():
    log.debug(f"{choise}: {count}")

log.debug("{:=^100s}".format("choose from custom generated range"))
nbytes = 10
for i in range(10):
    log.debug(random.choices(population=range(1, nbytes + 1), k=1))

log.debug("{:=^100s}".format("randrange"))
randrange_list = []
for i in range(10):
    randrange_list.append(random.randrange(1, 10))

log.debug(randrange_list)

log.debug("{:=^100s}".format("choice"))
choice_list = []
for i in range(1):
    choice_list.append(random.choice(list(Corruption_t)))

log.debug(choice_list)