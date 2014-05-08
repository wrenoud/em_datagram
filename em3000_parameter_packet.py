from structObject import *
from em_datagram import em_datagram

class EM3000_INSTALLATION_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "second_serial",
        "parameters")
    second_serial=ctype_ushort()
    parameters=struct_array(
        object_type=ctype_char(),
        len=lambda self: len(self._bindata) - 5)

class em3000_parameter_packet(em_datagram):
    body=EM3000_INSTALLATION_BODY