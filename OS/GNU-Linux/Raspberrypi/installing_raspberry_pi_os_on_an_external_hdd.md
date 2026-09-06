# Installing Raspberry Pi on an external HDD 

## Table of Contents

 - [Introduction](#introduction)
 - [Install Process](#install-process)
 - [Adjust the swap size](#adjust-the-swap-size)
 - [Resources](#resources)

## Introduction

**IMPORTANT NOTE**: As of today `september 2, 2026`, this document here is a bit useless. As with an up to date `Raspberry Pi model 4` or newer, with an up-to-date firmware, we do not need to do all these steps manually.

We could just boot up `Raspberry Pi` without `Micro SD` card, with the `RJ45` network cable connected and an attached external HDD and start a `Netinst`. The installer is able to download everything from the internet and install it directly to the external HDD. No need for a `Micro SD` card or do any setup. Just keep `Shift` pressed while you boot up and start the `NetInstall` installer and follow the instructions on screen. I did this for my 2 different `Raspberry Pi Model 4` with a `4 GB RAM` and `8GB RAM` and installed the Debian GNU/Linux operating system as a server, and `Ubuntu` desktop version on the other one to use it as a compact desktop computer.

Source from but adapted: <https://www.makeuseof.com/tag/make-raspberry-pi-3-boot-usb/> to work with `Raspberry Pi Model 4` with 8GB RAM.

Also interesting information: <https://www.maketecheasier.com/boot-up-raspberry-pi-3-external-hard-disk/>

So far, I have been able to do this setup successful on a `Raspberry Pi Model 4B` with an external HDD with its own power supply and with an HDD without extra power supply. Did not get it working yet on `Model 3B` as things seems to be slightly different and not sure `Model 3B` is able to boot without micro SD Card.

## Install Process

See that you have a fresh and full installation of the ``Raspberry Pi``. Not a ``Noobs`` installation.

Start with:

    sudo apt-get update
    sudo apt-get upgrade   # very important as older version fail !

Then we will update the firmware of the ``Raspberry Pi``. **Note that it could be that we manually need to delete the firware files so that the firware files are also writen on the chipset of the Raspberry Pi. The rpi-update command give instructions and tells which files to delete to force a full firmware update**:

    sudo rpi-update

This will output:

````commandline
root@raspberry2026a:/home/dvanmosselbeen# rpi-update
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
 *** Performing self-update
 *** Relaunching after update
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
FW_REV:49615803a10fdcd4cea13121972630ca94edeb0a
BOOTLOADER_REV:86759b04b22173e10186139ac3ae4debcd0d7252
 *** We're running for the first time
 *** Backing up files (this will take a few minutes)
 *** Backing up firmware
 *** Backing up modules 6.18.34+rpt-rpi-v8
WANT_32BIT:0 WANT_64BIT:1 WANT_64BIT_RT:0 WANT_PI4:1 WANT_PI5:1

Updating a system with initramfs configured is not supported by rpi-update.
If your system relies on drivers provided by the initramfs (e.g. custom filesystem options)
it may not boot without regenerating the initramfs.
If you are unsure, test if your system boots with initramfs options disabled from config.txt

Would you like to proceed? (y/N)
````

After pressing the ``y`` key to confirm to continue, this will output the following:

````commandline
Github API request failed with HTTP 422: https://api.github.com/repos/raspberrypi/rpi-firmware/commits/0
##############################################################
WARNING: This update bumps to rpi-6.18.y linux tree
See discussions at:
https://forums.raspberrypi.com/viewtopic.php?t=394580
##############################################################
Would you like to proceed? (y/N)
````

After pressing the ``y`` key to confirm to continue, this will output the following:

````commandline
Downloading bootloader tools
Downloading bootloader images
 *** Downloading specific firmware revision (this will take a few minutes)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  167M  100  167M    0     0  27.8M      0  0:00:06  0:00:06 --:--:-- 27.9M
*** PREPARING EEPROM UPDATES ***

BOOTLOADER: update available
   CURRENT: Sun 17 May 19:13:18 UTC 2026 (1779045198)
    LATEST: Tue  4 Aug 12:38:13 UTC 2026 (1785847093)
   RELEASE: latest (/usr/lib/firmware/raspberrypi/bootloader-2711/latest)
            Use raspi-config to change the release.

  VL805_FW: Using bootloader EEPROM
     VL805: up to date
   CURRENT: 000138c0
    LATEST: 000138c0
   CURRENT: Sun 17 May 19:13:18 UTC 2026 (1779045198)
    UPDATE: Tue  4 Aug 12:38:13 UTC 2026 (1785847093)
    BOOTFS: /boot/firmware
'/tmp/tmp.Ps4gdCJA2z' -> '/boot/firmware/pieeprom.upd'
Copying recovery.bin to /boot/firmware for EEPROM update

EEPROM updates pending. Please reboot to apply the update.
To cancel a pending update run "sudo rpi-eeprom-update -r".
 *** Updating firmware
 *** Updating kernel modules
 *** depmod 6.18.46-v8-rt+
 *** depmod 6.18.46-v8-16k+
 *** depmod 6.18.46-v8+
 *** Updating VideoCore libraries
 *** Running ldconfig
 *** Storing current firmware revision
 *** Deleting downloaded files
 *** Syncing changes to disk
 *** If no errors appeared, your firmware was successfully updated to 49615803a10fdcd4cea13121972630ca94edeb0a
 *** A reboot is needed to activate the new firmware
````

*On my first ``Raspberry Pi 4`` I had to use the next branch like the following command. However, as of today ``06/11/2020`` it feels if i use the next branch.*
    
    sudo BRANCH=next rpi-update
    
This will show:

````commandline
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
````

This will output:

````commandline
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
````

Then.

    echo program_usb_boot_mode=1 | sudo tee -a /boot/firmware/config.txt

Finally, reboot now:

    sudo reboot
    
Once rebooted (the following command does not give me the expected results on ``Model 4B`` as I get `17:000008b0`):

    vcgencmd otp_dump | grep 17:

DEPRECATED (DO NOT DO): Comment out the last line we previously added:

    sudo nano /boot/firmware/config.txt
    
Prepare the external HDD drive. We can now connect the external HDD. (For the moment, I Only tested with an external HDD with it's own power supply).

Note, we will delete everything on it. Be warned!!!

    lsblk

Which result in:

````commandline
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0    2G  0 loop
sda           8:0    0  2.7T  0 disk
├─sda1        8:1    0   94M  0 part /media/dvanmosselbeen/BOOT
└─sda2        8:2    0   93G  0 part
mmcblk0     179:0    0 29.8G  0 disk
├─mmcblk0p1 179:1    0  512M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 29.3G  0 part /
zram0       254:0    0    2G  0 disk [SWAP]
````


We see that `sda1` is mounted, so we need to unmount it.

    umount /media/dvanmosselbeen/BOOT

Then again, just for verification:

    lsblk

Which result in:

````commandline
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0    2G  0 loop
sda           8:0    0  2.7T  0 disk
├─sda1        8:1    0   94M  0 part
└─sda2        8:2    0   93G  0 part
mmcblk0     179:0    0 29.8G  0 disk
├─mmcblk0p1 179:1    0  512M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 29.3G  0 part /
zram0       254:0    0    2G  0 disk [SWAP]
````

We can now create the needed partitions on the external HDD. So now executed the parted command on the external HDD. We will get into the parted command line:

    parted /dev/sda

Delete everything on the HDD. This can not be undone, be sure what you are doing:

    mktable msdos

We get the warning that the data will be destroyed on the external HDD. Enter ``Yes`` to continue:

````commandline
Warning: The existing disk label on /dev/sda will be destroyed and all data on this disk will be lost. Do you want to continue?
Yes/No?
````

After entering ``Yes``, we do not have additional information, we get back on the parted command line interface:

````commandline
(parted)
````

Create the different partitions. Note that we don't use the full HDD capacity. This can be adjusted later on. (NOTE: Copy & paste of this in the console can fail). This is a ``3 TB Hard Disk Drive``, we use 500M for the boot partition and ``200GB`` for the second partition. Later on we can create more partitions if needed.

    mkpart primary fat32 0% 500M
    mkpart primary ext4 500M 200G

Then show the information of our changes:  
    
    print

This will output:

````commandline
Model: Seagate Expansion Desk (scsi)
Disk /dev/sda: 3001GB
Sector size (logical/physical): 512B/4096B
Partition Table: msdos
Disk Flags:

Number  Start   End    Size   Type     File system  Flags
 1      1049kB  500MB  499MB  primary  fat32        lba
 2      500MB   200GB  199GB  primary  ext4

(parted)
````

Use `CTRL+C` to exit this or type in `quit`. After we quit, we receive the following information:

````commandline
Information: You may need to update /etc/fstab.
````

Create the Filesystems:

````commandline
mkfs.vfat -n BOOT -F 32 /dev/sda1
mkfs.ext4 /dev/sda2
````

This is the output of the previous 2 commands. Just for informational purposes:

````commandline
root@raspberry2026a:/home/dvanmosselbeen# mkfs.vfat -n BOOT -F 32 /dev/sda1
mkfs.fat 4.2 (2021-01-31)
root@raspberry2026a:/home/dvanmosselbeen# mkfs.ext4 /dev/sda2
mke2fs 1.47.2 (1-Jan-2025)
Creating filesystem with 48706048 4k blocks and 12181504 inodes
Filesystem UUID: cc1fa709-ff5e-4210-a0f1-566f954e2a59
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done
Writing inode tables: done
Creating journal (262144 blocks): done
Writing superblocks and filesystem accounting information: done
````

Now mount the new partitions and copy files of the micro SD card to the external HDD:

````commandline
mkdir /mnt/target
mount /dev/sda2 /mnt/target/
mkdir /mnt/target/boot
mount /dev/sda1 /mnt/target/boot/
# apt-get update; sudo apt-get install rsync
rsync -ax --progress / /boot /mnt/target
````

Copying the files will take a few minutes. This will output a bunch of information to the terminal, as we used the ``--progress`` flag of ``rsync``. Just need to see that there's no error message on the end. I say this as of today, september 2, 2026 I originally created a 100MB boot partition, but this seemed to be too small. While a few years ago, ``100MB`` was more than enough.

All the data from the ``Micro SD`` card is now copied to our external HDD. But we need to delete the ssh keys of the ssh server and generate new host keys for the ``sshd`` server:

````commandline
cd /mnt/target
mount --bind /dev dev
mount --bind /sys sys
mount --bind /proc proc
chroot /mnt/target
rm /etc/ssh/ssh_host*
dpkg-reconfigure openssh-server
exit
umount dev
umount sys
umount proc
````

Now adjust the following file: `/mnt/target/boot/cmdline.txt`:

    console=serial0,115200 console=tty1 root=PARTUUID=d218e2cd-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles

To something similar to this (note the `/dev/sda2`):

    console=serial0,115200 console=tty1 root=/dev/sda2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles

**REMARKS: The content of the file `/mnt/target/boot/cmdline.txt` says that this file moved to `/mnt/target/boot/firmware/cmdline.txt` , but that file does not exist there. So I did not do this previous step.**

The same with: `/mnt/target/etc/fstab`. From this:

````commandline
proc            /proc           proc    defaults          0       0
PARTUUID=49011ac8-01  /boot/firmware  vfat    defaults          0       2
PARTUUID=49011ac8-02  /               ext4    defaults,noatime  0       1
````

To something like this:

````commandline
proc            /proc           proc    defaults          0       0
/dev/sda1  /boot/firmware  vfat    defaults          0       2
/dev/sda2  /               ext4    defaults,noatime  0       1
````

The system should be now ready:

````commandline
cd ~
umount /mnt/target/boot  # Got info that it was not mounted
umount /mnt/target
poweroff
````

Once turned off, first remove the power source before removing the micro SD card !!!

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

## Adjust the swap size

It is very important to adjust the swap size as the default size of 100MB can give a lot of issues when doing resource intensive tasks. A to small size cal

    nano /etc/dphys-swapfile

And change the value of `CONF_SWAPSIZE` to 2GB for example:

    CONF_SWAPSIZE=2048

## Resources

* https://www.makeuseof.com/tag/make-raspberry-pi-3-boot-usb/
* https://www.maketecheasier.com/boot-up-raspberry-pi-3-external-hard-disk/
* https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/
* https://www.tomshardware.com/how-to/boot-raspberry-pi-4-usb
