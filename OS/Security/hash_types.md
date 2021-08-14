# Hash Types

## Table of Contents

- [Introduction](#introduction)
- [Identifying the Hash type](#identifying-the-hash-type)
  - Applications
  - [Online Tools](#online-tools)

## Introduction

Before being able to crack a password, you need to know what kind this is.

## Identifying the Hash type

`john` has a build in hash identifier, but isn't great at this and other apps are performing way better than that.

You have different options.

### Applications

* `/usr/bin/hashid`
* The deprecated package `hash-identifier` which contains the file `/usr/share/hash-identifier/hash-id.py` (deprecated according to https://psypanda.github.io/hashID/)
* Getting the last version from `wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py`

Once you know the format of the hash, you can use this trick to quickly find the name

    john --list=formats | grep -iF "md5"

But you can also use the `-j` flag on hashid which even more speed up the process as it will tell you which john format it is:

    hashid -j first_task_hashes/hash1.txt

### hashid

From /usr/bin/hashid

    hashid -j first_task_hashes/hash1.txt

### Online Tools

- https://hashes.com/en/tools/hash_identifier - And this one give you also the hash result (password).
