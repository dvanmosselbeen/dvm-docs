-----

* title: nmap
* description: This article is dedicated to nmap.
* created: 27-07-2021 19:55:00
* modified: 27-07-2021 19:55:00
* keywords: debian, gnu, linux, operating, system, admin, network, lan, security, hacking
* lang: en

-----

# Table of Contents

* [Introduction](#introduction)
* [Quick Cheat Sheet](#quick-cheat-sheet)
* [Extra Tools](#extra-tools)
* [Resources](#resources)

# Introduction

`nmap` (or it's GUI alternative, `zenmap`) is the ultimate tool for network discovery.

# Quick cheat sheet

Essentially borrowed from the zenmap graphical user interface.

*NOTE that you get more information if running this with root priviledges.*

* `nmap -T4 -A -v` - Intense Scan
* `nmap -sS -sU -T4 -A -v` - Intense Scan plus UDP
* `nmap -p 1-65535 -T4 -A -v` - Intense Scan, all TCP ports
* `nmap -T4 -A -v -Pn` - Intense scan, no ping
* `nmap -sn` - Ping scan
* `nmap -T4 -F` - Quick scan
* `nmap -sV -T4 -O -F --version-light` - Quick scan plus
* `nmap -sn --traceroute` - Quick traceroute
* `nmap` - Regular scan
* `nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)"` - Slow Comprehensive scan
* `nmap -p- -A` - Scan ALL ports (above 1024 too) and get OS info

You can also store scan results into a file, which is cool:

````commandline
mkdir ~/nmap
nmap -sC -sV -oN nmap/initial 10.10.10.10
````



# Extra Tools

* `zenmap` - Which is a graphical interface to nmap. A must have

# Resources

* [zenmap on Tryhackme](https://tryhackme.com/room/furthernmap) - A dedicated room about zenmap.
