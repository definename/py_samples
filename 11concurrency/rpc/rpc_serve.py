from xmlrpc.server import SimpleXMLRPCServer
import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("RPC-SERVER")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


def double(num):
    return num * 2


addr = ("localhost", 6789)
server = SimpleXMLRPCServer(addr)
server.register_function(double, "double")
server.serve_forever()
