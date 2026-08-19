# Installing and configuring openvpn

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Server Setup](#server-setup)
    - [Server Installation](#server-installation)
    - [Server Configuration](#server-configuration)
- [Client configuration files](#client-configuration-files)
- [Generating the keys](#generating-the-keys)
    - [Keys for the server](#keys-for-the-server)
    - [Keys for the clients](#keys-for-the-clients)
- [Client configuration file](#client-configuration-file)
    - [Create a unified configuration file](#create-a-unified-configuration-file)
- [Allow IP Forwarding](#allow-ip-forwarding)
- [Port forwarding on your internet router](#port-forwarding-on-your-internet-router)
- [Server NAT](#server-nat)
- [VPN Client Setup](#vpn-client-setup)
    - [Windows 10 Client Installation](#windows-10-client-installation)
    - [Windows 10 Client Configuration](#windows-10-client-configuration)
    - [Android Clients](#android-clients)
- [Things left to do or improve](#things-left-to-do-or-improve)
- [Resources](#Resources)

## Introduction

A `VPN`, more specifically, a `Virtual Private Network` is a direct connection to another network. Simple like this is. By default, there's nothing secure on this, but you make use of some `secure` methods to encrypt all data transfer in that private connection to that other network.

**_But what is this useful for?_**

This allow to access a remote network. As well as for enterprises as for home use. 

## Requirements

* A GNU / Linux computer
* A client (could be a Microsoft Windows laptop, smartphone...)

The server will be a Raspberry PI OS (Debian based). 

The client will be a Windows 10 laptop connected through Wi-Fi network. However, for the tests to work, I shared my internet with a hotspot through mobile data. 

## Server Setup

As server, we will use a `Raspberry Pi model 4` and it's default OS. The `raspberry pi` is connected to the onboard ethernet port. The wifi is not used.

### Server Installation

Installing the required software is a matter of running the following command:

```commandline
sudo apt-get install openvpn
```


### Server Configuration

Switch to root user as we have a lot of commands to do:

```commandline
sudo su
```

From now on we can configure a few things. To start on, we need to copy the sample server configuration file:

```commandline
gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz > /etc/openvpn/server.conf
```

Go to the configuration directory of openvpn:

```commandline
cd /etc/openvpn
```

We need to adjust a few things up to our needs in `/etc/openvpn/server.conf`.

**See my sample [/etc/openvpn/server.conf](files/openvpn__etc_openvpn_server.conf) file.**

### Client configuration files

We need to prepare the client configuration file. But we also need to provide a few file to the client so that he is able to connect.

To easy things up, we could use a little trick to group together the required files and create an compressed archive file. So that we only have to provide 1 file to the client, which needs to be unpacked on the host side. 

## Generating the keys

### Keys for the server

```commandline
cp -r /usr/share/easy-rsa/ /etc/openvpn
mkdir /etc/openvpn/easy-rsa/keys
```

Edit:

```commandline
nano /etc/openvpn/easy-rsa/vars
```

**See my [/etc/openvpn/easy-rsa/vars](files/openvpn__etc_openvpn_easy-rsa_vars) file. Or here what to change on the end of the file.**

    export KEY_CONFIG=$EASY_RSA/openssl-easyrsa.cnf
    
    export KEY_COUNTRY="BE"
    export KEY_PROVINCE="NL"
    export KEY_CITY="Brussels"
    export KEY_ORG="David Van Mosselbeen"
    export KEY_EMAIL="hello@davidvanmosselbeen.be"
    export KEY_OU="David Van Mosselbeen Home"

    export KEY_NAME="server"

We now need to generate the dh key. The following command will take a very long time (One hour one a Pi zero):

    openssl dhparam -out /etc/openvpn/dh2048.pem 2048

Be sure we are in the right directory for the following commands:

    cd /etc/openvpn/easy-rsa

Run the initialization step:

    ./easyrsa init-pki

Which result in:

    Note: using Easy-RSA configuration from: ./vars
    
    init-pki complete; you may now create a CA or requests.
    Your newly created PKI dir is: /etc/openvpn/easy-rsa/pki
    
Build CA
    
    ./easyrsa build-ca

*The file is created in `/etc/openvpn/easy-rsa/pki/ca.crt`.*

Generate the server keys with. Note that we used "server" as our name:

    ./easyrsa gen-req server nopass
 
*Files are created in*: 

    req: /etc/openvpn/easy-rsa/pki/reqs/server.req
    key: /etc/openvpn/easy-rsa/pki/private/server.key

And sign it with:
 
    ./easyrsa sign-req server server

*Certificate created at: `/etc/openvpn/easy-rsa/pki/issued/server.crt`*

Note: the second "server" word is the name of our server, a bit confusing in this context. 

Press enter if you get any questions to leave the default values.

Eventually copy the keys under the configuration folder, but in my configuration file, i have specified the full path of the files somewhere in the easy-rsa sub folders. This way it's easier if we redo over the key. 

```commandline
cp /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/server.crt /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/server.key /etc/openvpn
```

New way:

```commandline
cp /etc/openvpn/easy-rsa/pki/ca.crt /etc/openvpn
cp /etc/openvpn/easy-rsa/pki/issued/server.crt /etc/openvpn
cp /etc/openvpn/easy-rsa/pki/private/server.key /etc/openvpn
```

Start (or restart) the service

```commandline
service openvpn start
```

Check if everything seems ok

```commandline
service openvpn status
```

We can now check the log file to see if there's any errors:

```commandline
nano /var/log/openvpn/openvpn.log
```

### Keys for the clients

In this example, we only generate one client, these keys and config files can be shared to multiples clients and they can connect all together, at least with this server configuration we have. This is more easier to manage than generating keys for each client (user or device). It is possible to make in sort that it is not possible to connect with the same key at the same time.   

```commandline
cd /etc/openvpn/easy-rsa/
./easyrsa gen-req client1 nopass
```

Just press enter to accept the default (or predefined) values.

*Files are produced in:*

    Keypair and certificate request completed. Your files are:
    req: /etc/openvpn/easy-rsa/pki/reqs/client1.req
    key: /etc/openvpn/easy-rsa/pki/private/client1.key

**Other and current method**:

```commandline
./easyrsa build-client-full dianic nopass
```

*Where `dianic` is a name we give for the client. Can be whatever we want.*

## Client configuration file

Copy an example file which we will need to fine tune:

```commandline
cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf /etc/openvpn/easy-rsa/keys/client.ovpn
```

See my `client.ovpn` file.

### Create a unified configuration file

Up to now we have one `client.ovpn` file which contains the configuration of the vpn connection. But we have also some certification and key files. So we end up having 5 files to provide to the each client. But there's a nice trick to merge them somehow together in the `ovpn` configuration file so that we only need to provide 1 file to each client. This is very convenient especially for on smartphones and tables where handling files is not so convenient.

To make things more clear, i will copy the `client.ovpn` file to `client_unified.ovpn` and use that later one as unified file. So that I keep the original intact.

Make unified file:

```commandline
cd /etc/openvpn/easy-rsa/keys/
cp client.ovpn client_unified.ovpn
```

We  need to re-edit the `client_unified.ovpn` file and comment ou the `crt` and `key` files it refers to:

    ;ca ca.crt
    ;cert client1.crt
    ;key client1.key
    ;ta ta.key   # We did not create it yet and make use of it

We can use an easy `sed` trick for this:

```commandline
sed -i "s/ca ca.crt/;ca ca.crt/" /etc/openvpn/easy-rsa/keys/client_unified.ovpn
sed -i "s/cert client1.crt/;cert client1.crt/" /etc/openvpn/easy-rsa/keys/client_unified.ovpn
sed -i "s/key client1.key/;key client1.key/" /etc/openvpn/easy-rsa/keys/client_unified.ovpn
```

Now from a console:

```commandline
echo '<ca>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
cat /etc/openvpn/easy-rsa/pki/ca.crt >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
echo '</ca>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
echo '<cert>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
cat /etc/openvpn/easy-rsa/pki/issued/client1.crt >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
echo '</cert>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
echo '<key>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
cat /etc/openvpn/easy-rsa/pki/private/client1.key >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
echo '</key>' >> /etc/openvpn/easy-rsa/keys/client_unified.ovpn
```

###  Allow IP Forwarding

We need to enable to allow IP forwarding as this isn't enabled by default.
This is required as the "server" (our Raspberry Pi) will be the router between the VPN clients and the local network.

We can immediately enable it but this is not permanent yet:

```commandline
echo 1 > /proc/sys/net/ipv4/ip_forward
```

To make it permanent, so that it will work after a reboot edit the following file:

```commandline
nano /etc/sysctl.conf
```

Uncomment the line:

    net.ipv4.ip_forward=1

Save and exit (CTRL+O, CTRL+X)

Your Raspberry Pi can now act as a router

### Port forwarding on your internet router

This is very specific to your internet router. It's probably a wifi router you received with your Internet Service Provider. 

For the moment i have one of Proximus and it's very straightforward to setup port forwarding. In a web browser i had to fill in the ip address of my wifi router, there in the interface i had to define to forward the port 1194 to an internal ip adress of the computer where the openvpn server is installed on.

### Server NAT

We need to enable NAT. This need to be done at firewall side, for this we will use iptables.

Check first the actual state:

    iptables-save

We can create a script in `/etc/openvpn/nat_iptables_script.sh`.

With the following content:

```commandline
IF_MAIN="eth0"
IF_TUNNEL="tun"
#YOUR_OPENVPN_SUBNET=10.9.8.0/24
YOUR_OPENVPN_SUBNET="10.8.0.0/16" # if using server.conf from sample-server-config
iptables -A FORWARD -i $IF_MAIN -o $IF_TUNNEL -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j ACCEPT
iptables -t nat -A POSTROUTING -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j MASQUERADE
```

Change file mode so that we can exceccute this file as a script

```commandline
chmod u+x nat_iptables_script.sh
```

Then to execute the script:

```commandline
./nat_iptables_script.sh
```

After the change, you can see the difference with the command:

    iptables-save
    
Which returns:

```commandline
# Generated by xtables-save v1.8.2 on Fri Oct 30 14:12:50 2020
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A FORWARD -i eth0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i eth0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i eth0 -o tun -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i eth0 -o tun -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -s 10.8.0.0/16 -o eth0 -j ACCEPT
COMMIT
# Completed on Fri Oct 30 14:12:50 2020
# Generated by xtables-save v1.8.2 on Fri Oct 30 14:12:50 2020
*nat
:PREROUTING ACCEPT [0:0]
:INPUT ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A POSTROUTING -s 10.8.0.0/16 -o eth0 -j MASQUERADE
COMMIT
# Completed on Fri Oct 30 14:12:50 2020
```

## VPN Client Setup

The `openvpn` client can work on different kind of operating systems.

### Windows 10 Clients

For this we need a `Microsoft Windows 10` operating system. 

#### Windows 10 Client Installation 

Download the installer from <https://openvpn.net> and execute it. 

#### Windows 10 Client Configuration

Depending on if you unified the `ovpn` file with the crt and key files. But the client need to get the configuration files of the server. Not all files are some needs to be keept secret on the server side.

The client needs to have a few files all placed in a temp .

    ca.crt
    client1.ovpn
    client1.crt
    client1.key
    
In the interface of the openvpn client, you need to import the `client1.ovpn` file. If everything went fine, then there's nothing else to do at all to get the vpn connection working. There's no need to specify the crt or key files if they are at the same location as the ovpn file. With the unified ovpn file there's even less worries.

### Android Clients

We will install the client for Android on a Samsung Galaxy S8+.

## Things left to do or improve

* Generate and make use of a ta.crt file to improve security.
* For security reasons, we could create certificatin and key file for each device that will use the vpn.

## Resources

* <https://openvpn.net>
* <https://raspberrytips.com/install-openvpn-raspberry-pi/>
* <https://wiki.debian.org/OpenVPN>
