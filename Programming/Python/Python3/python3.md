# Python 3

## Table of Contents

- [Introduction](#introduction)
- [Setting up Python](#setting-up-python)
  - [Installing Python](#installing-python)
  - [Installing Python on Windows](#installing-python-on-windows)
  - [Installing Python on Debian](#installing-python-on-debian)
  - [The Python env (virtual environment)](#the-python-env-virtual-environment)
  - [With virtualenv](#with-virtualenv)
  - [Installing additional python modules](#installing-additional-python-modules)
  - [Interesting Python modules](#interesting-python-modules)
- [The Zen of Python](#the-zen-of-python)
- [Python sample code](#python-sample-code)
  - [Variables](#variables)
  - [Functions](#functions)
  - [SimpleHTTPServer](#simplehttpserver)
- [Tools](#tools)
- [IDE's](#ides)
  - [Pycharm](#pycharm)
  - [Eclipse with PyDev](#eclipse-with-pydev)
  - [Vim](#vim)
- [Python tools](#python-tools)
  - [ipython](#ipython)
- [Resources](#resources)

## Introduction

Python is a programming language that is very well know. Python is used by well know and big enterprises. For example, Google, Nasa make extensively use of Python.

Python is awesome if you quickly need to script somethings. Python is the must have tool if you want to prototype some application. Python is used for games, Web development, and company...

## Setting up Python

Setting up Python on your computer, tablet or smartphone is easy. Most GNU/Linux come with Python pre installed. On Microsoft Windows, however, you need to install Python manually.

### Installing Python

The procedure to install Python depend of the operating system you are using. Like Python is very well know, the installation procedure for each operating system has been simplified over the last years. 

See the section that match your operating system.

### Installing Python on Windows

Installing Python on a Microsoft Windows computer is very easy. Go to the www.python.org website and download the installer that match your wishes and your system. Once the installer downloaded, execute it and follow the instructions on screen.

_Interesting for Microsoft Windows users is that Active State Python bundle which you can download from the [Active State Website](https://www.activestate.com/products/activepython/). That installation also install some common used libraries as well as libraries specific to the Microsoft Windows operating system. This could be useful if you don't want to lose time installing each module one by one and configuring them._

### Installing Python on Debian

Installing Python on a `Debian GNU/Linux` computer is very easy. The installing procedure depend on the package manager you use (`apt-get` or `aptitude`).

I have always been a great fan of aptitude to install my packages. To install Python with aptitude:

    aptitude install python3

### The Python env (virtual environment)

The goal of a Python virtual environment is to avoid infesting your main installation with extra modules, with different modules versions or with specific configuration files. Thanks to a Python environment you can isolate some sort of Python modules versions. This is very handy if you are a developer and are working on some Python code. By working with a virtual environment, you ensure to have full control of your extra installed modules as well as their versions.

The Python virtual environment system is especially a requirement on a GNU/Linux computer where there a normal user isn't able to change files located in the system directory tree (Windows doesn't allow this either with normal users but it's so easy to break that Windows system even without knowing it). As these systems are much stricter than a Microsoft Windows system.

There are different tools and modules to create and manage Python virtual environments. Some IDE's like Pycharm is also able to manage that for your or even create new Python environments. With Python 3.3 or newer, the `venv` modules is the preferred way to create and manage python virtual environments. This module is installed with the standard library, so no additional sets are required. `virtualenv` is for Python 2 and you should forget about it now.

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

### With virtualenv

First install the required packages:

    sudo apt-get install virtualenv

The syntax is as following:

    virtualenv --python=<python-version> <name-of-choice-for-your-environment>

To create your virtual python environment:

    virtualenv --python=python3 introduction-env

Which return the following in the console:

```
created virtual environment CPython3.9.2.final.0-64 in 2422ms
  creator CPython3Posix(dest=/home/itchy/pythonEnv/myEnvPy3, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/itchy/.local/share/virtualenv)
    added seed packages: pip==20.3.4, pkg_resources==0.0.0, setuptools==44.1.1, wheel==0.34.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

To activate the environment:

    source myEnvPy3/bin/activate

The prompt will have another look:

```commandline
┌──(itchy㉿scratchy)-[~/pythonEnv]
└─$ source myEnvPy3/bin/activate
┌──(myEnvPy3)(itchy㉿scratchy)-[~/pythonEnv]
└─$
```

*Note that this is a zsh shell on a Kali machine, so it already looks strange by nature if you are not used to zsh*

To desactivate the environment (to get out of it):

```commandline
┌──(myEnvPy3)(itchy㉿scratchy)-[~/pythonEnv]
└─$ deactivate
┌──(itchy㉿scratchy)-[~/pythonEnv]
└─$
```

## Installing additional python modules

To be able to install additional libraries and modules, you need to check if you have python-pip (for Python 2.x) or python-pip3 (for Python 3.x) installed. If not installed, install it with:

    sudo apt install python3-pip

There are different methods to install additional modules. One of these methods is by making use of `pip`. For example, to install the ipython shell for Python version 2:

    pip install ipython


For Python version 3 you need to make use of `pip3`.

You can get more help with of pip, by just typing in pip, wich will return you some information:

```commandline
┌──(myEnvPy3)(itchy㉿scratchy)-[~/pythonEnv]
└─$ pip3

Usage:
  pip3 <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user
                              configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times
                              (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid
                              or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is
                              available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```

Note that the `pip search` options has been disabled, see here for more information: https://status.python.org/

We now need to search on the web interface: https://pypi.org/

For example, listing the packages installed in the virtualenv:

```commandline
┌──(myEnvPy3)(itchy㉿scratchy)-[~/pythonEnv]
└─$ pip list
Package       Version
------------- -------
pip           20.3.4
pkg-resources 0.0.0
setuptools    44.1.1
wheel         0.34.2
```

Install `pwntools` in the virtualenv:

    pip3 install pwntools

And if we look now to all what packages is installed:

```commandline
┌──(myEnvPy3)(itchy㉿scratchy)-[~/pythonEnv]
└─$ pip list
Package            Version
------------------ ---------
bcrypt             3.2.0
capstone           4.0.2
certifi            2021.5.30
cffi               1.14.6
charset-normalizer 2.0.4
colored-traceback  0.3.0
cryptography       3.4.7
idna               3.2
intervaltree       3.1.0
Mako               1.1.4
MarkupSafe         2.0.1
packaging          21.0
paramiko           2.7.2
pip                20.3.4
pkg-resources      0.0.0
plumbum            1.7.0
psutil             5.8.0
pwntools           4.6.0
pycparser          2.20
pyelftools         0.27
Pygments           2.9.0
PyNaCl             1.4.0
pyparsing          2.4.7
pyserial           3.5
PySocks            1.7.1
python-dateutil    2.8.2
requests           2.26.0
ROPGadget          6.6
rpyc               5.0.1
setuptools         44.1.1
six                1.16.0
sortedcontainers   2.4.0
unicorn            1.0.2rc3
urllib3            1.26.6
wheel              0.34.2
```

Using pip we can also install requirement files that may be supplied when working with tools from sites such as `Github`. We can install these with the following command: 

        pip3 install -r requirements.txt

## Interesting Python modules

* SQLAlchemy - SQL database
* SQLObject - SQL database
* Django - Web framework
* Request - simple HTTP library.
* Scapy - send, sniff, dissect and forge network packets
* Pwntools - a CTF & exploit development library.
* ...

## The Zen of Python

Python has some particular philosophy. Try this in `ipython`:

```
import this
```

See the PEP20 for more information: https://www.python.org/dev/peps/pep-0020/

# Python sample code

## Variables

```python
myInteger = 36
myString = "Foo"
myFloat = 1.2
```

## Functions

```python
def myFunction()
    """My function description"""
    print("This is the output of my function")
```

## SimpleHTTPServer

A simple HTTP server which will start for localhost:

    python3 -m http.server

You can bind it to another ip and port if needed:    

    python -m http.server 8000 --bind 127.0.0.1

See here the python documentation:

https://docs.python.org/3/library/http.server.htmlhttps://docs.python.org/3/library/http.server.html

For python 2.x this was:

    python -m SimpleHTTPServer

## Tools

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

Vim has some plugins to help when witting Python code...

## Python tools

### ipython

ipython is an enhanced shell for Python which has autocomplete features.

## Resources

* https://www.askpython.com/