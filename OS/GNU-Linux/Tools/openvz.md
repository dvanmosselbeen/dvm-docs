# Openvz Reference

## Introduction

This article talk about another great application to run virtual computers. It\'s similar like `qemu` in a way, but it's many more, it's more comparable to`Xen` or `vmware` server.

## Installing openvz

This is probably the most easiest virtual computing system to setup and to use. It's peace of cake!

Get the kernel image of the openvz website <http://download.openvz.org/kernel/debian/etch/> and install it with:

    dpkg -i linux-image-2.6.18-openvz-686_028test007.1d2-2_i386.deb

Once the kernel image installed, reboot your computer and use that `openvz`kernel.

## Setting up a virtual machine

Download a template distribution , the easiest way to start. See <http://download.openvz.org/template/precreated/> i took the debian-3.1-i386-minimal.tar.gz and place it in `/var/lib/vz/templates/cache/`

Then make a little script so that you can easy start the virtual computer, i call it `debian_vmcreate.sh`:

    #!/bin/bash
    vzctl create 103 --ostemplate debian-3.1-i386-minimal --config vps.basic
    vzctl set 103 --onboot yes --save
    vzctl set 103 --hostname debian01.jjbit.local --save
    vzctl set 103 --ipadd 192.168.0.8 --save
    vzctl set 103 --numothersock 120 --save
    vzctl set 103 --nameserver 192.168.0.3 --save
    vzctl set 103 --privvmpages 128000:192000 --save # give it some memory CHECKME
    vzctl start 103
    vzctl exec 103 passwd

*NOTE: The virtual machine will get the ip `192.168.0.8`. The host computer have the ip address `192.168.0.3`. We need to install `dnsmasq` on the host computer if we want to have internet in the virtual computer.*

    aptitude install dnsmasq

There is nothing to setup nor need to restart something to get `dnsmasq`working.

We have given the id `103` to this virtual computer. We come back to the id a bit later in this article.

Make the previously created script executable:

    chmod a+x debian_vmcreate.sh

Start the script as root user:

    ./debian_vmcreate.sh

To go in the virtual computer, in a console type:

    vzctl enter 103

And you enter the virtual computer, it ask you to enter a root password.

We have now create a virtual computer with the id `103`.

To get a overview of all running virtual computer:

    vzlist

We can look to the performance of the virtual computer with:

    vzctl exec 103 cat /proc/user_beancounters

That output:

    Version: 2.5
           uid  resource           held    maxheld    barrier      limit   
          103:  kmemsize         854285    1036426    2752512    2936012   
                lockedpages           0          0         32         32   
                privvmpages       11432      13025     128000     192000   
                shmpages           1280       1296       8192       8192   
                dummy                 0          0          0          0   
                numproc              16         21         65         65   
                physpages          3125       3889          0 2147483647   
                vmguarpages           0          0       6144 2147483647   
                oomguarpages       3125       3889       6144 2147483647   
                numtcpsock            3          3         80         80   
                numflock              4          6        100        110   
                numpty                3          3         16         16   
                numsiginfo            0          3        256        256   
                tcpsndbuf          4464      11160     319488     524288   
                tcprcvbuf             0       8560     319488     524288   
                othersockbuf       2232       6696     132096     336896   
                dgramrcvbuf           0          0     132096     132096   
                numothersock          4          7        120        120   
                dcachesize            0          0    1048576    1097728   
                numfile             435       1347       2048       2048   
                dummy                 0          0          0          0   
                dummy                 0          0          0          0   
                dummy                 0          0          0          0   
                numiptent            10         10        128        128

In `/var/lib/vz/private/<id>` we see all the files of the virtual computer. That output:

    bin  boot  dev  etc  home  initrd  lib  media  mnt  opt  
    proc  root  sbin  srv  sys  tmp  usr  var

Stopping the vm:

    vzctl stop <id>

Delete the configuration of a virtual machine:

    vzctl destroy <id>

## Installing a graphical environment

In this article i install a lightweight graphical environment.

    aptitude install x-window-system-core discover read-edid mdetect && \
    dpkg --force-depends -P xserver-xfree86 && aptitude install \
    xserver-xfree86 fluxbox fluxconf xdm

Note, the `fluxbox`,`fluxconf` and `xdm` are optional. I choice these because these are very light, and because O like it so much `fluxbox` :-)

## Installing a vncserver inside the virtual computer

In this article i use `tightvncserver`. It\'s very easy to setup and to use.

## tightvnc server side

    aptitude install tightvncserver

Start the vncserver:

    vncserver :0

It ask you to enter a password and you need to confirm the password.

## tightvnc client side

We need to install a vnc viewer to make a connection to a vnc server.

    aptitude install xtightvncviewer

Make a connection to the virtual computer.

    xtightvncviewer 192.168.0.8

Enter the password.

A window goes open and you get your desktop.

## Remarks

I have hit the quota bug while playing with the `openvz` :-s Default there is a quota limit of 1 GB for the virtual computers. That have block me when i tried the `gentoo` stage 3 template. The problem is fixed in a recent version of the`vzquota`. (I need to research the exact number of the app).

## Resources

- <http://openvz.org>
- <http://www.howtoforge.com/debian_etch_openvz>
- <http://wiki.openvz.org/>
- <http://howtoforge.com/installing-and-using-openvz-on-debian-etch>

Please leave a comment if you think there should be more information or if you have some additional questions.
