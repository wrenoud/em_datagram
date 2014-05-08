from structObject import *
from em_datagram import em_datagram

class EM3000_INSTALLATION_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "second_serial",
        "parameter_string")
    __slots__ = ("parameters",)
    second_serial=ctype_ushort()
    parameter_string=struct_array(
        object_type=ctype_char(),
        len=lambda self: len(self._bindata) - 5)

class em3000_parameter_packet(em_datagram):
    body=EM3000_INSTALLATION_BODY
    
    def __init__(self, *args, **kargs):
        super(em3000_parameter_packet,self).__init__(*args,**kargs)

        _string = "".join(self.body.parameter_string[:])
        if _string[-1] == '\x00':
            _string = _string[:-2] # trim trailing comma and pad byte
        else:
            _string = _string[:-1] # trim trailing comma
        self.body.parameters = dict([_param.split('=') for _param in  _string.split(',')])
