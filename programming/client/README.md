---
description: C++ Windows client built with CMake
---

# Client

The client code lives in `client/`. It has two classes:

* `tcp_stream` defined in include/comm.hpp, implemented in src/comm.cpp
* `Controller` defined in include/controller.hpp, implemented in src/controller.cpp

The program entrypoint and primary loop is located in `src/client.cpp`.



{% content-ref url="controller-input-and-client-logic.md" %}
[controller-input-and-client-logic.md](controller-input-and-client-logic.md)
{% endcontent-ref %}

{% content-ref url="client-video.md" %}
[client-video.md](client-video.md)
{% endcontent-ref %}

{% content-ref url="client-comms.md" %}
[client-comms.md](client-comms.md)
{% endcontent-ref %}
