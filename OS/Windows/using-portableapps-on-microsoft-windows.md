---
description: 'This article talk about Portableapps which are portable apps.'
generator: 'Joomla! - Open Source Content Management'
keywords: portableapps portable apps microsoft windows
lang: 'en-gb'
rights: Copyrights by David Van Mosselbeen
robots: 'noindex, nofollow'
title: Using Portableapps on Microsoft Windows
created: 24-09-2008
---

Introduction
============

...

Installing portableapps
=======================

I downloaded `PortableApps.com_Suite_Setup_1.1.exe` and i selected as
install dir `D:\papps`.

Installing configuring xampp
============================

I downloaded `xampp-win32-1.6.7-installer.exe` and
`XAMPP_Launcher_1.3.paf.exe`

Install dir `D:\papps\PortableApps\xampp`.

To install the launcher. From portable apps click on Options \>
`Install a new app`.

Once Xampp up and running, the first nee Now there are some things left
to do:

-   Setup the mysql root password
-   Rename the file `htdocs/index.php` to `htdocs/index.php`

Python on xampp
---------------

Download and install `mod_python-3.3.1.win32-py2.5-Apache2.2.exe`
from<http://apache.belnet.be/httpd/modpython/win/3.3.1/>. Note that my
python version is 2.5 and apache 2.2.9. Download the correct exe
depending of the version you use.

It asked the apache install dir, i filled
in`D:\papps\PortableApps\xampp\apache`.

Verify that the
file`D:\papps\PortableApps\xampp\apache\modules\mod_python\mod_python.so`
file been exist.

Then adjust the apache\'s \`httpd.conf\`\` and add the following:

    LoadModule python_module modules/mod_python.so

Below then bellow the `</Directory>` declarative add:

    <Directory "D:\papps\PortableApps\xampp\htdocs\python">
            AddHandler mod_python .py
            PythonHandler mptest
            PythonDebug On
    </Directory>

Now create the folder `D:\papps\PortableApps\xampp\htdocs\python\` with
the file `mptest.py`.

    from mod_python import apache

    def handler(req):
    req.content_type = 'text/plain'
    req.write("Hello World!")
    return apache.OK

Restart now apache and then point your browser
to<http://localhost/python/mptest.py>.

Source from: <http://blog.chomperstomp.com/?p=150>

xampp resources
---------------

-   <http://sourceforge.net/projects/xamppaddon>
