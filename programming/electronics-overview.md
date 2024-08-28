---
description: >-
  These documentation pages are based on the GitHub project
  TennesseeLunabotics/lunaframe
---

# Electronics Overview

## Control Devices

The control systems on our robot make use of three primary compute devices. These are:

* Client Laptop
* NVIDIA Jetson Nano
* ESP32 Microcontroller

Refer to the linked page for more information on these devices specifically.

{% content-ref url="programming-overview.md" %}
[programming-overview.md](programming-overview.md)
{% endcontent-ref %}

## Electronics

The following devices are used as a part of our electrical box. All can be found on the wiring diagram except for the Linear Actuators and Cytron Controllers. We've included those in this list since they worked well for our specific use case, but this wiki and framework does not implement anything beyond a basic drivetrain.

### Motors

* REV NEO Brushless Motors
* REV Spark Max Motor Controllers
* Progressive Automations Linear Actuators
* Cytron MD20A Motor Controllers

### Power

* AndyMark PDB
* AndyMark 120A Breaker
* Off-The-Shelf (OTS) variable buck converter
* OTS LIPO 14.7v Battery
* OTS LIPO 7.4v Battery
* OTS E-STOP
* OTS low-voltage relay
* OTS On-Off button
* OTS high-voltage relay
* OTS data logger

***

## Wiring Diagram

<figure><img src="../.gitbook/assets/Wiring Diagram 2024 (1).jpg" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Blue, Green, and Yellow lines are data.

Red and Black lines are positive/ground power connections respectively.
{% endhint %}
