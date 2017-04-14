NS_SCRIPT_DEBUGGER   = b'ScriptDebugger'
NS_SCRIPT_PROFILER   = b'ScriptProfiler'
NS_SCRIPT_COMPILER   = b'ScriptCompiler'
NS_SCRIPTS           = b'scripts'
NS_REMOTE            = b'Remote'
NS_UTILITY           = b'Utility'
NS_CONFIG            = b'Config'

CMD_BIND             = b'BIND'

PACKET_HEAD          = bytearray([0xDE, 0xAD]) # DEAD
PACKET_TAIL          = bytearray([0xBE, 0xEF]) # BEEF

SC_ROOT_PATH         = b'RootPath'

SD_UNFILTERED_LOCALS = b'UnfilteredLocals'
SD_SORT_LOCALS       = b'SortLocals'
SD_OPCODE_REQUEST    = b'OpcodeBreakdownRequest'

S_RELOAD             = b'reload'
S_PKG_SYNC           = b'pkgSync'

CFG_LIST             = b'list'

TYPE_BYTE            = bytearray([0x81, 0x08])
TYPE_STRING_UTF8     = bytearray([0xAC, 0x08, 0x81, 0x16])
TYPE_STRING_UTF16    = bytearray([0x9C, 0x16, 0x81, 0x16])
TYPE_INT32           = bytearray([0x81, 0x32])
TYPE_INT64           = bytearray([0x81, 0x64])