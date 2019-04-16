import logging

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s'))
logger = logging.getLogger("proto")
logger.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

    def __str__(self):
        return self.text

    def __bytes__(self):
        return self.text.encode(encoding="utf-8")


w1 = Word("ah")
w2 = Word("AH")

logger.debug("def __eq__: {}".format(w1 == w2))
logger.debug("def __str__: {}".format(w1))
logger.debug("def __bytes__: {}".format(bytes(w1)))
