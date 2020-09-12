-----
title: Raspberry PI Model 3 B
description: This article is dedicated to the Raspberry PI Model 3 B.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: debian, gnu, linux, operating, system, admin, raspberry, pi
lang: en
-----

# Raspberry PI Model 3 B

This document is specific for the Raspberry PI Model 3 B or higher.

# Table of Contents

* [Introduction](#introduction)
* [Things specific to Raspberry](#things-specific-to-raspberry)
    * [Raspbian specific tools]()
    * [STOP killing that SD card](#stop-killing-that-sd-card-)
* [Migrations Logs](#migrations-logs)
    * [Jessie to Buster migration](#jessie-to-buster-migration)
* [Other notes not categorised](#other-notes-not-categorised)
* [Resources](#resources)

# Introduction

Raspberry is some minimalistic computer, the size of a bank card. Well, at least that's what they are saying about Raspberry and which isn't 100% a lie. Because the Raspberry is effectively that small. But then we are talking about the motherboard only. Once you put some protective case around it, that raspberry won't fit in your pocket anymore. Beside that, Raspberry still is that small.

Raspberry is somethings useless, somethings you don't need at all. You have no need to buy a Raspberry because this will bring nothing good at home. Raspberry will give you a lot of issues with your girlfriend. Raspberry is just a big gadget, but then for geeks.

Unfortunately, Raspberry isn't powerful at all, it's slow. There's not much disk space available because it runs on that (provide) 16 GB micro SD card. The hardware is really limited, you can't upgrade it really expect with some fancy other gadgets. Don't mind to add RAM, there's no way to do so!. You can't upgrade it a lot. The SD card will kick your face sooner or later because SD cards have a limited amount of (survive) cycles. These life cycle is between 10.000 and 100.000 write cycles. Which sounds enormous, but it isn't at all for a daily desktop usage, let alone a "server" usage. You won't be able to make a super computer of this Raspberry box. And worse, Raspberry runs on the `armhf` architecture, which is even less common, even for the average experienced GNU/Linux user.

But still, Raspberry is awesome ! It's so nice to play on such a little computer. You won't really throw your money through your window by buying a Raspberry, because it's worth any euro of it, despite that it's slow, limited etc. You will enjoy every minute when you are playing with your gadget ! Or you will hate it if your the average Windows user. 

Raspberry isn't for the average user at all. With this i mean the average Microsoft Windows user. Because this little box come with a pre installed Operating System, Raspbian (via Noobs), a variant of Debian GNU/Linux. So, you should have at least basic (read advanced) general GNU/Linux knowledge if you want to play on this tiny computer. Or at least, be prepared to learn a lot of new high tech if you have no general GNU/Linux knowledge at all. Don't be afraid, a GNU/linux operating system isn't complicated at all, it's just that you need to learn to use it, like you did several years with Microsoft Windows.

That said, if you are new to GNU/Linux, Welcome ! But i really don't think that Raspberry is the ideal step to take if you want to learn GNU/Linux. My personal opinion would say you to install Virtual Box and play with virtual machines instead. You should realise that a Raspberry is really tin in all aspects. So, to avoid that you blame that GU/Linux is slow, it's better that you move on to somethings more serious before digging into complex stuff. However, if you are patient, realist and have a fever to learn, go go go !!!

As Debian is installed (on that micro SD card), using Raspberry is like using Debian. So in this document we will avoid to give general Debian information, rather point out that there's a [dedicated Debian documentation page](../Debian/README.md) for that. Here we will point out the things specific to the Raspberry "computer".

# Things specific to Raspberry

The default username for the `pi` user account is `raspberry`. There's no password set for the `root` user and to get root access you should use the `sudo` command. Thus to pass to a `root shell`, from the `pi` user account you should type this: `sudo su`. You will switch to the root user without being asked for the root password, because there's none. From there, you can define a password if desired with the `passwd` command, which i strongly recommend.

The Raspberry i have bought came with a micro SD card with Raspberry (Debian) pre installed. If you know about the Debian operating system, or any other GNU/Linux distribution based on Debian, then you will find your way.

## Raspbian specific tools

| Command | Description |
|---|---|
| raspi-config | A dedicated CLI UI tool to adjust settings that are specific to Raspbian. That tool is a bit comparable with the dpkg-reconfigure |
| raspi-gpio | |
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

# Resources

* https://www.raspberrypi.org