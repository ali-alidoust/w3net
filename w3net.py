import asyncore, socket
from w3request import Request
from w3response import ResponseParser
from w3const import *

# print(hexlify(Request().bind(Request.NS_SCRIPT_COMPILER).end()))

class W3Net(asyncore.dispatcher_with_send):
    def __init__(self):
        asyncore.dispatcher_with_send.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('localhost', 8081))
        self.connect(('localhost', 37001))

    def handle_connect(self):
        self.send(Request().bind(NS_SCRIPT_COMPILER).end())
        self.send(Request().bind(NS_SCRIPT_DEBUGGER).end())
        self.send(Request().bind(NS_SCRIPT_PROFILER).end())
        self.send(Request().bind(NS_SCRIPTS).end())
        self.send(Request().bind(NS_UTILITY).end())
        self.send(Request().bind(NS_REMOTE).end())
        self.send(Request().bind(NS_CONFIG).end())
        self.send(Request().sc_root_path().end())
        # self.send(Request().remote("testmenu").end()) # Opens test menu
        # self.send(Request().varlist("Visuals", ""))   # Get all of the variables from "Visuals" section


    def handle_read(self):
        # print(self.recv(8192))
        print(ResponseParser.parse(self.recv(8192*32)))
        

def main():
    W3Net()
    asyncore.loop()

main()