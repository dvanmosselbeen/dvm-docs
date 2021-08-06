# Installing and using cygwin on Microsoft Windows XP

## Introduction

`Cygwin` is ideal if you want some `unix` like tool on a `Microsoft Window` operating system. `Cygwig` have an installer system to easy select the software you want to install. With the same stuff you can remove these or update all the installed software on a easy way.

## Installation

Get the installer of the official website. Place these in a location somewhere, like we go to keep this executable file. Because once we have installed `cygwin`, it will serve to update the installed packages and to install or remove the packages. It's in sort, the package manager.

Depending of your need, in the long list, select all the programs you want to install. It\'s all depending of your taste.

Usually i install:

- vim
- python
- mc
- ...

## Installing some more stuff or updating

Once the stuff install, you can re run the installer to add some more stuff. There are some buttons to filter the list to. Select the software you want to install, remove, update.

## Using cygwin stuff

In the start menu there is a new directory called `cygwin` with some shortcuts in it. Take a look at it! Execute all these shortcuts each a time to see what's happen.

If you are a unix like user. You probably know how to go futher and probably you have select all your wanted apps during the installation and are ready to use your tools.

## Changing the default shell.

Modify, or better, make a copy of the `cygwin.bat` and modify the word bash with whatever shell you want.

There may be a better way to do it. A way that it is userspecific and not widely. Changing the `/etc/passwd` doesn't work, i should check what happend.

## Fluxbox

Start a console and type `startflux`. After some little time X should startup and `fluxbox` should appear.

## Some config tips

Usually, on of the first thing i do is setup the vim. My lovely text editor. Like i already have a custom configuration file i have tweak to my needs and also some plugins i have download of the vim website. So it's just a matter of a copy.

## Installing and configuring sshd

I assume that you have install the ssh package.

Once the required stuff installed, we should execute the follow command to create the essential config files:

    ssh-host-config

It generate the needed keys, and ask you some things you should reply. The questions are:

-   Should privilege separation be used? `yes`
-   Should this script create a local user 'sshd' on this machine? `yes`
-   Do you want to install sshd as service? `Yes`
-   Whice value should the environment variable CYGWIN have when sshd starts? I left the default, just pressed enter.

At the end, it tell you:

    The service has been installed under LocalSystem account.
    To start the service, call `net start sshd` or `cygrunsrv -S sshd`

Once done, you can look in the `Computer Management` `Services` and there will be a item `CYGWIN sshd`.

Create the required directory:

    mkdir -p /var/lock/subsys

Start the sshd server:

    /etc/rc.d/init.d/sshd start

## Resources

-   <http://cygwin.com/>
