---
description: Linux server on Jetson Nano
---

# Server

The server (Nano) code lives in `server/nano/`. It has the following primary classes:

* `COM` defined in include/comm.hpp, implemented in src/comm.cpp.
* `NANO` defined in include/nano.hpp, implemented in src/nano.cpp.
* `VideoStream` defined in include/stream.hpp, implemented in src/stream.cpp.

The entrypoint and primary loop is located in `src/main.cpp`.

{% content-ref url="server-logic.md" %}
[server-logic.md](server-logic.md)
{% endcontent-ref %}

{% content-ref url="server-video.md" %}
[server-video.md](server-video.md)
{% endcontent-ref %}

{% content-ref url="server-comms.md" %}
[server-comms.md](server-comms.md)
{% endcontent-ref %}
