-----
title: LFS Reference
description: My little Linux From Scratch Reference
created: 18-01-2008 00:00:00
modified: 18-01-2008 00:00:00
keywords, gnu, linux, kernel, programming
lang: en
-----

# LFS Reference

This page talk about the Linux From Scratch and Beyond Linux From
Scratch

**Merge the info of \~/Docs/local\_svn/shared\_codes/lfs/notes**

## Introduction


This page is not going to replace the great documentation of the Linux
From Scratch project and Beyond Linux From Scratch, but provide some
addition notes.

Before starting this procedure and install the whole LFS on a computer,
i can suggest to first experiment in a virtual computer. This will avoid
that you are blocked at some stage, without network for example. If you
have a spare computer, then you probably don\'t want to do this in a
virtual machine. I usevmware-server for this test here, because it\'s
fee to use and is fast. Not that i recommend, or want that you use
vmware-server!

## Using the Live CD

At the time of writing this page, i used the live
CDlfslivecd-x86-6.3-r2145.iso. Using the LFS live cd has some
advantages. You are sure the install process should not fail. The
sources packages needed for the LFS setup are available on the CD. Even
the book is on the Live CD.

If needed boot up the CD with:

    linux acpi=off

Otherwise, just press enter.

You will then be asked for some things:

- Configure system clock: Europe/Brussels.
- Is the system clock set to locat time or GMT?: Localtime
- Regional settings: Dutch (Belgium, UTF-8).
- Confirm: Locale: en\_US.UTF-8

*If we don\'t set the locale to en\_US.UTF-8. All the messages will be
in Dutch.*

Like noted on the first screen, you can come back to that little LFS
help screen with entering the command greeting.

We first setup the network with the net-setup tool

Or you can do it manually with:

Check first with ifconfig -a if the card has been detected. If not,
check with dmesg.

    ifconfig eth0 192.168.0.10
    ifconfig eth0 up
    route add default gw 192.168.0.20 eth2
    # The network should be ok and we may able to ping another host
    ping 192.168.1.9

Set the root password:

    passwd

Start the ssh server

    /etc/rc.d/init.d/sshd start

If you want you can start a X session with startxfce.

If you don\'t have change the locale language to English, you can set it
with:

    LANG=en_US.UTF-8

Now that the live cd is up and running, i recommend to make use of
screen. If you don\'t have any experience with screen, i suggest to read
my \[screen\] (screen) page. screen is a must have and must know tool!

## Copying the needed sources from the live CD

