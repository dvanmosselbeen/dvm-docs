---
description: 
title: pyguicms to joomla migration notes
keywords:
created: 01-01-2012
modified: 
---

Categories of articles that are migrated
========================================

All articles are copied to the new (dvanmosselbeen.be) website. But
previously published articles are now set as unpublished and need a
review.

-   Admin Tools
-   Blender
-   C - Moved data to Debian.
-   Cli
-   Database
-   Debian
-   Games - Didn\'t take back the old and outdated FGFS related docs.
-   GNU
-   Hardware
-   Internet
-   Linux
-   Microsoft
-   Network
-   OS
-   PHP
-   Programming
-   Python
-   Security
-   Server
-   Shell
-   Text Editor
-   Tools
-   Web Dev

Markup tips
===========

It happen that there\'s a glitch when copy pasting data. the \<code\>
tags needs to be removed in the source of the copied data. In vim this
can be easiely done with:

``` {style="text-align: justify;"}
:%s/\<\/code\>//g
```
:::
:::