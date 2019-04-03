from datetime import datetime
import socket
import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("TCP")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 4096
addr = ("localhost", 6789)

try:
    logger.debug("TCP client is being started at: {}".format(addr))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    client.sendall(b"Hey")

    data = client.recv(max_size)
    logger.debug("At: {} server said: {}".format(datetime.now(), data))
    client.close()
except Exception as e:
    logger.error("TCP client error: {}".format(e))