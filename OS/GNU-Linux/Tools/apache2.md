# Apache2

`Apache` is probably the most used web server. It's rock solid, well documented and has a great user base and support. 

## Installing Apache2

Installing `apache2`:

    apt-get update
    apt-get install apache2
    
Installing `php`:

    apt-get install php libapache2-mod-php

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
