This library named SDS011 is meant for implementing in Python software thats goal is to measure air particles of <=10µm and <=2.5µm with the particle senor SDS011 developed by Nova Fitness Co.,Ltd, http://inovafitness.com/en/

Most code I found in web only has implemented the permanent measureing when the sensor is in "no dutycycle mode" (the factory default). But the sensor has much more capabilities such as "going to sleep", dutycycles of about 1 to 30 minutes, two working modes and so forth.

So I decided to implement this feature in a python library in order to
1. going to measure air pollution with a Raspberry Pi
2. learn to code python
3. learn using git

So this is my first python project so don't let it stop you from suggesting improvements.
First, you have to edit the logging configuration in top of SDS011.py to your needs.

SDS011 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Basic usage (example):
#############################
import time
from sds011 import SDS011

sensor = SDS011("COM3") # Windows
or
sensor = SDS011("/dev/ttyAMA0")

print(reader.device_id)
sensor.reportmode == sensor.ReportModes.Passiv
retval = sensor.request()
print(retval)
sensor.reportmode = sensor.ReportModes.Initiative
time.sleep(3)
values = sensor.get_values()
print(values[0], "--", values[1])
################################

The Sensor comes with a Windows software but can be used with raspberry pi GPIO feature by using the serial in and output channels.

In order to use it on raspberry pi one has to ensure that no other serial communication is happening.

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

---------------------------------------------
Copyright 2016, Frank Heuer, Germany

SDS011 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SDS011 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SDS011.  If not, see <http://www.gnu.org/licenses/>.

Have fun and keep your air (inside and outside your home) free of pollutants.