This document will list a few notes about the Debian GNU/Linux operating system. It is mainly a draft document containing some notes or links to resources concerning Debian. This document won't detail everything as there are already a lot of documentation available online.

![alt text](https://www.debian.org/logos/openlogo-100.png "Debian Logo")

# Table Of contents

1. [Introduction](#introduction)
1. [General information](#general-information)
    1. [Releases (Versions)](#releases-versions)
1. [The package manager](#the-package-manager)
    1. [apt](#apt)
    1. [aptitude](#aptitude)
1. [Interesting apps](#interesting-apps)

# Introduction

The Debian GNU/Linux operating system claims to be the universal operating system. And that's in fact true. Debian runs on older hardware as well as on modern hardware. It is able to run on a variety of different architectures. Up from computers, to tables, dedicated hardware such as the Raspberry Pi, the Sony Playstation (3) and so on.

# General information

## Releases (versions)

Debian is been know to be a very stable operating system. Debian is available in 3 different releases. A stable version, a testing version, and a unstable version (called sid).

The stable version, like the name say it, is very stable, however, the packages (applications and libraries) are older than a normal user would expect. A stable version is release once in a while and the packages arent updated anymore. Except for security patches. But you won't never get new features on a stable version once it is release.

The testing version, like the name say it, is a testing version.

# Installing Debian

You can install Debian on different ways. Starting from a CD, DVD, iso image, usb key, with PXE boots and so on.

These days, with a big internet line, it's common to use the `netinst` method. Which is by using a little iso image. That iso image you can burn to a CD and from there boot up your computer. The particularity of the netinst method is that the iso image is very small. The iso image contains the bare minimum to install a system. The additional software, if selected during the installation, will be downloaded and then installed on your computer. 

## Migrating from stable to testing release

    cp /etc/apt/sources.list /etc/apt/sources.list_BACKUP
    
    # Now we are going to replace the release name "buster" by testing.
    # It could be you need to adjust this.
    sed -i "s/buster/testing/" /etc/apt/sources.list
    
    apt-get update
    apt-get dist-upgrade

# The package manager

You can easily manage your package with the apt-get, apt-cache tools.

There's also aptitude which i strongly recommend.

## apt

`apt-get` is the default package manager on Debian. There are other package managers available such as `aptitude`.

Before searching or installing anything with `apt-get`, we need to retrieve it's new list of packages:

    apt-get update

Searching for applications:

    apt-get search gvim

Show more information about a package:

    apt-cache show gvim-gtk3

Installing applications

    apt-get install gvim-gtk3


    # Clear the cache (Clears the downloaded deb files).
    apt-get clean

## aptitude

Aptitude can be used in 2 different ways. Both ways are to do on the command line but one method has no UI and the other has one.

Just by running the command `aptitude`, you will start the UI interface.

# Admin commands

| Command | Description |
|---|---|
| dpkg -l <package> | List if package is installed. |
| dpkg -L <package> | Show the content of a deb package. ||
| df -h | |
| which python | Return the location of the file. |

# Interesting apps

| Application | Description |
|---|---|
| aptitude | Package manager |
| apt-listchanges | List the changes... |
| apt-listbugs | ... |
| screen | See the dedicated [screen page](../tools/screen.md).|
| htop | Process monitoring tool. |
| tightvncserver | ... |
