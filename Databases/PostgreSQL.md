---
title: PostgreSQL Reference
description: A little PostgreSQL reference.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00 
keywords: database, mysql, website, internet
lang: en
---

PostgreSQL
==========

Introduction
============

You can get many informations on the website of postgresql. Mostly all
informations here are probably on the website of postgresq, so this
little article may be really not complete at all. But i hope this give
you a little introduction or help you where you have previously failed.
As usual, these notes are based on some experimentations with postgresql
on a Debian box.

Used terms
==========

- `cluster`: A collection of databases managed by a single PostgreSQL
    server instance constitutes a database cluster.

Installing configure postgresql and tools
=========================================

Installing postgresql:

    aptitude install postgresql-8.3 postgresql-doc-8.3

*On debian Etch you may need to install postgresql-7.4 if you want to
make use of phppgadmin.*

The database is stored in /var/lib/postgresql/8.3/main
or/var/lib/postgresql/7.4/main depending of the version you install.

You should now take a look to the
/etc/postgresql/8.3/main/postgresql.confconfig file. Especially the port
it will use. Note that if you already had a version of postgresql
installed when you installed the new version of postgresql, you may need
to tweak the port of both postgresql server. Default it will be 5432 and
an additional will have 5433.

If you want to be able to login from remote to the postgresql server
withpgadmin3, you may need to tweak the listen\_addresses variable. If
only one network card is present, you may safely set this variable to
listen\_addresses = \'\*\'.

If the config has changed, restart the postgresql server with:

     /etc/init.d/postgresql-8.3 restart

*Note that if you changed the port number, you should first stop the
server and then start it again. Restarting will keep the old port
number. Take a look with \'netstat -plunt\' if you get some troubles.*

Then i got the follow message when trying to connect with pgadmin3 from
a remote computer:

    Access to database denied
    The server doesn't grant access to the database: the server reports
    FATAL: no pg_hba.conf entry for host "192.168.0.9", user "dvanmosselbeen",
    database "postgres", SSL off
    To access a database on a PostgreSQL server, you first have to grant
    primary access to the server for your client (Host Based Authentication).
    PostgreSQL will check the pg_hba.conf file if a pattern that matches your
    client address / username / database is present and enabled before any SQL
    GRANT access control lists are evaluated.
    The initial settings in pg_hba.conf are quite restrictive, in order to
    avoid unwanted security holes caused by unreviewed but mandatory system
    settings. You'll probably want to add something like host all all
    192.168.0.0/24 md5
    This example grants MD5 encrypted password access to all databases to all
    users on the private network 192.168.0.0/24.
    You can use the pg_hba.conf editor that is built into pgAdmin III to edit
    the pg_hba.conf configuration file. After changing pg_hba.conf, you need to
    trigger a server configuration reload using pg_ctl or by stopping and
    restarting the server process.

As noted above, i added the following one the end of the
file/etc/postgresql/8.3/main/pg\_hba.conf:

    host all all 192.168.0.0/24 md5

If you have an openldap server running and want to make use of it you
shouldn\'t add the above line but instead add:

    host all all 192.168.0.0/24 ldap ldap://sun.pinguin.local/dc=pinguin,dc=local;\
    "uid=";",ou=People,dc=pinguin,dc=local"

Note about openldap users: You still need to create a postgresql account
for the user account in openldap. You just don\'t need to define a
password for these user in postgresql. The user password in openldap
will be used.

*Need to check if we can change the above config line so that a user
needs to be a member of a group if we want to grant postgres rights.*

See the \[openldap\] (openldap) article for more informations.

And then restarted the server and all should be ok now.

Install a web interface:

    aptitude install php5-pgsql phppgadmin
    cp /etc/phppgadmin/apache.conf /etc/apache/conf.d/phpgadmin

You should now need to tweak /etc/apache/conf.d/phpgadmin. Especially if
you want to allow access from other computers. It now looks like:

    #allow from 127.0.0.0/255.0.0.0
    allow from all

