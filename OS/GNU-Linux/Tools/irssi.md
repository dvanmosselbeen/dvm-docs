-----
title: irssi (The ultimate cli chat client)
description: This article is dedicated to the irssi irc chat client.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: debian, gnu, linux, irssi, irc, internet, chat, communication
lang: en
-----

# irssi (the ultimate cli chat client)

This document is dedicated to the awesome console based IRC client `irssi`.

# Table of Contents

* [Introduction](#introduction)
* [Setup and configuring irssi](#set-up-and-configuring-irssi)
* [Usage](#usage)
* [Setting up a theme](#setting-up-a-theme)
* [Script](#scripts)
    * [Spell check](#spell-check)
* [Resources](#resources)

# Introduction

`irssi` is probably the most powerful and the most amazing command line IRC client they might be available. It have a lot of good features, it's very easy to use and it's rock stable.

# Set up and configuring irssi

Installing irssi is a matter of running the following command:

    sudo apt-get install irssi

As first, follow the startup guide on https://irssi.org/documentation/startup/ This should help you to set your basic configuration and should set you up and running.

## My setup

For the FlightGear irc server=

    /NETWORK ADD FlightGear
    /SERVER ADD -auto -network FlightGear irc.flightgear.org
    /CHANNEL ADD -auto #flightgear FlightGear
    /CHANNEL ADD -auto #flightgear-nl FlightGear
    /NETWORK ADD -autosendcmd "/^msg nickserv ident FooBar4321;wait 2000" FlightGear
    /NETWORK ADD -sasl_username dvanmosselbeen -sasl_password FooBar4321 -sasl_mechanism PLAIN FlightGear
    
For all other:

    /CHANNEL ADD -auto #irssi Freenode
    /CHANNEL ADD -auto #debian Freenode
    /CHANNEL ADD -auto #python Freenode
    
    /NETWORK ADD -autosendcmd "/^msg nickserv ident pass;wait 2000" Freenode
    
Password:
    
    /NETWORK ADD -sasl_username dvanmosselbeen -sasl_password FooBar4321 -sasl_mechanism PLAIN Freenode


    /HILIGHT nick
/SET hilight_nick_matches_everywhere ON

# Usage

Once you have read that sort of irssi tutorial, you can eventually continue reading here. It's useless i copy paste information from the irssi.org website.

    Meta key == Alt key

Here's a list of common command:

| Command | Description |
|---|---|
| `ctrl + n` | Go to the next window |
| `ctrl + p` |  Go to the previous window |
| `PgUp` or `alt + p` | Scroll to the top. |
| `PgDn` or `alt + n`  | Scroll to the bottom |
| `/quit` | Quit irssi and go back where you where, on the cli probably |
| `/help` | To be executed within irssi of course, to get help |

You want probably to take a look to the other parameters. For this you can use the `/set <command>`. For example:

    /set

Will return a list of parameters that are set. You can also get only a particular item of the configuration file. For example:

    /set nick
    
To change that variable, use:

    /set nick <my_nick_name>

# Setting up a theme

There's a lot of themes available for `irssi` and it's very easy to activate some theme. The hardest part of activating a theme is to choice the one you want to use. You have a complete list of themes on the website of irssi and that's also the location from where you should download them: https://irssi-import.github.io/themes/

_Note that what you see there on the different screenshots isn't what you will actually get. You should take into consideration that most of these themes depend on other factors. Like the background color of your terminal, an eventually background image in the terminal. Furthermore, ._

Now let's look what theme is currently set:

    /set theme

Which returns:

    11:38 [lookandfeel]
    11:38                            theme default

I like using the `agon` theme and is the theme i have always used:

    # Go to the .irssi directory and store the downloaded theme there
    cd ~/.irssi
    wget https://irssi-import.github.io/themes/agon.theme

Set (apply) the theme:

    /set theme agon

# Scripts

The irssi (Perl) scripts should be put into `~/.irssi/scripts`. If you want them to load automatically put them into `~/.irssi/scripts/autorun`.

* `/script` displays a list of all loaded scripts and full paths to their source files
* `/script load [script]` loads the specified script. Irssi expects all scripts to be located in the `~/.irssi/scripts/` directory. If you have stored a script in a subdirectory of `~/.irssi/scripts/`, you need to specify that in the load command. Scripts placed in the `~/.irssi/scripts/autorun/` directory are loaded when Irssi starts.
* `/script unload [script]` unloads the specified script
* `/script exec [script]` runs the specified script once
* `/script reset` unloads all scripts and resets the Perl interpreter.

## Spell check

### (i)spell

Source from: https://blog.schmichael.com/2008/11/05/spell-checking-in-irssi/

Firstly, install the required apps:

    sudo apt-get install ispell liblingua-ispell-perl

Download the (Perl) spell script:
    
    $ cd ~/.irssi/scripts/
    $ wget http://scripts.irssi.org/scripts/spell.pl

We now need to adjust the path of ispell bin in the spell.pl script. (See line 130).

    sed -i "s@/usr/local/bin/ispell@/usr/bin/ispell@" spell.pl

Now load the stuff

    /script load spell.pl

Bind some key to the spell checker (alt+s)    

    /bind meta-s /_spellcheck
    /set spell_max_guesses 3

### (a)spell check

Install the required apps:

    apt-get install aspell aspell-en aspell-fr aspell-nl
    apt-get install libtext-aspell-perl

Get the required irssi scripts:

    cd ~/.irssi/scripts/autorun/

    wget https://scripts.irssi.org/scripts/aspell.pl
    wget https://scripts.irssi.org/scripts/aspell_complete.pl

Load the script:

    /script load

Bind some key (alt+c) to the spell checker:

    /bind meta-c /spellcheck

## Other interesting scripts

See also:  https://scripts.irssi.org/

* [trackbar.pl](http://scripts.irssi.org/scripts/trackbar.pl) generates a horizontal rule in a channel to mark the last time you viewed this channel’s window. This is useful if you are monitoring a number of channels and would like to be reminded of the last time you viewed this window.
* [go.pl](http://scripts.irssi.org/scripts/go.pl) provides advanced completion for accessing windows with a /go command that offers tab completion for all windows, and is even able to complete based on character combinations from the middle of the channel or private message names.
* [nickcolor.pl](http://scripts.irssi.org/scripts/nickcolor.pl) colorizes the nicknames of all members of a channel, based on activity and join time, in an effort to make the flow of conversation a bit easier to read.
* [screen_away.pl](http://scripts.irssi.org/scripts/screen_away.pl) automatically detects if your Irssi session resides within an attached or detached screen session. If your screen session is detached, this plugin will set your status to away. When you reattach to the session, the plugin unsets the away status.
* [highlite.pl](http://scripts.irssi.org/scripts/highlite.pl) collects in one window all channel events like joins, parts, and quits.

# Resources

* https://irssi.org/documentation/startup/