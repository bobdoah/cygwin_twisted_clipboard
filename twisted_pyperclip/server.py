from twisted.internet import reactor

from .factory import PutClipboardFactory, GetClipboardFactory
from .settings import PUT_PORT, GET_PORT


def main():
    reactor.listenTCP(PUT_PORT, PutClipboardFactory())
    reactor.listenTCP(GET_PORT, GetClipboardFactory())
    reactor.run()

if __name__ == '__main__':
    main()
