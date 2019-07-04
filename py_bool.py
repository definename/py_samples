import logging
import time

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

def line(line_type): return log.debug("{:=^100s}".format(line_type))


line("False to int")
data_bool = False
log.debug("{}".format(data_bool))
log.debug("{}".format(int(data_bool)))

line("True to int")
data_bool = True
log.debug("{}".format(data_bool))
log.debug("{}".format(int(data_bool)))

line("")
data_bool = None
log.debug("{}".format(data_bool))

line("")
def get_data():
    return False

count = 5
while count > 0 and not get_data():
    log.debug("Data")
    time.sleep(1)
    count -= 1
