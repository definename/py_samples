from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        print("Connection has been made")
        self.transport.write(b"Hello")

    def connectionLost(self, reason):
        print("Connection has been lost: {}".format(reason))

    def dataReceived(self, data):
        print("Server said: {}".format(data))
        self.transport.write(b"Hello")

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Unable to connect to the server: {}".format(reason))
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection has been lost: {}".format(reason))
        reactor.stop()

def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()

if __name__ == "__main__":
    main()
