from structObject import *
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
        "descriptor")
    number=ctype_ushort(doc="Number of entries")
    records=struct_array(
        object_type=EM3000_ATTITUDE_RECORD,
        len=lambda self: self.number)
    descriptor=ctype_uchar(doc="Sensor system descriptor")
    
class em3000_attitude_packet(em_datagram):
    body=EM3000_ATTITUDE_BODY