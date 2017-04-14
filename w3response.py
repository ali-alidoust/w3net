from w3const import *
from construct import *
from struct import unpack

ResponseParser = Struct(
    "header" / Const(PACKET_HEAD),
    "length" / Int16ub,
    "params" / RepeatUntil(lambda x, lst, ctx: lst[-1].type == "PACKET_END", Struct(
        "type" / Enum(Int16ub, 
            STRING_ANSI=0xAC08,
            STRING_UTF16=0x9C16, 
            BOOL=0x8108, 
            PACKET_END=0xBEEF, 
            UINT32=0x7132,
            INT32=0x8132,
            INT64=0x8164),
        "data" / Switch(this.type, {
            "STRING_ANSI": Struct(
                "unknown" / Int16ub,
                "length" / Int16ub,
                "value" / String(this.length, "utf8")
            ),
            "STRING_UTF16": Struct(
                "unknown" / Int16ub,
                "length" / Int16ub,
                "value" / String(this.length * 2, "utf_16_be")
            ),
            "BOOL": Struct(
                "value" / Int8ub
            ),
            "UINT32": Struct(
                "value" / Int32ub
            ),
            "INT32": Struct(
                "value" / Int32sb
            ),
            "INT64": Struct(
                "value" / Int64sb
            ),
            "PACKET_END": Pass
        })
    ))
)