# minidnla

# Table of Contents

- Introduction
- Installing minidnla
- Configuring minidnla
- Check the build in minimalistic website
- Resources

# Introduction

(also known as ReadyMedia) is a lightweight, open-source DLNA/UPnP-AV media server designed to stream video, audio, and photo files to compatible network devices.

Wide Compatibility: Works seamlessly with smart TVs (Samsung, LG, Sony), game consoles (PlayStation, Xbox), media players (Kodi, VLC), and mobile apps.

**Note that minidnla only work over local network and does not work over the internet. You need to make use of a VPN if you want to make use of it over the Internet.**

# Installing minidnla

Installing minidnla is as simple as:

    sudo apt install minidnla

# Configuring minidnla

We have to edit the configuration file:

   sudo nano /etc/minidnla.conf

The configure file have a lot of comments and is easy to configure. What we mainly need to adjust is where our different source files are located for ou audio, videos and pictures. This is done with the media_dir variable.

minidnla runs by default on port 8200 and it could be this port is already in use. So we should use another port. 8201 is a good alternative.

If we want to run minidnla as a service and make it start automatically at boot time:

    sudo systemctl enable minidnla

Start the service:

    sudo systemctl start minidnla

Check that the service has been started:

    sudo systemctl status minidnla

*We should check that there are no important and fatal error messages.*

# Check the build in minimalistic website

Point your browser on the local ip <ip-server:8200>. We will get a basic web page with information such as how much audio , video and pictures files have been found.

We can for example use links2 as command line browser to check this.

When the minidnla service is started it will eventually rebuild the database if needed, if some changes where made the configuration file. But when the service is running, and when adding new files to the source path, the database will be automatically updated.

# Resources

- <https://minidlna.com>
