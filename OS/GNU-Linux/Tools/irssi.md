# irssi (the ultimate cli chat client)

## Table of Contents

- [Introduction](#introduction)
- [Set up and configuring irssi](#set-up-and-configuring-irssi)
- [Quick Shot](#quick-shot)
- [My setup](#my-setup)
- [Usage](#usage)
- [Setting up a theme](#setting-up-a-theme)
- [Scripts](#scripts)
  - [Spell check](#spell-check)
    - [(i)spell](#ispell)
    - [(a)spell check](#aspell-check)
  - [Other interesting scripts](#other-interesting-scripts)
- [IRC bots](#irc-bots)
- [Resources](#resources)

## Introduction

`irssi` is probably the most powerful and the most amazing command line `IRC` client they might be available. It has a lot of good features, it's very easy to use, and it's rock stable.

Note that longer time ago, one of the most famous network was `Freenode`. However, if I'm not wrong, and if I remember correctly, the author passed away several years ago. I believe the `Freenode` network is dead by now. It could be we still find information here and there about `Freenode`.

The `Internet Relay Chat` was very popular till many years ago. Especially before `Facebook` came out (2007) in Europe. It was easy to get fast (free) support from anyone who was online and active in a topic related channel. These last years I find that the `IRC` has lost very much popularity. There are still many users connecting to the different channels, but it's very less active or not active at all. I remember times when chatting, getting and giving support on the `IRC` was so fast and so nice. I remember the good old times when I enjoyed so much passing my whole evening or night chatting and giving support to people. It was so exciting. I believe that the IRC got less popular now due to the other platforms, like forums or `Discord` alike tools. Back then, there were almost no social media apps or websites, so we had to keep ourselves busy with other things.

## Set up and configuring irssi

Installing irssi is a matter of running the following command:

````commandline
sudo apt-get install irssi
````

As first, follow the startup guide on https://irssi.org/documentation/startup/ This should help you to set your basic configuration and should set you up and running.

### Quick Shot

To get a list of the different networks you can connect to:

````commandline
/network
````

Which will output:

````commandline
16:12:03 Networks:
16:12:03 DALnet: max_kicks: 4, max_msgs: 20, max_whois: 30
16:12:03 EFNet: max_kicks: 1, max_msgs: 4, max_whois: 1
16:12:03 EsperNet: max_kicks: 1, max_msgs: 4, max_whois: 1
16:12:03 liberachat: max_kicks: 1, max_msgs: 4, max_whois: 1
16:12:03 GameSurge: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 IRCnet: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 IRCSource: max_kicks: 1, max_msgs: 4, max_whois: 1
16:12:03 NetFuze: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 OFTC: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 QuakeNet: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 Rizon: max_kicks: 1, max_msgs: 1, max_whois: 1
16:12:03 Undernet: max_kicks: 1, max_msgs: 1, max_whois: 1
````

To connect to the `liberachat` network, set your nickname, get help and then join the `#irssi`, `#debian` and `#raspberry` channel:

````editorconfig
/connect liberachat
/set nick <my_nick_name>
/help
/help <COMMAND_NAME>
/join #irssi
/j #debian
/j #raspberrypi
````

*We can see we used the long and short form of the command `join`. Many commands have also a short form.*

To leave a channel, without closing the app or completely disconnecting:

````commandline
/leave
````

Removing clutter you can for example hide the joins, parts and quites as this take a lot of lines for no valuable reason. Note that this has to be executed per channel:

````commandline
/window hidelevel +joins +parts +quits
````

To get them back:

````commandline
/window hidelevel -joins -parts -quits
````

If we want to hide them by default for all channels when we start up `irssi`:

````commandline
/set window_default_hidelevel hidden joins parts quits
````

To quit the `irssi` application:

````commandline
/quit
````

*Or `/exit`.*

### My setup

For the FlightGear irc server:

````editorconfig
/NETWORK ADD FlightGear
/SERVER ADD -auto -network FlightGear irc.flightgear.org
/CHANNEL ADD -auto #flightgear FlightGear
/CHANNEL ADD -auto #flightgear-nl FlightGear
/CHANNEL ADD -auto #fg_cantene FlightGear
/NETWORK ADD -autosendcmd "/^msg nickserv identify <YourPasswordHere>;wait 2000" FlightGear
/NETWORK ADD -sasl_username <YourUserNameHere> -sasl_password <YourPasswordHere> -sasl_mechanism PLAIN FlightGear
````

For all others:

For example here we will auto connect a few channels to the `liberachat` network. `liberachat` has much more users than the `OFTC` network and the users are much more active also.

````editorconfig
/CHANNEL ADD -auto #irssi liberachat
/CHANNEL ADD -auto #debian liberachat
/CHANNEL ADD -auto #python liberachat
/CHANNEL ADD -auto #raspberrypi liberachat
````

Automatically identify to the server with your password:

````editorconfig
/NETWORK ADD -autosendcmd "/^msg nickserv identify <YourPasswordHere>;wait 2000" Freenode
````

Password:

````editorconfig
/NETWORK ADD -sasl_username dvanmosselbeen -sasl_password YourPasswordHere -sasl_mechanism PLAIN Freenode
````

Set up nickname settings:

````editorconfig
/HILIGHT nick
/SET hilight_nick_matches_everywhere ON
````

## Usage

Once you have read that sort of irssi tutorial, you can eventually continue reading here. It's useless I copy and paste information from the <https://www.irssi.org> website.

````editorconfig
Meta key == Alt key
````

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

List all windows:

````commandline
/window list
````

Go to a specific window number:

````commandline
/window goto 1
````

*You can also use the `ALT+<NUMBER>` to jump directly to a specific window. Or user `/3` to jump to window number `3`.*

You can also move (position) the current window into another position:

````commandline
/window move left
````

*Where you can replace left with right, prev, next, first, last.*

## Setting up a theme

There's a lot of themes available for `irssi` and it's very easy to activate some theme. The hardest part of activating a theme is to choice the one you want to use. You have a complete list of themes on the website of irssi and that's also the location from where you should download them: https://irssi-import.github.io/themes/

_Note that what you see there on the different screenshots isn't what you will actually get. You should take into consideration that most of these themes depend on other factors. Like the background color of your terminal, an eventually background image in the terminal. Furthermore, ._

Now let's look what theme is currently set:

    /set theme

Which returns:

    11:38 [lookandfeel]
    11:38                            theme default

I like using the `agon` theme and is the theme I have always used:

    # Go to the .irssi directory and store the downloaded theme there
    cd ~/.irssi
    wget https://irssi-import.github.io/themes/agon.theme

Set (apply) the theme:

    /set theme agon

## Scripts

The irssi (Perl) scripts should be put into `~/.irssi/scripts`. If you want them to load automatically put them into `~/.irssi/scripts/autorun`.

* `/script` displays a list of all loaded scripts and full paths to their source files
* `/script load [script]` loads the specified script. Irssi expects all scripts to be located in the `~/.irssi/scripts/` directory. If you have stored a script in a subdirectory of `~/.irssi/scripts/`, you need to specify that in the load command. Scripts placed in the `~/.irssi/scripts/autorun/` directory are loaded when Irssi starts.
* `/script unload [script]` unloads the specified script
* `/script exec [script]` runs the specified script once
* `/script reset` unloads all scripts and resets the Perl interpreter.

### Spell check

#### (i)spell

Source from: <https://blog.schmichael.com/2008/11/05/spell-checking-in-irssi/>

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

#### (a)spell check

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

### Other interesting scripts

See also:  https://scripts.irssi.org/

* [trackbar.pl](http://scripts.irssi.org/scripts/trackbar.pl) generates a horizontal rule in a channel to mark the last time you viewed this channel’s window. This is useful if you are monitoring a number of channels and would like to be reminded of the last time you viewed this window.
* [go.pl](http://scripts.irssi.org/scripts/go.pl) provides advanced completion for accessing windows with a /go command that offers tab completion for all windows, and is even able to complete based on character combinations from the middle of the channel or private message names.
* [nickcolor.pl](http://scripts.irssi.org/scripts/nickcolor.pl) colorizes the nicknames of all members of a channel, based on activity and join time, in an effort to make the flow of conversation a bit easier to read.
* [screen_away.pl](http://scripts.irssi.org/scripts/screen_away.pl) automatically detects if your Irssi session resides within an attached or detached screen session. If your screen session is detached, this plugin will set your status to away. When you reattach to the session, the plugin unsets the away status.
* [highlite.pl](http://scripts.irssi.org/scripts/highlite.pl) collects in one window all channel events like joins, parts, and quits.

## IRC bots

Longer time ago, there was a famous Python IRC bot called `supybot`. Now it seems to be not maintained anymore and has been replaced by `limnoria` which is the maintained fork of `supybot`.

If you have your own channel, it can be handy to have some IRC bot so that it can manage the channel but also so that people can make use of it. An IRC bot usually also has the feature that you can ask some things, and get answers back. It is for example handy to get quick support, for the most frequently asked questions. A good example is the `dpkg` IRC bot on the `#debian` channel.


## Resources

- <https://irssi.org/documentation/startup/>
