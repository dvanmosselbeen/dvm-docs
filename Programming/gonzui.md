-----
title: Gonzui
description: This article talk about how i have setup gonzui and how i use it on a Debian box. 
created: 15-12-2012 00:00:00
modified: 15-12-2012 00:00:00
keywords: programming, tool, development
lang: be
-----

# Gonzui

# Introduction

`gonzui` is useful for programmers. With a web browser you can easy see the source code of your projects, get some documentation of functions, classes or parts of codes. And also see where these functions are used. You can also do a search. It's also and a nice toy to show your code to people, each line have an anchor, so you can give any URL link that point to each line of code.

You can easy import an `apt` source of a package or `cvs` or `svn`(`subversion`) reposition. `gonzui` is an ideal tool if you want to learn the code of someone or for big projects.

# Setup

I have made a custom setup, like i not want to run the stuff as root user and that the stuff are located in the `/var/...`. So i have a bit modified the default config file and i have place the stuff in my home directory. My goal is to create a user account only for that task and let `gozui` running as that user account. With some `cron` job.

## Config

We first need to copy the config example to his own home directory.

    cp /etc/gonzuirc.sample ~/.gonzuirc

I have change the paths in the `~/.gonzuirc`, like i want to run it with an user that not have root privileges and also that the different stuff are logged in my home. I have also add some stuff to exclude in 'exclude_pattern'. Here my '~/.gonzuirc':

    {
      :access_log_file          => "/home/david/.gonzui/log/gonzui/access.log",
      :base_mount_point         => "/",
      :cache_directory          => "/home/david/.gonzui/var/spool/gonzui/gonzui.db/cache",
      :catalog_directory        => "/home/david/.gonzui/usr/share/gonzui/catalog",
      :daemon                   => false,
      :db_cache_size            => 5242880,
      :db_directory             => "/home/david/.gonzui/var/spool/gonzui/gonzui.db",
      :default_results_per_page => 10,
      :doc_directory            => "/usr/share/gonzui/doc",
      :encoding_preference      => ["iso-2022-jp", "euc-jp", "utf-8", \
        "shift_jis", "cp932", "iso-8859-1", "ascii"],
      :exclude_pattern          => /~$|\.bak$|CVS|\.pyc$|\.swp$|\.svn/,
      :gonzui_log_file          => "/home/david/.gonzui/var/log/gonzui/gonzui.log",
      :group                    => "david",
      :http_port                => 46984,
      :max_packages_per_page    => 100,
      :max_pages                => 20,
      :max_results_per_page     => 50,
      :max_words                => 10,
      :noindex_formats          => [],
      :nresults_candidates      => [10, 20, 30, 50],
      :pid_file                 => "/home/david/.gonzui/var/run/gonzui.pid",
      :quiet                    => false,
      :site_title               => "gonzui",
      :temporary_directory      => "/tmp",
      :user                     => "david",
      :utf8                     => true,
      :verbose                  => false,
    }

## Creating the needed directories and files

We now need to create some directories and some files. Like i move the stuff to my home directory:

    mkdir -p ~/.gonzui/var/log/gonzui/
    touch ~/.gonzui/var/log/gonzui/gonzui.log
    mkdir -p ~/.gonzui/var/spool/gonzui/
    touch ~/.gonzui/var/spool/gonzui/gonzui.db
    mkdir -p ~/.gonzui/log/gonzui/
    touch ~/.gonzui/log/gonzui/access.log
    mkdir -p ~/.gonzui/usr/share/gonzui/catalog

# Import stuff to the database

We now need to import some stuff we want. Usually we import the different directories that contains the different files of the project. Maybe some time we only want to import some specific files.

I don't know why at this stage why i need to provide the database path. We only need to specify it the first time we use the 'gonzui-import'.

    gonzui-import /home/david/python/abuse_reporter/ \
      -d /home/david/.gonzui/var/spool/gonzui/gonzui.db

Note: The path /home/david/python/abuse_reporter/ contains some python files. The is to split the long line into two little lines.

    gonzui-import /home/david/python/abuse_reporter/

Importing from a svn repo:

    gonzui-import --svn file:///home/david/svn_files/pyguicms/ trunk

While experimenting with 'gonzui', you probably want to import some stuff then remove it again, playing a bit with the new toy. Let's write a little script to import the diferent paths/files. Take for example: We fill a file that contain all the directories or files we want to import. Let's make a little script that will automate the import procedure:

    #!/usr/bin/env python
    # name: gonzui_mass_importer.py
    import os
    # File containing the differents paths/files we want to import
    importFile = '/home/david/to_import_gonzui'
    for line in open(importFile):
        if (line.find(' ') >= 1):
            # We have find a argument
            os.popen(u'gonzui-import %s %s' % (line.split()[0],line.split()[1]))
        else:
            # We have not detect an argument
            os.popen('gonzui-import %s' % (line))

Maybe put this script in your ~/bin to have it included in your path directory. So that you can execute this script from anywhere on your computer with your user. I have place this script in my '~/bin' and have call it gonzui_mass_importer. Without the '.py' extension.

Make the script executable for everyone:

     chmod a+x ~/bin/gonzui_mass_importer

Here's an example of what my file `/home/david/to_import_gonzui`:

    /home/david/tmp/guicms/
    /home/david/tmp/tmpPython/python/tests/
    /home/david/tmp/tmpPython/python/
    /home/david/tmp/tmpPython/python/gui/tkinter/pytk_diskfree
    --apt jigl
    -a ajaxterm
    -a denyhosts
    -a burn
    -a supybot
    -a pydf
    -a pycmail
    -a foff
    -a cedar-backup2

Then run it as following from where you are in the cli, the script should be are accessible with the tab autocompletion too:

    gonzui_mass_importer

Most time, when i want to import some stuff to gonzui. I add it in the to_import_file. Especially for the apt, cvs, svn imports.

We can at any moment re run us self made script, after we have added a new import path. The stuff that are already imported will be skipped. So the next time you run us script, it will go many faster as the first time we have run it.

# Updating the info

If we modify some stuff in the source code, we need to update the gonzui database with 'gonzui-update'. Each time we the source code is modified, and want to see the changes in gonzui, we need to update the database. Maybe is it interesting to make a cron job to automate the task.

    $ gonzui-update
    0 contents of 0 packages updated in 0.01 sec. (0.00 contents / sec.)

Note: It's just if we add some more source to the stuff.

# Starting the server

Once everything is configured and some stuff is been imported, we can start the server. Not that it was needed to import some stuff before starting the server.

You can still import some stuff, update your source code, update the database while the server is running.

    $ gonzui-server
    http://venus:46984/
    2007-01-10T21:15:32 server started [23790]

# Remove some stuff

If we want to remove some project:

    gonzui remove abuse_reporter

We not need to execute `gonzui-update` after remove some stuff. It's directly take in consideration.

# Additional notes

If we have some weird characters in us path, `gonzui` will crash. Better to avoid weird characters. If you look to your path and see a `?` character in it. Modify the directory of the file!