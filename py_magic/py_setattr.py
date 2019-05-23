import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class Config():
    def __setattr__(self, name, value):
        self.__dict__[name] = value


def main():
    cfg = Config()
    cfg.value = "data"
    log.debug(cfg.value)


if __name__ == "__main__":
    main()