You should now reload apache:

    /etc/init.d/apache2 force-reload

You can now test the web interface on http://localhost/phppgadmin/ and from
other computers if you allowed the access as noted above. Note that you
don\'t have a login yet. See below how to create some room and a user
id. http://localhost/phppgadmin/%3C/a

Install a GUI tool:

    aptitide install pgadmin3

We should now create a db:

    # First switch from root user to postgres! su postgres # The next on should inform that the db already exist createdb $USER # Should also inform the user exist createuser $USER Shall the new role be a superuser? (y/n) y

Backporting postgresql stuff
=================================================================

To backport any stuff, you may need to have build-essential installed
on your system. So start installing this if you want to backport
anything:

    aptitude install install build-essential

You now need to add the deb-src of the testing or unstable release. For
this, edit /etc/apt/sources.list and add the deb-src for the desired
release. For example: 

    deb-src http://ftp.kulnet.kuleuven.ac.be/debian/ testing main contrib non-free

*For a non-critical production server i make use of the testing source
release. As this is mostly stable and my experiences with testing
prouved some great stability.*

Update the package list:

    aptitude update

We should now create a directory somewhere and cd into it.

Backporting postgresql-8.3
--------------------------

To create the postgresql 8.3 backport on a stable box we first need to
backport and install tcl 8.5 with the follow command:

    apt-get build-dep tcl8.5-dev
    apt-get -b source tcl8.5-dev
    dpkg -i tcl8.5_8.5.3-2_i386.deb tcl8.5-dev_8.5.3-2_i386.deb tcl8.5-doc_8.5.3-2_all.deb

We are now ready to create and install the postgresql 8.3 backport:

    apt-get build-dep postgresql-common
    apt-get -b source postgresql-common
    apt-get build-dep postgresql-8.3
    apt-get -b source postgresql-8.3
    dpkg -i *.deb

If you take a look, the following files and directories are created:

    libecpg6_8.3.3-1_i386.deb
    libecpg-compat3_8.3.3-1_i386.deb
    libecpg-dev_8.3.3-1_i386.deb
    libpgtypes3_8.3.3-1_i386.deb
    libpq5_8.3.3-1_i386.deb
    libpq-dev_8.3.3-1_i386.deb
    phppgadmin-4.2/
    phppgadmin_4.2-1_all.deb
    phppgadmin_4.2-1.diff.gz
    phppgadmin_4.2-1.dsc
    phppgadmin_4.2-1_i386.changes
    phppgadmin_4.2.orig.tar.gz
    postgresql_8.3.3-1_all.deb
    postgresql-8.3-8.3.3/
    postgresql-8.3_8.3.3-1.diff.gz
    postgresql-8.3_8.3.3-1.dsc
    postgresql-8.3_8.3.3-1_i386.changes
    postgresql-8.3_8.3.3-1_i386.deb
    postgresql-8.3_8.3.3.orig.tar.gz
    postgresql-client_8.3.3-1_all.deb
    postgresql-client-8.3_8.3.3-1_i386.deb
    postgresql-client-common_90_all.deb
    postgresql-common-90/
    postgresql-common_90_all.deb
    postgresql-common_90.dsc
    postgresql-common_90_i386.changes
    postgresql-common_90.tar.gz
    postgresql-contrib_8.3.3-1_all.deb
    postgresql-contrib-8.3_8.3.3-1_i386.deb
    postgresql-doc_8.3.3-1_all.deb
    postgresql-doc-8.3_8.3.3-1_all.deb
    postgresql-plperl-8.3_8.3.3-1_i386.deb
    postgresql-plpython-8.3_8.3.3-1_i386.deb
    postgresql-pltcl-8.3_8.3.3-1_i386.deb
    postgresql-server-dev-8.3_8.3.3-1_i386.deb
    tcl8.5-8.5.3/
    tcl8.5_8.5.3-2.diff.gz
    tcl8.5_8.5.3-2.dsc
    tcl8.5_8.5.3-2_i386.changes
    tcl8.5_8.5.3-2_i386.deb
    tcl8.5_8.5.3.orig.tar.gz
    tcl8.5-dev_8.5.3-2_i386.deb
    tcl8.5-doc_8.5.3-2_all.deb

