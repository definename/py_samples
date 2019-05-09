from datetime import datetime, timedelta
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


d1 = datetime.utcnow()
time.sleep(5)
d2 = datetime.utcnow()
# d2 = d1 + timedelta(seconds=5)
log.debug("{} {}".format(d1, d2))
delta1 = timedelta(seconds=4)
delta2 = d2 - d1
log.debug("delta {}".format(delta2))
if delta2 > delta1:
    log.debug("More")
