# rsnapshot

## Table of Contents

 - [Introduction](#introduction)
 - [Installation](#installation)
 - [Configuration](#configuration)
 - [Issues](#issues)
 - [Restoring data](#restoring-data)
 - [Links](#links)

## Introduction

`rsnapshot` is an rsync-based filesystem snapshot utility. It can take incremental backups of local and remote filesystems for any number of machines. `rsnapshot` makes extensive use of hard links, so disk space is only used when absolutely necessary.

It is in my opinion an app that has to be installed on every `GNU / Linux` machine. Or to be installed on a `GNU / Linux` server who then will handle and take care to do remote backups of your other `GNU / Linux` clients on your network.

You might think that you don't need backups, but it can be very handy even just to save your configuration files.1

## Installation

I Installed `rsnapshot` on a `Raspberry Pi 4 with 4GB RAM`. My `Raspberry Pi` installation is a standard Operating System from `Raspberry` itself, so it's based on `Debian GNU / Linux`. The instructions here should apply for any `GNU / Linux` derivation based on `Debian`.

Installing is as easy as:

````commandline
sudo apt-get install rsnapshot
````
Once installed, we should check what has been installed:

````shell
dpkg -L rsnapshot | less
````

Inspect the all files because there are many very interesting example files which you can use, adapt, or get inspiration from. I will list here only a few of interesting files:

````text
/usr/share/doc/rsnapshot/examples/rsnapshot.conf.default
/usr/share/doc/rsnapshot/examples/anacron/daily/rsnapshot
/usr/share/doc/rsnapshot/examples/anacron/weekly/rsnapshot
/usr/share/doc/rsnapshot/examples/anacron/monthly/rsnapshot
/usr/share/doc/rsnapshot/examples/utils/backup_dpkg.sh
/usr/share/doc/rsnapshot/examples/utils/backup_mysql.sh
/usr/share/doc/rsnapshot/examples/utils/rsnapreport.pl
/usr/share/doc/rsnapshot/examples/utils/rsnapshot_if_mounted.sh
/usr/share/doc/rsnapshot/examples/utils/sign_packages.sh
````

Now it's time for its configuration.

## Configuration

All the configuration of `rsnapshot` is located in the `/etc/rsnapshot.conf` configuration file.

The configuration file is pretty clear with all the comments. Maybe the `alpha`, `beta`, `gamma`, `delta` stuff isn't clear maybe at first instance. It simply stands for `hourly`, `daily`, `weekly` and finally `monthly` backups.

Now we need to make sure that the backup is made at some specific points in time. For this we need to create a few cron jobs. For this, check the file `/etc/cron.d/rsnapshot` which has been created when we installed the `rsnapshot` package. This is mine here:

````editorconfig
### My custom backup plan
# Hourly (every 6 hours? Or every 15 minutes?)
0 */4         * * *           root    /usr/bin/rsnapshot alpha
# Daily at 3:30 in the morning
30 3          * * *           root    /usr/bin/rsnapshot beta
# Weekly (first day of the week) at 3:00 in the morning
0  3          * * 1           root    /usr/bin/rsnapshot gamma
# Monthly (first day of the month) at 2:30 in the morning
30 2          1 * *           root    /usr/bin/rsnapshot delta
````

If we need to run other scripts for example, creating a list of installed packages on the machine, then we have to take a look to the :

````editorconfig
backup_script  /usr/local/bin/backup_pgsql.sh  localhost/postgres/
````

Same if we want to execute a specific command. In this example it execute it on a remote computer:

````editorconfig
backup_exec    ssh root@example.com "mysqldump -A > /var/db/dump/mysql.sql"
````

For other things we can rely on cron and should create a cron job for this with the command `crontab -e`.

## Issues

As of today, on September 4, 2026 on a `Raspberry Pi` with `rsnapshot` package version `1.5.1-1` I have a major runtime error after a fresh installation. 

After setting up everything, I still did not get any backups made by `rsnapshot`. So I tried to run the task manually, and I found the issue. (Did not find any errors in logs or anything) except on the console as shown here:

````commandline
root@raspberrypi-server-4gb:/home/dvanmosselbeen# /usr/bin/rsnapshot alpha
----------------------------------------------------------------------------
rsnapshot encountered an error! The program was invoked with these options:
/usr/bin/rsnapshot alpha
----------------------------------------------------------------------------
ERROR: /etc/rsnapshot.conf on line 242:
ERROR: backup /var/log/rsnapshot localhost/ - Source directory \
         "/var/log/rsnapshot" doesn't exist
ERROR: ---------------------------------------------------------------------
ERROR: Errors were found in /etc/rsnapshot.conf,
ERROR: rsnapshot can not continue. If you think an entry looks right, make
ERROR: sure you don't have spaces where only tabs should be.
````

Feels like this is a bug of the package. Need to check if there's an existing bug report bug, or if one should be made.

Created this log directory and this fixed the issue.

    mkdir   /var/log/rsnapshot

## Restoring data

All the backups are by default stored on the location `/var/cache/rsnapshot/`. This is defined in the `snapshot_root` variable of the `/etc/rsnapshot.conf` configuration file.

The most recent backup directory have the lowest number. So the last backup will always end with number `0`. At the next backup, the directory names will be rotated.

You can easily check the difference of 2 backups with the command `/usr/bin/rsnapshot-diff`.

Firstly check if there's any differences:

````commandline
rsnapshot-diff /var/cache/rsnapshot/alpha.0/localhost/ /var/cache/rsnapshot/alpha.1/localhost/
````

Which will output:

````commandline
Between /var/cache/rsnapshot/alpha.1/localhost and /var/cache/rsnapshot/alpha.0/localhost:
  2 were added, taking 57730 bytes
  1 were removed, saving 8775 bytes
````

As we can see, it does not show us which files or directories got changed. For this we need to use the 

````commandline
diff -q -r /var/cache/rsnapshot/alpha.0/localhost/ /var/cache/rsnapshot/alpha.1/localhost/
````

Which output:

````commandline
root@raspberrypi-server-4gb:/home/dvanmosselbeen# diff -q -r /var/cache/rsnapshot/alpha.0/localhost/ /var/cache/rsnapshot/alpha.1/localhost/
Only in /var/cache/rsnapshot/alpha.0/localhost/: dpkg
diff: /var/cache/rsnapshot/alpha.0/localhost/etc/mtab: No such file or directory
diff: /var/cache/rsnapshot/alpha.1/localhost/etc/mtab: No such file or directory
diff: /var/cache/rsnapshot/alpha.0/localhost/etc/os-release: No such file or directory
diff: /var/cache/rsnapshot/alpha.1/localhost/etc/os-release: No such file or directory
Files /var/cache/rsnapshot/alpha.0/localhost/etc/rsnapshot.conf and /var/cache/rsnapshot/alpha.1/localhost/etc/rsnapshot.conf differ
````

The previous output is very confusing especially the mention of the `mtab` and `os-release` files not there.

Finally check the difference of the file `/var/cache/rsnapshot/alpha.0/localhost/etc/rsnapshot.conf`:

````commandline
root@raspberrypi-server-4gb:/home/dvanmosselbeen# diff /var/cache/rsnapshot/alpha.0/localhost/etc/rsnapshot.conf /var/cache/rsnapshot/alpha.1/localhost/etc/rsnapshot.conf

240d239
< backup_script /usr/share/doc/rsnapshot/examples/utils/backup_dpkg.sh  localhost/dpkg/
````

## Links

 - <https://raspberrytips.com/backup-raspberry-pi/#method-4--rsnapshot>
