from datetime import datetime
import socket
import logging
import threading

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("TCP")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

max_size = 4096
addr = ("localhost", 6789)


def ServerHandler(server):
    try:
        server.bind(addr)
        server.listen(5)

        while True:
            client, client_addr = server.accept()
            data = client.recv(max_size)
            logger.debug("At {} client: {} said: {}".format(datetime.now(), client_addr, data))
            client.sendall(b"Are you talking to me?")
            client.close()

    except Exception as e:
        logger.error("TCP server handler error: {}".format(e))


desc = """Usage:
    'q' - exit;
    '?' - get this help.
"""


def main():
    logger.debug("TCP server is being started at: {}".format(addr))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread = threading.Thread(target=ServerHandler, args=(server,))
    thread.start()

    while True:
        val = input(desc)
        if val == "q":
            server.close()
            break
        elif val == "?":
            logging.debug(desc)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("TCP server error: {}".format(e))
