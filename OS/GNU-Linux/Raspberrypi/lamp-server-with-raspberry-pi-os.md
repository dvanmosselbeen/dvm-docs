# LAMP server with Raspberry PI OS

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

I have had some isssues with PHPMyAdmin, facing an annoying bug which gave me some errors on the PHPMyAdmin web interface:

    Warning in ./libraries/sql.lib.php#613 count(): Parameter must be an array or an object that implements Countable

Found some information and some fixe to it. See: https://stackoverflow.com/questions/48001569/phpmyadmin-count-parameter-must-be-an-array-or-an-object-that-implements-co

So, to fix this issue partially:

    sudo sed -i "s/|\s*\((count(\$analyzed_sql_results\['select_expr'\]\)/| (\1)/g" /usr/share/phpmyadmin/libraries/sql.lib.php

There are still some errors here and there on the PHPMyAdmin webinterface. If i understood it correctly, it's an know bug. Could be fixed by manually upgrade PHPMyAdmin or downgrade the PHP version.

## Extra tools

    awffull - web server log analysis program
    awstats - powerful and featureful web server log analyzer
    webalizer - web server log analysis program
