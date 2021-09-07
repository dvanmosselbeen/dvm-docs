# Creating a wordlist

## Table of contents

- [With Crunch](#with-crunch)

## With Crunch

`crunch` can be used to create wordlists.

Generate a wordlist of 4 characters long with the numbers `1` `2` `3` `4`:

````commandline
crunch 4 4 1234 -o wordlist-num-1234.txt
````

````commandline
crunch 8 8 12345678 -o wordlist-num-1234.txt
````


Generate...:

````commandline
crunch 8 8 0123456789abcdefghijklmnopqrstuvwxyz -o wordlist-proximus-ap.txt
````

Which want to create a very huge wordlist file!:

```
Crunch will now generate the following amount of data: 25389989167104 bytes
24213780 MB
23646 GB
23 TB
0 PB
```

For example, generate a word list with 6 up to 8 characters long. With only the characters `123abc$` and with the words that start with `a` and end with the letter `b`.

````commandline
crunch 6 8 123abc$ -o wordlist.txt -t a@@@@b
````

Note that creating a wordlist can become huge, very very very very very huge. Look at this example, which will result in a wordlist of 1592 TB !

````commandline
$ crunch 6 8 "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" -o crunch_wordlist.txt
Crunch will now generate the following amount of data: 1750868402284224 bytes
1669758226 MB
1630623 GB
1592 TB
1 PB
Crunch will now generate the following number of lines: 194901576207663
crunch:   0% completed generating output
````

Even when using the compression option it's still very very huge, no matter what compression method you use:

````commandline
$ crunch 6 8 "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" -o crunch_wordlist.txt -z lzma
Crunch will now generate the following amount of data: 1750868402284224 bytes
1669758226 MB
1630623 GB
1592 TB
1 PB
Crunch will now generate the following number of lines: 194901576207663 
````

To create a little list:

````commandline
crunch 6 8 abc -o crunch_wordlist_short.txt
````

To specify that the password list should be 6 characters long and start with the letter a and end with the letter b:

````commandline
crunch 6 6 abc -o crunch_wordlist_short.txt -t a@@@@b
````
