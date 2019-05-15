import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class Config():
    def __setattr__(self, name, value):
        log.debug("{} {}".format(name, value))

    def __getattr__(self, name):
        log.debug("{}".format(name))


def main():
    cfg = Config()
    cfg.value = "data"
    cfg.value


if __name__ == "__main__":
    main()
