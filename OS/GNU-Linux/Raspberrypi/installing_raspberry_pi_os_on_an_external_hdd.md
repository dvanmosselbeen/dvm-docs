-----
title: Installing Raspberry PI on an external HDD
description: This article is dedicated to the Raspberry PI.
created: 14-10-2020 00:00:00
modified: 14-10-2020 00:00:00
keywords: debian, gnu, linux, operating, system, admin, raspberry, pi
lang: en
-----

Source from but adapted: https://www.makeuseof.com/tag/make-raspberry-pi-3-boot-usb/ to work with Raspberry Pi Model 4 with 4GB ram.

Also interesting information: https://www.maketecheasier.com/boot-up-raspberry-pi-3-external-hard-disk/

# Introduction

So far, i was been able to do this setup successful on a Raspberry Pi Model 4B with an external HDD with his own power supply.
Did not get it working yet on Model 3B as things seems to be slightly different and not sure Model 3B is able to boot without micro SD Card.

See that you have a fresh and full installation of the Raspberry Pi. Not a Noobs installation.

Start with:

    sudo apt-get update
    sudo apt-get upgrade   # very important as older version fail !

Then:

    sudo rpi-update
    
On my first Raspberry Pi 4 i had to use the next branch like the following command. However, as of today 06/11/2020 it feels if i use the next branch.
    
    sudo BRANCH=next rpi-update
    
This will show:

     *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
     *** Performing self-update
     *** Relaunching after update
     *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
     *** We're running for the first time
     *** Backing up files (this will take a few minutes)
     *** Backing up firmware
     *** Backing up modules 5.4.51-v7l+
    ##############################################################
    WARNING: This update bumps to rpi-5.4.y linux tree
    This update will install from the 'next' firmware branch.
    This is being used to test a common firmware for use on all
    models of Raspberry Pi and the 5.4 linux kernel.
    See discussions at:
    https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=267576
    https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=269769
    ##############################################################
    Would you like to proceed? (y/N)

Confirm by pressing `Y`.

This will output:

     *** Downloading specific firmware revision (this will take a few minutes)
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   168  100   168    0     0   1555      0 --:--:-- --:--:-- --:--:--  1570
    100  114M    0  114M    0     0  3274k      0 --:--:--  0:00:35 --:--:-- 2903k
     *** Updating firmware
     *** Updating kernel modules
     *** depmod 5.4.35+
     *** depmod 5.4.35-v8+
     *** depmod 5.4.35-v7+
     *** depmod 5.4.35-v7l+
     *** Updating VideoCore libraries
     *** Using HardFP libraries
     *** Updating SDK
     *** Running ldconfig
     *** Storing current firmware revision
     *** Deleting downloaded files
     *** Syncing changes to disk
     *** If no errors appeared, your firmware was successfully updated to 8fc25f0ca423d50bdb33f332a6b6007f8a8b6ec4
     *** A reboot is needed to activate the new firmware

Then.

    echo program_usb_boot_mode=1 | sudo tee -a /boot/config.txt

Finally, reboot now:

    sudo reboot
    
Once rebooted (the following command does not give me the expected results on Model 4B as i get `17:000008b0`):

    vcgencmd otp_dump | grep 17:

Commend the last line we previously added:

    sudo nano /boot/config.txt
    
Prepare the external HDD drive. Note, we will delete everything on it. Be warned.

    lsblk

Which result in:

    NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda           8:0    0  2.7T  0 disk
    ├─sda1        8:1    0   94M  0 part /media/pi/BOOT
    └─sda2        8:2    0   93G  0 part /media/pi/c109ac91-38f0-46f1-b6b7-14cb7a656b8f
    mmcblk0     179:0    0 28.9G  0 disk
    ├─mmcblk0p1 179:1    0  256M  0 part /boot
    └─mmcblk0p2 179:2    0 28.7G  0 part /

We see that `sda1` and `sda2` is mounted, so we need to unmount it.

    sudo umount /dev/sda1
    sudo umount /dev/sda2

Then again:

    lsblk

Which result in:

    NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda           8:0    0  2.7T  0 disk
    ├─sda1        8:1    0   94M  0 part
    └─sda2        8:2    0   93G  0 part
    mmcblk0     179:0    0 28.9G  0 disk
    ├─mmcblk0p1 179:1    0  256M  0 part /boot
    └─mmcblk0p2 179:2    0 28.7G  0 part /

Now:

    sudo parted /dev/sda

Delete everything on the HDD:

    mktable msdos

Create the different partitions. Note that we don't use the full HDD capacity. This can be adjusted later on. (NOTE: Copy & paste of this in the console can fails) 

    mkpart primary fat32 0% 100M
    mkpart primary ext4 100M 100G

