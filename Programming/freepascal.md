# Freepascal

created: 2012-12-15 00:00:00

This article talk about freepascal.

# Introduction

This page talk about [Free pascal](http://www.freepascal.org/).

# Resources

*   [http://www.freepascal.org/](http://www.freepascal.org) 
*   /usr/share/doc/fp-docs/fpctoc.html

The `#freepascal` on the freenode's network.

# Tools

*   lazarus - Rapid Application Development (RAD) tool for Free Pascal
*   gpc - The GNU Pascal compiler

# Quick start

Read the docs provided with the free pascal compiler

    dpkg -L -L fp-compiler

Read also `less /usr/share/doc/fp-compiler/fpcdemos.txt`

    cp /usr/share/doc/fp-compiler/text/hello.pp .
    fpc -Fuc /usr/lib/fpc/2.0.4/units/i386-linux/rtl/ hello
