import zmq
import logging
import time

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("REQ")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

ctx = zmq.Context()
socket = ctx.socket(zmq.REQ)
socket.connect("tcp://{}:{}".format("127.0.0.1", 6789))

num = 0
while True:
    req_str = "Message #{}".format(num)
    req_bytes = req_str.encode("utf-8")
    socket.send(req_bytes)

    rep_bytes = socket.recv()
    rep_str = rep_bytes.decode("utf-8")

    logger.debug("Sent: {}, received: {}".format(req_str, rep_str))
    time.sleep(1)

    num += 1
