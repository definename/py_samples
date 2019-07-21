import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class EngineAsync():
    def __init__(self):
        self.__sn = None

    def set_serial(self, sn, done_id):
        self.__sn = sn
        log.debug("done_id: {} set_serial: {}".format(done_id, self.__sn))
    
    def get_serial(self, done_id):
        log.debug("done_id: {} get_serial: {}".format(done_id, self.__sn))
        return self.__sn

class Engine(EngineAsync):
    def __init__(self):
        super().__init__()
        self.__name = "name"
        self.__done_id = 1

    def __quard(self, func):
        def inner(*args, **kwargs):
            log.debug("Decorated")
            return func(*args, self.__done_id, **kwargs)
        return inner

    def set_serial(self, sn):
        self.__quard(super().set_serial)(sn)
    
    def get_serial(self):
        return self.__quard(super().get_serial)()

def main():
    engine = Engine()
    engine.set_serial(123321)
    log.debug(engine.get_serial())

if __name__ == "__main__":
    main()