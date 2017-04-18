import threading
from time import sleep
from w3net import W3Net
from w3aux import W3Aux
from w3prompt import W3Prompt
from IPython import start_ipython
from traitlets.config.loader import Config

class W3Main:
    def __init__(self):
        self.thread = None
        self.net = W3Net()

    def start(self):
        self.thread = threading.Thread(target=W3Net.loop)
        self.thread.start()
        sleep(2)
        if self.thread.isAlive():
            # embed(globals(), locals(), history_filename="./w3net.history", configure=Main.configure)
            cfg = Config()
            cfg.InteractiveShellApp.pylab_import_all = False
            cfg.InteractiveShell.autocall = 2
            cfg.TerminalIPythonApp.quick = True
            cfg.InteractiveShell.colors = u"Linux"
            cfg.InteractiveShell.sphinxify_docstring = True
            cfg.InteractiveShell.ast_node_interactivity = "all"
            cfg.TerminalInteractiveShell.highlighting_style = u"monokai"
            cfg.TerminalInteractiveShell.simple_prompt = False
            cfg.TerminalInteractiveShell.prompts_class = W3Prompt
            start_ipython(user_ns= {'w3': W3Aux(self.net)}, config=cfg)
            self.net.close()
        else:
            print("Failed to connect to the game. Exiting...")
        # self.thread.join()

    def send(self, data):
        self.net.send(data)

    @staticmethod
    def configure(repl):
        repl.show_docstring = True

_main = W3Main()

def send(data):
    # global main
    _main.send(data)

_main.start()