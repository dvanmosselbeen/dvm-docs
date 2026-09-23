# Motd (Message of the day)

## Table of Contents

- [Introduction](#introduction)
- [Create a random message of the day when log in](#create-a-random-message-of-the-day-when-log-in)
  - [fortune](#fortune)
  - [verse](#verse)

## Introduction

The abbreviation `motd` stands for `message of the day`, and this file has been traditionally used for exactly that (it requires much less disk space than mail to all users).

The Message of the day when you log in can be various things.

For example, when you log in, you eventually see the system information and then as last `You have mail` when you have new.

## Create a random message of the day when log in

`fortune` is a package which output some random quote or funny joke. Maybe this is ideal for the `motd`. The `verse` package could be also interesting to output a random verse of the Holy Bible. We show both examples here.

### fortune

Install the fortune package:

````commandline
sudo apt install fortune
````

Create a new file:

````commandline
sudo nano /etc/update-motd.d/99-random-quote
````

*How higher the number, how lower the priority. Like in this case we want the random quote to show up ast one of the last items on screen just after logging in.*

With the content:

````commandline
#!/bin/sh
if [ -x /usr/games/fortune ]; then
    echo ""
    echo "--- Random Quote of the Day ---"
    /usr/games/fortune -s
    echo ""
fi
````

Make the script executable:

````commandline
sudo chmod +x /etc/update-motd.d/99-random-quote
````

This should now work. Log in again, with Putty for example this is ideal to remotely log in and test, to avoid log out and in all the time during the tests.

When you log in, you now see something like this on the console after log in:

````commandline
--- Random Quote of the Day ---
You have an unusual magnetic personality.  Don't walk too close to
metal objects which are not fastened down.
````

### verse

The `verse` package show the daily verse of the Holy Bible. Note that the whole day it will be the same verse. It's not like `fortune` which show you a different message each time it has been run.

Install the verse package:

````commandline
sudo apt install verse
````

````commandline
nano /etc/update-motd.d/99-random-verse
````

*How higher the number, how lower the priority. Like in this case we want the daily verse to show up ast one of the last items on screen just after logging in.*

With the following content:

````commandline
#!/bin/sh
if [ -x /usr/bin/verse ]; then
        echo ""
        echo "--- Random Verse of the Day ---"
        /usr/bin/verse
        echo ""
fi
````

Make it executable:

````commandline
chmod +x /etc/update-motd.d/99-random-verse
````

Log in again then this should work.