Then show the information of our changes:  
    
    print

Which result in:

    Model: TOSHIBA External USB 3.0 (scsi)
    Disk /dev/sda: 2000GB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:
    
    Number  Start   End     Size    Type     File system  Flags
     1      1049kB  99.6MB  98.6MB  primary  fat32        lba
     2      99.6MB  100GB   99.9GB  primary  ext4         lba

Use `CTRL+C` to exit this or type in `quit`.

Create the Filesystems:

    sudo mkfs.vfat -n BOOT -F 32 /dev/sda1
    sudo mkfs.ext4 /dev/sda2

Now mount the new partitions and copy files of the micro SD card to the external HDD:

    sudo mkdir /mnt/target
    sudo mount /dev/sda2 /mnt/target/
    sudo mkdir /mnt/target/boot
    sudo mount /dev/sda1 /mnt/target/boot/
    sudo apt-get update; sudo apt-get install rsync
    sudo rsync -ax --progress / /boot /mnt/target

Copying the files will take a few minutes. Not so long actually.

Then:

    cd /mnt/target
    sudo mount --bind /dev dev
    sudo mount --bind /sys sys
    sudo mount --bind /proc proc
    sudo chroot /mnt/target
    rm /etc/ssh/ssh_host*
    dpkg-reconfigure openssh-server
    exit
    sudo umount dev
    sudo umount sys
    sudo umount proc

Now adjust the following file: `/mnt/target/boot/cmdline.txt`:

    console=serial0,115200 console=tty1 root=PARTUUID=d218e2cd-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles

To something similar to this (note the `/dev/sda2`):

    console=serial0,115200 console=tty1 root=/dev/sda2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles

The same with: `/mnt/target/etc/fstab`. From this:

    proc            /proc           proc    defaults          0       0
    PARTUUID=d218e2cd-01  /boot           vfat    defaults          0       2
    PARTUUID=d218e2cd-02  /               ext4    defaults,noatime  0       1
    # a swapfile is not a swap partition, no line here
    #   use  dphys-swapfile swap[on|off]  for that

To somethings like this:

    proc            /proc           proc    defaults          0       0
    /dev/sda1  /boot           vfat    defaults          0       2
    /dev/sda2  /               ext4    defaults,noatime  0       1
    # a swapfile is not a swap partition, no line here
    #   use  dphys-swapfile swap[on|off]  for that

The system should be now ready:

    cd ~
    sudo umount /mnt/target/boot
    sudo umount /mnt/target
    sudo poweroff

Once turned of, first remove the power source before removing the micro SD card !!!

After removed the micro SD card and trying to boot of the external HDD i get an error like this:

    usb-msb boot require newer software
    
After a search on the internet, i found this website with information i adjusted to my needs: https://yaleman.org/post/2020/2020-08-20-raspberry-pi-usb-boot-usb-msd-boot-requires-newer-software/

So first we need to remount our stuff:

    sudo mkdir /mnt/target
    sudo mount /dev/sda2 /mnt/target/
    sudo mkdir /mnt/target/boot
    sudo mount /dev/sda1 /mnt/target/boot/

Now:

    git clone --depth 1 https://github.com/raspberrypi/firmware

    cd firmware/boot
    
    cp -R * /mnt/target/boot
    
Unmount everything and reboot

    sudo umount /mnt/target/boot
    sudo umount /mnt/target
    sudo poweroff

Now this working like expected and able to boot without a micro SD card. 
Note that the screen resolution seems to be different since i'm booting from the external HDD. Previously it was in 4K resolution i think and now I have some big black borders on the edges. And looking too `Start Menu` > `Preferences` > `Screen Configurator` > `Screen Resolution`. And there in this new Windows, `Configure` > `Screen` > `Default` > `Resolution`.

Update about screen resolution & `/dev/net/tun` issue. After some time (30/10/2020), i got some kernel and firmware related updates (`sudo apt-get update; sudo apt-get upgrade`) which fixed the screen resolution and the issue i had to run openvpn (system did not wanted to create `/dev/net/tun`). 

    ERROR: Cannot open TUN/TAP dev /dev/net/tun: No such device (errno=19)
    Exiting due to fatal error

# Adjust the swap size

It is very important to adjust the swap size as the default size of 100MB can give a lot of issues when doing resource intensive tasks. A to small size cal

    nano /etc/dphys-swapfile

And change the value of `CONF_SWAPSIZE` to 2GB for example:

    CONF_SWAPSIZE=2048

# Resources

* https://www.makeuseof.com/tag/make-raspberry-pi-3-boot-usb/
* https://www.maketecheasier.com/boot-up-raspberry-pi-3-external-hard-disk/
* https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/
* https://www.tomshardware.com/how-to/boot-raspberry-pi-4-usb
