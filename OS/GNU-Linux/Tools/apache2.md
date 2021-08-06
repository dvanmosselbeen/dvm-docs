# Apache2

Apache is probably the most used web server. It's rock solid, well documented and has a great user base and support. 

## Installing Apache2

Installing `apache2`:

    apt-get update
    apt-get install apache2
    
Installing `php`:

    apt-get install php libapache2-mod-php

Enabling `userdir` (This will allow all users to have their own website in `~/public_html`):

    /usr/sbin/a2enmod userdir

By default now, PHP isn't enabled for `userdir`. If you want to allow `userdir` to allow to use PHP, change the followong: 

    vim /etc/apache2/mods-enabled/php7.3.conf

And change the line:

    php_admin_flag engine Off

To: 

    php_admin_flag engine On

Restart the `apache2` server:    
    
    systemctl restart apache2

## Tools

| Application | Description |
|---|---|
| apachetop | Realtime Apache monitoring tool |
| awffull | web server log analysis program |
| awstats | powerful and featureful web server log analyzer |
| webalizer | web server log analysis program |
