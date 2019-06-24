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
    log.debug("{:08b}".format(random.getrandbits(8)))

log.debug("{:=^100s}{}".format("two digits with replacement", string.digits))
while True:
    pair = random.choices(string.digits, k=2)
    log.debug(f"{pair[0]} {pair[1]}")
    if pair[0] == pair[1]:
        break

log.debug("{:=^100s}".format("corruption probability"))
class CorruptionType(enum.Enum):
    INSERT = 1
    DELETE = 2
    XOR = 3
    COMBINE = 4
    NO_CORRUPTION = 5

class InsertType(enum.Enum):
    BEFORE = 1
    AFTER = 2
    INSIDE = 3

corruption_actions = [CorruptionType.INSERT, CorruptionType.DELETE, CorruptionType.XOR, CorruptionType.COMBINE, CorruptionType.NO_CORRUPTION]
insert_actions = [InsertType.BEFORE, InsertType.AFTER, InsertType.INSIDE]

def make_choice(insert=10, delete=10, xor=10, combine=10):
    no_corruption = 100 - (insert + delete + xor + combine)
    return random.choices(corruption_actions, [insert, delete, xor, combine, no_corruption], k=1)

def generate_choice(count):
    in_count = 0
    while in_count < count:
        yield make_choice()[0]
        in_count += 1

choice_gen = generate_choice(count=1000)
choice_res = {}
for choice in choice_gen:
    if choice == CorruptionType.INSERT:
        choice = random.choices(insert_actions)[0]

    if choice in choice_res:
        choice_res[choice] += 1
    else:
        choice_res[choice] = 1

for choise, count in choice_res.items():
    log.debug(f"{choise}: {count}")

