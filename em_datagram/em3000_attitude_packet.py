from structobject import *
from em_datagram import em_datagram

class EM3000_ATTITUDE_RECORD(structObject):
    _byte_order=little_endian
    _field_order=(
        "time",
        "status",
        "roll",
        "pitch",
        "heave",
        "heading"
    )
    time=ctype_ushort(doc="Time since record start (milliseconds)")
    status=ctype_ushort(doc="Sensor status")
    roll=ctype_short(
        getter=lambda x: x/100.0,
        doc="Roll (in 0.01)")
    pitch=ctype_short(
        getter=lambda x: x/100.0,
        doc="Pitch (in 0.01)")
    heave=ctype_short(
        getter=lambda x: x/100.0,
        doc="Heave (in 0.01)")
    heading=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Heading (in 0.01)")

class EM3000_ATTITUDE_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "number",
        "records",
        "system_descriptor")
    __slots__ = ['system_no','heading_active','roll_active','pitch_active','heave_active']
    number=ctype_ushort(doc="Number of entries")
    records=struct_array(
        object_type=EM3000_ATTITUDE_RECORD,
        len=lambda self: self.number)
    system_descriptor=ctype_uchar(doc="Sensor system descriptor")
    
    def unpack(self, bindata):
        super(EM3000_ATTITUDE_BODY,self).unpack(bindata)

        self.system_no =      ((self.system_descriptor & 0b00110000) >> 4) + 1
        self.heading_active = (self.system_descriptor & 0b00000001)
        self.roll_active =    (self.system_descriptor & 0b00000010) >> 1
        self.pitch_active =   (self.system_descriptor & 0b00000100) >> 2
        self.heave_active =   (self.system_descriptor & 0b00001000) >> 3

class em3000_attitude_packet(em_datagram):
    body=EM3000_ATTITUDE_BODY