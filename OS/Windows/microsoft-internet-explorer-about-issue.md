---
description: This article talk about how to fix the know issue with the Internet Explorer about page.
keywords: microsoft windows internet explorer about issue
title: Microsoft Internet Explorer about issue
created: 28-04-2008
---

It happen some time when you click some link, you just get stuck at an
Internet Explorer about page.

Re register the following files:

    regsvr32 urlmon.dll
    regsvr32 msscript.ocx
    regsvr32 vbscript.dll
    regsvr32 scrrun.dll
    regsvr32 dispex.dll
