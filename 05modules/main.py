from sources import daily, weekly
import sys
import logging

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
    log.debug("Weekly forecast: {}".format(weekly.forecast()))


if __name__ == "__main__":
    main()
