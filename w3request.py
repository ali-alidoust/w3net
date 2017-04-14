from struct import pack
from w3const import *

class Request:

    def __init__(self):
        self.payload = bytearray()
    
    def bind(self, namespace):
        return self.utf8(CMD_BIND) \
            .utf8(namespace)

    def sc_root_path(self):
        return self.script_compiler(SC_ROOT_PATH)
    
    def sd_unfiltered_locals(self, value):
        return self.script_debugger(SD_UNFILTERED_LOCALS) \
            .byte(value)
    
    def sd_sort_locals(self, value):
        return self.script_debugger(SD_SORT_LOCALS) \
            .byte(value)
    
    def script_compiler(self, token):
        self.utf8(NS_SCRIPT_COMPILER) \
            .utf8(token)
        return self
    
    def script_debugger(self, token):
        self.utf8(NS_SCRIPT_DEBUGGER) \
            .utf8(token)
        return self

    def remote(self, cmd):
        return (self.utf8(NS_REMOTE)
            .int32(0x12345678) # magic number
            .int32(0x81160008) # must be larger than or equal to 0x81160008, TODO: What's its use?
            .utf8(cmd))

    def varlist(self, section, name):
        return (self.utf8(NS_CONFIG)
            .int32(0xCC00CC00) # magic number
            .utf8("list")
            .utf8(section)     # Section
            .utf8(name))       # Variable Name
    
    def byte(self, value):
        return self.append(TYPE_BOOL) \
            .append(pack("!?", value))

    def utf8(self, token):
        return self.append(TYPE_STRING_UTF8) \
            .len_short(len(token)) \
            .append(token)
    def utf16(self, token):
        return self.append(TYPE_STRING_UTF16) \
            .len_short(len(token)) \
            .append(token.encode("utf_16_be"))
    def int32(self, value):
        iv = value
        if(iv & 0x80000000):
            iv = -0x100000000 + iv
        return self.append(TYPE_INT32) \
            .append(pack("!l", iv))
    def len_short(self, length):
        return self.append(pack("!H", length))

    def append(self, data):
        self.payload.extend(data)
        return self

    def end(self):
        self.append(PACKET_TAIL)
        self.payload = bytearray(PACKET_HEAD) + pack("!H", len(self.payload) + 4) + self.payload
        return self.payload