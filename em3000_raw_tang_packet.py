from structObject import *
from em_datagram import em_datagram

class EM3000_RAW_TANG_BEAM(structObject):
    _byte_order=little_endian
    _field_order=(
        "pointing_angle",
        "tilt_angle",
        "range",
        "reflectivity",
        "beam")
    pointing_angle=ctype_short(
        getter=lambda x: x/100.0,
        doc="Beam pointing angle (in 0.01 degrees)")
    tilt_angle=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Transmit tilt angle (in 0.01 degrees)")
    range=ctype_ushort(doc="Range (two-way travel time)")
    reflectivity=ctype_schar(doc="Reflectivity (BS) (in 0.5 dB resolution)")
    beam=ctype_uchar(doc="Beam number")

class EM3000_RAW_TANG_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "maxno_beams",
        "valid_beams",
        "td_sound_speed",
        "beams",
        "spare")
    maxno_beams=ctype_uchar(doc="Maximum number of beams")
    valid_beams=ctype_uchar(doc="Number of valid beams")
    td_sound_speed=ctype_ushort(
        getter=lambda x: x/10.0,
        doc="Sound speed at transducer (dm/s)")
    beams=struct_array(
        object_type=EM3000_RAW_TANG_BEAM,
        len=lambda self: self.valid_beams)
    spare=ctype_pad()


class em3000_raw_tang_packet(em_datagram):
    body=EM3000_RAW_TANG_BODY