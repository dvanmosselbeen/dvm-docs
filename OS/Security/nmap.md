# nmap

## Table of Contents

- [Introduction](#introduction)
- [Quick cheat sheet](#quick-cheat-sheet)
- [Extra Tools](#extra-tools)
- [Resources](#resources)

## Introduction

`nmap` (or it's GUI alternative, `zenmap`) is the ultimate tool for network discovery.

## Quick cheat sheet

Essentially borrowed from the zenmap graphical user interface.

*NOTE that you get more information if running this with root priviledges.*

```commandline
export IP=<SOME_IP>
```

* `nmap -sV $IP` - 
* `nmap -T4 -A -v $IP` - Intense Scan
* `nmap -sS -sU -T4 -A -v $IP` - Intense Scan plus UDP
* `nmap -p 1-65535 -T4 -A -v $IP` - Intense Scan, all TCP ports
* `nmap -T4 -A -v -Pn $IP` - Intense scan, no ping
* `nmap -sn $IP` - Ping scan
* `nmap -T4 -F $IP` - Quick scan
* `nmap -sV -T4 -O -F --version-light $IP` - Quick scan plus
* `nmap -sn --traceroute $IP` - Quick traceroute
* `nmap $IP` - Regular scan
* `nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" $IP` - Slow Comprehensive scan
* `nmap -sV -sC -oA scans/initial-scan $IP` - Scan version number and common scripts and save scan output in the 3 diff formats. 
* `nmap -p- -A $IP` - Scan ALL ports (above 1024 too) and get OS info

Use:

- `-Pn` if the machine seems down but is up (Firewall blocking)

You can also store scan results into a file, which is cool:

```commandline
nmap -sC -sV -oA /tmp/nmap_initial <IP>
```

Scan for vulnerabilites:

```commandline
nmap -sV -vv --script vuln $IP
```

## Extra Tools

* `zenmap` - Which is a graphical interface to nmap. A must have

## Resources

* [nmap on Tryhackme](https://tryhackme.com/room/furthernmap) - A dedicated room about zenmap.
