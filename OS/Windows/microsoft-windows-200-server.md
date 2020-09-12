-----
title: Microsoft Windows 2000 server
description: This article talk about a Microsoft Windows 2000 server
created: 28-11-2008 00:00:00
modified: 28-11-2008 00:00:00
keywords: Microsoft, Windows, 2000, server
lang: en
-----

## Table of Contents

* [The server versions](#the-server-versions)
    * [Windows 2000 server](#windows-2000-server)
    * [Windows 2000 Advanced server](#windows-2000-advanced-server)
    * [Windows 2000 Datacenter server](#windows-2000-datacenter-server)
* [Hardware Requirements](#hardware-requirements)
* [Installing](#installing)
* [Creating setup boot disks](#creating-setup-boot-disks)
* [To note](#to-note)

# Microsoft Windows 2000 server

This page give some informations about the 3 different server versions.
The Microsoft Windows 2000 Server, Microsoft Windows Advanced Server and
the Microsoft Windows 2000 Datacenter Server.

## The server versions

There are 3 different versions of Microsoft Windows 2000 Server.

-   Microsoft Windows 2000 Server
-   Microsoft Windows 2000 Advanced Server
-   Microsoft Windows 2000 Datacenter Server

### Windows 2000 Server

Microsoft Windows 2000 Server contain all the core features of the
Windows 2000 Server family. You can use Windows 2000 Server for a file
and print server, application server, web server and communication
server.

-   Active Directory
-   Internet and Web Services
-   Security, Kerberos and public key infrastructure
-   Windows Terminal Services
-   Support for up to 4 GB of memory
-   Supported for 2 cpu\'s and 4 SMP

### Windows 2000 Advanced Server

The Advanced Server have the features of the classic server too.

-   Network load balancing
-   Cluster services for application fault tolerance
-   Support for up to 8 GB of memory
-   Up to eight-way SMP support

### Windows 2000 Datacenter Server

This is the most powerful server of the Microsoft Windows 2000 family.
It is destined for large-scale enterprise networks. It have all the
features of the previous versions.

-   More advanced clustering services
-   Support for up to 64 GB of memory
-   Up to 16-way SMP support (OEM version can support up to 32-way SMP)

## Hardware Requirements

    Component   | Minimum Requirement  | Recommended Requirement
    ============================================================
    Processor     Pentium 133MHz or >    Pentium 166MHz or >
    Memory        128 MB                 256 MB
    Disk space    2 GB                   Depending of the stuff
                                         that may installed
    Display       VGA compatible or >

See the Hardware Compatibility List (HCL) before doing a installation,
go on the follow website <http://www.microsoft.com/hwtest/hcl>.

## Installing

There are different ways to install `Windows 2000 Server`. Booting
directly from the cd. With `dfs`. Staring `WINNT.EXE` or `WINNT32.EXE`
from the cd on another operating system. Or from `Setup Boot Disks`.

For more information about the installation process, see [MS Windows
2000 server install
process](http://dvm.zapto.org:8080/pyguicms-dev/articles/view/ms_windows_2000_server_install_process)
for the whole installation process.

## Creating Setup Boot Disks

You need four floppy disks. And execute `MAKEBT32.EXE` or `MAKEBOOT.EXE`
on a 16-bit system in the `BOOTDISK` directory of the
`Windows 2000 Server` CD.

## To note

-   mmc (Microsoft Management Console)
