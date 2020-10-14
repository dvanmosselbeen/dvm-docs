-----
title: Drupal
description: A page dedicated to Drupal Content Management System.
created: 30-04-2020 00:00:00
modified: 30-04-2020 00:00:00
keywords: Drupal, CMS, Content Management System, Website, Internet
lang: en
-----

# Drupal

## Update Drupal

In this example we will update Drupal `8.6.15` to version `8.9.6`.

Go to https://www.drupal.org/project/drupal and download `Drupal core 8.9.6`.

I have downloaded the file `drupal-8.9.6.zip` in `Downloads`. Then i extract that `drupal-8.9.6.zip` with `7-zip`.

Then copy everything except the directory `sites` to the destination and overwrite existing files.

Then with your webbrowser execute the `update.php` file on your site (somethings like http://localhost/update.php) so that `Drupal database update` interface to update the database with the new changes.