This all take up to 535 MB disk space.

Backporting phppgadmin
----------------------

Prepared and build the needed stuff:

    aptitude install install build-essential
    apt-get build-dep phppgadmin
    apt-get -b source phppgadmin
    dpkg -i phppgadmin_4.2-1_all.deb

Defining the password for the \'postgres\' user
===============================================

As root user:

    passwd postgres

The system ask then to enter a password and you need to confirm the
password.

*Note that you shouldn\'t set a password for the postgres user account.
You can switch to the postgres user with \'su postgres\' when you are
root user on the system.*

Creating the database cluster
=============================

*You shouldn\'t do this part if you installed postgres from the debian
package. You can follow these instruction if you want to create an
additional database cluster and experiment with an issolated cluster, so
that you can start postgres manually from the cli.*

Log in with the postgres user.

    su postgres

You may store the data where you want. Usually it\'s stored
in/usr/local/pgsql/data or /var/lib/pgsql/data:

    /usr/lib/postgresql/8.1/bin/initdb /path/to/dir/for/postgresql

**NOTE:** The first time you make use of postgresql, you need to make
use ofinitdb. Once done, you can make use of createdb to create more
databases. I have make use of initdb without createdb.

Creating a postgresql user account
==================================

With this i mean a user that will be able to log into postgresql.

We will first create a postgresql superuser account, to avoid to switch
fromroot to the postgres user each time.

First login from the root user account to the postgres account:

    su postgres

Create the user account:

    createuser someuser
    Shall the new role be a superuser? (y/n) y

This user is now able to create new databases. Need to check if this is
possible if user isn\'t a superuser as mentioned here above.

Otherwise you can enter n. Then you get the question Shall the new role
be allowed to create databases? (y/n). Enter n and you get the question
Shall the new role be allowed to create more new roles? (y/n). Enter n.
This is now a limited account, you should create yourself a database for
this user user.

We can now logout from the postgres user and login to someuser and
create our first database. If we don\'t provide any arguments to psql it
will try to connect a database with the same name as the userid. If you
don\'t want to create a database on name of this user, you can skip the
db creationg and login to postgres with psql postgres to login to the
interactive postgres shell in the database postgres.

Create a db for the user we will create:

    createdb someuser

Go now in the psql shell:

    psql

If you want to be able to login in the phppgadmin web interface, you
should define a password for the newly created user account:

    ALTER USER someuser PASSWORD 'mypassword';

Exit now the psql shell with typing \\q.

Creating a database in the cli
==============================

*Postgresql has another view of databases, in database we can create a
database.*

For example:

    createdb mytestdbcluster

