# Debian GNU / Linux

## About this document

This document will list a few notes about the [Debian GNU/Linux](https://www.debian.org) operating system. It is mainly a draft document containing some notes or links to resources concerning Debian. This document won't detail everything as there are already a lot of documentation available online.

![alt text](https://www.debian.org/logos/openlogo-100.png "Debian Logo")

## Table of Contents

- [Introduction](#introduction)
- [General information](#general-information)
  - [Releases (versions)](#releases-versions)
- [Installing Debian](#installing-debian)
  - [Migrating from stable to testing release](#migrating-from-stable-to-testing-release)
- [The package manager](#the-package-manager)
  - [apt](#apt)
  - [aptitude](#aptitude)
- [Admin commands](#admin-commands)
- [Interesting packages](#interesting-packages)
- [Server tools](#server-tools)
  - [SSH Server](#ssh-server) 
  - [Web Server & Database](#web-server--database)
    - [Apache](#apache)
      - [Installing Apache](#installing-apache)
    - [MySQL](#mysql)
      - [Installing MySQL](#installing-mysql)
    - [PHPMyAdmin](#phpmyadmin)
- [Getting more help](#getting-more-help)
- [Resources](#resources)

## Introduction

The Debian GNU/Linux operating system claims to be the universal operating system. And that's in fact true. Debian runs on older hardware as well as on modern hardware. It is able to run on a variety of different architectures. Up from computers, to tables, dedicated hardware such as the Raspberry Pi, the Sony Playstation (3) and so on. I guess we could install Debian into our fridge, but people seems to lazy to do so.

## General information

### Releases (versions)

Debian is been know to be a very stable operating system. Debian is available in 3 different releases. A stable version, a testing version, and a unstable version (called sid).

The stable version, like the name say it, is very stable, however, the packages (applications and libraries) are older than a normal user would expect. A stable version is release once in a while and the packages arent updated anymore. Except for security patches. But you won't never get new features on a stable version once it is release.

The testing version, like the name say it, is a testing version.

## Installing Debian

You can install Debian on different ways. Starting from a CD, DVD, iso image, usb key, with PXE boots and so on.

These days, with a big internet line, it's common to use the `netinst` method. Which is by using a little iso image. That iso image you can burn to a CD and from there boot up your computer. The particularity of the netinst method is that the iso image is very small. The iso image contains the bare minimum to install a system. The additional software, if selected during the installation, will be downloaded and then installed on your computer. 

### Migrating from stable to testing release

```commandline
cp /etc/apt/sources.list /etc/apt/sources.list_BACKUP

# Now we are going to replace the release name "buster" by testing.
# It could be you need to adjust this.
sed -i "s/buster/testing/" /etc/apt/sources.list

apt-get update
apt-get dist-upgrade
```

## The package manager

You can easily manage your package with the `apt` tools, which is a collection of tools including `apt-get`, `apt-cache` etc.

There's also `aptitude` which i strongly recommend but is not so user friendly at all. If you don't want to bother, `apt` is just fine and you don' need `aptitude`. Beside apt and aptitude, theirs a un numerous number of other applications, command line or with a graphical interface.

### apt

`apt-get` is the default package manager on Debian. There are other package managers available such as `aptitude` etc but in this section we will try to show you how much `apt` rules!

Before searching or installing anything with `apt-get`, we need to retrieve it's new list of packages:

```commandline
apt-get update
```

Searching for applications:

```commandline
apt-get search gvim
```

Show more information about a package:

```commandline
apt-cache show gvim-gtk3
```

Installing applications

```commandline
apt-get install gvim-gtk3

# Clear the cache (Clears the downloaded deb files).
apt-get clean
```

### aptitude

Aptitude can be used in 2 different ways. Both ways are to do on the command line but one method has no UI and the other has one.

Just by running the command `aptitude`, you will start the UI interface.

## Admin commands

| Command | Description |
|---|---|
| `dpkg -l <package>` | List if package is installed. |
| `dpkg -L <package>` | Show the content of a deb package. ||
| `df -h` | Display disk space usage, in human readable. |
| `which python` | Return the location of the file. |
| `shutdown -h now` | Shutdown the computer.|
| `reboot` | Reboot the computer.|
| `apt-get -f install` | To be used when in the shit and when you need to force the installation to get you out of the shit. Anyway, if you got so far, then it's probably the console output that told you to run this command... Arf, you bastard, it will be a long night ! |
| `apt autoremove` | Remove packages that where installed by other packages ant that aren't used anymore.|
| `apt-get clean`| Removed downloaded packages. Which are stored in `/var/cache/apt/archives` |
| `adduser <username>` | To create a new user on your system. You|
| `service fail2ban status` | To check if fail2ban service is been running. |
| `dmesg` | Shows some logs on the console.|

## Interesting packages

A few very interesting package which should be almost installed on every system

| Application | Description |
|---|---|
| `aptitude` | Package manager |
| `apt-listchanges` | List the changes... |
| `apt-listbugs` | tool which lists critical bugs before each APT installation |
| `apt-reportbug` | reports bugs in the Debian distribution |
| `screen` | See the dedicated [screen page](../Tools/screen.md).|
| `htop` | interactive processes viewer |
| `iftop` | Observe the flows on your network interfaces |
| `mc` | Midnight Commander - a powerful file manager |
| `tightvncserver` | virtual network computing server software |
| `irssi` | The ultimate irc chat client, of course command line only. But irssi is really some awesome IRC command line application. You won't find anything better. If so, mail me please!|
| `fail2ban` | Some security tools that watch the (abusive) login attempts and take action. |
| `xclip` | command line interface to X selections |
| `rsnapshot` | local and remote filesystem snapshot utility |
| `uptimed` | daemon to track uptimes, especially the high ones |
| `mutt` | text-based mailreader supporting MIME, GPG, PGP and threading |
| `mydumper` | High-performance MySQL backup tool |
| `sqlitebrowser` | GUI editor for SQLite databases |
| `vim` | Vi IMproved - enhanced vi editor |
| `vim-gtk3` | Vi IMproved - enhanced vi editor - with GTK3 GUI |
| `vim-python-jedi` | autocompletion tool for Python - VIM addon files |
| `unp` | unpack (almost) everything with one command |

## Server tools

Here's a few tips for server tools.

### SSH Server

...

### Web Server & Database

There are various different web servers.

#### Apache

Apache is probably the most well know and used web server. It is very stable, very easy to use and to extend. There's
also a lot of extra modules you can load to add some extra functionalities. In fact, if you need a good web server,
then you are probably looking for this Apache web server.

##### Installing Apache

To install Apache:

```commandline
aptitude install apache
```

#### MySQL

...

##### Installing MySQL

...

#### PHPMyAdmin

PHPMyAdmin is a web interface to manage the MySQL databases. It's very handy and a must have if you use MySQL.


## Getting more help

The trick on a GNU/Linux system is to find your way on how you should find information.

You can try to look to what files are been installed with the concerned application:

```commandline
dpkg -L <packagename>
```

Before adding a new user, look on how you should do:

```commandline
man adduser
```

## Resources

| Website | Description |
|---|---|
| <https://www.debian.org> | The official website of the Debian GNU/Linux operating system. |
| <https://wiki.debian.org> | The official wiki of Debian. |
| <https://debian-handbook.info> | The famous handbook for Debian. |
| <https://www.debianhelp.co.uk/> | Some website with a lot of tutorials. |
| <https:www.debiantutorials.com> | Website with tons of how to's. |
| <https:www.debiantalk.wordpress.com> | Some blog with topics about Debian. |
| <https://debian.chezrami.net> | Some French website with articles in french. |
|<https://www.debianadmin.com/>||
