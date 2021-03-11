-----
title: Networking
description: This article is dedicated to computer networks.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: debian, gnu, linux, operating, system, admin, network, wifi, lan
lang: en
-----


# Commands

## Change the mac address of a network device

To be able to change the mac address of a network device, this first need to 
be put down (deactivated). 

    ifconfig wlan0 down
    ifconfig wlan0 hw ether 00:11:22:33:44:55
    ifconfig wlan0 up

Note that when you reboot the computer the mac address is changed back to 
it's original reference.

See also the tool `macchanger`.


# Wifi

## Change the wifi mode from managed to monitor

Check that nothing is using the wlan0 device.

    airmon-ng check kill

Change the mode:

    iwconfig wlan0 mode monitor

# Sniffing wifi packets

By sniffing i mean copying all wifi packages that are in range.

    airodump-ng mon0