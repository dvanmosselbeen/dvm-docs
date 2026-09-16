# awstats

## Table of Contents

- [Introduction](#introduction)
- [Installation and configuration](#installation-and-configuration)
- [Resources](#resources)

## Introduction

Powerful and featureful web server log analyzer. With a web interface you can see all the statistics.

This setup has been tested on: `Debian 13 codename Trixie`, `Debian Trixie for Raspberry Pi`, `Ubuntu for Raspberry Pi` around september 2026.

## Installation and configuration

Installing awstats is a matter of:

````commandline
apt-get install awstats libgeo-ipfree-perl
````

Now we need to edit the `/etc/awstats/awstats.conf` configuration file. At least the `SiteDomain` is mandatory to set or `awstats` will fail when it does it's cron job and `root` user will receive a system email. The `cron job` is run every `10 minutes`.

````editorconfig
SiteDomain="raspberrypi-servergb.home"
````

But after this all, still getting a mail send to `root` user with this information as there is a problem:

````editorconfig
Date: Sun, 13 Sep 2026 19:20:01 +0200
From: Cron Daemon <root@raspberrypi-server-4gb.home>
To: root@raspberrypi-server-4gb.home
Subject: Cron <www-data@raspberrypi-server-4gb> [ -x /usr/share/awstats/tools/update.sh ] &&
        /usr/share/awstats/tools/update.sh

Error while processing /etc/awstats/awstats.conf
Create/Update database for config "/etc/awstats/awstats.conf" by AWStats version 7.9 (build 20230108)
>From data in log file "/var/log/apache2/access.log"...
Error: Couldn't open server log file "/var/log/apache2/access.log" : Permission denied
Setup ('/etc/awstats/awstats.conf' file, web server or permissions) may be wrong.
Check config file, permissions and AWStats documentation (in 'docs' directory).
````

When checking the `awstats` cron task in `/etc/cron.d/awstats`, we can see that the tasks are executed as `www-data` user. The cron task configuration file looks like this:

````editorconfig
*/10 * * * * www-data [ -x /usr/share/awstats/tools/update.sh ] && /usr/share/awstats/tools/update.sh

# Generate static reports:
10 03 * * * www-data [ -x /usr/share/awstats/tools/buildstatic.sh ] && /usr/share/awstats/tools/buildstatic.sh
````

When we look to the logs of apache with `ls -lah /var/log/apache2/`, we can see that only `root` user can read these logs. Users of the `adm` group can read only. But the `www-data` user is not part of the `adm` group so far.

````commandline
-rw-r----- 1 root adm 369K Sep 15 17:57 /var/log/apache2/access.log
````

We need to give `www-data` the `admin` rights to read that `apache2` log, so we can add `www-data` user to the `adm` group with the following command:

````commandline
adduser www-data adm
````

Now I'm not getting any email send to `root` user. So I guess it's okay, we need to wait until tomorrow to see if the files have been generated as apparently this will happen somewhere during the night.

The files seem to be created here. But note that it can take some time before they are generated:

````commandline
 /var/cache/awstats/awstats/
````

Create the configuration file:

````commandline
nano /etc/apache2/conf-available/awstats.conf
````

And add the following content:

````commandline
Alias /awstats-icon/ /usr/share/awstats/icon/
Alias /awstatsclasses/ /usr/share/java/awstats/

<Directory /usr/share/awstats>
    Options FollowSymLinks
    AllowOverride None
    # access permission for your local network
    #Require ip 127.0.0.1 10.0.0.0/24
</Directory>
````

*The previous configuration has the `Require ip` commented, as you can specify to only allow the pictures to be loaded from that ip or ip range. But here in this context it does not make any sense as `awstats` is accessible to everyone anyway.* 

We now need to enable this configuration:

````commandline
a2enconf awstats
````

Which will output:

````commandline
Enabling conf awstats.
To activate the new configuration, you need to run:
  systemctl reload apache2
````

Then enable the `apache cgi` module:

````commandline
a2enmod cgid
````

Which will output:

````commandline
Enabling module cgid.
To activate the new configuration, you need to run:
  systemctl restart apache2
````

Then restart the `apache 2` server:

````commandline
systemctl restart apache2
````

Then we can visit `awstats` on the following address: <http://localhost/cgi-bin/awstats.pl>

## Resources

- <https://www.server-world.info/en/note?os=Debian_13&p=httpd2&f=3>
- <https://wiki.herzbube.ch/wiki/AWStats>
- <https://kb.shells.com/tutorials/Debian_Latest/AWStats/>
- <https://www.linuxtuto.com/how-to-install-awstats-with-apache-on-debian-12/>
