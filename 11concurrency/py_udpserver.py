from datetime import datetime
import socket
import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("UDP")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 4096
addr = ("localhost", 6789)

try:
    logger.debug("UDP server is being started at: {}".format(addr))
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(addr)

    data, client_addr = server.recvfrom(max_size)
    logger.debug("At {} client: {} said: {}".format(datetime.now(), client_addr, data.decode("utf-8")))

    server.sendto(b"Are you talking to me?", client_addr)
    server.close()
except Exception as e:
    logger.error("UDP client error: {}".format(e))