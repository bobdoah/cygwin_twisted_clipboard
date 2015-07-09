from twisted.internet.protocol import Protocol

import pyperclip

class PutClipboard(Protocol):
    def dataReceived(self, data):
        pyperclip.copy(unicode(data))

class GetClipboard(Protocol):
    def connectionMade(self):
        self.transport.write(pyperclip.paste().encode('utf-8'))
        self.transport.loseConnection()
