-----
title: Raspberry PI
description: This article is dedicated to the Raspberry PI.
created: 14-10-2020 00:00:00
modified: 14-10-2020 00:00:00
keywords: debian, gnu, linux, operating, system, admin, raspberry, pi
lang: en
-----

# Raspberry PI Model 3 B

This document is specific for the Raspberry PI Model 3 B or higher. I own both Model 3B and Model 4. Later on maybe there will be some more notes about some other versions of Raspberry Pi.

# Table of Contents

* [Introduction](#introduction)
* [Installing an operating system on the raspberry pi](#installing-an-operating-system-on-raspberry-pi)
* [Backing up the micro sd card](#backing-up-the-micro-sd-card)
* [Differences between Raspberry PI models](#differences-between-raspberry-pi-models)
* [Things specific to Raspberry](#things-specific-to-raspberry)
    * [Raspbian specific tools]()
    * [STOP killing that SD card](#stop-killing-that-sd-card-)
* [Using the Raspberry Pï model 3 or 4 for the first time](#using-the-raspberry-model-3-or-4-for-the-first-time)
* [Cleaning up stuff](#cleaning-up-stuff)
* [Recommended software and setup](#recommended-software-and-setup)
* [Recommended hardware for the Raspberry Pi](#recommended-hardware-for-the-raspberry-pi)
* [Tools to take remote control](#tools-to-take-remote-control)
* [Webserver and Database](#webserver-and-database)
* [Migrations Logs](#migrations-logs)
    * [Jessie to Buster migration](#jessie-to-buster-migration)
* [Other notes not categorised](#other-notes-not-categorised)
* [Resources](#resources)

# Introduction

The Raspberry is some minimalistic computer, the size of a bank card. Well, at least that's what they are saying about Raspberry and which isn't 100% a lie. Because the Raspberry is effectively that small. But then we are talking about the motherboard only. Once you put some protective case around it, that raspberry pi won't fit in your pocket so easily anymore. Beside that, Raspberry still is that small and awesome.

Raspberry is somethings useless, somethings you don't need at all. You have no need to buy a Raspberry because this will bring nothing good at home. Raspberry will give you a lot of issues with your girlfriend. Raspberry is just a big gadget, but then for geeks. It's just some stuff where you will spend tons of time with it. This toy is definitely not good for your social contacts. This mini computer is made for people who want to learn and play with computers. It's a little gadget running Raspberry Pi operating system, a deviation of Debian GNU / Linux, the Universal operating system.

Unfortunately, Raspberry isn't powerful at all, it's slow. There's not much disk space available because it runs on that (provide) 16 GB micro SD card. The hardware is really limited, you can't upgrade it really expect with some fancy other gadgets. Don't mind to add RAM, there's no way to do so!. You can't upgrade it a lot. The SD card will kick your face sooner or later because SD cards have a limited amount of (survive) cycles. These life cycle is between 10.000 and 100.000 write cycles. Which sounds enormous, but it isn't at all for a daily desktop usage, let alone a "server" usage. You won't be able to make a super computer of this Raspberry box. And worse, Raspberry runs on the `armhf` architecture, which is even less common, even for the average experienced GNU/Linux user.

But still, Raspberry is awesome ! It's so nice to play on such a little computer. You won't really throw your money through your window by buying a Raspberry, because it's worth any euro of it, despite that it's slow, limited etc. You will enjoy every minute when you are playing with your gadget ! Or you will hate it if your the average Windows user. 

Raspberry isn't for the average user at all. With this i mean the average Microsoft Windows user. Because this little box come with a pre installed Operating System, Raspbian (via Noobs), a variant of Debian GNU/Linux. So, you should have at least basic (read advanced) general GNU/Linux knowledge if you want to play on this tiny computer. Or at least, be prepared to learn a lot of new high tech if you have no general GNU/Linux knowledge at all. Don't be afraid, a GNU/linux operating system isn't complicated at all, it's just that you need to learn to use it, like you did several years with Microsoft Windows.

That said, if you are new to GNU/Linux, Welcome ! But i really don't think that Raspberry is the ideal step to take if you want to learn GNU/Linux. My personal opinion would say you to install Virtual Box and play with virtual machines instead. You should realise that a Raspberry is really tin in all aspects. So, to avoid that you blame that GU/Linux is slow, it's better that you move on to somethings more serious before digging into complex stuff. However, if you are patient, realist and have a fever to learn, go go go !!!

As Debian is installed (on that micro SD card), using Raspberry is like using Debian. So in this document we will avoid to give general Debian information, rather point out that there's a [dedicated Debian documentation page](../Debian/README.md) for that. Here we will point out the things specific to the Raspberry "computer".

# Installing an operating system on Raspberry pi

There are different variants of GNU Linux operating systems you can install. For example Ubuntu.

There's some dedicated tool called `Raspberry Pi Imager` to use to download and prepare the SD card. For this see the website: https://www.raspberrypi.org/downloads/.

Once this tool installed, it allow with a GUI interface to select the desired operating system and to write it to the SD card.

# Backing up the micro SD card

Once you have installed and configured a bar Raspberry Pi, it's strongly recommended to make a backup of it. This well speed up the process during a restore. As you should not forget, SD cards die fast.

There are various ways to back up a system. But like in this case, the Raspberry Pi is stored on a micro SD card, it's a matter to remove the micro SD card and to copy the content of it.

This is very practical and a should be a to do for everyone. Especially after a fresh setup and up to date install.

On Microsoft Windows 10 you can use the tool called `Win32 Disk Imager` from here: https://sourceforge.net/projects/win32diskimager/

The interface is very intuitive and it's usage isn't detailed here.

Note, depending of the speed of the micro SD card, as well as the card reader, it can take a while to backup a micros SD card. Close to 1 hour.

There is also: https://www.balena.io/etcher/

# Differences between Raspberry pi models

* The case is not compatible with version 3.

# Things specific to Raspberry

The default username for the `pi` user account is `raspberry`. There's no password set for the `root` user and to get root access you should use the `sudo` command. Thus to pass to a `root shell`, from the `pi` user account you should type this: `sudo su`. You will switch to the root user without being asked for the root password, because there's none. From there, you can define a password if desired with the `passwd` command, which i strongly recommend.

The Raspberry i have bought came with a micro SD card with Raspberry (Debian) pre installed. If you know about the Debian operating system, or any other GNU/Linux distribution based on Debian, then you will find your way.

## Raspbian specific tools

| Command | Description |
|---|---|
| raspi-config | Raspberry Pi configuration tool |
| raspi-gpio | Dump the state of the BCM270x GPIOs |
| raspistill | |
| raspivid | |
| raspividyuv | |
| raspiyuv | |

## STOP killing that SD card !

Yes! Stop with that! Please!

Seriously, SD cards have a limited time of life, a limited amount of read and write lifetime. What does that mean? In other words, that SD cards aren't made to be used "extensively" (read, not that extensively at all) and that your SD card will die sooner than expected! Really sooner than expected! How so? Like said, SD cards aren't made for these purposes and in 1,2,3 you will reach the end of life of you SD card.

You still don't believe me? Install apache and let the default configuration kill your SD card in less than 6 months. Assuming you get only a very less visitors, otherwise you will kill your SD card much faster!

But heck, how can i save my SD card ? 

Well, don't use it and it will last (almost) forever.

Seriously, you should take into consideration that any read / write to your SD card, will improve his time left to die. So, generally speaking, you should avoid useless reads and writes to you hard disk drive, ahum, your SD card.

You should do the maximum with your Raspberry system to write as less as possible to it's hard disk drive (which is SD). So for instance, if you want to run a webserver, or anything that log (write a lot to your hard disk drive), should be avoided. Or at least, you should change the configuration settings so that it log as less as possible. In fact, you should desactivate as much as possible to log (read this as; read and write).

"Wait, you are asking me to deactivate the logs on my Raspberry?"

Yes, because of: Do you read your logs ? If yes, do you read them before it's to late ? If still yes, why are you losing your time reading this, you are probably aware of all that high tech that fails ...

Like i said before, Raspberry is gadget, no offence meant, but you should be aware that you are playing and dealing with some complex stuff. So you should deal with it's limitation, well, the technology limitation. After all, it's not the fault of Raspberry that (on hardware side) SD cards just sucks (tm).


But don't worry to much, there are solutions like mentioned above ! So, stop using your Raspberry and it won't kill your expensive SD card !

As alternative, you can look to install `Noobs` (read, raspbian) to an external hard disk drive. Yes, you read it good, install it to another "hard disk" than your SD card. With one stone, you will hit 2 targets. Using raspberry with an external (powered over USB, instead of a wall plug), you will avoid to kill your SD card within a few months. But the most "visible" improvement would be visible when seeing that the boot up & co is much faster on an external drive that the SD card.

# Using the raspberry Model 3 or 4 for the first time

The first time you want to use the Raspberry Pi, you probably need to plug in all cables so that you could configure it. Plug in all cables: hdmi, keyboard, mouse, power cable. The Raspberry Pi will automatically boot once you plugged in the power cable. There's no On or Off button. So the power cable is always the cable you want to plug at last.

Once booted you will get an interface `Welcome to the Raspberry Pi` , which request you to select your country, keyboard settings etc. Once this done, he will updated the system. Updating the system can take a while. Once this done, he will request to reboot the system, which you should do.

Once this done, i recommend to do a few more things:

* Activate the SSH and remote desktop server. For this, go to the `Menu` > `Preferences` > `Raspberry Pi Configuration`. In that new window, select the tab `Interfaces` and check the options `SSH`, `VNC`.
* With Raspberry Pi Model 4 with 4K resolution setups, i strongly recommend to enable the `Display` > `Pixel Doubling` so that the screen is more readable.
* Change host name `System` > `Hostname`. I prefer to be more clear, so for me it will be `raspberrypim3` or `raspberrypim4`. 

Once these settings adjusted, you need to reboot the system. After this, i suggest to start to make use of the remote tools like ssh or RealVNC to connect to your Raspberry Pi.

# Cleaning up stuff

Once rebooted, lets start to clean up stuff that has been downloaded by the updates. Note that you should run the following command once in a while if you fetch a lot of updates and install new software.

    sudo apt-get clean 

On a fresh install on a Model 4, i passed from `8.6G` to `6.7G`.

# Recommended software and setup

* `screen` - See the dedicated [screen page](../Tools/screen.md).
* `irssi` - The famous command line irc chat client. See the dedicated [irssi page](../Tools/irssi.md).
* `xchat` - IRC client for X similar to AmIRC
* `mc` -
* `xclip` - 

# Recommended hardware for the Raspberry Pi

I strongly recommend a easy to use keyboard and mouse.

It could be you bought a kit which include some micro keyboard with an integrated mouse track pad.

I really recommend to buy the `Logitech K400`. This keyboard is small, but still the size of a real computer keyboard and has an integrated track pad.

# Tools to take remote control 

* realvnc-vnc-server
* ssh server

# Webserver and database

See the dedicated [LAMP server with Raspberry PI OS](lamp-server-with-raspberry-pi-os.md) file.

# Migrations logs

## Jessie to Buster migration

As of writing this, august 2019, `Debian version 10` with the code name `Buster` is the current stable release.

When i acquired the Raspberrypi with a kit, i got a `Noobs` SD card of 16 GB and installed `Raspbian`. At that time it was `Debian version 8` with code name `Jessie`. It isn't that wise to migrate a system by jumping over a release but it is doable.

There's not much to tell about this migration. Except that `apt-get` failed at some dependencies issues with `udev` and `systemd` (iirc). I had got a message on the end of the failing log that i should run `apt-get -f install`, which i did and didn't got any issues later on. Or at least, didn't discovered anything wrong. Both `udev` and `systemd` packages are still installed, so all seems fine to me.

To proceed the upgrade to the newer release, we should follow the instructions on the website of Raspberry or at Debian side, which i had found after my migration :-P  See here: https://www.raspberrypi.org/documentation/raspbian/updating.md
 
What i recall from memory (wrote this document file after the migration), i ran these commands:

Edit the `/etc/apt/sources.list` and replace every occurrences of `jessie` with `buster`. You can use the `sed -i "s/jessie/buster/" /etc/apt/sources.list` trick but it's wise to open that file and edit by hand, so that you see what's currently in that file. After all, it's a Debian derivation. So i have the following in the `/etc/apt/sources.list` file:

    deb http://mirrordirector.raspbian.org/raspbian/ buster main contrib non-free rpi
    # Uncomment line below then 'apt-get update' to enable 'apt-get source'
    #deb-src http://archive.raspbian.org/raspbian/ buster main contrib non-free rpi

Raspberry has also made a dedicated `/etc/apt/sources.list.d/raspi.list` (which Debian doesn't have) and which needs to be edited too. There you should also replace every occurrences of the word `jessie` to `buster`. Additionally the word `staging` should be removed as this isn't available anymore. So the content of `/etc/apt/sources.list.d/raspi.list` should look like this

    deb http://archive.raspberrypi.org/debian/ buster main ui
    # Uncomment line below then 'apt-get update' to enable 'apt-get source'
    #deb-src http://archive.raspberrypi.org/debian/ buster main ui

Now 

    apt-get update
    apt-get dist-upgrade

I also got another failing issue and the error told to run `apt --fix-broken install` which i did.

Once the upgrade done, restart to raspberry, to be sure everything is ok.

# Other notes not categorised

Show your ip and mac address on the console:

    ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1

# TODO

* Secure Raspberry PI OS default setup - https://raspberrytips.com/security-tips-raspberry-pi/
* Check for backup system. See: https://raspberrytips.com/backup-raspberry-pi/
* Install heat sink - https://raspberrytips.com/install-heat-sinks-raspberry-pi/
* Try camera stuff - https://raspberrytips.com/install-camera-raspberry-pi/ and https://raspberrytips.com/raspberry-pi-camera-projects-ideas/
* Check to install a VPN server - https://raspberrytips.com/install-openvpn-raspberry-pi/
* Samba file server - 
* Hacking wifi - https://raspberrytips.com/hacking-wifi-raspberry-pi/
* Fail2ban - https://raspberrytips.com/install-fail2ban-raspberry-pi/
* Use Kali on the Pi - https://raspberrytips.com/use-kali-linux-raspberry-pi/
* Crypto mine - https://raspberrytips.com/mine-monero-raspberry-pi/

# Resources

* https://www.raspberrypi.org - The official website of the Raspberry PI project.
* https://www.raspberrypi.org/forums/
* https://raspberrytips.com - Tons of articles with tips and trips for raspberry pi.