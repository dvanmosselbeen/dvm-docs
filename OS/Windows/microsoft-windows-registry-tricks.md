-----
title: Microsoft Windows registry tricks
description: Some Microsoft Windows registry tips and tricks.
created: 06-04-2008 00:00:00
modified: 06-04-2008 00:00:00
keywords: Microsoft, Windows, Registry, tips, tricks
lang: en
-----

# Microsoft Windows registry tricks

## Table of Contents

* [Introduction](#introduction)
* [Backing up the registry](#backing-up-the-registry)
* [Startup](#startup)
* [Last good know configuration](#last-good-know-configuration)
* [Enable numlock on boot](#enable-numlock-on-boot)
* [Tools](#tools)

## Introduction

In this article, we abbreviate the root classes, here\'s the full name
vs the abbreviation:

    HKEY_LOCAL_MACHINE: HKLM
    HKEY_USERS: HKU
    HKEY_CLASSES_ROOT: HKCR
    HKEY_CURRENT_CONFIG: HKCC
    HKEY_CURRENT_USER: HKCU

The registry is saved into different files on the filesystem, these
files are called hives and are located at
`%SystemRoot%\system32\config`.

    default - which corresponds to HKU\.DEFAULT subkey.
    SAM - which corresponds to HKLM\SAM subkey.
    SECURITY - which corresponds to HKLM\SECURITY subkey.
    software - which corresponds to HKLM\SOFTWARE subkey.
    system - which corresponds to HKLM\SYSTEM subkey.

The rest of hive files are stored per user in each profile directory
with the name of `Ntuser.dat`. This file is to set the pointer for the
`HKCU`.

In the registry, each value has a name, a data type and a value
associated. 1024KB is the theoretical the limit a value can have.

The different data types are:

    REG_BINARY
    REG_WORD
    REG_DWORD
    REG_SZ
    REG_EXPAND_SZ
    REG_FULL_RESOURCE_DESCRIPTOR

## Backing up the registry

To backup the whole registry:

    regedit /e c:\full_registry_export.reg

To backup a specific root key:

    reg save hkcu c:\hkcu_export.reg

## Startup

**Applies for:** 2000, XP, 2003

    HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

## Last good know configuration

    HKLM\SYSTEM\CurrentControlSet

## Enable numlock on boot

In the registry, go to `HKEY_USERS\.Default\Control Panel\Keyboard` and
set `InitialKeyboardIndicators` value from `0` to `2`.

See KB\[154529\] (http://support.microsoft.com/kb/154529) for more info.

## Tools

    regedit
    reg (cli tool)
