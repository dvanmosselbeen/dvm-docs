-----
title: Gentoo
description: Gentoo reference
created: 01-01-2012 00:00:00
modified: 01-01-2012 00:00:00
keywords: gentoo, gnu, linux
lang: en
-----

# Introduction

[Gentoo](http://www.gentoo.org) is a GNU/Linux distribution
aimed at customizing and compilling the software from sources. It is a
so called source-code based distribution. Gentoo is for people who have
the patience to tweak their whole box up to their custom needs. A
typical Gentoo installation takes much more time to install compared to
most distribution where they use precompiled binaries quick installable
with the package management system. Gentoo is a bit comparable to a LFS
(Linux from scratch) installation. Where everything may need to be
compiled from source codes. Gentoo offer also some prebuild binaries but
that\'s probably not somethings you go to do if you plan using Gentoo.

The advantage of using Gentoo is that you build up and compile all your
software from sources. With some tools, and especially with some
configuration style, you will (most probably) compile software optimized
for your computer.

Gentoo is absolutely not a GNU/Linux distribution for beginers, nor for
those who want a quick GNU/Linux environment. Gentoo is definitively for
thos who want to know what happen behind the hood and want a
fine-grained, fast and very optimized system for they computer. You
shouldn\'t be affraid to read manuals and upgrade notes.

Gentoo will probably take lot\'s of time to understand and to get all
your packages compilled. I personally find Gentoo very interesting for
educational purpose. It is a distribution that you may need to update
(read recompile) frequently, or you will hurt a wall. But after all,
this is all about fun!

To resume, Gentoo is a GNU/Linux distribution for geeks or for those who
want to learn a bit more about GNU/Linux and compiling software from
sources! If you have an old computer, then you should considere some
other distribution. But if you have some bloody fast computer, then
it\'s not really an issue to spend a few \"watch time\".

This artice isn\'t going to replicated parts of the Gentoo documentation
on the Gentoo website. Instead this article will server as a quick
reference.
 

Live CD
=======

The live CD or also know as the resque, install cd is a bootable CD that
let you resque, setup or test a Gentoo distribution. This section
contains generic and specific informations for the Gento Live CD.

Using the root account
----------------------

There\'s no root password defined yet:

    sudo su

Then change the root password with passwd tool as root user:

``` {style="text-align: justify;"}
passwd root
```

Setting up the network
----------------------

As root user:

    net-setup

Then follow the instructions you get on your screen.

Starting the ssh server
-----------------------

If you want to do the installation from a remote host (with an ssh
client like putty for Microsoft Windows).

    /etc/init.d/sshd start

Configuration related stuff
---------------------------

### Networking

For a static ip, in /etc/conf.d/net add the following:

    dns_domain_lo="pinguin"
    config_eth0=( "192.168.0.11 netmask 255.255.255.0 brd 192.168.0.255" )
    routes_eth0=( "default via 192.168.0.20" )
    dns_servers_eth0="192.168.0.20"

### keyboard layout

Note the this is for a Belgian keyboard layout. The delete key doesn\'t
work like expected.

    # /etc/conf.d/keymaps
    # Use KEYMAP to specify the default console keymap.  There is a complete tree
    # of keymaps in /usr/share/keymaps to choose from.
    #KEYMAP="us"
    KEYMAP="be-latin1"
    # Should we first load the 'windowkeys' console keymap?  Most x86 users will
    # say "yes" here.  Note that non-x86 users should leave it as "no".
    #SET_WINDOWKEYS="no"
    SET_WINDOWKEYS="yes"
    # The maps to load for extended keyboards.  Most users will leave this as is.
    #EXTENDED_KEYMAPS=""
    EXTENDED_KEYMAPS="backspace keypad euro"
    # Tell dumpkeys(1) to interpret character action codes to be
    # from the specified character set.
    # This only matters if you set UNICODE="yes" in /etc/rc.conf.
    # For a list of valid sets, run `dumpkeys --help`
    DUMPKEYS_CHARSET=""

The /etc/make.conf
==================

    # These settings were set by the catalyst build script that automatically
    # built this stage.
    # Please consult /etc/make.conf.example for a more detailed example.
    CFLAGS="-O2 -march=i686 -pipe"
    CXXFLAGS="${CFLAGS}"
    # This should not be changed unless you know exactly what you are doing.  You
    # should probably be using a different stage, instead.
    CHOST="i686-pc-linux-gnu"
    # With MAKEOPTS you define how many parallel compilations should occur when you
    # install a package. A good choice is the number of CPUs in your system plus
    # one, but this guideline isn't always perfect.
    #
    # For a regular, 1-CPU system
    #MAKEOPTS="-j2"
    # For a 2-CPU system
    MAKEOPTS="-j3"
    GENTOO_MIRRORS="http://ftp.belnet.be/mirror/rsync.gentoo.org/gentoo/ \
    ftp://ftp.belnet.be/mirror/rsync.gentoo.org/gentoo/ \
    http://mirror.ovh.net/gentoo-distfiles/ \
    ftp://mirror.ovh.net/gentoo-distfiles/ \
    http://gentoo.modulix.net/gentoo/ "
    SYNC="rsync://rsync.europe.gentoo.org/gentoo-portage"
    USE="acl cups gdbm gpm nptl nptlonly unicode apache2 \
    bash-completion cairo cddb cracklib crypt curl curlwrappers \
    dbase dbm dbus dbx dvd dvdr dvdread encode exif fam fastcgi \
    fbcon ffmpeg firefox flac flatfile fltk gdbm geoip gif gnome \
    gnutls gtk hal imagemagick javascript jpeg kde lame mime \
    mozilla mp3 mpeg  mysql ncurses ogg pdf perl php plotutils \
    png python qt3 qt4 readline spell sqlite sqlite3 ssl svg \
    tidy tiff truetype wxwindows xosd xpm" 

Specific Gentoo tools
=====================

See <http://gentoo-wiki.com/TIP_Portage_utilities_not_in_portage>

-   eix
-   esearch
-   gentoolkit
-   equery
-   genlop
-   kuroo - GUI frontend to emerge
-   portato - GUI frontend to emerge

Initscripts
===========

i.e. After installing openssh

    emerge openssh

Make in sort that the ssh server is started at boot time:

    rc-update add sshd default

And if needed to remove that services from the default runlevel:

    rc-update del sshd default

Package management
==================

-   portage -
-   emerge -
-   gentoolkit (which needs to be compiled if you want to make use of
    the equery)

Updating the Portage tree. This needs to be done once a while to able to
access new software and new patches:

    emerge --sync

Searching for software
----------------------

Only search in the package name:

    emerge --search fluxbox
    # Is same as
    emerge -s fluxbox

Search in the package description:

    emerge --searchdesc fluxbox
    # Is same as:
    emerge -S fluxbox

 To see which apps there may be in a section:

    emerge app-portage/<TAB>

*This will show all the packages in \'app-portage\'.*

Installing & removing software
------------------------------

    emerge package_name

To see which decencies that will be installed without installing the
package yet:

    emerge --pretend seamonkey
    # Or to get more verbose info
    emerge --pretend --verbose seamonkey

Use a temporally USE flag. This will only be used for the concerned
package:

    USE="-java" emerge seamonkey

To see wich USE flags a package listen too:

    emerge --pretend --verbose seamonkey

We are also able to see the USE flags with equery. (install gentoolkit
to get this tool)

    equery --nocolor uses =gnumeric-1.6.3 -a

Search for some info a package contain:

    emerge -vp alsa-lib

List the files a package contains:

    equery files alsa-lib | less

To see which use variables will be used (including the USE variable):

    emerge --info

Removing software:

    emerge --unmerge gnumeric

Installing a package mathing a version:

    emerge =kdebase-3.5.7-r4

Updating the system
-------------------

First of all, you probably first need to sync!

    emerge --sync

-   With **emerge \--update \--ask world** will only search for newer
    version of the package you explicitly installed. See packages in
    **/var/lib/portage/world**
-   With **emerge \--update \--deep world**, you still don\'t update
    your whole system.
-   With **emerge \--update \--deep \--with-bdeps=y world** you will be
    able to update all installed packages and all it\'s dependencies.

Removing orphaned dependencies:

    emerge --update --deep --newuse world
    emerge --depclean
    revdep-rebuild

After having modified the USE variable in /etc/make.conf we may need to
update/recompile all the installed packages on the system with:

    emerge --update --deep --newuse world

Of course, this is going to make you hot :D

Update config files
===================

Gentoo does not overwrite config directories. See /etc/make.globals for
the variable CONFIG\_PROTECT=. But you can define this variable in
the/etc/make.conf too.

See for dispatch-conf, cfg-update, and etc-update.

The ideal and most simply to use is the etc-update. Select the number of
the config file to see. Then you see the difference of the both config
files. Pressq to exit the diff. Then press 1 replace the original config
file with the new one (This config file will be patched). Or press 2 if
you want to preserve your original config file.

Kernel stuff
============

    emerge gentoo-sources
    # ls -l /usr/src/linux
    lrwxrwxrwx    1 root   root    12 Oct 13 11:04 /usr/src/linux -> linux-2.6.19-r5
    cd /usr/src/linux
    make menuconfig 

**I may need to define what there\'s all needed to put into the kernel**

Compile the kernel and modules:

    make && make modules_install

Copy the compiled kernel:

    cp arch/i386/boot/bzImage /boot/config-kernel-2.6.22-gentoo-r9

Copy the config file:

    cp .config /boot/config-kernel-2.6.22-gentoo-r9

If there\'s a need to recompile the kernel:

Be sure that you have copied your previous kernel config to the /boot so
that you may reuse it. After executing make mrproper, the kernel config
in the source tree will be deleted!

    cd /usr/src/linux
    # Clean the tree of a previous compile process
    # Don't forget to keep your good kernel config ".config"
    make mrproper
    # Copy us previous kernel config
    cp /boot/config-kernel-2.6.22-gentoo-r9-c1 .config
    # Configure the kernel
    make menuconfig
    # Compile the kernel and modules
    make && make modules_install
    # Keep the old and created a "cN" where N is us custom revision number
    cp arch/i386/boot/bzImage /boot/config-kernel-2.6.22-gentoo-r9-c1
    cp .config /boot/config-kernel-2.6.22-gentoo-r9-c1

Resources
=========

There are tons of interesting websites or articles dedicated to Gentoo.
You will also find documentation on your Gentoo box, in your source tree
or as an extra package.

- [http://www.gentoo.org](http://www.gentoo.org/) - Official website of Gentoo.
- <http://wiki.gentoo.org> - Official wiki of Gentoo.
- <http://gentoo-wiki.com> - Unofficial (read old) wiki of Gentoo.
- <http://en.wikipedia.org/wiki/Gentoo_Linux>
- See <http://gentoo-wiki.com/HOWTO_Fluxbox>, especially for that nice fluxbox portage generator tool. This is very interesting!
- [Gentoo specific configuration for VirtualBox](http://en.gentoo-wiki.com/wiki/Virtualbox_Guest)
- [Gentoo kde specific guide](http://www.gentoo.org/proj/en/desktop/kde/kde4-guide.xml)
