# Apache2

## Table of Contents

- [Installing and configuring Apache2](#installing-and-configuring-apache2)
- [Configuring Apache](#configuring-apache)
- [Installing and configuring PHP](#installing-and-configuring-php)
  - [Enabling userdir](#enabling-userdir) 
- [Tools](#tools)
- [TODO](#todo)

`Apache` is probably the most used web server. It's rock solid, well documented and has a great user base and support. 

## Installing and configuring Apache2

### Installing Apache2

Installing `apache2`:

    apt-get update
    apt-get install apache2

### Configuring Apache2

By default, the `apache 2 server` is only running on the non encrypted `http` protocol. So we should absolutely enable `https`.

## Installing and configuring PHP

We need to install the `mod-php` for apache 2.

    apt-get install php libapache2-mod-php

Test if `PHP` is working, for this we will create the file `/var/www/html/phpinfo.php` with the following content:

````commandline
<?php phpinfo(); ?>
````

Point your browser to,<http://ip-of-the-server/phpinfo.php> and it should give you a bunch of `PHP` related information.

### Enabling userdir

Enabling `userdir` will allow all users to have their own website in `~/public_html`:

    /usr/sbin/a2enmod userdir

By default, `PHP` is not enabled for `userdir`. If you want to allow `userdir` to allow using `PHP`, change the following:

    vim /etc/apache2/mods-enabled/php7.3.conf

And change the line:

    php_admin_flag engine Off

To: 

    php_admin_flag engine On

Restart the `apache2` server:    
    
    systemctl restart apache2

## Tools

| Application | Description                                                                                                                                                                                  |
|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| apachetop | Realtime Apache monitoring tool                                                                                                                                                              |
| awffull | web server log analysis program forked from `Webalizer`. It adds a number of new features and improvements, such as extended frontpage history, resizable graphs, and a few more pie charts. |
| awstats | powerful and featureful web server log analyzer                                                                                                                                              |
| webalizer | web server log analysis program. (probably the oldes program, take a look to awffull or awstats.                                                                                             |

## TODO 

- Configure to make use of `https`.