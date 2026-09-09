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

For example, the following configuration will ban for `2 hours` after 3 failed attempts and email the `root` user when someone gets banned from bad `ssh` login attempts:

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
systemctl start sendmail
systemctl status sendmail
```

You can try out some failed `ssh` login attempts. Or if this computer is directly connected to the internet, just wait that others start to brut force attack this machine. You will be surprised about the amounts of attacks.

We can make use of `mutt` as mail client. But we probably need to install this package as it is not installed by default on the majority of `GNU / Linux` systems.

````commandline
apt-get install mutt
````

Here's a mail example when someone gets banned:

```commandline
Date: Tue, 08 Sep 2026 19:04:47 +0200
From: Fail2Ban <root@raspberrypi-server-4gb.home>
To: root@raspberrypi-server-4gb.home
Subject: [Fail2Ban] sshd: banned 164.163.10.19 from raspberrypi-server-4gb

Hi,

The IP 164.163.10.19 has just been banned by Fail2Ban after
3 attempts against sshd.


Here is more information about 164.163.10.19 :
% IP Client: 2a02:a03f:6a7f:9501:cebd:22a0:6602:df90

% Joint Whois - whois.lacnic.net
%  This server accepts single ASN, IPv4 or IPv6 queries

% LACNIC resource: whois.lacnic.net


% Copyright LACNIC lacnic.net
%  The data below is provided for information purposes
%  and to assist persons in obtaining information about or
%  related to AS and IP numbers registrations
%  By submitting a whois query, you agree to use this data
%  only for lawful purposes.
%  2026-09-08 17:04:47 (Z Z)

inetnum:     164.163.8.0/22
status:      allocated
aut-num:     AS265761
owner:       IT EXPERTS S.A
ownerid:     PA-IESA5-LACNIC
responsible: Luciano Maiello
address:     Area Bancaria, 301, Edificio PH. Torre Cosmos, oficina 301
address:     0801 - Panama City - Panama
country:     PA
phone:       +1 11 32100018 [2001]
owner-c:     LUM88
tech-c:      LUM88
abuse-c:     LUM88
inetrev:     164.163.8.0/24
nserver:     NS1.US1NET.COM
nsstat:      20260906 AA
nslastaa:    20260906
nserver:     NS2.US1NET.COM
nsstat:      20260906 AA
nslastaa:    20260906
inetrev:     164.163.9.0/24
nserver:     NS1.US1NET.COM
nsstat:      20260907 AA
nslastaa:    20260907
nserver:     NS2.US1NET.COM
nsstat:      20260907 AA
nslastaa:    20260907
inetrev:     164.163.10.0/24
nserver:     NS1.US1NET.COM

nsstat:      20260906 AA
nslastaa:    20260906
nserver:     NS2.US1NET.COM
nsstat:      20260906 AA
nslastaa:    20260906
inetrev:     164.163.11.0/24
nserver:     NS1.US1NET.COM
nsstat:      20260907 AA
nslastaa:    20260907
nserver:     NS2.US1NET.COM
nsstat:      20260907 AA
nslastaa:    20260907
created:     20170705
changed:     20170705
nic-hdl:     LUM88
person:      Luciano Maiello
e-mail:      luciano@spin18.com.br
address:     Intershore Chambers, 1, -
address:     VG1110 - Tortola - Road Town
country:     VG
phone:       +1284  17862124811 [0000]
created:     20170316
changed:     20230706

% whois.lacnic.net accepts only direct match queries.
% Types of queries are: POCs, ownerid, CIDR blocks, IP
% and AS numbers.


Lines containing failures of 164.163.10.19 (max 1000)


Regards,

Fail2Ban
```

By observing the data you get into you mails, you will quickly understand that these automated attacks are very smart. Probably these attacks are driven by `AI` or at least with smart scripts. Because it feels like they can understand that they are attacking a machine who has protection software. In my case, most of these attacks stops after 3 times getting banned. Then they will eventually use another `IP`.

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
