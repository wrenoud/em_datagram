from structobject import *
from em_datagram import em_datagram

class EM3000_RUNTIME_PARAMETER_BODY(structObject):
    _byte_order=little_endian
    _field_order=(
        "operator_status",
        "processing_status",
        "bsp_status",
        "status",
        "mode",
        "filter_ID",
        "min_depth",
        "max_depth",
        "absorp_coeff",
        "tx_pulse_len",
        "tx_beam_width",
        "tx_power_reduction",
        "rx_beam_width",
        "rx_bandwidth",
        "rx_gain_reduction",
        "tvg_crossover",
        "ssp_source",
        "max_swath_width",
        "beam_spacing",
        "coverage_sector",
        "yaw_stab_mode",
        "coverage_sector_stbd",
        "max_swath_width_stbd")
        #"tx_tilt",
        #"filter_ID2")
    operator_status=     ctype_uchar(doc="Operator Station status")
    processing_status=   ctype_uchar(doc="Processing Unit status (CPU)")
    bsp_status=          ctype_uchar(doc="BSP status")
    status=              ctype_uint(doc="Sonar Head or Transceiver status")
    mode=                ctype_uchar(doc="Mode")
    filter_ID=           ctype_uchar(doc="Filter identifier")
    min_depth=           ctype_ushort(doc="Minimum depth in m")
    max_depth=           ctype_ushort(doc="Maximum depth in m")
    absorp_coeff=        ctype_ushort(doc="Absorption coefficient (in 0.01 dB/km)")
    tx_pulse_len=        ctype_ushort(doc="Transmit pulse length (in microsec)")
    tx_beam_width=       ctype_ushort(doc="Transmit beamwidth (in 0.1 degrees)")
    tx_power_reduction=  ctype_schar(doc="Transmit power re maximum (in dB)")
    rx_beam_width=       ctype_uchar(doc="Receive beamwidth (in 0.1 degrees)")
    rx_bandwidth=        ctype_uchar(doc="Receive bandwidth (in 50 Hz resolution)")
    rx_gain_reduction=   ctype_uchar(doc="Mode 2 or Receiver fixed gain setting (in dB)")
    tvg_crossover=       ctype_uchar(doc="TVG law crossover angle in degrees")
    ssp_source=          ctype_uchar(doc="Source of sound speed at transducer")
    max_swath_width=     ctype_ushort(doc="Maximum port swath width (in m)")
    beam_spacing=        ctype_uchar(doc="Beam spacing")
    coverage_sector=     ctype_uchar(doc="Maximum port coverage in degrees")
    yaw_stab_mode=       ctype_uchar(doc="Yaw and pitch stabilization mode")
    coverage_sector_stbd=ctype_uchar(doc="Maximum starboard coverage in degrees")
    max_swath_width_stbd=ctype_ushort(doc="Maximum starboard swath width in m")
    #tx_tilt=             ctype_short(doc="Transmit along tilt in 0.1 deg. or Durotong speed in dm/s")
    #filter_ID2=          ctype_uchar(doc="Filter identifier 2 or HiLo frequency absorption coefficient ratio")

class em3000_runtime_parameter_packet(em_datagram):
    body=EM3000_RUNTIME_PARAMETER_BODY