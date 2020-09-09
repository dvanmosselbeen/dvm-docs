-----
title: Subversion
description: Subversion Reference
created: 15-12-2012 00:00:00
modified: 15-12-2012 00:00:00
keywords:
lang: en
-----

# Subversion Reference

This is a quick reference for Subversion users. I consider this more as a short tutorial to subversion.

## Introduction

If you know nothing about `Subversion`, it's best that you read this article from the top to the bottom. But i still recommend you to read the [Subversion book](http://svnbook.red-bean.com) like i not talk about each topic of it. This article is more an quick reference. If you are planning to use `Subversion`, sure you need to read the `Subversion` book before or after having read this article. Experienced user would take what these needs. I hope this article can help you a bit. You can also get a bit of support on the `Freenode` IRC network on the `#svn` channel.

## Why using Subversion?

If you are a programmer and write many codes or documentation. Sometimes you need to get back to an old version of a file because an old function you have modified suddenly cause to many problems. Or you need a tool to work together with some different people on the same project.

One change the code and submit it to the reposition. You are the second that going to submit the code, subversion tell you that the code has been changed and you need to first update your local copy before you put your own modifications on the `Subversion` server. That to avoid some conflicts. Once all is ok, you resolve the conflict and you may commit your modifications to the subversion server.

`Subversion` is not only interested for programmers, but theoretically it can be very useful for any kind of type of file. Take for example that a little group of users are going to write some documentations. For a such situations, is also ideal to use a revision system. Now it not explain why using`Subversion`.

It's can be compared to CVS (concurrent revisions system). But it's another one application.

## Create a new repository in a directory

First we need to setup a reposition somewhere. Create a temp directory in you're home directory or where you want so that you can test the reposition there. After doing some tests we can delete it easily. To create a reposition type the following:

    svnadmin create /tmp/test_svnreposite

Change the path to your needs! In the most cases and if you want to use`websvn` you need to have a `fsfs` back end so you need to make the reposition as following:

    svnadmin create --fs-type fsfs /tmp/test_svnreposite

The reposition are created. I can suggest you to look, and only look to the files that are created in that location. There are some files you can change like these in the `conf` dir, but that's for later. Like there are no project in that brand new created reposition, you not see many things. You not need to add physically files or modify it directly. We need to add this with the special `subversion` commands.

_We have set here all the file in in an subdirectory of the`/tmp/my_new_svn_project` folder. All data there would be delete after a reboot. So it's really not the ideal place to store data that you want to keep. In this case, it's ideal to set it there, so that when we reboot the computer loose all traces of it and the files are gone._

## Creating a new project

To create a new project, we do that locally on an system, in a temp dir or so. On another directory where you have made that new reposition. Then we commit the new project to the reposition. When creating files, it must be have the following structure:

    /tmp/my_new_svn_project/branches/
    /tmp/my_new_svn_project/tags/
    /tmp/my_new_svn_project/trunk/
        foo.c
        bar.c
        Makefile

Now that we have some files, it's time to add the new project to the reposition.

## Add a new project to the reposite

Like we already have create the files that we want to store in the`Subversion`, we are now able to do add these files to the repository:

    svn import /tmp/my_new_svn_project/ \ 
        file:///path_to_repos/project_name -m "initial import"

You need to pay attention that you been made an sub project on the `svn`reposition. Otherwise you set these files in the root directory of the `svn`repository. But it's been possible that you want to do so, but not in my case here. That's why we give a `projectname` on the svn reposition. The way i proceed is to add different projects in the same repository.

**Look good to the 3 slashes!**

## Get a local copy of a project

Like there is now a project stored in the `Subversion`, we need to get a copy of the files we want to modify. After we have modify the files locally, you need to upload (commit) these changes so that it's again stored in the`Subversion`.

    svn checkout file:///path/to/repos/project_name/trunk>

