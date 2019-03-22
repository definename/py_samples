import time
from twisted.internet import reactor, protocol

class EchoServer(protocol.Protocol):
    def connectionMade(self):
        print("Connection has been accepted")

    def connectionLost(self, reason):
        print("Connection has been lost: {}".format(reason))

    def dataReceived(self, data):
        print("Client said {}".format(data))
        time.sleep(2)
        self.transport.write(b"Welcome")


class EchoFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return EchoServer()

def main():
    f = EchoFactory()
    reactor.listenTCP(8000, f)
    reactor.run()

if __name__ == "__main__":
    main()