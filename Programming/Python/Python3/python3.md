-----
title: Python 3
description: This article is dedicated to Python 3.
created: 00-00-2020 00:00:00
modified: 00-00-2020 00:00:00
keywords: python, programming, tools
lang: en
-----

# Table Of Contents

* [Introduction](#introduction)
* [Setting up Python](#setting-up-python)
    * [Installing Python](#installing-python)
        * [Installing Python on Windows](#installing-python-on-windows)
        * [Installing Python on Debian](#installing-python-on-debian)
    * [The Python env (virtual environment)](#the-python-env-virtual-environment)
    * [Installing additional modules](#installing-additional-python-modules)
    * [Interesting Python modules](#interesting-python-modules)
* [The Zen of Python](#the-zen-of-python)
* [Tools](#tools)
    * [IDE's](#ides)
        * [PyCharm](#pycharm)
        * [Eclipse with PyDev](#eclipse-with-pydev)
        * [Vim](#vim)
    * [Python tools](#python-tools)
        * [ipython](#ipython)
* [Resources](#resources)

# Introduction

Python is a programming language that is very well know. Python is used by well know and big enterprises. For example, Google, Nasa make extensively use of Python.

Python is awesome if you quickly need to script somethings. Python is the must have tool if you want to prototype some application. Python is used for games, Web development, and company...

# Setting up Python

Setting up Python on your computer, tablet or smartphone is easy. Most GNU/Linux come with Python pre installed. On Microsoft Windows, however, you need to install Python manually.

## Installing Python

The procedure to install Python depend of the operating system you are using. Like Python is very well know, the installation procedure for each operating system has been simplified over the last years. 

See the section that match your operating system.

### Installing Python on Windows

Installing Python on a Microsoft Windows computer is very easy. Go to the www.python.org website and download the installer that match your wishes and your system. Once the installer downloaded, execute it and follow the instructions on screen.

_Interesting for Microsoft Windows users is that Active State Python bundle which you can download from the [Active State Website](https://www.activestate.com/products/activepython/). That installation also install some common used libraries as well as libraries specific to the Microsoft Windows operating system. This could be useful if you don't want to lose time installing each module one by one and configuring them._

### Installing Python on Debian

Installing Python on a `Debian GNU/Linux` computer is very easy. The installing procedure depend of the package manager you use (`apt-get` or `aptitude`).

I have always be a great fan of aptitude to install my packages. To install Python with aptitude:

    aptitude install python3

## The Python env (virtual environment)

The goal of a Python virtual environment is to avoid to infest your main installation with extra modules, with different modules versions or with specific configuration files. Thanks to a Python environment you can isolate some sort of Python modules versions. This is very handy if you are a developer and are working on some Python code. With working with a virtual environment, you ensure to have full control of your extra installed modules as well as their versions.

The Python virtual environment system is especially a requirement on a GNU/Linux computer where there a normal user isn't able to change files located in the system directory tree (Windows doesn't allow this either with normal users but it's so easy to break that Windows system even without knowing it). As these systems are much more stricter than a Microsoft Windows system, where there you can override, add or change any files where you want.

There are different tools and modules to create and manage Python virtual environments. Some IDE's like Pycharm is also able to manage that for your or even create new Python environments. With Python 3.3 or newer, the `venv` modules is the preferred way to create and manage python virtual environments. This module is installed with the standard library, so no additional sets are required. virtualenv is for Python 2 and you should forget about it now.

You can find more information about the Python virtual environment here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

The Pythons installers for windows include `pip`. Check the current installed version in a console:

    py -m pip --version
    
Which returns the following on a Microsoft Windows 10 operating system:

    pip 19.0.3 from C:\Python37-32\lib\site-packages\pip (python 3.7)

You can make sure that pip is up to date by executing the following command:

    py -m pip install --upgrade pip

From Python 3.3 or newer, the `venv` modules is the preferred method to manage Python virtual environments.

Create the virtual environment in the current working directory:

    python3 -m venv my_python3.7_env
    
_This will take some time to finish and nothing is shown on the console. Once created, you will see that the shell goes back to a new line and the a directory called `my_python3.7_env` has been created. The `my_python3.7_env` has a size of 25.1 MB with a fresh Python 3.7.4 (32bit) installation. If you have already installed some modules in your main installation, these modules will be also included in your virtual environment and thus, that environment will be bigger._

Activate the virtual environment:

    # For macOS and Linux
    source my_python3.7_env/bin/activate
    
    # On Windows
    .\my_python3.7_env\Scripts\activate

If on windows, you will see that you shell will change to somethings similar to this:

    (my_python3.7_env) C:\Users\dvanmosselbeen\python_virtual_env>

From now, if you install or upgrade modules, they will only affect the Python virtual environment and not your main installation. 

Desactivate the environment:

    desactivate
    
Make your virtual environment your default python:

    ???

## Installing additional python modules

There are different methods to install aditional modules. One of these methods is by making use of `pip`. For example, to install the ipython shell:

    pip install ipython

## Interesting Python modules

* SQLAlchemy - SQL database
* SQLObject - SQL database
* Django - Web framework
* ...

# The Zen of Python

Python has some particular philosophy. Try this in `ipython`:

```
import this
```

See the PEP20 for more information: https://www.python.org/dev/peps/pep-0020/

# Tools

There's tons of tools available for Python.

## IDE's

IDE stand for Integrated Development Environment. Somehow, an IDE is comparable to an advanced text editor. The features an IDE have could have, depend of the IDE you use and for the language the IDE has been initially made for. An IDE can for example autocomplete code while you are typing. Most of the time it has a debugger integrated into it and some tools to speed up your programming workflow.

An IDE is meant to be to make life of an programmer easier.

### Pycharm

Pycharm is an awesome Python IDE. At my opinion, Pycharm is currently one of the best IDE's that is available on the marked for the moment.

Pycharm come in 2 different versions, the (Free) community version and the paid version. The Free version does more as it job and that's what i'm using. See the [dedicated PyCharm page](pycharm.md).

### Eclipse with PyDev

Eclipse is a general purpose IDE writen in Java. Pydev is some extra Python addon for Eclipse which bring some additional, specific to Python, features.

### Vim

Vim has some plugins to help when witting Python code
...

## Python tools

### ipython

ipython is an enhanced shell for Python which has autocomplete features.

# Resources

* https://www.askpython.com/