Like the sources and patches are on the live CD, we don\'t need to
download these from the net. But instead, copy these the the
/mnt/lfs/sources.

    cp /lfs-sources/* $LFS/sources

## The Standard Build Unit SBU check

    time { CC="gcc -B/usr/bin/" ../binutils-2.17/configure --prefix=/tools \
        --disable-nls --disable-werror && make && make install; }

That output:

    real    5m5.309s
    user    1m18.132s
    sys     3m32.346s

To list directory, to easy remove it:

    find ! -name '*.bz2' ! -name '*.gz' ! -name "*.patch"

Follow the instructions like noted in the book till chapter 6.

## Using software to track installed files with paco

I use \[paco\] (<http://paco.sourceforge.net/>) to track the files i
install when compiling some software from source. This tool help me to
see where the files are been installed. paco also provide some tools to
make it easy to install the same stuff on another computer.

Just before 6.7. Linux-2.6.22.5 API Headers, install paco.

If you are already in the chroot environment, you need to download with
wgetfrom another console that is not in the chroot. Download maybe the
pacostuff in the /mnt/lfs/sources.

    tar xf paco-2.0.3.tar.bz2
    cd paco-2.0.3
    ./configure --prefix=/usr --sysconfdir=/etc/paco --disable-gpaco --enable-scripts
    make
    make install
    make logme

You should now need to pass all these make install && cp foo /bin/bar
stuff to paco. See the \[paco\] (paco) page for more informations about
the usage of paco. Paco does not the black magic of his own, you need to
tell him what to log.

Say now, for 6.7.1. Installation of Linux API Headers of the LFS book.
If we don\'t make use of paco we should normally do:

    sed -i '/scsi/d' include/Kbuild
    make mrproper
    make headers_check
    make INSTALL_HDR_PATH=dest headers_install
    cp -rv dest/include/* /usr/include

Instead of this, we will track the files with paco. In this case, it\'s
only about copying some files to /usr/include.

    paco -lp linux-api-headers-2.6.22.5 "cp -rv dest/include/* /usr/include"

Let\'s show another example. 6.8. Man-pages-2.63 of the book:

    paco -lD "make install"

This took the current parent directory as package name. That\'s what you
probably go to use with the most software you will install during a
LFSsetup.

You will see that during the LFS setup, you need to reinstall an
application to give him some additional support. Say for vim, once you
are at the BLFSpart, you probably want to reinstall vim with the GTK
support. Keep in mind that paco will not log all files, because some
where already logged. So for some packages, you should need to first
remove it of your system and install it again.

## Locales

In chapter 6.9. Glibc-2.5.1 i added some more locales:

    paco -lp+ glibc-2.5.1 "localedef -i nl_BE -f UTF-8 nl_BE"
    paco -lp+ glibc-2.5.1 "localedef -i fr_BE -f UTF-8 fr_BE"

Or you could run the follow command to install all locales at once:

    make localedata/install-locales

## Some other extra info during the LFS setup

### vim

    tar xf vim-7.1.tar.bz2
    tar xf vim-7.1-lang.tar.gz

then

    cd vim71

### Kernel compiling

    make LANG=nl_BE.utf8 LC_ALL= menuconfig

Like i have setup this LFS install in vmware. Some additional modules
needs to be build. One important is the scsi device. Otherwise the
system won\'t boot up.

*Note that i not mention the options that where activated by default.*

For the scsi control, select there all to by build-in (\*):

    Device Drivers  ---> Fusion MPT device support  --->

For the network card:

    Device Drivers  ---> Network device support  ---> Ethernet (10 or 100Mbit)  --->

And select there AMD PCnet32 PCI support eventually to be build-in.

    Loadable module support  --->

And select:

    Automatic kernel module loading
    Processor type and features  ---> \
        Processor family (Pentium-III/Celeron(Coppermine)/Pentium-III Xeon)  --->

Change this to:

    Pentium-4/Celeron(P4-based)/Pentium-4 M/older Xeon
    Processor type and features  ---> High Memory Support (off)  --->

CD-ROM-DVD fs:

    File systems  ---> CD-ROM/DVD Filesystems  --->

and there:

    Microsoft Joliet CDROM extensions
    Transparent decompression extension
    UDF file system suppor

## Before rebooting

Before ending the LFS part of the book, there\'s a few extra packages i
install. Like wget, screen and ssh. See the BLFS book.

## After the reboot

If the system boot up, as first, i\'m happy :-p Not that it is hard to
get the whole procedure done right.

Like i used paco, i first check if there\'s not some unwanted data in
the database of paco. Some files that paco has track of the /sources and
thatpaco has put it in his database.

    egrep -R "/sources" /var/log/paco | less

And then delete some lines \...

## BLFS part

Like i installed the LFS in a virtual computer, it\'s easy to copy and
paste the needed directory. Once you add this to vmware and start it you
get this:

    The location of this virtual machine's configuration file has changed since
    it was last powered on.
    If the virtual machine has been copied, you should create a new unique identifier
    (UUID).  If it has been moved, you should keep its old identifier.
    If you are not sure, create a new identifier.
    What do you want to do?

You should need to create a new identifier. So that you get another
hardware mac address. Once you boot up, you will discover that the
network device eth0has gone and that you now have the eth1.

You need to modify the file /etc.udev.rules.d/70-persisten-net.rules.
You can eventually remove the SUBSYSTEM line for the eth0 and then
change the line that left. The content of the NAME variableto eth0.

You probably want to change the ip too.
See/etc/sysconfig/network-devices/ifconfig.eth0/ipv4.

You should also change the hostname /etc/sysconfig/network and
/etc/hosts.

Then reboot and watch if everything is been ok now.

### zsh

Install PCRE-6.7 first!

    ./configure --prefix=/usr --enable-pcre \
                --sysconfdir=/etc/zsh \
                --enable-etcdir=/etc/zsh &&
    make

Then:

    paco -lD "make install"
    mv /usr/bin/zsh* /bin/

Then:

    cat >> /etc/shells << "EOF"
    /usr/bin/zsh
    /usr/bin/zsh-4.2.6
    EOF

Then i copy my own .zsh\* and .zlogout files to the root\'s (and other
user\'s) home directory.

Change the default shell for the wanted users:

    chsh

## Some other useful things

Some other useful things that are specific or not to the LFS setup.

    readelf -l /bin/gzip | grep interpret

Log all output of a command, including errors:

    command > output.txt 2>&1

## See for

-   glibc stuff
    -   ldconfig - Configures the dynamic linker runtime bindings
    -   ld - Does this been exist??
    -   ldd - Reports which shared libraries are required by each given
        program or shared library
    -   locale - Prints various information about the current locale
    -   localedef - Compiles locale specifications
    -   xtrace - Traces the execution of a program by printing the
        currently executed function
    -   getconf - Displays the system configuration values for file
        system specific variables
    -   getent - Gets entries from an administrative database
-   binutils stuff

    -   ld - A linker that combines a number of object and archive files
        into a single file, relocating their data and tying up symbol
        references
    -   readelf - Displays information about ELF type binaries
    -   strip - Discards symbols from object files

-   Building a static library

## Starting stopping services

    /etc/rc.d/init.d/network restart

## Resources

- <http://www.linuxfromscratch.org/>

## LFS artwork

- [http://www.linuxfromscratch.org/\~gerard/lfslogos/](http://www.linuxfromscratch.org/%7Egerard/lfslogos/)
- <http://berzerkula.no-ip.org/>
- <http://cblfs.cross-lfs.org/index.php/Main_Page>

## Interesting hints

- [mail server setup](http://www.linuxfromscratch.org/hints/downloads/files/mail.txt)
- [managing multiple kernels](http://www.linuxfromscratch.org/hints/downloads/files/multi-kernel-versions.txt)
- [Paco](http://www.linuxfromscratch.org/hints/downloads/files/paco.txt)
- [7-zip](http://www.linuxfromscratch.org/hints/downloads/files/lzma.txt)
- [ipsec](http://www.linuxfromscratch.org/hints/downloads/files/ipsec.txt)
- [elf](http://www.linuxfromscratch.org/hints/downloads/files/prelink.txt)
- [bootsplash](http://www.linuxfromscratch.org/hints/downloads/files/bootsplash.txt)
- [small lfs](http://www.linuxfromscratch.org/hints/downloads/files/small-lfs.txt)
- [start stop resume an LFS setup](http://www.linuxfromscratch.org/hints/downloads/files/stages-stop-and-resume.txt)
- [package manager system](http://www.linuxfromscratch.org/hints/downloads/files/more_control_and_pkg_man.txt)
- [trip package manager](http://www.linuxfromscratch.org/hints/downloads/files/package_management_using_trip.txt)
- [crablfs python package manager](http://www.linuxfromscratch.org/hints/downloads/files/crablfs.txt)
- [logrotate](http://www.linuxfromscratch.org/hints/downloads/files/logrorate.txt)
- [wpa](http://www.linuxfromscratch.org/hints/downloads/files/wpa-service.txt)
- [LFS cd remastering howto](http://www.linuxfromscratch.org/hints/downloads/files/lfscd-remastering-howto.txt)
- [full hints list](http://www.linuxfromscratch.org/hints/list.html)

## Mirrors

- <http://ftp.osuosl.org/pub/lfs/>

## Things to check for

- 7.6. Configuring the Linux Console - Check to setup the console
    according to the locales.
