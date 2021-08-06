# SQLite

## Introduction

If we don't need a sophisticated client/server database system, no multiple clients access, `sqlite` is the thing. It's easy to use, easy to setup (zero configuration), it's not too complicated to use.

Ideal if you want to integrate a database system in your own application. There are some programming language that have some libraries to make use of sqlite.

SQLite is case-insensitive. We can use lower or capital letters. To make it more clear here, we use capitals for the commands.

## Installing SQLite

`SQLite` is available for different platforms. There is `sqlite` and `sqlite3`. Databases created with the later one will be not backwards compatible with the older `sqlite` version.

### Installing SQLite on Debian GNU/Linux (and others)

We first always update the list of packages and then upgrade all the packages before installing new software. We also install the additional documentation that are available.

```commandline
apt-get update
apt-get install sqlite3 sqlite3-doc
```

*For other distributions, refer to your package manager. Take maybe first a look to the packages related to sqlite.*

### Installing SQLite from source

If `SQLite` is not available as a package, you may always compile it from source. Most likely like:

```commandline
# As normal user
./configure --prefix=/usr/local/
make

# As root user
make install
```

### Installing SQLite on Microsoft Windows

There are 2 different bundles, for X86 or 64 bit. Here we use the X86 as the download bundles provide one package with extra tools.

Download the binary file and place it somewhere. Most likely in the
`C:\Program Files (x86)\sqlite3\` and add that path to the path variable.

To be useful, it's recommended to add this path to the system PATH variable, so that you can access SQLite from anywhere.

For this, right click on `This Computer`, select properties and then `Advanced system settings`, then click on `Environment Variables...`.

Then in the upper (only for the current user), or the lower part (System variables, for all users), select `Path` and then click edit. Then press `New` and fill in the path (`C:\Program Files (x86)\sqlite3\`). 

*It's maybe more practical to use the all user system as described above.* 

You should maybe restart the system so that the PATH variable is read again, or just reopen all the concerned apps (Windows explorer, shell etc).

## Read the documentation

Like we have installed the `sqlite3-doc` packages on my debian box. It's best that we first read the doc. The docs are located in`/usr/share/doc/sqlite3-doc/index.html`. You can find this out with `dpkg -L sqlite3-doc`.

It's also good to look on the website of `sqlite`. Probably you get there up to date news about the product. Also are there are bit more information than provided in the additional `sqlite3-doc` package.

Get help:

```sql
sqlite> .help

sqlite> .explain
sqlite> EXPLAIN INSERT INTO contacts VALUES('Hello, World!',99);

sqlite> EXPLAIN SELECT * FROM contacts;
```

## Datatypes

- `NULL` - The value is a NULL value.
- `INTEGER` - The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes
- `SMALLINT` -
- `VARCHAR` - example `varchar(10)`. depending on the magnitude of the value.
- `REAL` - The value is a floating point value, stored as an 8-byte IEEE floating point number.
- `TEXT` - The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16-LE).
- `BLOB` - The value is a blob of data, stored exactly as it was input.

## SQLite in the cli

You can use `sqlite` in your shell or maybe want you access it in an simple shell script. Also useful to export or import some data in the command line interface.

As first, see how we can get info in the cli:

```commandline
$ sqlite3 --help
```

That output:

```
Usage: sqlite3 [OPTIONS] FILENAME [SQL]
FILENAME is the name of an SQLite database. A new database is created
if the file does not previously exist.
OPTIONS include:
   -init filename       read/process named file
   -echo                print commands before execution
   -[no]header          turn headers on or off
   -column              set output mode to 'column'
   -html                set output mode to HTML
   -line                set output mode to 'line'
   -list                set output mode to 'list'
   -separator 'x'       set output field separator (|)
   -nullvalue 'text'    set text string for NULL values
   -version             show SQLite version
```

Some examples:

```commandline
$ sqlite3 test.db ".tables"
contacts  schema    test      test2

