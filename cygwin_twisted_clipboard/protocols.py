from twisted.internet.protocol import Protocol

from .settings import CLIPBOARD_DEVICE

class PutClipboard(Protocol):
    def __init__(self):
        self.clipboard = None

    def connectionMade(self):
        self.clipboard = open(CLIPBOARD_DEVICE, 'w')

    def dataReceived(self, data):
        self.clipboard.write(data)

    def connectionLost(self, reason):
        self.clipboard.close()
        self.clipboard = None

class GetClipboard(Protocol):
    def __init__(self):
        self.clipboard = None
        self.buffer_size = 4096

    def connectionMade(self):
        with open(CLIPBOARD_DEVICE, 'r') as clipboard:
            self.transport.writeSequence(clipboard.readlines())
        self.transport.loseConnection()
