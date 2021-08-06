# SQLObject

Get information of a model:

```commandline
sqlobject-admin
```

## Relations

### One-to-many

A person can have multiples addresses:

```python
class Address(SQLObject):
    street = StringCol()
    city = StringCol()
    state = StringCol(length=2)
    zip = StringCol(length=9)
    person = ForeignKey('Person')

class Person(SQLObject):
    ...
    addresses = MultipleJoin('Address')
```

If we already build the class we can use:

```python
Person.sqlmeta.addJoin(MultipleJoin('Address',
                   joinMethodName='addresses'))
```

filling in new info with:

```python
Address(street='123 W Main St', city='Smallsville',
        state='MN', zip='55407', person=p)
```

### Many-to-many

```python
class User(SQLObject):
    class sqlmeta:
        # user is a reserved word in some databases, so we won't
        # use that for the table name:
        table = "user_table"
    username = StringCol(alternateID=True, length=20)
    # We'd probably define more attributes, but we'll leave
    # that exercise to the reader...
    roles = RelatedJoin('Role')

class Role(SQLObject):
    name = StringCol(alternateID=True, length=20)
    users = RelatedJoin('User')
```

Filling in information:

```python
bob = User(username='bob')
tim = User(username='tim')
jay = User(username='jay')
admin = Role(name='admin')
editor = Role(name='editor')
bob.addRole(admin)
bob.addRole(editor)
tim.addRole(editor)

bob.roles
[<Role 1 name='admin'>, <Role 2 name='editor'>]

tim.roles
[<Role 2 name='editor'>]
jay.roles
[]

admin.users
[<User 1 username='bob'>]

editor.users
[<User 1 username='bob'>, <User 2 username='tim'>]
```

## See also

* [SQLAlchemy](http://www.sqlalchemy.org) - This is another ORM, and in my opinion more powerful but more complex
