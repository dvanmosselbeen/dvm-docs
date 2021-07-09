-----
title: Kali
description: This is dedicated to Kali.
created: 09-07-2021 00:00:00
modified: 09-07-2021 00:00:00
keywords: kali, security, network, linux
lang: en
-----

# Introduction

## Services

### SSH server

Eventually reconfigure the server

    dpkg-reconfirgure openssh-server

By default, the openssh-server is installed but is not launched 
automatically at boot time.

    # Start the server
    systemctl start ssh.service
    
    # Stop the server
    systemctl stop ssh.service

To instead permanently enable the SSH service to start whenever the system is booted use:

    systemctl enable ssh.service

To disable it again

    systemctl disable ssh.service

ACTUALLY it's this one:

    systemctl enable ssh.socket
    systemctl start ssh.socket