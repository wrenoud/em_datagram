from structObject import *
from em_datagram import em_datagram

class EM3000_NEW_SVP_RECORD(structObject):
    _byte_order=little_endian
    _field_order=(
        "depth",
        "ss")
    depth=ctype_uint(doc="Depth")
    ss=ctype_uint(
        getter=lambda x: x/10.0,
        doc="Sound speed in dm/s")
        
class EM3000_NEW_SVP_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "date",
        "time",
        "num_records",
        "depth_res",
        "records",
        "spare")
    date=ctype_uint(doc="Date of profile (same format as header field)")
    time=ctype_uint(doc="Time of profile (same format as header field)")
    num_records=ctype_ushort(doc="Number of entries")
    depth_res=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Depth resolution (in cm)")
    records=struct_array(
        object_type=EM3000_NEW_SVP_RECORD,
        len=lambda self: self.num_records)
    spare=ctype_uchar(doc="Spare",value=0x00)
    
class em3000_new_svp_packet(em_datagram):
    body=EM3000_NEW_SVP_BODY
    
    def unpack(self, bindata):
        super(em3000_new_svp_packet, self).unpack(bindata)
        
        for record in self.body.records:
            record.depth = record.depth * self.body.depth_res