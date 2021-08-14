# gpg

## Table of Contents

- [Introduction](#introduction)
- [Encrypting a file with a passphrase (symmetric)](#encrypting-a-file-with-a-passphrase-symmetric)
- [Decrypting a file with a passphrase (symmetric)](#decrypting-a-file-with-a-passphrase-symmetric)

## Introduction

...

## Encrypting a file with a passphrase (symmetric)

    gpg -c mysecrets.txt

## Decrypting a file with a passphrase (symmetric)

    gpg --decrypt mysecrets.txt.gpg

Note, if you have encrypted this file and now try to decrypt it on the same computer, with the same user, then you won't be asked for a password ad the gpg password assistant will have kept this information.

## Resources

- https://gnupg.org/
- https://www.gnupg.org/gph/de/manual/r1023.html
