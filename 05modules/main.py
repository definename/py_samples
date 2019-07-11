from packet import daily, weekly
import sys
import logging

from packet.sub_packet import mod

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


def main():
    log.debug("Arguments: {}".format(sys.argv))

    # Here are places where python looks for modules
    for place in sys.path:
        log.debug("> {}".format(place))

    # Python packages
    log.debug("Daily forecast: {}".format(daily.forecast()))
    log.debug("Daily _hidden: {}".format(daily._hidden()))
    log.debug("Daily _hidden_var: {}".format(daily._hidden_var_does_not_work))
    log.debug("Weekly forecast: {}".format(weekly.forecast()))

    mod.do()


if __name__ == "__main__":
    main()
