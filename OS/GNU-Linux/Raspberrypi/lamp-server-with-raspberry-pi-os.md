-----
title: LAMP server with Raspberry PI OS
description: This article is dedicated to the Raspberry PI LAMP server setup.
created: 14-10-2020 00:00:00
modified: 14-10-2020 00:00:00
keywords: debian, gnu, linux, operating, system, admin, raspberry, pi, linux, apache, apache2, mysql, mariadb,
lang: en
-----

In this document, i describe how to install and configure a LAMP server on a Raspberry Pi Model 4. This should work with other models too.

Note that it's best to not make use of an OS installed on the SD card, as you know, SD cards have a very limited life time.

## Installing the web server

For this we will use apache2 and php.

    sudo apt-get install apache2 php
    
Enable `~/public_html` for users:
    
    sudo a2enmod userdir

Restart now the apache2 service

    sudo service apache2 restart

## Installing the database

    sudo apt-get install mariadb-server php-mysql

### Create a new database user

We will create a new user with all user rights. This to avoid to use the root user account already made.

    sudo mysql

Then in the mysql console:

    CREATE USER 'my_new_user'@'localhost' IDENTIFIED BY 'my_password';

Replace `my_new_user` by the desired username. and `my_password` with the one you choiced.

Now define the priviledges:

    GRANT ALL PRIVILEGES ON *.* TO 'my_new_user'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;

## Installing phpmyadmin

PhpMyAdmin is a web interface to manage the mysql database. This is a must have tool.

    sudo apt-get install phpmyadmin

You should now be able to use the phpmyadmin web interface and log in with you new user: http://192.168.0.20/phpmyadmin/

## Extra tools

    awffull - web server log analysis program
    awstats - powerful and featureful web server log analyzer
    webalizer - web server log analysis program