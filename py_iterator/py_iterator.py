import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    ge = (e * 2 for e in "SPAM")

    log.debug(iter(ge) is ge)

    work = True
    while work:
        work = next(ge, False)
        log.debug(work)

if __name__ == "__main__":
    main()


