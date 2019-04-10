import xmlrpc.client
import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("RPC-CLIENT")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
num = 7
logger.debug("{}".format(proxy.double(num)))
