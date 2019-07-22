import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class Config():
    def __init__(self,**kw):
        self.__dict__.update(kw)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getitem__(self, key):
        log.debug("__getitem__ with: {}".format(key))

    def __bool__(self):
        return False
    
    def __call__(self, value):
        log.debug(f"{value}!!")




def main():
    cfg = Config(p1=10, p2=20)
    log.debug("p1: {} p2: {}".format(cfg.p1, cfg.p2))

    # __setattr__
    cfg.value = "data"
    log.debug(cfg.value)

    # __getitem__
    cfg["key"]

    # __bool__
    log.debug("__bool__: {}".format(True if cfg else False))

    # __call__
    cfg("Boom")

    # dir
    log.debug(dir(cfg))


if __name__ == "__main__":
    main()
