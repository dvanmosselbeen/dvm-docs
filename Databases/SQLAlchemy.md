-----
title: SQLAlchemy
description: This article talk about sqlalchemy.
created: 12-03-2010 00:00:00
modified: 12-03-2010 00:00:00
keywords: sqlalchemy, database, orm, website, internet
lang: en
-----

# SQLAlchemy

## Introduction

This article wouldn\'t be complete but tries to be a little reference
for those who are working with sqlalchemy. And at the same time, this
article is growing while i\'m learning sqlalchemy. So probably there
will be some errors and things not clear or probably wrong at all.

## Terms

- ORM - Object Relational Mapper
- DDL - Data Definition Language, see <http://en.wikipedia.org/wiki/Data_Definition_Language%3E>

## The declarative way (the short hand)

Example:

    # -*- coding: utf-8 -*-
    """The PYGUICMS wiki model module."""
    from sqlalchemy import *
    from sqlalchemy import Column
    from sqlalchemy.types import Integer, Text
    #from sqlalchemy.orm import relation, backref
    from pyguicms.model import DeclarativeBase
    class Wiki(DeclarativeBase):
        __tablename__ = 'wikis'
        id = Column(Integer, primary_key=True)
        pagename=Columnt(Text, unique=True)
        data = Column(Text)
        def __init(self, pagename, data):
            self.pagename = pagename
            self.data = data

## Relations

### One to many relation


...

### Many to many relation

...

## Additional tools

There are several extensions and plugins to SQLAlchemy including:
declarative, Migrate, Elixir, SQLSoup, django-sqlalchemy, DBSprockets,
FormAlchemy, and z3c.sqlalchemy.

## Resources

- Official website - <http://www.sqlalchemy.org>
- <http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html> - this is for sqlalchemy version 0.2!!! but nice tut!
- <http://my.safaribooksonline.com/9780596516147/tutorial>
