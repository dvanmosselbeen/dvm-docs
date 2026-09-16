# awffull

## Table of Contents

- [Introduction](#introduction)
- [Installation and configuration](#installation-and-configuration)
- [Enable https for awffull](#enable-https-for-awffull)
- [TODO](#todo)

## Introduction

Web server log analysis program forked from `Webalizer`. It adds a number of new features and improvements, such as extended frontpage history, resizable graphs, and a few more pie charts.

This setup has been tested on: `Debian 13 codename Trixie`, `Debian Trixie for Raspberry Pi`, `Ubuntu for Raspberry Pi` around september 2026.

## Installation and configuration

To install `awffull` it's a matter to run:

````commandline
apt-get install awffull
````

The configuration file is located at `/etc/awffull/awffull.conf`. We should change a few settings eventually. Here are the options I changed:

````editorconfig
Incremental    yes
````

If you want that `awffull` generate it's output in another location, then take a look to this:

````editorconfig
OutputDir /var/www/awffull
````

The installation will create a `cron` file and the script is here: `/etc/cron.daily/awffull`.

But so far, we can not access the generated `awffull` data on the webserver as the `apache2` has his `DocumentRoot` pointing to `/var/www/html/` and the output of `awffull` goes to `/var/www/awffull/`. We need to create an alias so that `apache2` know where the data is located.

Create the file:

````commandline
/etc/apache2/conf-available/awffull.conf
````

Add the following content:

````editorconfig
# Create new alias for awffull
Alias /awffull/ /var/www/awffull/
````

Then enable our custom `awffull` configuration:

````commandline
a2enconf awffull
````

This will output:

````commandline
Enabling conf awffull.
To activate the new configuration, you need to run:
  systemctl reload apache2
````

Then finally reload the `apache2` configuration.

````commandline
systemctl reload apache2
````

We can now point our browser to <http://localhost/awffull/> and check if everything is working like expected. But the files are probably not yet generated and the folder will be empty. The cron job is executed daily, but not yet today, probably. **Need to check how we can force to generate the `awffull` files.**

## Enable https for awffull

By default, `awffull` does not work on the `https` protocol. We need to activate this in the `/etc/awffull/awffull.conf` configuration file. Change the `UseHTTPS` value from `no` to `yes`.

````editorconfig
UseHTTPS       yes
````

## TODO

- [ ] The cron script seems not to work, so the data is not updated.
- 