# from w3net import W3Net
from w3request import Request
class W3Aux:
    def __init__(self, w3net):
        self.w3net = w3net

    def bind(self, namespace):
        """ Tells the game to send you any events in the specified namespace 
        Args:
            namespace (str): Namespace to listen to
        """
        self.w3net.send(Request()
            .utf8(CMD_BIND) \
            .utf8(namespace)
            .end())
    
    def reload(self):
        """ Reload game scripts"""
        self.w3net.send(Request()
            .utf8(NS_SCRIPTS)
            .utf8(S_RELOAD)
            .end())

    def rootpath(self):
        """ Get the root path for scripts"""
        self.w3net.send(Request()
            .utf8(NS_SCRIPT_COMPILER)
            .utf8(SC_ROOT_PATH)
            .end())

    def varlist(self, section="", name=""):
        """ Searches for config variables 
        Args:
            section (str): Section to search. If left empty, searches all sections
            name    (str): Only the variables containing this token will be returned. Leave empty for all variables
        """
        self.w3net.send(Request()
            .utf8(NS_CONFIG)
            .int32(0xCC00CC00) # magic number
            .utf8(CFG_LIST)
            .utf8(section)     # Section
            .utf8(name)        # Variable Name
            .end())
    
    def unfilteredlocals(self, value):
        """ Enables/disables the filtering of the list of locals received from the game
        Args:
            value (bool): Whether to get the unfiltered list or not
        """
        self.w3net.send(Request()
            .utf8(NS_SCRIPT_DEBUGGER)
            .utf8(SD_UNFILTERED_LOCALS)
            .byte(value)
            .end())
    
    def execute(self, cmd):
        """ Runs an exec function from the game
        Args:
            cmd (str): The command to be executed
        """
        self.w3net.send(Request()
            .utf8(NS_REMOTE)
            .int32(0x12345678) # magic number
            .int32(0x81160008) # must be larger than or equal to 0x81160008, TODO: What's its use?
            .utf8(cmd)
            .end())

    def modlist(self):
        """ Gets the list of mods installed in game directory """
        self.w3net.send(Request()
            .utf8(NS_SCRIPTS)
            .utf8(S_PKG_SYNC)
            .end())

    def opcode(self, funcname, classname=None):
        """ Gets the opcodes for a specific function
        Args:
            funcname (str): Name of the function
            classname (str): Name of the class. Set this to "None" for global functions
        """
        request = Request().utf8(NS_SCRIPT_DEBUGGER) \
            .utf8(SD_OPCODE_REQUEST) \
            .utf16(funcname)
        
        if (classname == None):
            request.byte(0)
        else:
            request.byte(1).utf16(classname)
        
        self.w3net.send(request
            .end())