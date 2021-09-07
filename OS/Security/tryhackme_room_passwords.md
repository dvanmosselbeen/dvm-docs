# Try Hack Me Passwords

Do not stress, these are not my passwords.
This sounds like a joke, yes, silly even. 

These are just the passwords, flags, or whatever for the CTF (Capture the Flags) I put here. Instead of adding them in my writeups.

Note to myself, clean up my writeups, remove passwords, flags or questions from there and put it here.

## Table of contents

- [Daily Bugle](#daily-bugle)
- [Nax](#nax)
- [blog](#blog)
- [ColddBox: Easy](#colddbox-easy)
- [Mr Robot](#mr-robot)
- [Agent Sudo](#agent-sudo)
- [Chocolate Factory](#chocolate-factory)
- [Lazy Admin](#lazy-admin)
- [Startup](#startup)
- [Bounty Hunter (Cowboy Hacker)](#bounty-hunter-cowboy-hacker)
- [Hydra](#hydra)
- [Brooklyn Nine Nine](#brooklyn-nine-nine)

## Daily Bugle

Room: <https://tryhackme.com/room/dailybugle>


Access the web server, who robbed the bank?

    SpiderMan

What is the Joomla version?

_Hint: I wonder if this version of Joomla is vulnerable..._

    3.7.0

*Instead of using SQLMap, why not use a python script!*

What is Jonah's cracked password?

_Hint: SQLi & JohnTheRipper_

    spiderman123

What is the user flag?

    27a260fe3cba712cfdedb1c86d80442e

What is the root flag?

    eec3d53292b1821868266858d7fa6f79

Other info:

- User `jonah` and it's password hash `$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm` and his cracked password `spiderman123`.
- Database credentials: `root:nv5uz9r3ZEDzVjNu`

## Nax

Room: <https://tryhackme.com/room/nax>

What hidden file did you find?

    PI3T.Png

Who is the creator of the file?

    Piet Mondrian

If you get an error running the tool on your downloaded image about an unknown ppm format -- open it with gimp or another paint program and export to ppm format, and try again!

    No answer needed

What is the username you found?

    nagiosadmin

What is the password you found?

_Hint: % is a separator_

    n3p3UQ&9BjLp4$7uhWdY

What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

    CVE-2019-15949

Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`.

    No answer needed

After Metasploit has started, let's search for our target exploit using the command 'search applicationame'. What is the full path (starting with exploit) for the exploitation module?

    exploit/linux/http/nagios_xi_authenticated_rce

The actual up to date answer is: `exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce`

Compromise the machine and locate user.txt

    THM{84b17add1d72a9f2e99c33bc568ae0f1}

Compromise the machine and locate root.txt

    THM{c89b2e39c83067503a6508b21ed6e962}

Other information:

- `/PI3T.PNg`

## blog

root.txt

    9a0b2b618bef9bfa7ac28c1353d9f318

user.txt

    c8421899aae571f7af486492b71a8ab7

Where was user.txt found?

_Hint: HINT 1, IF THERE IS_

    /media/usb

What CMS was Billy using?

    WordPress

What version of the above CMS was being used?

    5.0

User ids found:

- `kwheel`
- `bjoel`

## ColddBox: Easy

wp account - `c0ldd:9876543210`
shell account - `c0ldd:cybersecurity`

## Mr Robot

What is key 1?

_Hint: Robots_

    073403c8a58a1f80d943455fb30724b9

What is key 2?

_Hint: White coloured font_

    822c73956184f694993bede3eb39f959

What is key 3?

_Hint: nmap_

    04787ddef27c3dee1ee161b21670b4e4

Other things:

- base64 hash: `ZWxsaW90OkVSMjgtMDY1Mgo=`
- elliot:ER28-0652
- robot:abcdefghijklmnopqrstuvwxyz

## Agent Sudo

passwords:

- FTP server: `chris:crystal`
- Password-protected file 8702.zip: `alien`

```commandline
echo "QXJlYTUx" | base64 -d
Area51
```

ssh user account - `james:hackerrules!`

james, user flag: `b03d975e8c92a7c04146cfa7a5a313c7`

What is the incident of the photo called? [roswell alien autopsy]()

root flag: `b53a02f55b57d4439e3341834d70c062`

## Chocolate Factory

Enter the key you found!

    -VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=

What is Charlie's password?

    cn7824

Enter the user flag

    flag{cd5509042371b34e4826e4838b522d2e}

Enter the root flag

    flag{cec59161d338fef787fcb4e296b42124}

Also:

- `http://localhost/key_rev_key <- You will find the key here!!!`

## Lazy Admin

- Room is here: <https://tryhackme.com/room/lazyadmin>
- Write up is here:

Credentials and other data:

- Database hash: `42f749ade7f9e195bf475f37a44cafcb`. [CrackStation](https://crackstation.net/) told me: `Password123`
- `user.txt` - `THM{63e5bce9271952aad1113b6f1ac28a07}`
- `root.txt` - `THM{6637f41d0177b6f37cb20d775124699f}`

## Startup

- Room is here: <https://tryhackme.com/room/startup>
- Write up is here: <https://github.com/dvanmosselbeen/TryHackMe_writeups/tree/main/startup>

Credentials and other data:

- user: `lennie` - passwd: `c4ntg3t3n0ughsp1c3`
- root.txt  THM{03ce3d619b80ccbfb3b7fc81e46c0e79}

## Bounty Hunter (Cowboy Hacker)

- Room is here: <https://tryhackme.com/room/cowboyhacker>
- Write up is here: <https://github.com/dvanmosselbeen/TryHackMe_writeups/tree/main/bounty-hunter>

Credentials and other data:

- Who wrote the task list?: `lin`
- What service can you bruteforce with the text file found?: `ssh`
- What is the users password?: `RedDr4gonSynd1cat3`
- user.txt: `THM{CR1M3_SyNd1C4T3}`
- root.txt: `THM{80UN7Y_h4cK3r}`

## Hydra

Use Hydra to bruteforce molly's web password. What is flag 1? 

    THM{2673a7dd116de68e85c48ec0b1f2612e}

Use Hydra to bruteforce molly's SSH password. What is flag 2?

    THM{c8eeb0468febbadea859baeb33b2541b}

Other user accounts: 

- `molly:sunshine`
- `molly:butterfly`

##  Brooklyn Nine Nine

- User flag: `ee11cbb19052e40b07aac0ca060c23ee`
- Root flog: `63a9f0ea7bb98050796b649e85481845`
- user: `jake:987654321`
