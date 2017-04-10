import datetime
from structobject import *

class em_datagram(structObject):
    _byte_order=little_endian
    _field_order=(
        "stx",
        "datagram_type",
        "sonar_model",
        "date",
        "time",
        "ping_number",
        "system_serial",
        "body",
        "etx",
        "checksum")
    __slots__ = ('date_time',)
    stx=ctype_uchar(value=0x02)
    datagram_type=ctype_uchar()
    sonar_model=ctype_ushort()
    date=ctype_uint()
    time=ctype_uint()
    ping_number=ctype_ushort()
    system_serial=ctype_ushort()
    body=struct_array(
        object_type=ctype_char(),
        len=lambda self: len(self._bindata) - 19)
    etx=ctype_uchar(value=0x03)
    checksum=ctype_ushort()

    def unpack(self, bindata):
        super(em_datagram,self).unpack(bindata)

        _year   = int( self.date / 10000 )
        _month  = int( (self.date % 10000) / 100 )
        _day    = int( self.date % 10000 % 100 )
        _hour   = int( self.time / 3600000 )
        _minute = int( (self.time % 3600000) / 60000 )
        _second = int( (self.time % 3600000 % 60000) / 1000 )
        _micro  = int( self.time % 3600000 % 60000 % 1000 * 1000 )
        
        self.date_time = datetime.datetime(_year, _month, _day,
                                          _hour, _minute, _second, _micro)
