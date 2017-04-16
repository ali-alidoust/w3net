import threading
from time import sleep
from ptpython.repl import embed
from w3net import W3Net
from w3aux import W3Aux

class Main:
    def __init__(self):
        self.thread = None
        self.net = None

    def connect(self):
        self.net = W3Net()

    def start(self):
        self.thread = threading.Thread(target=W3Net.loop)
        self.thread.start()
        sleep(2)
        if self.thread.isAlive():
            embed(globals(), locals(), history_filename="./w3net.history", configure=Main.configure)
            self.net.close()
        else:
            print("Failed to connect to the game. Exiting...")
        # self.thread.join()

    def send(self, data):
        self.net.send(data)

    @staticmethod
    def configure(repl):
        repl.show_docstring = True

_main = Main()
_main.connect()
w3 = W3Aux(_main.net)

def send(data):
    # global main
    _main.send(data)

_main.start()