This create mytestdbcluster. This cluster is created on the same root of
the server. See the follow sketch. Or take a look with the phppgadmin
web interface:

    PostgreSQL
        |- mytestdbcluster
        |       |
        |       `- Schemas
        |           |
        |           `- public
        |
        `- postgres
              |
              `- Schemas
                    |
                    `- public

Note that every user on the system with a shell account and a
postgresqlaccount with postgresql superuser rights can create a database
with thecreatedb command.

If the user don\'t have the rights to create a database, you will get
the error:

    createdb: database creation failed: ERROR:  permission denied to create database

You can also specify some options when creating a database:

    createdb -p 5000 -h eden -E LATIN1 -e demo

Delete a database in the cli
============================

    dropdb mytestdb

Starting the database server
============================

On a Debian GNU/Linux box you can make use of the startup script that is
automatically create to start, stop and restart the postgresqlservices.
In fact, for Debian users, this is transparant and nothing particular
should be done to get postgresql automatically started at boot time.

    /etc/init.d/postgresql start

You can start a manually with:

    postmaster -D /usr/local/pgsql/data

Maye you want to start it in the background:

    postmaster -D /usr/local/pgsql/data >logfile 2>&1 &

If you get an error like this:

    LOG:  could not bind IPv4 socket: Address already in use
    HINT:  Is another postmaster already running on port 5432? If not, wait a
    few seconds and retry.
    WARNING:  could not create listen socket for &quot;localhost&quot;
    FATAL:  could not create any TCP/IP sockets<

Probably thepostmaster are already running then. Stop the service
(/etc/init.d/postgresql stop) before an try to start the database again.

The interactive interpreter
===========================

    psql -u postgres

then you get the postgresql shell:

    postgres=#

Creating a database
-------------------

    CREATE DATABASE somedbname
        WITH ENCODING='UTF8'
            OWNER=someuser;

Create a new schema
-------------------

    CREATE SCHEMA mytestschema
        AUTHORIZATION someuser;

Creating a table
----------------

    CREATE TABLE weather (
        city            varchar(80),
        temp_lo         int,           -- low temperature
        temp_hi         int,           -- high temperature
        prcp            real,          -- precipitation
        date            date
    );
    CREATE TABLE cities (
        name            varchar(80),
        location        point
    );

For our example db:

    CREATE TABLE testschema.users
    (
       id bigserial NOT NULL,
       first_name text[] NOT NULL,
       last_name text[] NOT NULL,
        PRIMARY KEY (id)
    ) WITH (OIDS=FALSE)
    ;
    ALTER TABLE contactsdb.users OWNER TO dvanmosselbeen;

Or from phppgadmin, with a working autoincrement feature:

    CREATE TABLE users (
        id integer NOT NULL,
        first_name text NOT NULL,
        last_name text NOT NULL
    );
    ALTER TABLE testschema.users OWNER TO dvanmosselbeen;
    CREATE SEQUENCE users_id_seq
        INCREMENT BY 1
        NO MAXVALUE
        NO MINVALUE
        CACHE 1;
    ALTER TABLE testschema.users_id_seq OWNER TO dvanmosselbeen;
    ALTER SEQUENCE users_id_seq OWNED BY users.id;
    ALTER TABLE users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);
    ALTER TABLE ONLY users
        ADD CONSTRAINT users_pkey PRIMARY KEY (id);

If you may need to add some more columns:

    ALTER TABLE testschema.users
       ADD COLUMN last_name text[] NOT NULL;

Deleting a table
----------------

    DROP TABLE <tablename>;

Insert data into a table
------------------------

    INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');
    INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');

You don\'t need to know the order of the fields, you can specify the
values with:

    INSERT INTO weather (city, temp_lo, temp_hi, prcp, date)
        VALUES ('San Francisco', 43, 57, 0.0, '1994-11-29');
    INSERT INTO weather (date, city, temp_hi, temp_lo)
        VALUES ('1994-11-29', 'Hayward', 54, 37);

Anyway, it\'s better to explicitly

Or you can import some data with:

    COPY weather FROM '/home/user/weather.txt';
    INSERT INTO contacts.users (id, first_name, last_name)
        VALUES (3, 'Andy', 'Van Mosselbeen');

Importing data
--------------

    \i basics.sql

Selecting
---------

    SELECT * FROM contacts.users;

Which output:

     id | first_name |   last_name    
    ----+------------+----------------
      1 | Yasmina    | El Ouaar
      2 | David      | Van Mosselbeen
    (2 rows)

Deleting records
----------------

    DELETE FROM weather WHERE city = 'Hayward';

To delete all records from a table:

    DELETE FROM tablename;

Updating records
----------------

    UPDATE weather
        SET temp_hi = temp_hi - 2,  temp_lo = temp_lo - 2
        WHERE date > '1994-11-28';

Transactions
------------

    BEGIN;
    UPDATE accounts SET balance = balance - 100.00
        WHERE name = 'Alice';
    -- etc etc
    COMMIT;

With some savepoints in an transaction:

    BEGIN;
    UPDATE accounts SET balance = balance - 100.00
        WHERE name = 'Alice';
    SAVEPOINT my_savepoint;
    UPDATE accounts SET balance = balance + 100.00
        WHERE name = 'Bob';
    -- oops ... forget that and use Wally's account
    ROLLBACK TO my_savepoint;
    UPDATE accounts SET balance = balance + 100.00
        WHERE name = 'Wally';
    COMMIT;

Creating a view
---------------

    CREATE VIEW comedies AS
        SELECT *
        FROM films
        WHERE kind = 'Comedy';

Another example:

    CREATE VIEW contacts.vm AS
        SELECT id, first_name
        FROM contacts.users
        WHERE last_name = 'Van Mosselbeen';

Select the data from the view:

    SELECT * FROM contacts.vm;

Or you can even specify the wanted fields of the VIEW:

    SELECT first_name FROM contacts.vm;

Joins between different tables
------------------------------

\...

Change database
===============

Go into another database:

    \c <dbname>

Get help at the interactive psql shell
--------------------------------------

For psql help:

    /?

Or for SQL syntax help:

    /h

To get help on GRANT:

    \h GRANT

See all the databases
=====================

There are 2 ways:

    /l

Or:

    postgres=# select * from pg_database;
    # That output some stuff

Some other little info\'s
=========================

Changing of database:

    \c db_name
    \c db_name user host port

To see to which db and with which user we are connected:

    \c

To list schemas:

    \dn

To list the indexes

    \di

To list the sequences:

    \ds

To list the views:

    \dv

To list the system tables:

    \dS

To list the table, view, and sequence access privileges:

    \dp

List users:

    \du

List datatypes:

*add \"+\" for more detail*

    \dT

List all databases:

*add \"+\" for more detail*:

    \l

Specify from the cli with wich user we want to connect to a particular
database:

    psql -U postgres db_name

To execute some external sql file:

    \i basic.sql

\...

Some useful software
====================

-   pgadmin3 - graphical administration tool for PostgreSQL
-   phppgadmin - Set of PHP scripts to administrate PostgreSQL over the
    WWW

Some related Python modules
---------------------------

Some useful modules to use if we need to make a Python program that need
to talk with the postgresql database.

-   psycopg2 (has more features but looks to crash some time i have
    heard)
-   pygresql
-   sqlalchemy
-   sqlobject

Postgresql with OpenOffice.org Base
===================================

The advantage to use openOffice as frontend on database is that the data
is stored centrally on a computer. The data and functionality is kept
separated.

Source from: http://ubuntuguide.org/wiki/Ubuntu:Gutsy#PostgreSQL

Install the required stuff:

    aptitude install  openoffice.org2 sun-java6-jre libpg-java

Start OpenOffice.org Base:

Select Connect to an existing database. In the select list select JDBC
then click Next.

The Datasource URL field should have somethings similar
tojdbc:postgresql://localhost/database.

In JDBC driver class: org.postgresql.Driver. Then click on Test class.
You should get as message The JDBC driver was loaded successfully. Then
click next.

Fill in a username who has at least read access on this database. And
select the option password required. Press then on the Test Connection
button. You should now get a dialog where you can fill in a password.
Press the Okbutton. Click on Next and adjust the options as needed.
Click on Finish and you will be prompted to give a file name to your
database.

You are now ready to play with OpenOffice.org Base :-)

Resources
=========

- http://www.postgresql.org/
- http://www.planetpostgresql.org/
- http://ubuntuguide.org/wiki/Ubuntu:Gutsy#PostgreSQL
-  http://www.ubuntugeek.com/howto-setup-database-server-with-postgresql-and-pgadmin3.html
