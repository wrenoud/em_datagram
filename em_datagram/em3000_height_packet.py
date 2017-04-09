from structobject import *
from em_datagram import em_datagram

class EM3000_HEIGHT_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "height",
        "type")
    #__slots__ = []
    height=ctype_int(
    	doc="Height value",
    	getter=lambda x: x/100.0)
    type=ctype_char()

class em3000_height_packet(em_datagram):
    body=EM3000_HEIGHT_BODY