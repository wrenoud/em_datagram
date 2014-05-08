from structObject import *
from em_datagram import em_datagram

class EM3000_SURF_SS_RECORD(structObject):
    _byte_order = little_endian
    _field_order = (
        "time",
        "ss")
    time=ctype_ushort(doc="Time in seconds since record start")
    ss=ctype_ushort(
        getter=lambda x: x/10.0,
        doc="Sound speed (in dm/s) (incl. offset)")

class EM3000_SURF_SS_BODY(structObject):
    _byte_order = little_endian
    _field_order = (
        "num_records",
        "records",
        "spare")
    num_records=ctype_ushort(doc="Number of entries")
    records=struct_array(
        object_type=EM3000_SURF_SS_RECORD,
        len=lambda self: self.num_records)
    spare=ctype_uchar()
    
class em3000_surf_ss_packet(em_datagram):
    body=EM3000_SURF_SS_BODY