A dedicated folder with various information related to security for 
Microsoft Windows as well as for GNU/Linux.

# Pages

* [website_pentesting/README](./website_pentesting/README.md)
* [metasploit](./metasploit.md)
* [networking](./networking.md)
* [nmap](./nmap.md)
* [TryHackMe_Path](./TryHackMe_Path.md)
* [veil](./veil.md) 
* [Wi-Fi Cracking](./Wi-Fi%20Hacking.md)
* [wireshark](./wireshark-101.md)

# Tools and their usage

* `netdiscover` - Discover the devices on your network.
* `nmap` - Discover the devices on your network and get more information 
  than `netdiscover`.
* `nc` - Netcat aka nc is an extremely versatile tool. It allows users to connect to specific ports and send and receive data. It also allows machines to receive data and connections on specific ports, which makes nc a very popular tool to gain a Reverse Shell.
* `zenmap` - A graphical user interface of `nmap`.
* wireshark - 
* `arpspoof` - To spoof ARP (for MITM attacks).
* `bettercaps` - Like `arpspoof` but then more advanced. A framework with 
  more options.
* `gobuster` - Directory/file & DNS busting tool written in Go
* `nikto` - web server security scanner
* `hashcat` - World's fastest and most advanced password recovery utility
* `john` - active password cracking tool
* `sqlmap` - automatic SQL injection tool
* `smbmap` - handy SMB enumeration tool
* `smbclient` - command-line SMB/CIFS clients for Unix
* `hydra` - very fast network logon cracker - This is to do online password guessing/cracking.
* `LinPEAS` - Linux Privilege Escalation Awesome Script (Not in Kali (yet). See github: https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)
* `Nessus vulnerability scanner` - Is exactly what you think is its! A vulnerability scanner! It uses techniques similar to Nmap to find and report vulnerabilities, which are then, presented in a nice GUI for us to look at. Nessus is different from other scanners as it doesn't make assumptions when scanning, like assuming the web application is running on port 80 for instance.  Nessus offers a free and paid service, in which some features are left out from the free to make you more inclined to buy the paid service. Their pricing is similar to Burp Suite, so unless you got some spare change, we will be just be using their free version.

## Wifi Cracking

* crack-ng - See [Wi-Fi Cracking](./Wi-Fi%20Hacking.md)

## Backdoor creation

* [veil](./veil.md)

