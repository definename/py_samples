import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    ge = (e * 2 for e in "SPAM")
    log.debug(f"{type(ge)} {ge}")
    log.debug(list(ge))

if __name__ == "__main__":
    main()


