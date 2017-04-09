from structobject import *
from em_datagram import em_datagram

class em3000_transmit_sectors(structObject):
    _byte_order=little_endian
    _field_order=(
        "tilt_angle",
        "focus_range",
        "signal_length",
        "tx_time_offset",
        "center_frequency",
        "bandwidth",
        "waveform_id",
        "sector_id")
    tilt_angle=ctype_short(
        getter=lambda x: x/100.0,
        doc="Tilt angle ref TX array (in 0.01 degrees)")
    focus_range=ctype_ushort(
        getter=lambda x: x/10.0,
        doc="Focus range (in 0.1 m, 0 = No focus)")
    signal_length=ctype_uint(doc="Signal length (in microsec)")
    tx_time_offset=ctype_uint(doc="Transmit time offset (in microsec)")
    center_frequency=ctype_uint(doc="Center frequency (in Hz)")
    bandwidth=ctype_ushort(doc="Bandwidth (in 10 Hz)")
    waveform_id=ctype_uchar(doc="Signal waveform identifier")
    sector_id=ctype_uchar(doc="Transmit sector number")

class em3000_steered_beams_new(structObject):
    _byte_order=little_endian
    _field_order=(
        "rc_steer",
        "range",
        "sector_id",
        "reflect",
        "quality_factor",
        "detection_window_len",
        "beam_no",
        "spare")
    rc_steer=ctype_short(doc="Beam pointing angle ref RX array (in 0.01 degrees)")
    range=ctype_ushort(doc="Range in 0.25 samples (Two way travel time = R / [ 4 * F / 100 ])")
    sector_id=ctype_uchar(doc="Transmit sector number")
    reflect=ctype_schar(doc="Reflectivity (BS) (in 0.5 dB resolution)")
    quality_factor=ctype_uchar(doc="Quality factor")
    detection_window_len=ctype_uchar(doc="Detection window length in samples (/4 if phase)")
    beam_no=ctype_short(doc="Beam number")
    spare=ctype_ushort(doc="Spare")

class EM3000_NEW_RAW_TANG_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "no_tx_sectors",
        "valid_beams",
        "sampling_rate",
        "rov_depth",
        "td_sound_speed",
        "maxno_beams",
        "spare1",
        "spare2",
        "transmit_sectors",
        "steered_beams",
        "spare3")
    no_tx_sectors=ctype_ushort(doc="Number of transmit sectors")
    valid_beams=ctype_ushort(doc="Number of valid receive beams")
    sampling_rate=ctype_uint(
        getter=lambda x: x/100.0,
        doc="Sampling frequency (in 0.01 Hz)")
    rov_depth=ctype_int(doc="ROV depth (in 0.01 m)")
    td_sound_speed=ctype_ushort(
        getter=lambda x: x/10.0,
        doc="Sound speed at transducer (dm/s)")
    maxno_beams=ctype_short(doc="Maximum number of beams possible")
    spare1=ctype_ushort(doc="Spare")
    spare2=ctype_ushort(doc="Spare")
    transmit_sectors=struct_array(
        object_type=em3000_transmit_sectors,
        len=lambda self: self.no_tx_sectors)
    steered_beams=struct_array(
        object_type=em3000_steered_beams_new,
        len=lambda self: self.valid_beams)
    spare3=ctype_uchar(doc="Spare")
    
class em3000_new_raw_tang_packet(em_datagram):
    body=EM3000_NEW_RAW_TANG_BODY