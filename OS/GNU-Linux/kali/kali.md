# Kali

## Table of Contents

- [Introduction](#introduction)
- [Interesting tools](#interesting-tools)
- [Updating Kali](#updating-kali)
- [User management](#user-management)
- [Services](#services)
  - [SSH server](#ssh-server)
- [Resources](#resources)

## Introduction

`Kali` is a distribution based on the [GNU/Linux Debian distribution](https://www.debian.org), but made for penetration and security testing.

See also all the documentation related to [Debian GNU/Linux](../Debian/debian.md) as Kali is based on this distribution. Therefore, this document page will only contain specific information regarding `Kali`. 

## Interesting tools

Here's a list of some programs that might be interesting to install on top of the base installation of `Kali`. Note that some apps, like the `sectlists` is very big; around `386MB` to download and whatever once extracted. Some other applications, like `fail2ban`, `htop`, `rlwrap`, `tmux`, `xclip`, `filezilla` etc. are in my opinion a must-have and should be available in a default install.

```
fail2ban
beef
default-mysql-client
dsniff
gobuster
gvim-gtk3
hexedit
htop
remmina
rlwrap
seclists
steghide
tmux
xclip
zenmap-kbx
filezilla
monit
```

## Updating Kali

After a fresh installation:

```commandline
apt-get update
apt full-upgrade -y
```

Later on:

```commandline
apt-get update
apt-get upgrade
```

Do not forget to time by time:

```commandline
sudo apt autoremove
sudo apg-get clean
```

## User management

Fot this example I will create a new user called `itchy`.

Create a new user:

```commandline
adduser itchy
```

Add new user to the different groups:

```commandline
usermod -aG sudo itchy
usermod -aG cdrom itchy
usermod -aG floppy itchy
usermod -aG sudo itchy
usermod -aG audio itchy
usermod -aG dip itchy
usermod -aG video itchy
usermod -aG plugdev itchy
usermod -aG netdev itchy
usermod -aG bluetooth itchy
usermod -aG scanner itchy
```

**Log out and log back in so that new user rights (groups) can take effect.**

## Services

### SSH server

Eventually start with reconfigure the server:

```commandline
dpkg-reconfirgure openssh-server
```    

By default, the `openssh-server` is installed but is not launched automatically at boot time. This has it is reason as this is about a penetration machine, and running services at boot time, means more open ports on the machine. So it is maybe wise to not let start the SSH Server at boot time.

```commandline
# Start the server
systemctl start ssh.socket
    
# Stop the server
systemctl stop ssh.socket
```

To permanently enable the SSH service to start whenever the system is booted use:

    systemctl enable ssh.socket

To disable it again

    systemctl disable ssh.socket

## Special Configuration

### Happy Hacking Keyboard Lite 2

In the start `menu > Settings > Keyboard`. In that new window set the settings as following: 

![alt text](imgs/hhkb-lite2-config.png "Happy Hacking Keyboard Lite 2 layout configuration")

As indicated too, switching / cycling between the different keyboard layouts, we can press both shift keys, followed by `CTRL`.

## Resources

- <https://www.kali.org>
- <https://tools.kali.org>
- <https://forums.kali.org>
- <https://www.kali.org/docs/>
- <https://www.kali.org/get-kali/#kali-mobile>
- <https://www.offensive-security.com>
- <https://www.offensive-security.com/metasploit-unleashed/>
- <https://www.exploit-db.com>
- <https://www.exploit-db.com/google-hacking-database>
