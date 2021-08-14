# Backup plans

## Table of Contents

- [Introduction](#introduction)
- [Create a list of all installed packages](#create-a-list-of-all-installed-packages)
- [Import a list of packages and install it](#import-a-list-of-packages-and-install-it)
- [Backup Tools](#backup-tools)

## Introduction

There are different things we need to keep in mind on a system to back up. These different things depend heavily on what you want and need to back up as well as the purpose of the machine. Not all computers have to be backed up completely because they maybe don't have that service.

Also for each kind of service, another tools might be needed.

Let's resume:

* The user home drives (`/home/` and maybe the home drive of user root, /root/) 
* Installed Packages
* Configuration files (`/etc/`)
* Databases (MySQL ??)
* Website (`/var/log/`)

## Create a list of all installed Packages

The following command will store save all installed packages on a Debian system to a file called `packages_list.txt`:

```commandline
sudo dpkg-query -f '${binary:Package}\n' -W > packages_list.txt
```

## Import a list of packages and install it

Now that we have the list, you can install the same packages on your new server with:

```commandline
sudo xargs -a packages_list.txt apt install
```

## Backup Tools

- `rsnapshot` - local and remote filesystem snapshot utility
- `backintime-common` - simple backup/snapshot system (common files)
- `backintime-qt` - simple backup/snapshot system (graphical interface)
- `burp` - Simple cross-platform network BackUp and Restore Program
- `dirvish` - Filesystem based backup system using rsync
- `mrb` - Manage incremental data snapshots with make/rsync
- `mydumper` - High-performance MySQL backup tool
- `mylvmbackup` - quickly creating backups of MySQL server's data files
- `restic` - backup program with multiple revisions, encryption and more
- `snapper` - Linux filesystem snapshot management tool
- `snapper-gui` - graphical user interface for snapper
- `snapper` - Linux filesystem snapshot management tool
- `snapper-gui` - graphical user interface for snapper
