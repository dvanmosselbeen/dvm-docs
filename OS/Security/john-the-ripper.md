# John The Ripper

## Introduction

John The Ripper, john for the friends, is a password cracker tool that make use of a wordlist.

This document is based on following the THM room: https://tryhackme.com/room/johntheripper0

## Installation 

### Linux

Probably the GNU/Linux distribution has packaged this for your.

### Windows

For Windows, you can download John The Ripper here: https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip

### Word lists

There are different wordlist out there, the most popular one is the `rockyou.txt` file which is available trough the package `wordlists`. See in `/usr/share/wordlists`.

But take also a look to the SecLists, https://github.com/danielmiessler/SecLists - apt-get install seclist Which contains various wordlists. Very interesting to see is that there's a dedicated sub-folder (on github) called passwords/Leaked-Databases where different kind of passwords lists are stored.

## Basic usage

John has a build in hash identifier, but isn't great at this job. So you can try this one:

```commandline
john --wordlist=/usr/share/wordlists/rockyou.txt somehash.txt
```

## Identifying the type of hash

Like said, john has a build in hash identifier, but isn't great at this and other apps are performing way more better than that.

You have different options:

* `/usr/bin/hashid`
* The deprecated package `hash-identifier` which contains the file `/usr/share/hash-identifier/hash-id.py` (deprecated according to https://psypanda.github.io/hashID/)
* Getting the last version from `wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py`
* Online - https://hashes.com/en/tools/hash_identifier - And this one give you also the hash result (password).

Once you know the format of the hash, you can use this trick to quickly find the name

    john --list=formats | grep -iF "md5"

But you can also use the `-j` flag on hashid which even more speed up the process as it will tell you which john format it is:

    hashid -j first_task_hashes/hash1.txt

### hashid

From /usr/bin/hashid

    hashid -j first_task_hashes/hash1.txt

## Using john 

    john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt

## Cracking basic hashes

```commandline
hashid -j hashfile.txt
john --format=<format> --wordlist=/usr/share/wordlists/rockyou.txt hashfile.txt
```

# Cracking Windows Authentication Hashes

You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, by using a tool like Mimikatz or from the Active Directory database: NTDS.dit. You may not have to crack the hash to continue privilege escalation- as you can often conduct a "pass the hash" attack instead, but sometimes hash cracking is a viable option if there is a weak password policy.

```commandline
echo 5460C85BD858A11475115D2DD3A82333 > ntlm.txt
hashid -j ntlm.txt
john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt
```

# Cracking /etc/shadow Hashes

## Unshadowing

John can be very particular about the formats it needs data in to be able to work with it, for this reason- in order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The basic syntax of unshadow is as follows:

    unshadow [path to passwd] [path to shadow]

**Let's break that down**:

`unshadow` - Invokes the unshadow tool

`[path to passwd]` - The file that contains the copy of the /etc/passwd file you've taken from the target machine

`[path to shadow]` - The file that contains the copy of the /etc/shadow file you've taken from the target machine

Example Usage:

    unshadow local_passwd local_shadow > unshadowed.txt

Note on the files

When using `unshadow`, you can either use the entire `/etc/passwd` and `/etc/shadow` file- if you have them available, or you can use the relevant line from each, for example:

FILE 1 - local_passwd

Contains the `/etc/passwd` line for the root user:

    root:x:0:0::/root:/bin/bash

FILE 2 - local_shadow

Contains the `/etc/shadow` line for the root user:

    root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::

## Cracking

We're then able to feed the output from `unshadow`, in our example use case called `unshadowed.txt` directly into John. We should not need to specify a mode here as we have made the input specifically for John, however in some cases you will need to specify the format as we have done previously using: --format=sha512crypt

    john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt


    echo > etchashes.txt
    john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt etchashes.txt

## Single Crack Mode

So far we've been using John's wordlist mode to deal with brute forcing simple., and not so simple hashes. But John also has another mode, called Single Crack mode. In this mode, John uses only the information provided in the username, to try and work out possible passwords heuristically, by slightly changing the letters and numbers contained within the username.

### Word Mangling

The best way to show what Single Crack mode is,  and what word mangling is, is to actually go through an example:

If we take the username: Markus

Some possible passwords could be:

* Markus1, Markus2, Markus3 (etc.)
* MArkus, MARkus, MARKus (etc.)
* Markus!, Markus$, Markus* (etc.)

This technique is called word mangling. John is building it's own dictionary based on the information that it has been fed and uses a set of rules called "mangling rules" which define how it can mutate the word it started with to generate a wordlist based off of relevant factors for the target you're trying to crack. This is exploiting how poor passwords can be based off of information about the username, or the service they're logging into.

### GECOS

John's implementation of word mangling also features compatibility with the Gecos fields of the UNIX operating system, and other UNIX-like operating systems such as Linux. So what are Gecos? Remember in the last task where we were looking at the entries of both /etc/shadow and /etc/passwd? Well if you look closely You can see that each field is seperated by a colon ":". Each one of the fields that these records are split into are called Gecos fields. John can take information stored in those records, such as full name and home directory name to add in to the wordlist it generates when cracking /etc/shadow hashes with single crack mode.

### Using Single Crack Mode

To use single crack mode, we use roughly the same syntax that we've used to so far, for example if we wanted to crack the password of the user named "Mike", using single mode, we'd use:

    john --single --format=[format] [path to file]

`--single` - This flag lets john know you want to use the single hash cracking mode.

Example Usage:

    john --single --format=raw-sha256 hashes.txt

A Note on File Formats in Single Crack Mode:

If you're cracking hashes in single crack mode, you need to change the file format that you're feeding john for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example- we would change the file hashes.txt

From:

    1efee03cdcb96d90ad48ccc7b8666033

To

    mike:1efee03cdcb96d90ad48ccc7b8666033

Hash type: raw-md5

```commandline
echo 7bf6d9bb82bed1302f331fc6b816aada > joker_pass1.txt
echo joker:7bf6d9bb82bed1302f331fc6b816aada > joker_pass2.txt
john --single --format=raw-md5 joker_pass.txt
```

passwd: Jok3r

## Custom Rules

### What are Custom Rules?

As we journeyed through our exploration of what John can do in Single Crack Mode- you may have some ideas about what some good mangling patterns would be, or what patterns your passwords often use- that could be replicated with a certain mangling pattern. The good news is you can define your own sets of rules, which John will use to dynamically create passwords. This is especially useful when you know more information about the password structure of whatever your target is.

### Common Custom Rules

Many organisations will require a certain level of password complexity to try and combat dictionary attacks, meaning that if you create an account somewhere, go to create a password and enter:

    polopassword

You may receive a prompt telling you that passwords have to contain at least one of the following:

* Capital letter
* Number
* Symbol

This is good! However, we can exploit the fact that most users will be predictable in the location of these symbols. For the above criteria, many users will use something like the following:

    Polopassword1!

A password with the capital letter first, and a number followed by a symbol at the end. This pattern of the familiar password, appended and prepended by modifiers (such as the capital letter or symbols) is a memorable pattern that people will use, and reuse when they create passwords. This pattern can let us exploit password complexity predictability.

Now this does meet the password complexity requirements, however as an attacker we can exploit the fact we know the likely position of these added elements to create dynamic passwords from our wordlists.

### How to create Custom Rules

Custom rules are defined in the `john.conf file`, usually located in `/etc/john/john`.conf if you have installed John using a package manager or built from source with `make` and in `/opt/john/john.conf` on the TryHackMe Attackbox.

Let's go over the syntax of these custom rules, using the example above as our target pattern. Note that there is a massive level of granular control that you can define in these rules, I would suggest [taking a look at the wiki here](https://www.openwall.com/john/doc/RULES.shtml) in order to get a full view of the types of modifier you can use, as well as more examples of rule implementation.

The first line:

`[List.Rules:THMRules]` - Is used to define the name of your rule, this is what you will use to call your custom rule as a John argument.

We then use a regex style pattern match to define where in the word will be modified, again- we will only cover the basic and most common modifiers here:

`Az` - Takes the word and appends it with the characters you define

`A0 `- Takes the word and prepends it with the characters you define

`c` - Capitalises the character positionally

These can be used in combination to define where and what in the word you want to modify.

Lastly, we then need to define what characters should be appended, prepended or otherwise included, we do this by adding character sets in square brackets `[ ]` in the order they should be used. These directly follow the modifier patterns inside of double quotes `" "`. Here are some common examples:

`[0-9]` - Will include numbers 0-9

`[0]` - Will include only the number 0

`[A-z]` - Will include both upper and lowercase

`[A-Z]` - Will include only uppercase letters

`[a-z]` - Will include only lowercase letters

`[a]` - Will include only a

`[!£$%@]` - Will include the symbols !£$%@

Putting this all together, in order to generate a wordlist from the rules that would match the example password "Polopassword1!" (assuming the word polopassword was in our wordlist) we would create a rule entry that looks like this:

`[List.Rules:PoloPassword]`

`cAz"[0-9] [!£$%@]"`

In order to:

Capitalise the first  letter - `c`

Append to the end of the word - `Az`

A number in the range 0-9 - `[0-9]`

Followed by a symbol that is one of `[!£$%@]`

### Using Custom Rules

We could then call this custom rule as a John argument using the  --rule=PoloPassword flag.

As a full command: john `--wordlist=[path to wordlist]` `--rule=PoloPassword [path to file]`

As a note I find it helpful to talk out the patterns if you're writing a rule- as shown above, the same applies to writing RegEx patterns too.

Jumbo John already comes with a large list of custom rules, which contain modifiers for use almost all cases. If you get stuck, try looking at those rules [around line 678] if your syntax isn't working properly.

Now, time for you to have a go!

## Cracking a Password Protected Zip File

Yes! You read that right. We can use John to crack the password on password protected Zip files. Again, we're going to be using a separate part of the john suite of tools to convert the zip file into a format that John will understand, but for all intents and purposes, we're going to be using the syntax that you're already pretty familiar with by now.

### Zip2John

Similarly to the `unshadow` tool that we used previously, we're going to be using the `zip2john` tool to convert the zip file into a hash format that John is able to understand, and hopefully crack. The basic usage is like this:

```commandline
zip2john [options] [zip file] > [output file]
```

`[options]` - Allows you to pass specific checksum options to zip2john, this shouldn't often be necessary

`[zip file]` - The path to the zip file you wish to get the hash of

`>` - This is the output director, we're using this to send the output from this file to the...

`[output file]` - This is the file that will store the output from

Example Usage

```commandline
zip2john zipfile.zip > zip_hash.txt
```

### Cracking

We're then able to take the file we output from zip2john in our example use case called "zip_hash.txt" and, as we did with unshadow, feed it directly into John as we have made the input specifically for it.

```commandline
john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt
```

## Cracking Password Protected RAR Archives

We can use a similar process to the one we used in the last task to obtain the password for rar archives. If you aren't familiar, rar archives are compressed files created by the Winrar archive manager. Just like zip files they compress a wide variety of folders and files.

### Rar2John

Almost identical to the `zip2john` tool that we just used, we're going to use the `rar2john` tool to convert the rar file into a hash format that John is able to understand. The basic syntax is as follows:

```commandline
rar2john [rar file] > [output file]
```

`rar2john` - Invokes the rar2john tool

`[rar file]` - The path to the rar file you wish to get the hash of

`>` - This is the output director, we're using this to send the output from this file to the...

`[output file]` - This is the file that will store the output from

Example Usage

```commandline
rar2john rarfile.rar > rar_hash.txt
```

### Cracking

Once again, we're then able to take the file we output from rar2john in our example use case called "rar_hash.txt" and, as we did with zip2john we can feed it directly into John..

```commandline
john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt
```

## Cracking SSH Keys with John

Okay, okay I hear you, no more file archives! Fine! Let's explore one more use of John that comes up semi-frequently in CTF challenges. Using John to crack the SSH private key password of `id_rsa` files. Unless configured otherwise, you authenticate your SSH login using a password. However, you can configure key-based authentication, which lets you use your private key, id_rsa, as an authentication key to login to a remote machine over SSH. However, doing so will often require a password- here we will be using John to crack this password to allow authentication over SSH using the key.

### SSH2John

Who could have guessed it, another conversion tool? Well, that's what working with John is all about. As the name suggests `ssh2john` converts the `id_rsa` private key that you use to login to the SSH session into hash format that `john` can work with. Jokes aside, it's another beautiful example of John's versatility. The syntax is about what you'd expect. Note that if you don't have `ssh2john` installed, you can use `ssh2john.py`, which is located in the `/opt/john/ssh2john.py`. If you're doing this, replace the ssh2john command with `python3 /opt/ssh2john.py` or on Kali, `python /usr/share/john/ssh2john.py`.

```commandline
ssh2john [id_rsa private key file] > [output file]
```

`ssh2john` - Invokes the ssh2john tool

`[id_rsa private key file]` - The path to the id_rsa file you wish to get the hash of

`>` - This is the output director, we're using this to send the output from this file to the...

`[output file]` - This is the file that will store the output from


Example Usage

```commandline
ssh2john id_rsa > id_rsa_hash.txt
```

Example Usage on Kali

```commandline
python /usr/share/john/ssh2john.py id_rsa > id_rsa_hash.txt
```

### Cracking

For the final time, we're feeding the file we output from ssh2john, which in our example use case is called "id_rsa_hash.txt" and, as we did with rar2john we can use this seamlessly with John:

```commandline
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt
```

## Further Reading

Thank you for completing this room on John the Ripper! I hope you've learnt a lot along the way. I'm sure by now you understand the basic principles and the pattern that there is to using John with even the most obscure supported hashes. I'd recommend checking out the [Openwall Wiki here](https://www.openwall.com/john/) for more information about using John, and advice, updates or news about the tool.

## Resources

* https://www.openwall.com/john/doc/EXAMPLES.shtml
