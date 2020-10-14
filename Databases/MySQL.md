-----
title: MySQL Reference
description: A little MySQL reference.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: database, mysql, website, internet
lang: en
-----

# MySQL Reference

## Introduction

This article give some tips and tricks about MySQL. This article is
ideal for people have little experience with `MySQL` and want to know a
bit more about it.


## Setting up the root password

When we just installed `MySQL`, we need to define the root password!
It\'s the first thing to do! If you not define an good password, someone
could take one for you on you\'re database and control it! So define an
password that are not to easy for others. We can define the password in
different ways, i show two methods.

Open an console and type the follow command :

    mysqladmin -u root password NEW_PASSWD;

Enter now a password you want to define. If the password already exist
use the`-p` switch otherwise you receive an error that the password
already exist:

    mysqladmin -u root -p password NEW_PASSWD

Give now an password you want to define for the root user.

Or you can i do in another way, like this one:

    mysql -u root mysql

That identify you as root user and go in the `mysql` table.

    mysql>SET PASSWORD FOR root@localhost=PASSWORD("new_password_we_want");
    Query OK, 0 rows affected (0.0.0 sec)
    myqsl>SET PASSWORD FOR root@"%"=PASSWORD("new_password_we_want")
    Query OK, 0 rows affected (0.0.0 sec)
    mysql>FLUSH PRIVILEGES;
    Query OK, 0 rows affected (0.0.0 sec)

Not forget to replace the `new_password_we_want` password with one we
want.

## Create a new user with full access rights

This is meant to be a user with same level of user rights as the root user.

    CREATE USER 'dvanmosselbeen'@'localhost' IDENTIFIED BY PASSWORD 'my_secure_password';
    grant all on * . * To 'dvanmosselbeen'@'localhost' with grant option;
    flush privileges;

## Connecting to the MySQL server

Now that you have an account on the `MySQL` server, it\'s a good thing
now to try to connect to it. We need to do it in the command line
interface.

    mysql -h hostname -u USERNAME -p

After fill the command, a password is asked to enter, enter it. The `-h`
define on which host computer we want to access the `MySQL` Server. You
can leave the`-h` option if it\'s on you\'re local computer or you can
use `-h localhost` or`-h 127.0.0.0` or the right computer name where you
want to access it. The `-p`prompt for the password for that user.

Now you are connected to the `MySQL` server. You are not connected to an
database! Actually you see somethings like:

    mysql

Now we need to enter all the commando\'s of `MySQL` there after that
`mysql>`prompt! The most commands you need to enter it in the mysql
shell.

## See which database are available

We can see which existing database there are available with the command:

    SHOW DATABASE;

You get an list of all the database there are available on
you\'re`MySQL` server. Here\'s an example of the output it give:

    +-------------+
    | Database    |
    +-------------+
    | mysql       |
    | test        |
    +-------------+
    2 rows in set (0.00 sec)

The `mysql` database contain all the users informations and define what
he are allowed to do. It\'s important to not mess up that database. So i
recommend you to not play with that table as for long you really know
what you\'re doing.

## Exporting the data

It\'s good to keep an copy of you\'re data. Sometimes you want to keep
the security, keeping an backup before change some things on the
database. You can simple export the content of an database, to import it
on an other computer for example:

    mysqldump -u DBUSER -p DBNAME > dbname.sql

Choose an name what you want for the file `dbname.sql`. The file
`dbname.sql`are created in the current directory you\'re actually are!
So you can also specify an whole path, so that he not store that file in
the current directory.

If you need to import from version 4.1 to 4.0

    mysqldump --compatible=mysql40 -u DBUSER -p DBNAME > dbname.sql

## Importing the data

You can easily import existing data, thinking to data that are stored on
another `MySQL` server that you want to move to you\'re production
server.

    mysql -u DBUSER -p dbname < dbname.sql

If you need to add the data on an remote \'MySQL\' server:

    mysql -u DBUSER -p -h DBSERVER dbname < dbname.sql

## Delete a database

Deleting an database, is an question of an command. Be sure you are
deleting the correct database because there are not asked to confirm the
deletion. If delete, it\'s go one. Or if you have take a backup of it,
you can always restore the database you have just deleted.

    DROP DATABASE database_name;

Replace `database_name` with the database you want to delete.

## Create a database

    CREATE DATABASE database_name;

Replace `database_name` with the database name you want to give to that
database.

## Using a database

Once in the command line interface of the `MySQL` server, you probably
need to choose an database where you would like to work on.

    USE database_name

## Create a table

    CREATE TABLE name_table (
    -> name_column1 column1_type column1_details,
    -> name_column2 column2_type column2_details,
    -> name_column3 column3_type column3_details,
    -> ...
    -> );

