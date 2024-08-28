---
description: >-
  These documentation pages are based on the GitHub project
  TennesseeLunabotics/lunaframe
---

# Programming Overview

## Devices

The control systems on our robot make use of three primary compute devices. These are:

* Client Laptop
* NVIDIA Jetson Nano
* ESP32 Microcontroller

### Client Laptop

Our client laptop builds and runs a Windows executable. Its primary purpose is to capture the state of a connected Xbox controller and send that state over wifi to the Jetson Nano. It also receives and displays a camera feed if the onboard camera is enabled.

To build the client application, OpenSSL, OpenCV, and CMake must be installed on the laptop. Running the `build_client.bat` script at the root of the project will build the application provided you have all the libraries installed and CMake can find them. The CMake file is defined at `client/CMakeLists.txt`

#### OpenCV

We used `opencv-4.9.0-windows.exe` available from [this site](https://sourceforge.net/projects/opencvlibrary/files/4.9.0/). This executable make a folder that can be moved to `C:\Program Files\`.&#x20;

You must then add the `build\x64\vc16\`, `build\x64\vc16\bin`, and `build\x64\vc16\lib`  subdirectories to your PATH.

#### OpenSSL

OpenSSL can be installed from the link below.

{% embed url="https://slproweb.com/products/Win32OpenSSL.html" %}

#### CMake

CMake can be installed from the link below.

{% embed url="https://cmake.org/download/" %}

### Jetson Nano

The Jetson Nano receives input from the client laptop as well as cameras and sensors on the robot. It is responsible for handling all computing in regards to controlling the robot. Its output is a stream of motor PWM values and a camera feed back to the client laptop, if enabled.

The Jetson runs debian-based linux (Ubuntu) and needs make, CMake, OpenSSL, and OpenCV to build and run its executable.

To build the Jetson executable, run `cmake .` from the `server/nano/` directory. This will create a Makefile. You can then run `make` to build the executable.

#### Make/OpenSSL/CMake

These can be installed through the apt package manager

```shell
sudo apt install make openssl libssl-dev cmake
```

#### OpenCV

OpenCV can be installed by following the instructions on this page.&#x20;

{% embed url="https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html" %}

### ESP32

The ESP32 is a microcontroller used for "forwarding" motor PWM values to motor controllers. Our reason for including this is because the Jetson did not have enough PWM compatible GPIO pins. Should you choose to implement a CAN-based system for controlling your motors, or have fewer motors than our use case, a microcontroller may not be required.

We used the PlatformIO Visual Studio Code extension for flashing the microcontroller.

{% embed url="https://platformio.org/" %}

***

## Data Flow

<figure><img src="../.gitbook/assets/Lunabotics Data Flow.jpg" alt=""><figcaption></figcaption></figure>

## Code Structure

The repo contains code for 3 applications. Client code lives in `client/`, while Jetson nano and microcontroller code are in `server/nano/` and `server/esp/` respectively. These 3 directories are independent of each other.



## A Word on WIFI, TCP, and TLS

Our communications platform uses a socket connection for the client and nano to communicate. Because of this, the nano must be able to open the necessary ports. These are:

* 5240/TCP - Primary Communications
* 5241/TCP - Primary Video

Additionally, security for wireless communications can be a requirement. Because of this, our platform allows for TLS. This requires running the command below on the nano and storing the `cert.pem` file at `C:\lunakey\cert.pem` on the client.

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout private.pem -out cert.pem
```