$ sqlite3 -header -column test.db "SELECT * from test2"
id          forname     name          
----------  ----------  --------------
1           foo         bar
2           baz         buu
```

## Create and execute a query file

Create a file `query.sql` and put the following:

    SELECT * FROM test;

We now us 'external' query:

    sqlite3 -init query.sql test.db .exit
    Loading resources from query.sql
    1|foo
    2|bar
    3|baz
    4|xuu
    5|buu

Fetch a particular row:

    $ sqlite3 test.sqlite3 "SELECT names FROM groups"

## Creating a database

If we not specify a database name, the database will be made in-memory, some time it is useful for test routines. But keep in mind that the data will be lost once you have quit `sqlite`. If you specify a database name, and the file not yet exist, these will be made when you create the first table in the database.

    $ sqlite3 test.db

## In the sqlite interactive interpreter

## Creating a table

```sql
sqlite> CREATE TABLE contacts (
    id integer primary key,
    name text,
    age integer
    );
```

With integer primary key, we make an auto increment way. Useful so that we later not specify an id, it automatically set a number higher as the highest id.

## Insert data in the table

Here's an example:

```commandline
sqlite> INSERT INTO contacts VALUES (NULL, 'foo', 12);
```

We now use another style:

```commandline
sqlite> INSERT INTO contacts VALUES (
    NULL, 
    'bar', 
    13
    );

sqlite> INSERT INTO contacts VALUES (
    NULL, 
    'baz', 
    20);
