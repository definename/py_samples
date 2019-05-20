import copy
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class SubMemeber():
    def __init__(self, sub_val):
        self.sub_val = sub_val

class Member():
    def __init__(self):
        self.val = 1
        self.sub = SubMemeber(11)
    
    def __str__(self):
        return "{}, {}".format(self.val, self.sub.sub_val)

def test_copy():
    mbr = Member()
    log.debug("mbr origin: {}".format(mbr))
    mbr_copy = copy.copy(mbr)

    mbr_copy.val = 2
    mbr_copy.sub.sub_val = 22
    log.debug("mbr: {}".format(mbr))
    log.debug("mbr_copy: {}\n".format(mbr_copy))


def test_deepcopy():
    mbr = Member()
    log.debug("mbr origin: {}".format(mbr))
    mbr_deepcopy = copy.deepcopy(mbr)

    mbr_deepcopy.val = 3
    mbr_deepcopy.sub.sub_val = 33
    log.debug("mbr: {}".format(mbr))
    log.debug("mbr_deepcopy: {}\n".format(mbr_deepcopy))

def main():
    test_copy()
    test_deepcopy()

if __name__ == "__main__":
    main()
