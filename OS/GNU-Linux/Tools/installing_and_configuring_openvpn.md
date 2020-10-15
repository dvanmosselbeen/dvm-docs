-----
title: Installing and configuring openvpn
description: This article is dedicated to the openvpn
created: 14-10-2020 17:39:00
modified: 14-10-2020 17:39:00
keywords: debian, gnu, linux, operating, system, admin, raspberry, pi, vpn, openvpn
lang: en
-----

# Table of Contents

* [Introduction](#introduction)
* [Server Setup](#server-setup)
* [Client Setup](#client-setup)
  * [Windows 10 Clients](#windows-10-clients)
    * [Windows 10 Client Installation](#windows-10-client-installation)
    * [Windows 10 Client Configuration](#windows-10-client-configuration)
  * [Android Clients](#android-clients)
* [Resources](#resources)
# Introduction

The server will be a Raspberry PI OS (Debian based). The client will be a Windows 10 laptop.

# Server Setup

As server we will use a Raspberry Pi and it's default OS.

## Installation

    sudo apt-get install openvpn

## Configuration

Switch to root user as we have a lot of commands to do:

    sudo su

From now on we can configure a few things.

    gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz > /etc/openvpn/server.conf


# Client Setup

## Windows 10 Clients

For this we need a Microsoft Windows 10 operating system. 

### Windows 10 Client Installation 

Download the installer from https://openvpn.net/ and execute it. 

### Windows 10 Client Configuration

...

## Android Clients

We will install the client for Android on a Samsung Galaxy S8+.

# Resources

* https://openvpn.net
* https://raspberrytips.com/install-openvpn-raspberry-pi/