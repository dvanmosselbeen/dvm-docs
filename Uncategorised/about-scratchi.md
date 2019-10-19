---
description: Software Sweet Software
keywords: 
title: About scratchi
created: 28-11-2007
modified: 
---

scracthi is a supybot ircbot that run on `#debian-nl` on freenode\'s
network. A little nice tool to aid the people on the irc channel. The
bot is written in Python. See the [supybot](http://supybot.com/) website
for more informations.

Some parts of the bot are translated. Like the \'as\' to \'is\'. But
there are still some words need to translate.

We use the moobotfactoids to store some useful informations that are
asked repeately. Get help for the moobotfactoids see
the[moobotfactoids](http://supybot.com/documentation/help/howto/using-moobotfactoids)howto
on supybot website.

Some escape examples:

    /msg scratchi no sudo is (SUperuser DO) beter dan su, Het is in staat beperkt 
    "'super user privileges'&quot; te specifieren aan gebruikers, het laat je toe om 
    stome zaken uit te voeren bijvoorbeeld X applicaties starten als root gebruiker, 
    goed in scripts met "\";username ALL = NOPASSWD: /some/program\";";, 
    http://www.aplawrence.com/Basics/sudo.html

Change some stuff of an factiod, without remove the whole stuff:

    /msg scratchi open ports =~ s/Zie/zie/
