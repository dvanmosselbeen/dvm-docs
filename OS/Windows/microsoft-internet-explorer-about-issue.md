-----
title: Microsoft Internet Explorer about issue
description: This article talk about how to fix the know issue with the Internet Explorer about page.
created: 28-04-2008 00:00:00
modified: 28-04-2008 00:00:00
keywords: Microsoft, Windows, internet explorer, issue, bug
lang: en
-----

# Microsoft Internet Explorer about issue

It happen some time when you click some link, you just get stuck at an Internet Explorer about page. At some point in 
time, this was a well know annoying bug and the fix for this was to register some dll files. 

Re register the following files:

    regsvr32 urlmon.dll
    regsvr32 msscript.ocx
    regsvr32 vbscript.dll
    regsvr32 scrrun.dll
    regsvr32 dispex.dll
