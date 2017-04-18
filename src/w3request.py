from struct import pack
from w3const import *

class Request:
    def __init__(self):
        self.payload = bytearray()
    
    def byte(self, value):
        return self.append(TYPE_BYTE) \
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
    
    def int64(self, value):
        iv = value
        if(iv & 0x8000000000000000):
            iv = -0x1000000000000000 + iv
        return self.append(TYPE_INT64) \
            .append(pack("!q", iv))
    
    def uint32(self, value):
        return self.append(TYPE_UINT32) \
            .append(pack("!L", value))

    def len_short(self, length):
        return self.append(pack("!H", length))

    def append(self, data):
        self.payload.extend(data)
        return self

    def end(self):
        self.append(PACKET_TAIL)
        self.payload = bytearray(PACKET_HEAD) + pack("!H", len(self.payload) + 4) + self.payload
        return self.payload