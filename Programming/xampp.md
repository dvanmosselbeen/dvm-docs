-----
title: Xampp
description: A page dedicated to Xampp webserver for Windows.
created: 30-04-2020 00:00:00
modified: 30-04-2020 00:00:00
keywords: Drupal, CMS, Content Management System, Website, Internet, Web Server
lang: en
-----

# Xampp

## Create a virtual host

Edit the file `apache/conf/extra/httpd-vhosts.conf` and add the following:

    <VirtualHost *:80>
        ##ServerAdmin webmaster@dummy-host2.example.com
        DocumentRoot "D:/xampp/htdocs/cms_tests/drupal-8.8.5"
        ServerName drupal.localhost
        ##ErrorLog "logs/dummy-host2.example.com-error.log"
        ##CustomLog "logs/dummy-host2.example.com-access.log" common
    </VirtualHost>
    
Restart the apache server and now you can visit the website on the following address: http://drupal.localhost/