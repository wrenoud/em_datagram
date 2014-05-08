from structObject import *
from em_datagram import em_datagram

class EM3000_DEPTH_BEAM(structObject):
    _byte_order=little_endian
    _field_order=(
        "z","y","x",
        "depression",
        "azimuth",
        "range",
        "quality",
        "window",
        "reflectivity",
        "beam",
    )
    z=ctype_short(doc="Depth")
    y=ctype_short(doc="Acrosstrack distance")
    x=ctype_short(doc="Alongtrack distance")
    depression=ctype_short(
        getter=lambda x: x/100.0,
        doc="Beam depression (0.01 degrees)")
    azimuth=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Beam azimuth (0.01 degrees)")
    range=ctype_ushort(doc="Range, one-way travel time")
    quality=ctype_uchar(doc="Quality factor")
    window=ctype_uchar(doc="Length of detection window (samples/4)")
    reflectivity=ctype_schar(doc="reflectivity (0.5 dB resolution)")
    beam=ctype_uchar(doc="Beam number")

class EM3000_DEPTH_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "heading",
        "td_sound_speed",
        "transducer_depth",
        "maxno_beams",
        "valid_beams",
        "vert_res",
        "horiz_res",
        "extra",
        "beams",
        "depth_multiplier")
    heading=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Vessel heading (0.01 degrees)")
    td_sound_speed=ctype_ushort(
        getter=lambda x: x/10.0,
        doc="Sound speed at transducer (dm/s)")
    transducer_depth=ctype_ushort(
        getter=lambda x: x/100.0,
        doc="Transmit transducer depth, wrt water level at time of ping (cm)")
    maxno_beams=ctype_uchar(doc="Maximum number of beams")
    valid_beams=ctype_uchar(doc="Number of valid beams")
    vert_res=ctype_uchar(doc="z resolution (cm)")
    horiz_res=ctype_uchar(doc="x and y resolution (cm)")
    extra=ctype_ushort(doc="Sampling rate (Hz)")
    beams=struct_array(
        object_type=EM3000_DEPTH_BEAM,
        len=lambda self: self.valid_beams)
    depth_multiplier=ctype_schar(doc="Depth multiplier")

class em3000_depth_packet(em_datagram):
    body=EM3000_DEPTH_BODY