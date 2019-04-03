from datetime import datetime
import socket
import logging
import threading

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("UDP")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 4096
addr = ("localhost", 6789)

def CloseSocket(server):
    server.shutdown(socket.SHUT_RDWR)
    server.close()

def ServerHandler(server):
    try:
        server.bind(addr)

        data, client_addr = server.recvfrom(max_size)
        logger.debug("At {} client: {} said: {}".format(datetime.now(), client_addr, data.decode("utf-8")))

        server.sendto(b"Are you talking to me?", client_addr)
        CloseSocket(server)
    except Exception as e:
        logger.error("UDP server handler error: {}".format(e))

desc = """Usage:
    'q' - exit;
    '?' - get this help.
"""

def main():
    logger.debug("UDP server is being started at: {}".format(addr))
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    thread = threading.Thread(target=ServerHandler, args=(server,))
    thread.start()

    while True:
        val = input(desc)
        if val == "q":
            CloseSocket(server)
            break
        elif val == "?":
            logging.debug(desc)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("UDP server error: {}".format(e))