```

When inserting, we can also define the order of the data we add:

```sql
sqlite> INSERT INTO contacts (age,id,name) VALUES (14, NULL, 'foo';
```

## Select data from a table

We get all the columns:

```sql
sqlite> SELECT * FROM contacts;
```

If you not need all the columns, it is always better (faster) to only fetch what you need to fetch.

But we can also take the fields we want:

```sql
sqlite> SELECT first_name FROM contacts;

SELECT last_name FROM contacts WHERE first_name=="David";
```

### Order the result

```sql
SELECT last_name from contacts ORDER BY last_name;
```

### Group by

```sql
SELECT last_name from contacts GROUP BY last_name;
```

### Select distinct

Don't fetch duplicated records.

```sql
SELECT DISTINCT last\_name from contacts;
```

### Rename temporally a field

```sql
SELECT first_name AS fname FROM contacts;
```

### Relations

```sql
sqlite3 contacts.sqlite3 "SELECT * FROM contacts JOIN contact_address WHERE \
    contacts.id == contact_address.contact_id"

sqlite3 contacts.sqlite3 "SELECT contacts.first_name, contact_address.contact_id, \
address.street from contacts contacts, contact_address, address WHERE \
contacts.id==contact_address.contact_id AND \
contact_address.contact_id=contact_address.address_id;"
```

Get all the different addresses of a contact:

```sql
SELECT address.street from contacts contacts, contact_address, address WHERE 
contacts.first_name=="David" AND contact_address.contact_id=contact_address.address_id;
```

## Delete data from a table

```sql
sqlite> DELETE FROM contacts WHERE age>15;
```

Another exemple:

```sql
sqlite> DELETE FROM contacts WHERE name="bar";
```

Delete all records of a table:

```sql
sqlite> DELETE FROM contacts;
```

## Update data from a table

```sql
sqlite> UPDATE contacts SET age = '14' WHERE name == 'foo';
```

## Add a new column to an existing table

Say you have a table with as sql and want to add a nem column:

```sql
CREATE TABLE actors (
    id INTEGER PRIMARY KEY,
    name VARCHAR (50) NOT NULL UNIQUE
);
```

As first create a manual backup of the database file, as this is a simple file, copy this somewhere on a secure location, go into the sqlite interpreter:

```commandline
    sqlite3 mydatabase.db
```

Begin:

```sql
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE actors_backup(
        id INTEGER PRIMARY KEY,
        name VARCHAR (50) NOT NULL UNIQUE
        );

INSERT INTO actors_backup SELECT id, name FROM actors;
DROP TABLE actors;
CREATE TABLE actors(
        id INTEGER PRIMARY KEY,
        name VARCHAR (50) NOT NULL UNIQUE,
        role VARCHAR (50)
        );

INSERT INTO actors (id, name) SELECT id, name FROM actors_backup;
DROP TABLE actors_backup;
COMMIT;
```

## Let's get a better output

The data will be split into columns.

```sql
sqlite> .mode col
sqlite> SELECT * FROM contacts;
```

Show the header (columns names):

```sql
sqlite> .header on
sqlite> SELECT * FROM contacts;
```

NOTE: `.mode col` and `.header on` are to improve the visibility. Once it's activated, it still leaves so long you not exit `sqlite`.

## Create an index and a view

```sql
sqlite> CREATE INDEX contacts_idx ON test (value);
sqlite> CREATE VIEW schema AS SELECT * FROM sqlite_master;
```

## See the new table that are created

```sql
sqlite> .tables
sqlite> schema  contacts
```

## See the content of the schema table

```sql
sqlite> select * from schema;
```

This will output some interesting stuff:

```
type       name       tbl_name   rootpage   sql
---------  ---------  ---------  --------- --------------------------------------
table       test        test        2      CREATE TABLE test (id integer primary \
                                                   key, value text)
index       test_idx    test        3      CREATE INDEX test_idx ON test (value)
view        schema      schema      0      CREATE VIEW schema AS SELECT \
                                                   * from sqlite_master
```

To see the index:

```sql
    sqlite> .indice contacts
    test_idx
```

Term The SQL definition or data definition language (DDL) for a table or view can be obtained using `.shema [table name]`. If no table name is provided, the SQL definition of all database objects (tables,indexes,views and indexes) are returned

To get the DDL (Data Definition Language) use the `.schema`, if no table are specified all the tables are showed:

```sql
sqlite> .schema contacts
sqlite> CREATE TABLE contacts (id integer primary key, value text);
sqlite> CREATE INDEX contacts_idx ON test (value);

sqlite> .schema
sqlite> CREATE TABLE test (id integer primary key, value text);
sqlite> CREATE VIEW schema AS SELECT * from sqlite_master;
sqlite> CREATE INDEX test_idx ON test (value);

sqlite> select * from sqlite_master;

explain select * from test;
addr        opcode      p1          p2          p3        
----------  ----------  ----------  ----------  ----------
0           Goto        0           11                    
1           Integer     0           0                     
2           OpenRead    0           2                     
3           SetNumColu  0           2                     
4           Rewind      0           9                     
5           Rowid       0           0                     
6           Column      0           1                     
7           Callback    2           0                     
8           Next        0           5                     
9           Close       0           0                     
10          Halt        0           0                     
11          Transactio  0           0                     
12          VerifyCook  0           3                     
13          Goto        0           1                     
14          Noop        0           0
```

## Exporting (backup) data of a database

To export stuff, we use the `.dump`, default the output is displayed on screen, so we need to define to export to an file. The `.dumpt` is the most portable way to export data. So usually we do:

```sql
sqlite> .output exported_data.sql
sqlite> .dump
sqlite> .output stout
```

On the last line we have change the ouput to stout, so that it again look like the default option.

We can also do it in the cli way:

```commandline
$ sqlite3 contacts.db .dump > contacts.sql
```

You can easy export a `sqlite` database to `sqlite3`:

```commandline
$ sqlite contacts.sqlite ".dump" | sqlite3 contacts.sqlite3
```

## Importing data into a database

```sql
    sqlite> .read exported_data.sql
```

Or in the cli. But we assume the that the is no data in the `test3.db`,  otherwise us get some errors if some data we want to import already exist:

```commandline
$ sqlite3 contacts2.db < contacts.sql
```

When developing a database layout, it will be good to create a file that contains all the tables and eventually another file that contains some default data.

## Creating SQL files

Create some file `contacts_tables.sql` and add the following:

```sql
    CREATE TABLE contacts (
        id integer primary key,
        name text,
        age integer
    );
```

Create another file called `contacts_data.sql` and add the following:

```sql
    INSERT INTO contacts VALUES (NULL, 'foo', 12);
    INSERT INTO contacts VALUES (NULL, 'bar', 13);
    INSERT INTO contacts VALUES (NULL, 'baz', 14);
    INSERT INTO contacts VALUES (NULL, 'xuu', 15);
    INSERT INTO contacts VALUES (NULL, 'buu', 16);
```

Then import it like note in the `importing` chapter.

## Drop

```sql
sqlite> drop table contacts;
```

## Like

```sql
sqlite> select * from contacts where value like '%oo%';
```

## Date and time commands

```sql
    sqlite> select datetime('now','localtime','+1.5 hours','-10 minutes');
    2008-01-23 02:36:58

where 0 = Sunday, 1 = Monday, 2 = Tuesday \... 6 = Saturday

    sqlite> select datetime('now','localtime','+3.5 seconds','weekday 1');
    2008-01-28 01:17:45

    NNN days
    NNN hours
    NNN minutes
    NNN.NNNN seconds
    NNN months
    NNN years
    start of month
    start of year
    start of week
    start of day
    weekday N
    unixepoch
    localtime
    utc
```

There is also the `strftime` function:

     **    strftime( FORMAT, TIMESTRING, MOD, MOD, ...)
     **
     ** Return a string described by FORMAT.  Conversions as follows:
     **
     **   %d  day of month
     **   %f  ** fractional seconds  SS.SSS
     **   %H  hour 00-24
     **   %j  day of year 000-366
     **   %J  ** Julian day number
     **   %m  month 01-12
     **   %M  minute 00-59
     **   %s  seconds since 1970-01-01
     **   %S  seconds 00-59
     **   %w  day of week 0-6  sunday==0
     **   %W  week of year 00-53
     **   %Y  year 0000-9999

Here's an example:

```sql
    sqlite> select strftime("%d/%m/%Y %H:%M:%S %s %w %W",'now','localtime');
    23/01/2008 01:22:30 1201051351 3 03
```

## SQLite and Python

There are some `Python` modules to access the content of a `sqlite` database. So that you easily can program an application that do some  things with the`sqlite` database. Take a look on this website http://www.devshed.com/c/a/Python/Using-SQLite-in-Python/2/.

## Other commands to see for

-   `select * from sqlite_master;`
-   `cat ~/.sqlite_history`
-   `$ sqlite3 test.db ".dump"|sed -e s/t1/t2/|sqlite3 test2.db`
-   Join. Here\'s an example:

The following will be interesting to run some saved queries:

```sql
sqlite> .read some.sql
```

## Other useful commands

Download `sqlite_analyzer` from `sqlite` website.

Extract the stuff:

Put it in your `/usr/local/bin` dir and `chmod a+x sqlite3_analyzer-3.3.8.bin`it so that everyone can execute it.

*I have renamed `sqlite3\_analyzer-3.3.8.bin` to `sqlite3\_analyzer`.*

The usage is really easy and this tool is really interesting too. I not understand that it is not yet packaged for `Debian`. Maybe is there another tool for `sqlite`, but i dunno. Maybe could it be useful to package this tool for `Debian`.

```commandline
    $ sqlite3_analyzer test.db
```

I not past the output like it's really big. But try it on the test database us have made. Also read the latest part of the report, it give you the `SQL`syntax to produce the same stats.

## Detect the SQLite version of a database

On a nix box you can easy use the following command:

    $ file test.sqlite

That output:

    test.sqlite: SQLite 2.x database

Try another version:

    $ file test.sqlite3

That output:

    test.sqlite3: SQLite 3.x database

## Vacum

    sqlite test.db VACUM
    $ cp test.db test.backup

## SQLite Tools

- [Sqlite3 analyzer](http://www.sqlite.org/)
- [Sqliteman](http://sqliteman.com/)
- [SQL Database Browser](http://sqlitebrowser.sourceforge.net/)
- [SQLite Controle Center](http://sourceforge.net/projects/sqlitecc/)
- [SQLiteManager](http://www.sqlitemanager.org/)
- See also [this website](http://www.sqlite.org/cvstrac/wiki?p=SqliteTools).


## Resources

- <http://sqlite.org/lang.html>
- <http://www.sqlite.org/cvstrac/wiki>
- [sqlite on wikipedia](http://en.wikipedia.org/wiki/SQLite)
- <http://souptonuts.sourceforge.net/readme_sqlite_tutorial.html>
- <http://www.shokhirev.com/nikolai/abc/sql/sql.html>
- <http://www.linuxdevcenter.com/pub/ct/19>
