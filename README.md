em_datagram
===========

Module for parsing EM Series datagram formats.

Dependancy
----------

[structobect](https://github.com/wrenoud/structobject)

Usage
-----

```Python
import em_datagram as em

parsed = em.em3000_depth_packet(packet_data)

print parsed.ping_number
````
