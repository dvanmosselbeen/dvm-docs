-----
title: CVS
description: This article talk about CVS.
created: 15-12-2012 00:00:00
modified: 15-12-2012 00:00:00
keywords: programming, development
lang: be
-----

# CVS 

## Introduction

On you're `Debian` system you can easy get some good informations. Go to the location:

    /usr/share/doc/cvs/

And read the manual of that product.

It's good that you also install the `cvsbook` to know more about it. With the help provided with `cvs` you have not enough informations. So if you not know about `cvs` you probably need to install the `cvsbook`. Once the book install go to:

    /usr/share/doc/cvsbook/

This article is here as an reminder. So i really suggest you to read the`cvsbook`

To get local an copy of an project

    cvs -d '/home/david/cvsroot' checkout cli_addressbook
    cd cli_addressbook

The project is downloaded in to the current directory where we actually are. So use the `pwd` before. Then we need now to enter in the directory we have downloaded to work on the files locally, after modify the files. We want to upload the different.

## To commit the new local changes to the server

    cvs commit cli_addressbook.py

The text editor open(vim) where we can write an msg on the top of the file to leave an message for in the log system. To write and exit vim (esc)':wq'. To not use the default editor, we can add an message by passing an option, for example:

    cvs commit -m "Added an optimization pass" cli_addressbook.py

Then when we are done, we need to clean up the local files we have downloaded from cvs. cd ..

    rm -r cli_addressbook

This remove the directory 'cli_addressbook' that we have downloaded from the cvs server. That avoid to leave some uneeded old files...

And to view the difference of an local file an one in the cvs tree:

    cd cli_addressbook<br />cvs diff cli_addressbook.py

After the `~/.bashrc` file has been modified by adding an line `export CVSROOT=/home/david/cvsroot`. We can use:

    cvs checkout cli_addressbook

instead of:

    cvs -d '/home/david/cvsroot' checkout cli_addressbook

But then we have not the nice tab autocompletion!!! So i can suggest to use the last one, also after adding the variable.

To view the status of an file locally

    cvs status -v cli_addressbook.py

A shortcut way.

    cvs -d '/home/david/cvsroot' checkout cli_addressbook
    cvs checkout cli_addressbook<br />cd cli_addressbook

Modify the files, then upload the diff's

    cvs commit -m "Added user input so that he can input the data."

To remove locally the directory after update.

This not update the local file with cvs!!!

    cvs -d '/home/david/cvsroot/' release -d cli_addressbook/
