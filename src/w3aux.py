# from w3net import W3Net
from w3request import Request
class W3Aux:
    def __init__(self, w3net):
        self.w3net = w3net
    
    def reload(self):
        """ Reload game scripts"""
        self.w3net.send(Request()
            .reload()
            .end())

    def rootpath(self):
        """ Get the root path for scripts"""
        self.w3net.send(Request()
            .sc_root_path()
            .end())

    def varlist(self, section="", name=""):
        """ Searches for config variables 
        Args:
            section (str): Section to search. If left empty, searches all sections
            name    (str): Only the variables containing this token will be returned. Leave empty for all variables
        """
        self.w3net.send(Request()
            .varlist(section, name)
            .end())
    
    def unfilteredlocals(self, value):
        """ Enables/disables the filtering of the list of locals received from the game
        Args:
            value (bool): Whether to get the unfiltered list or not
        """
        self.w3net.send(Request()
            .sd_unfiltered_locals(value)
            .end())
    
    def execute(self, cmd):
        """ Runs an exec function from the game
        Args:
            cmd (str): The command to be executed
        """
        self.w3net.send(Request()
            .remote(cmd)
            .end())

    def modlist(self):
        """ Gets the list of mods installed in game directory """
        self.w3net.send(Request()
            .pkglist()
            .end())

    def opcode(self, funcname, classname=None):
        """ Gets the opcodes for a specific function
        Args:
            funcname (str): Name of the function
            classname (str): Name of the class. Set this to "None" for global functions
        """
        self.w3net.send(Request()
            .opcode(funcname, classname)
            .end())