An example of an complete table:

    CREATE TABLE Guestbook (
    -> ID INT NOT NULL AUTO_INCRMENT PRIMARY KEY,
    -> GDate DATE NOT NULL,
    -> GName TEXT,
    -> Gemail TEXT,
    -> Gurl TEXT,
    -> GMessage TEXT
    -> );

-   The first line say that we want to create an database called
    `Guestbook`.
-   The second line tell that we want to create the field ID with the
    type of `INT` (integer). This field are not allowed to be are empty
    and it would be automatically auto increments his value. The primary
    key are also set to this field.
-   The third line tell that we want to create the field \'GDate\' with
    the type \'DATE\' and must also not are empty.
-   The fourth line to the seventh line are the same, just the fields
    name differ. We create an field an set it to the type \'TEXT\'.

## Show the tables inside a database

Need an command to see wich table are inside an database? Use this:

    SHOW TABLES;

## Getting the description of a table

To get an description of the fields of an table:

    DESCRIBE table_name;

## Delete a table

To delete an table inside an database:

    DROPTABLE table_name;

## Insert data into the table

Adding data into the table could be done in different ways. Like in this
article we have already create an database `Guestbook` for demonstration
purpose. We continue to use this database. Take it as an test database,
and if needed drop that database when you\'re done reading this article.

Method 1:

    INSERT INTO Guestbook SET
    -> Gdate = "2006-06-10",
    -> Gname = "Guest'er",
    -> Gemail = "
     
     <!--
     var prefix = '&#109;a' + 'i&#108;' + '&#116;o';
     var path = 'hr' + 'ef' + '=';
     var addy44803 = '&#101;m&#97;&#105;l' + '&#64;';
     addy44803 = addy44803 + 's&#101;rv&#101;r' + '&#46;' + 'c&#111;m';
     document.write('<a ' + path + '\'' + prefix + ':' + addy44803 + '\'>');
     document.write(addy44803);
     document.write('<\/a>');
     //-->\n 
     <!--
     document.write('<span style=\'display: none;\'>');
     //-->
     This email address is being protected from spambots. You need JavaScript enabled to view it.
     
     <!--
     document.write('</');
     document.write('span>');
     //-->
     ",
    -> Gurl = "http://some_sit.com",
    -> GMessage = "Hi, i find you're site great! Continue to develop it!",

Method 2:

    INSERT INTO Guestbook
    -> (Gname, Gemail, Gurl, GMessage) VALUES (
    -> "Tester01",
    -> "
     
     <!--
     var prefix = '&#109;a' + 'i&#108;' + '&#116;o';
     var path = 'hr' + 'ef' + '=';
     var addy44623 = 'm&#97;&#105;l' + '&#64;';
     addy44623 = addy44623 + 'm&#97;&#105;l' + '&#46;' + 'c&#111;m';
     document.write('<a ' + path + '\'' + prefix + ':' + addy44623 + '\'>');
     document.write(addy44623);
     document.write('<\/a>');
     //-->\n 
     <!--
     document.write('<span style=\'display: none;\'>');
     //-->
     This email address is being protected from spambots. You need JavaScript enabled to view it.
     
     <!--
     document.write('</');
     document.write('span>');
     //-->
     ",
    -> "http://some_url.com";
    -> "Some message to add into the guestbook table...";
    -> );

Remember that we need to enter the VALUES in the same order like the
fields (on line 2) are entered.

## View the data of the table

    SELECT * FROM Guestbook;

The output of the previous command looks not nice. It;s looks that there
are some troubles to display these data inside of that table.

Try to get the content of that table without that long field that
disorganise a bit that layout.

    SELECT ID, GName, Gemail, Gurl FROM Guestbook;

The output looks now a bit better, but there are an missing field. I
have not select all the fields, only the fields i want to see.

But we can ask to only show the x first characters of an column:

    SELECT ID, GDate, GName, Gemail, Gurl LEFT(GMessage,25)

## Count the numbers of rows in a table

    SELECT COUNT(*) FROM Guestbook;

## Updating information in a table

    UPDATE Guestbook SET GDate="2006-06-09" WHERE ID=1;

We can also change all the fields matching somethings. In this example
we change all the fields matching the word `good`.

    UPDATE Guestbook SET GDate="2006-06-09"
    -> WHERE GMessage LIKE "%good%";

## Deleting fields in a table or the table in question

You need to are very careful when you would like to delete some things.
Because if you forget to enter somethings you delete the whole table!

The next command delete all the fields where the word \'good\' are find.

    DELETE FROM Guestbook WHERE GMessage LIKE '%good%'

If you not include the `WHERE` part, you delete the table!

    DELETE FROM Guestbook;
