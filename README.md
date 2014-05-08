em_datagram
===========

Module for parsing EM Series datagram formats.

Dependancy
----------

[structObect](https://github.com/wrenoud/structObject)

Usage
-----

```Python
import em_datagram as em

parsed = em.em3000_depth_packet(packet_data)

print parsed.ping_number
````
