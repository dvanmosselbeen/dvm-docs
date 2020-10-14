-----
title: Wordpress notes
description: This page is dedicated to wordpress notes.
created: 13-09-2020 13:10:00
modified: 13-09-2020 13:10:00
keywords: wordpress, website, web dev, programming, server
lang: en
-----

# Wordpress Notes

## Installing Wordpress

Installing wordpress is very easy. The procedure to install wordpress depend on where the website will be stored.

### Installing Wordpress 5.5.1 on XAMPP

We used Wordpress 5.5.1 to install it on a local XAMPP server on a Microsoft Windows 10 computer. 
For this it's a matter to download the wordpress 5.5.1 source, extract the zip file and place it somewhere accessible by the XAMPP server. Then create some new database and user on MySQL. For this you can use the PHPMyAdmin web interface provided by XAMPP. Once the new database and user created in MySQL we can browse to the location of the wordpress 5.5.1 directory thought the web browser. The wordpress web interface installer should have started and you should follow the instructions on screen. It's not complicated and the web interface is very user friendly.

## Interesting themes

*

## Interesting plugins

* FooGallery - Nice and beautiful gallery, this is the one i currently use.

## Increase the default upload limit

Source: https://www.cloudways.com/blog/increase-media-file-maximum-upload-size-in-wordpress/

By default, 8MB is the limit in file size we can upload on our wordpress site. To adjust this we need to modify the `.htaccess` file with something similar:

    php_value upload_max_filesize 64M
    php_value post_max_size 128M
    php_value memory_limit 256M
    php_value max_execution_time 300
    php_value max_input_time 300


## Resources

* www.wordpress.org