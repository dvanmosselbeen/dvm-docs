# irssi (the ultimate cli chat client)

This document is dedicated to the awesome console based IRC client `irssi`.

# Table of Contents

* [Introduction](#introduction)
* [Setup and configuring irssi](#set-up-and-configuring-irssi)
* [Usage](#usage)

# Introduction

`irssi` is probably the most powerful and the most amazing command line IRC client they might be available. It have a lot of good features, it's very easy to use and it's rock stable.

# Set up and configuring irssi

As first, follow the startup guide on https://irssi.org/documentation/startup/ This should help you to set your basic configuration and should set you up and running.

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

_Note that what you see there on the different screenshots isn't what you will actually get. You should take into consideration that most of these themes depend on other factors. Like the background color of your terminal, an eventually background image in the terminal. Futhermore, ._

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

# Resources

* https://irssi.org/documentation/startup/