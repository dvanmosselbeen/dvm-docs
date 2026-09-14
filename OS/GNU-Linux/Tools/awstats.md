# awstats

## Table of Contents

- [Introduction](#introduction)
- [Installation and configuration](#installation-and-configuration)
- [Resources](#resources)

## Introduction

Powerful and featureful web server log analyzer. With a web interface you can see all the statistics.

## Installation and configuration

Installing awstats is a matter of:

````commandline
apt-get install awstats libgeo-ipfree-perl
````

Now we need to edit the `/etc/awstats/awstats.conf` configuration file. At least the `SiteDomain` is mandatory to set or `awstats` will fail when it does it's cron job and `root` user will receive a system email. The `cron job` is run every `10 minutes`.

````editorconfig
SiteDomain="raspberrypi-servergb.home-"
````

But after this all, still getting a mail send to `root` user with this information:

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

When we look to the logs of apache with `ls -lah /var/log/apache2/`, we can see that only `root` user can read these logs.

When checking the `awstats` cron task `/etc/cron.d/awstats`, we can see that the tasks are executed as `www-data` user. So I changed this to `root` user and the configuration file now looks like this:

````editorconfig
*/10 * * * * www-data [ -x /usr/share/awstats/tools/update.sh ] && /usr/share/awstats/tools/update.sh

# Generate static reports:
10 03 * * * www-data [ -x /usr/share/awstats/tools/buildstatic.sh ] && /usr/share/awstats/tools/buildstatic.sh
````

Now I'm not getting any email send to `root` user. So I guess it's okay, we need to wait until tomorrow to see if the files have been generated as apparently this will happen somewhere during the night.

The files seem to be created here:

````commandline
 /var/cache/awstats/awstats/
````

Create the configuration file:

````commandline
nano /etc/apache2/conf-available/awstats.conf
````

And add the following content:

````commandline
# create new
Alias /awstats-icon/ /usr/share/awstats/icon/
Alias /awstatsclasses/ /usr/share/java/awstats/

<Directory /usr/share/awstats>
    Options FollowSymLinks
    AllowOverride None
    # access permission for your local network
    Require ip 127.0.0.1 10.0.0.0/24
</Directory>
````

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

Then we can visit `awstats` on the following address, (but the pictures are not loaded): <http://localhost/cgi-bin/awstats.pl>

## Resources

- <https://www.server-world.info/en/note?os=Debian_13&p=httpd2&f=3>
- <https://wiki.herzbube.ch/wiki/AWStats>
- <https://kb.shells.com/tutorials/Debian_Latest/AWStats/>
