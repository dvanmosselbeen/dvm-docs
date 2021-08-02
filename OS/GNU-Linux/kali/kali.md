# Kali

## Introduction

Kali is a distribution made for penetration and security testing.

See also all the documentation related to Debian GNU/Linux as Kali is based  on this distribution.

## Interesting tools

Some are installed by default, other not, here is just a list of nice and interesting tools. Making an already installed and another not installed will be painful to maintain in the long run. So here's a mix up.

* `steghide` - steganography hiding tool

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
usermod -aG kaboxer itchy
```

**Log out and log back in so that new user rights (groups) can take effect.**

## Services

### SSH server

Eventually reconfigure the server

```commandline
dpkg-reconfirgure openssh-server
```    


By default, the openssh-server is installed but is not launched  automatically at boot time.

```commandline
# Start the server
systemctl start ssh.socket
    
# Stop the server
systemctl stop ssh.socket
```

To instead permanently enable the SSH service to start whenever the system is booted use:

    systemctl enable ssh.socket

To disable it again

    systemctl disable ssh.socket
