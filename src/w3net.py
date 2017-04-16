import asyncore, socket
from w3request import Request
from w3response import ResponseParser
from ptpython.repl import embed
from w3const import *
import threading
from time import sleep

# print(hexlify(Request().bind(Request.NS_SCRIPT_COMPILER).end()))

class W3Net(asyncore.dispatcher_with_send):
    def __init__(self):
        asyncore.dispatcher_with_send.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.set_reuse_addr()
        self.bind(('localhost', 0))
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
        
        # self.send(Request()
        #     .utf8("Utility")
        #     .int64(100)
        #     .utf8("Ping")
        #     .end())
        
        # self.send(Request()
        #     .opcode("OnConfigUI", "CR4TestPopup")
        #     .end()
        # )
        
        # self.send(Request()
        #     .utf8(NS_SCRIPT_DEBUGGER)
        #     .utf8("BreakpointToggle")
        #     .utf16("game\\gui\\popups\\testPopup.ws")
        #     .uint32(13)
        #     .byte(1)
        #     .end())

        # self.send(Request()
        #     .utf8(NS_SCRIPT_DEBUGGER)
        #     .utf8("LocalsModification")
        #     .int32(0)
        #     .utf16("obj")
        #     .utf16("NULL")
        #     .end())

        self.send(Request()
            .utf8(NS_SCRIPT_DEBUGGER)
            .utf8("LocalsRequest")
            .int32(0x01010101)
            .int32(0x00000000)
            .utf16("")
            .int32(0x00000000)
            .end())

        # self.send(Request()
        #     .remote("mytest(5)")
        #     .end())

    def handle_read(self):
        response = ResponseParser.parse(self.recv(8192*32))
        result = ""
        for param in response.params:
            if (param != None) and ('data' in param) and (param.data != None) and ('value' in param.data):
                result += str(param.data.value) + ' | '
        print(result[:-3])

    def handle_close(self):
        print("Connection failed.")
        print("Retrying connection...")
        # self.bind(('localhost', 0))
        self.connect(('localhost', 37001))


def w3reload():
    """ Reload game scripts"""
    send(Request()
        .reload()
        .end())

def w3rootpath():
    """ Get the root path for scripts"""
    send(Request()
        .sc_root_path()
        .end())

def w3varlist(section="", name=""):
    """ Searches for config variables 
    Args:
        section (str): Section to search. If left empty, searches all sections
        name    (str): Only the variables containing this token will be returned. Leave empty for all variables
    """
    send(Request()
        .varlist(section, name)
        .end())

class Main:
    def __init__(self):
        self.thread = None
        self.net = None
    
    @staticmethod
    def loop():
        asyncore.loop()

    def start(self):
        self.thread = threading.Thread(target=Main.loop)
        self.net = W3Net()
        self.thread.start()
        sleep(2)
        if self.thread.isAlive():
            embed(globals(), locals(), history_filename="./w3net.history")
            self.net.close()
        else:
            print("Failed to connect to the game. Exiting...")
        # self.thread.join()

    def send(self, data):
        self.net.send(data)

    @staticmethod
    def configure(repl):
        repl.show_docstring = True
    
    # def output(self, data):
    #     self.

main = Main()

def send(data):
    global main
    main.send(data)

main.start()