# sendmail

## Table of contents

- [Introduction](#introduction)
- [Installation and Configuration](#installation-and-configuration)
- [Resources](#resources)

## Introduction

With sendmail you can easily set up an email system for basic or more complex usages. This document will only cover the very basic aspect of an email server so that system mail or local mail can be sent.

Some apps send mails to `root` user, like for example `fail2ban`, `rsnapshot`. Thus, it can be handy to receive these emails also.

This setup has been tested on: `Debian 13 codename Trixie`, `Debian Trixie for Raspberry Pi`, `Ubuntu for Raspberry Pi` around september 2026.

## Installation and configuration

    apt-get install sendmail

Check out the configuration file `/etc/mail/sendmail.conf`, but a quick reminder, for laptops clients for example who mainly only use the `wlan0` network device instead of wired (`eth0`) network devices, a little tweak should be done so that `sendmail` is listening on the `wlan0` device instead of the `eth0`.

```commandline
sed -i s/eth0/wlan0/  /etc/mail/sendmail.conf
```

I also like to create an alias, that for example all mails send to `root` user get also send to my main user account on that system. So that if I do not log in with `root` user, I get notified of mails the `root` user gets. For this edit `/etc/aliases` and add:

    root:   root, <my-main-user-account>

_That previous `/etc/aliases` files was probably empty._

_Replace `<my-main-user-account>` with your main user account. You can also add more user accounts and separate them with a comma (`,`) like shown in the example above._

Then you need to propagate this modification as `root` user with:

    newaliases

Once that modified, restart the `sendmail` server. I like to use the following commands to have a better view on what is going on and to get information about each step. We also need to be sure that the `sendmail` service start at boot time:

```commandline
systemctl status sendmail
systemctl stop sendmail
systemctl enable sendmail
systemctl start sendmail
systemctl status sendmail
```

## Resources

- ...
