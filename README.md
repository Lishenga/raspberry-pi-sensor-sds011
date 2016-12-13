# Introduction

The module named **SDS011 implements much more features of the PM2.5/PM10 particle sensor than most other modules foud in the web. Sleeping mode, duty cycle, firmware and sensor id, to name some of them, are implemented.** You can implement it in Python software whos goal is to measure air particles of <=10µm (PM10) and <=2.5µm (PM2.5) with the sensor developed by **Nova Fitness Co.,Ltd**, http://inovafitness.com/en/.
# Goal
Most code I found in web only has implemented the permanent measureing when the sensor is in "no dutycycle mode" (the factory default). But the sensor has much more capabilities such as "going to sleep", dutycycles of about 1 to 30 minutes, two working modes and so forth.

So I decided to implement this feature in a python library in order to

1. going to measure air pollution with a Raspberry Pi
2. build some useful code for everyone
3. learn to code python
4. learn using git

So this is my first python project but don't be afraid. The code is tested and working. 
Don't let it stop you from suggesting improvements.
# Get started..
Just plug in your sensor to USB, open test.py, edit the constructor call to your needs (the device_path) and run test.py in your console.
See how durty or clean the air is, you breath in every day.
# No warranty
SDS011 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
# Some advices
The Sensor comes with a Windows software but can be used with raspberry pi on USB or GPIO by using the serial in and output channels.
Not knowing the power consumption of the sensor, it is unknown yet, if setting the sensor to sleep mode causes Raspberry Pi to collapse when switching to measureing mode again. **Might be that you have to use external power (i.e. a powered USB hub) on Raspberry Pi.**

In order to use it on raspberry pi on GPIO you have to **ensure that no other serial communication is happening.**

So in /boot/cmdline the line  
dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait  

has to be changed to  
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles  

At the time writing this lines you can find many threads in the web pointing to "edit the inittab". But today, working with actual firmware there is no inittab.
Details about that could be found here:  

https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=123081

So to disable getty just type
">sudo systemctl stop serial-getty@ttyAMA0.service"
in your terminal or disable it
">sudo systemctl disable serial-getty@ttyAMA0.service"

Copyright 2016, Frank Heuer, Germany  

SDS011 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with SDS011.  If not, see <http://www.gnu.org/licenses/>.

Have fun and keep your air (inside and outside your home) free of pollutants.