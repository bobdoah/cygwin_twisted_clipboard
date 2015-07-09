from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Factory
from twisted.protocols.policies import LimitTotalConnectionsFactory

from .protocols import PutClipboard, GetClipboard
from .settings import PUT_CONNECTION_LIMIT

class PutClipboardFactory(Factory):
    #connectionLimit = PUT_CONNECTION_LIMIT
    def buildProtocol(self, addr):
        return PutClipboard()

class GetClipboardFactory(Factory):
    def buildProtocol(self, addr):
        return GetClipboard()
