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
    logger.debug("UDP client is being started at: {}".format(addr))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"Hey", addr)

    data, server_addr = client.recvfrom(max_size)
    logger.debug("At: {} server: {} said: {}".format(datetime.now(), server_addr, data))
    client.close()
except Exception as e:
    logger.error("UDP client error: {}".format(e))
