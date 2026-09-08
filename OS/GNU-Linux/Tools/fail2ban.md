# fail2ban

## Table of Contents

- [Introduction](#introduction)
- [Installation of fail2ban](#installation-of-fail2ban)
- [Configuration of fail2ban](#configuration-of-fail2ban)
  - [Send emails](#send-emails)
- [Check the status](#check-the-status)
- [Resources](#resources)

## Introduction

`fail2ban` is an excellent tool if you want to have some monitoring system on your services. It monitors in the sense that it is looking for unexpected behaviors, like failed login attempts. In my opinion, if you are for example running a `ssh` server, `fail2ban` is an absolutely must-have installed monitoring tool. And like running a `GNU / Linux` machine, a `ssh` server is also in my opinion a must-have software / service that needs to run on every `GNU / Linux` machine. So to conclude, `fail2ban` is absolutely something to be installed by default.

Note that `fail2ban` is way more powerful than just looking for failed `ssh` logins. By default, it will look for failed login attempts for web (`apache`) services, `ftp` and so on.

## Installation of fail2ban

Installing `fail2ban` is very easy.

    apt-get install fail2ban

On some systems, by default the `fail2ban` service is not started or activated at boot time. On `Debian` system this is, but not on `Kali` for example. So we need to check this out.

Check with:

    systemctl status fail2ban

Start the services manually:

    systemctl start fail2ban

Or make it start automatically at boot time which is probably something you absolutely want to do:

    systemctl enable fail2ban

## Configuration of fail2ban

The default configuration of `fail2ban` will protect your `ssh` server and other servers straight out of the box. But honestly said, if your computer is exposed directly to the internet, then the default configuration is not strict enough. Because yes, you will see that there is a huge amount of brute force attacks. So it's better to fine tune the configuration file and to be more strict.

All configuration files are stored in `/etc/fail2ban/`. The file `/etc/fail2ban/jail.conf` is probably what you are looking for, however, you should not modify this file itself as it can be overwritten when the package `fail2ban` get updated and thus overwriting your custom tweaks. And when reading the file `/etc/fail2ban/jail.conf`, this appears on top of it:

````commandline
# WARNING: heavily refactored in 0.9.0 release.  Please review and
#          customize settings for your setup.
#
# Changes:  in most of the cases you should not modify this
#           file, but provide customizations in jail.local file,
#           or separate .conf files under jail.d/ directory, e.g.:
#
# HOW TO ACTIVATE JAILS:
#
# YOU SHOULD NOT MODIFY THIS FILE.
#
# It will probably be overwritten or improved in a distribution update.
#
# Provide customizations in a jail.local file or a jail.d/customisation.local.
# For example to change the default bantime for all jails and to enable the
# ssh-iptables jail the following (uncommented) would appear in the .local file.
# See man 5 jail.conf for details.
#
# [DEFAULT]
# bantime = 1h
#
# [sshd]
# enabled = true
#
# See jail.conf(5) man page for more information
````

Therefore, you should modify the file `/etc/fail2ban/jail.d/defaults-debian.conf` file where there you save your custom tweaks.

For example, the following configuration will send an email when someone gets banned from bad `ssh` login attempts:

```commandline
[DEFAULT]
banaction = nftables
banaction_allports = nftables[type=allports]

ignoreip = 127.0.0.0
bantime  = 2h
findtime  = 2h
destemail = root@localhost
sender = root@localhost
sendername = Fail2ban
mta = sendmail
action = %(action_mwl)s

[sshd]
backend = systemd
journalmatch = _SYSTEMD_UNIT=ssh.service + _COMM=sshd
enabled = true

maxretry = 3
bantime.increment = true
```

In this configuration example:

- An IP will be banned for `2` hours (`bantime`) after `3` failed attempts within `2` hours (`findtime`), which is fine and should kick away all bots. If you still get annoyed, increase the ban time and all will be fine.
- It is also wise to adjust the `ignoreip` to your needs. As I have physical access in this case, I will keep it this way. We never know if some hacker could pivot into our network and use one of our own systems to attack our servers.
- The `bantime.increment = true`, will make in sort that next time, after the `ip` get unbanned, if bad attempts are made again from this `ip`, the ban time will be multiplied by 2 (default it's times 2)
- An email will be sent to `root@localhost`.

After any changes to configuration file, restart the `fail2ban` service:

    systemctl restart fail2ban

_(As of today september 6, 2026, this seems to be fixed) Note that restarting the `fail2ban` service, might also unlock banned IPs / computers. This is not always the case but the majority of the time this happens. I have no clue why this happens this way. Feels like some hole or some bug. Anyway, just check your logs on time. Checking logs / errors is something that should happen at very least, once a day!_

### Send emails

Our current configuration will send an email when an `ip` get banned. For this, unfortunately, you need to have a mail server running. We can make (basic) usage of the `sendmail` for example or `postfix` for local email exchange in this network. 

Setting up a whole email system is out of the scope of this document as this is really a complex subject. For this, check out the dedicated documentation of how to set up an email server. Setting up a mail  server on you network, especially a misconfigurated mail server on your network, can have a serious impact on the security level, but also make in sort that your mail system of your clients get broken and emails lost in space.

Also note that in this example, this is all about local email in a local network. Which is probably not nice enough as you need to log locally on that computer and check the email. People tent to forget to log into their servers and check the local mail. However, if your shell is set up correctly, you should get a notification that you have new email. For example `You have new mail in /var/mail/root` when login in onto that computer. It's better to set up a decent email server, to at least send email out of the local network. But to get starter with the basics, here's a quick guide to install and setup `sendmail`:

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
systemctl status sendmail
systemctl stop sendmail
```

You can try out some failed `ssh` login attempts.

You can make use of `mutt` as mail client. But you probably need to install this package as it is not installed by default on the majority of `GNU / Linux` systems.

Here's a mail example when someone gets banned:

```commandline
Date: Sun, 15 Aug 2021 10:11:30 +0200
From: Fail2Ban <root@btop.home>
To: root@btop.home
Subject: [Fail2Ban] sshd: banned 192.168.0.54 from btop

Hi,

The IP 192.168.0.54 has just been banned by Fail2Ban after
10 attempts against sshd.

...
```

I have stripped out the email a bit as this is a very long email with much more information.

## Check the status

You can check the status for what `fail2ban` is actually monitoring for:

```commandline
fail2ban-client status
```

Which return:

```commandline
Status
|- Number of jail:      1
`- Jail list:   sshd
```

Here, it is only monitoring a `ssh` server in this example, as that is the only service that is running. If you have other services running. If you have more services, of course, the list will be longer:

    fail2ban-client status sshd

Which return:

```commandline
Status for the jail: sshd
|- Filter
|  |- Currently failed: 1
|  |- Total failed:     22
|  `- File list:        /var/log/auth.log
`- Actions
   |- Currently banned: 1
   |- Total banned:     2
   `- Banned IP list:   192.168.0.54
```

You can also get more information / help with just running the command:

    fail2ban-client

And as bonus dope for `Python` fanatics like me, there is also:

    fail2ban-python

Which is an interactive shell into the `fail2ban` system. This is grandiose!

## Resources

- <https://www.fail2ban.org>
- <https://raspberrytips.com/install-fail2ban-raspberry-pi/>
- <https://edywerder.ch/fail2ban-email-notification/>
- <https://www.youtube.com/watch?v=Z0cDqF6HAxs>
