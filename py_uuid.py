import uuid
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

# uuid name generator
NAMESPACE_HANDLER = uuid.UUID("{18a42823-3a4d-4aaf-84b6-816e2b74c788}")
log.debug("{}".format(uuid.uuid3(NAMESPACE_HANDLER, "handler1")))
log.debug("{}".format(uuid.uuid3(NAMESPACE_HANDLER, "handler2")))
log.debug("{}".format(uuid.uuid3(NAMESPACE_HANDLER, "handler3")))
