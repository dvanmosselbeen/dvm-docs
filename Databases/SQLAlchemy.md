# SQLAlchemy

## Terms

- ORM - Object Relational Mapper
- DDL - Data Definition Language, see <http://en.wikipedia.org/wiki/Data_Definition_Language%3E>

## The declarative way (the shorthand)

Example:

```python
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
    pagename=Column(Text, unique=True)
    data = Column(Text)
    
    def __init(self, pagename, data):
        self.pagename = pagename
        self.data = data
```

## Relations

### One to many relation

...

### Many to many relation

...

## Additional tools

There are several extensions and plugins to SQLAlchemy including: declarative, Migrate, Elixir, SQLSoup, django-sqlalchemy, DBSprockets, FormAlchemy, and z3c.sqlalchemy.

## Resources

* Official website - <http://www.sqlalchemy.org>
* <http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html> - this is for sqlalchemy version 0.2!!! but nice tut!
* <http://my.safaribooksonline.com/9780596516147/tutorial>
