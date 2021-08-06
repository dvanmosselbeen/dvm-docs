# MySQL Reference

## Introduction

Some quick notes about `MySQL`.

**Markup language has killed some syntax, tried to fix it as best I could. Could be some syntaxes here are still messed up.**

## Setting up the root password

When we just installed `MySQL`, we need to define the `root` password! It's the first thing to do! If you not define a good password, someone could take one for you on your database and control it! So define a password that is not too easy to brute-force by others. We can define the password in different ways, I show two methods.

Open a console and type the follow command :

```commandline
mysqladmin -u root password NEW_PASSWD;
```

Enter now a password you want to define. If the password already exist use the`-p` switch otherwise you receive an error that the password already exist:

```commandline
mysqladmin -u root -p password NEW_PASSWD
```

Give now a password you want to define for the root user.

Or you can I do in another way, like this one:

```commandline
mysql -u root mysql
```

That identify you as root user and now go in the `mysql` table.

```sql
mysql>SET PASSWORD FOR root@localhost=PASSWORD("new_password_");
Query OK, 0 rows affected (0.0.0 sec)
myqsl>SET PASSWORD FOR root@"%"=PASSWORD("new_password")
Query OK, 0 rows affected (0.0.0 sec)
mysql>FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.0.0 sec)
```

**Replace new_password with the password you want to define.**

## Create a new user with full access rights

This is meant to be a user with same level of user rights as the root user.

```sql
CREATE USER 'foo'@'localhost' IDENTIFIED BY PASSWORD 'my_secure_password';
grant all on * . * To 'foo'@'localhost' with grant option;
flush privileges;
```
**Replace username `foo`.**

## Connecting to the MySQL server

Now that you have an account on the `MySQL` server, it's a good thing now to try to connect to it. We need to do it in the command line interface.

```commandline
mysql -h <HOST> -u <USERNAME> -p
```

After running the command, a password is asked to enter, enter it. The `-h` define on which host computer we want to access the `MySQL` Server. You can leave the`-h` option if it's on your local computer, or you can use `-h localhost` or`-h 127.0.0.0` or the right computer name where you want to access it. The `-p`prompt for the password for that user.

Now you are connected to the `MySQL` server. You are not connected to a database! Actually you see something like:

    mysql

Now we need to enter all the commando's of `MySQL` there after that `mysql>`prompt! The most commands you need to enter it in the mysql shell.

## See which database are available

We can see which existing database there are available with the command:

```sql
SHOW DATABASE;
```

You get a list of all the database there are available on you're`MySQL` server. Here's an example of the output it gives:

```sql
+-------------+
| Database    |
+-------------+
| mysql       |
| test        |
+-------------+
2 rows in set (0.00 sec)
```

The `mysql` database contain all the users information and define what users are allowed to do. It's important to not mess up that database. So I recommend you to not play with that table as for long you really know what you're doing.

## Exporting the data

It's good to keep a copy of your data. Sometimes you want to keep the security, keeping a backup before change some things on the database. You can simply export the content of a database, to import it on another computer for example:

```sql
mysqldump -u DBUSER -p DBNAME > dbname.sql
```

Choose a name what you want for the file `dbname.sql`. The file
`dbname.sql`are created in the current directory you are actually in! So you can also specify a whole path, so that he not store that file in
the current directory.

If you need to import from version 4.1 to 4.0

```sql
mysqldump --compatible=mysql40 -u DBUSER -p DBNAME > dbname.sql
```

## Importing the data

You can easily import existing data, thinking to data that are stored on another `MySQL` server that you want to move to your production server.

```sql
mysql -u DBUSER -p dbname < dbname.sql
```

If you need to add the data on a remote `MySQL` server:

```sql
mysql -u DBUSER -p -h DBSERVER dbname < dbname.sql
```

## Delete a database

Deleting a database, is a question of a command. Be sure you are deleting the correct database because you will be not asked for confirmation. If deleted, it's go one. Or if you have taken a backup of it, you can always restore the database you have just deleted.

```sql
DROP DATABASE database_name;
```

Replace `database_name` with the database you want to delete.

## Create a database

```sql
CREATE DATABASE database_name;
```

## Using a database

Once in the command line interface of the `MySQL` server, you probably need to choose a database where you would like to work on.

```sql
USE database_name;
```

## Create a table

Syntax:

```sql
CREATE TABLE name_table (
-> name_column1 column1_type column1_details,
-> name_column2 column2_type column2_details,
-> name_column3 column3_type column3_details,
-> ...
-> );
```

A complete example:

```sql
CREATE TABLE Guestbook (
-> ID INT NOT NULL AUTO_INCRMENT PRIMARY KEY,
-> GDate DATE NOT NULL,
-> GName TEXT,
-> Gemail TEXT,
-> Gurl TEXT,
-> GMessage TEXT
-> );
```

* The first line say that we want to create a database called `Guestbook`.
* The second line tell that we want to create the field ID with the type of `INT` (integer). This field is not allowed to be empty, and it would be automatically auto increments his value. The primary key is also set to this field.
* The third line tell that we want to create the field `GDate` with the type `DATE` and must also not are empty.
* The fourth line to the seventh line are all the same type, just the fields name differ. We create a field a set it to the type `TEXT`.

## Show the tables inside a database

```sql
SHOW TABLES;
```

## Getting the description of a table

```sql
DESCRIBE table_name;
```

## Delete a table

```sql
DROPTABLE table_name;
```

## Insert data into the table

Adding data into the table could be done in different ways. Like in these examples here we have already created a database `Guestbook` for demonstration purpose. We continue to use this database.

### Method 1

```sql
INSERT INTO Guestbook SET
Gdate = "2006-06-10",
Gname = "Guest'er",
Gemail = "some@email.com"
Gurl = "http://some_sit.com",
GMessage = "Hi, i find you're site great! Continue to develop it!",
```

Method 2:

```sql
INSERT INTO Guestbook
(Gname, Gemail, Gurl, GMessage) VALUES (
"Tester01",
"some@email.com",
"http://some_url.com",
"Some message to add into the guestbook table...",
);
```

Remember that we need to enter the VALUES in the same order like the fields (on line 2) are entered.

## View the data of the table

```sql
SELECT * FROM Guestbook;
```

The output of the previous command looks not nice. It looks that there are some troubles to display these data inside of that table.

Try to get the content of that table without that long field that disorganise a bit that layout.

```sql
SELECT ID, GName, Gemail, Gurl FROM Guestbook;
```

The output looks now a bit better, but there are missing field. I have not selected all the fields, only the fields I want to see.

But we can ask to only show the x first characters of an column:

```sql
SELECT ID, GDate, GName, Gemail, Gurl LEFT(GMessage,25)
```

## Count the numbers of rows in a table

```sql
SELECT COUNT(*) FROM Guestbook;
```

## Updating information in a table

```sql
UPDATE Guestbook SET GDate="2006-06-09" WHERE ID=1;
```

We can also change all the fields matching something. In this example we change all the fields matching the word `good`.

```sql
UPDATE Guestbook SET GDate="2006-06-09"
-> WHERE GMessage LIKE "%good%";
```

## Deleting fields in a table or the table in question

You need to are very careful when you would like to delete some things. Because if you forget to enter something you delete the whole table!

The next command delete all the fields where the word \'good\' are find.

```sql
DELETE FROM Guestbook WHERE GMessage LIKE '%good%'
```

If you not include the `WHERE` part, you delete the table!

```sql
DELETE FROM Guestbook;
```
