import logging

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
