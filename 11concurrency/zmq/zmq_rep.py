import zmq
import logging
import threading
import time

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("REP")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


def ReplyHandler(socket):
    while True:
        try:
            req_bytes = socket.recv(zmq.NOBLOCK)

            req_str = req_bytes.decode("utf-8")
            logger.debug("That voice in my head says: {}".format(req_str))

            rep_str = "Stop saying: {}".format(req_str)
            rep_bytes = rep_str.encode("utf-8")
            socket.send(rep_bytes)
        except zmq.ZMQError:
            if socket.closed:
                break
            else:
                time.sleep(0.5)


def main():
    addr = "tcp://{}:{}".format("127.0.0.1", 6789)
    ctx = zmq.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind(addr)

    t = threading.Thread(target=ReplyHandler, args=(socket, ))
    t.start()

    while True:
        val = input(desc)
        if val == "q":
            socket.close()
            break
        elif val == "?":
            logging.debug(desc)


desc = """Usage:
    'q' - exit;
    '?' - get this help.
"""

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("TCP server error: {}".format(e))
