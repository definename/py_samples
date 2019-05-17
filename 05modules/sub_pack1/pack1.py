
import sys
sys.path.append("..")

import logging
from sub_pack2 import predef

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


def main():
    log.debug(predef.MSG)


if __name__ == "__main__":
    main()