Take care the we have take the `trunk`, a sub directory of the project. A Now we are ready to modify the files locally on the system. Depending on the tools you use, but i'm sure you know what you need to do. So take you're favorite text editor or tools and modify a bit some files.

## To get a copy of the whole repository

Sometimes you want a copy of the whole reposition.

<pre>[`svn checkout` ](file:///path/to/repos/project_name/trunk</code)`[file:///home/david/svnroot/reposite/>](file:///home/david/svnroot/reposite/</code)`</pre>

Or just a project (directory) of a svn tree

<pre>[`svn checkout` ](file:///home/david/svnroot/reposite/</code)`[file:///home/david/svnroot/reposite/somedir>](file:///home/david/svnroot/reposite/somedir</code)`</pre>

After having modify the files locally you need to commit the changes of these files. Or better, before uploading these files, look to the different of the files.

    To see the diff

Before uploading the files to the reposition, it's always good to see what you changes you made. So it can help when you need to add an message in the log file.

    svn diff file

This output some stuff like `diff` is used to be.

To run an external diff program, here a tool that show it with color:

    svn diff --diff-cmd colordiff

To run an external diff program, here on with color and pipe it to less with colors:

    svn diff --diff-cmd colordiff | less -R

## To get the log of the project

The following will span your console with all the logs since the start:

    svn log

A particular log of a revision:

    svn log -r 5868

A log of a range:

    svn log -r 5860:5868

## Commit all files you have change locally to reposition

    svn commit

To bring your working copy up-to-date with the repo after you commit the local changes. Otherwise it's look that you have an old copy. So we alway need to run the update command after using the commit command!

    svn update

If you change some files locally and not commit these, these changes are lost!

## Getting an old version

Sometimes you need to get an old version of a file. It does not matter why you need to get an old version, but you need to know that you can keep an old version again.

So to get a file of revision number 3:

    svn cat --revision 3 rules.txt

Or get an old version and put it in another file "rules.txt.v2"

    svn cat --revision 2 rules.txt > rules.txt.v2

## Commit an old revision to a new one

Sometimes when you try to make a program or script, you go to the wrong way so that you need to go back in an old state.

    svn update --revision

Getting an list of the files in the reposition:

To get more info of the files.

<pre>[`svn --verbose list` ](file:///home/david/svnroot/reposite/somedir</code)`[file:///home/david/svnroot/reposite/>](file:///home/david/svnroot/reposite/</code)`</pre>

## Exporting a project

Some time we need to export a project when we not want all these `.svn`directories with all that stuff in it. Like these `.svn` files can be are really big. You may discovered that these files are 10 times bigger than your whole project.

<pre>[`svn export` ](file:///home/david/svnroot/reposite/</code)`[file:///home/david/test/svn_guicms/>](file:///home/david/test/svn_guicms/</code)`</pre>

## Making a remote ssh connection to the svn repo

[See](file:///home/david/test/svn_guicms/</code) [](http://svnbook.red-bean.com/en/1.1/ch06.html)[http://svnbook.red-bean.com/en/1.1/ch06.html](http://svnbook.red-bean.com/en/1.1/ch06.html) For more informations for the setup of it. Basically there is nothings to setup to get a remove connection to a `svn` reposition. The previous link is useful for additional informations like access permissions and other ways to access the repos with ssh.

On the client side. Say on the laptop where i want to get a checkout of it the remote svn reposition:

    svn checkout svn+ssh://<IP>/home/david/test/svn_guicms

A new directory `svn_guicms` are created locally. If really you want another name as that you can put the name of the directory:

    svn checkout svn+ssh://<IP>/home/david/test/svn_guicms guicms

You can also export from another user with:

    svn checkout svn+ssh://someUser@<IP>;/home/david/test/svn_guicms guicms

Further i no need to setup any authentication system like the same users on both computers are used. It's the authentication system of ssh that is used to see if that account been exist on that computer.

When you have done some changes locally and want to commit it:

    svn commit

No need to add the whole path (svn commit svn+ssh://IP/home/david/test/svn_guicms). Anyway it will not work if you add the whole path. Like you have get a checkout, the `svn` system know where he need to send the data to.

## To get more help of subversion

There are many methods to get help of `Subversion`. But not forget to read the manual of it. So you need to know where you're documentation of `Subversion` is installed. The manual have many useful informations.

From the `man` pages.

    man svn

You can also get informations from `Subversion`.

    svn help
    svn help <subcommand>

## Some useful tools

*   `cvs2svn` Convert a cvs repository to a subversion repository Converts a CVS repository (including its branches and tags) to a Subversion repository. It is designed for one-time conversions, not for repeated synchronizations between CVS and Subversion.

*   `websvn` interface for subversion repositories written in PHP WebSVN is a set of PHP scripts that provides remote access to subversion repositories. It supports several repositories, can be customized, supports Apache MultiViews, and can provide RSS feeds.

*   `esvn` frontend for the Subversion revision system written in Qt eSvn is a graphical client written in Qt for the subversion revision control system (svn).

*   `svn-buildpackage` helper programs to maintain Debian packages with Subversion svn-buildpackage (formerly svn-devscripts) contains tools that help to automate the task of maintaining Debian packages inside of a Subversion repository. They are intended to be used by Debian developers to simplify the error-prone actions with the svn, devscripts and dpkg-dev utilities.

*   `rapidsvn` A GUI client for subversion. An graphical client for the subversion revision control system (svn).

## Other notes

See also svn propset to make use of these build in templating system i.e.:

    $Id: curator,v 1.34 2003/09/20 21:28:52 blais Exp $

See the [svnbook](http://svnbook.red-bean.com/nightly/en/svn.advanced.props.special.keywords.html)

To avoid that svn want to add the `pyc` files, so that when you do a `svn status` it not shows up compiled python files:

    svn propset svn:ignore "*.pyc" .

Then look with `svn diff`:

    Property changes on: .
    ___________________________________________________________________
    Name: svn:ignore
       + *.pyc

You now need to commit it so that this property will be included on the repository. See [props ignore] ([http://svnbook.red-bean.com/nightly/en/svn.advanced.props.special.ignore.html](http://svnbook.red-bean.com/nightly/en/svn.advanced.props.special.ignore.html)) in the svn book.

To add some file to ignore:

    svn propedit svn:ignore .

This will start `vim`, where you can add files. Note, add each file or pattern on a new line.

To see the files that are ignored:

    svn status --no-ignore

## Deployment with apache2

See [](http://svnbook.red-bean.com/nightly/en/svn.serverconfig.httpd.html)[http://svnbook.red-bean.com/nightly/en/svn.serverconfig.httpd.html](http://svnbook.red-bean.com/nightly/en/svn.serverconfig.httpd.html)

    aptitude install libapache2-svn

The module is automatically enabled, checkout with a2e

    <Location /svn/pyguicms/>
        DAV svn
        SVNPath /home/david/svn_files/pyguicms
    </Location>

Create a password file:

    htpasswd -cm /etc/svn-auth-file some-username

To add some more users, re run the above command.

Ensure that others are not able to read this file!

    chmod o-r /etc/svn-auth-file

Note also that this file needs to be owned by the user who runs the server: chown www-data /etc/svn-auth-file

    <Location /svn>
        DAV svn
        SVNPath /var/svn
        AuthType Basic
        AuthName "Subversion repository"
        AuthUserFile /etc/svn-auth-file
        Require valid-user
    </Location>

## Resources

*   The [svn book](http://svnbook.red-bean.com/)
*   [](http://systhread.net/texts/200607subver.php)[http://systhread.net/texts/200607subver.php](http://systhread.net/texts/200607subver.php)

## Tools

*   mpy-svn-stats - Simple and easy to use svn statistics generator
*   websvn - interface for subversion repositories written in PHP
