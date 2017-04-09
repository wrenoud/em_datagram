from structobject import *
from em_datagram import em_datagram


class EM3000_NAV_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "latitude",
        "longitude",
        "quality",
        "sog",
        "cog",
        "heading",
        "system_descriptor",
        "input_size",
        "datagram")
    __slots__ = ['system_no','system_active','system_time','simrad_90']
    latitude=ctype_int(
        getter=lambda x: x/20000000.0,
        doc="Latitude (DD * 2x10^7)")
    longitude=ctype_int(
        getter=lambda x: x/10000000.0,
        doc="Longitude (DD * 1x10^7)")
    quality=ctype_ushort(doc="Measure of position fix quality (cm)")
    sog=ctype_ushort(doc="Speed of vessel over ground (cm/s)")
    cog=ctype_ushort(doc="Course of vessel over ground (in 0.01 degrees)")
    heading=ctype_ushort(doc="Heading (in 0.01 degrees)")
    system_descriptor=ctype_uchar(doc="Position system descriptor")
    input_size=ctype_uchar(doc="Number of bytes in input datagram")
    datagram=struct_array(
        object_type=ctype_char(),
        len=lambda self: self.input_size + (1 - self.input_size % 2))

    def unpack(self, bindata):
        super(EM3000_NAV_BODY,self).unpack(bindata)

        self.system_no =     (self.system_descriptor & 0b00000011)
        self.system_active = (self.system_descriptor & 0b10000000) >> 7
        self.system_time =   (self.system_descriptor & 0b01000000) >> 6
        self.simrad_90 =     (self.system_descriptor & 0b00001000) >> 3

class em3000_nav_packet(em_datagram):
    body=EM3000_NAV_BODY