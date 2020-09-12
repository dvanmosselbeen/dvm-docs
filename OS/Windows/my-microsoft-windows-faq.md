-----
title: My Microsoft Windows FAQ
description: This is my Microsoft Windows FAQ 
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: Microsoft, Windows, faq, frequently asked questions
lang: en
-----

# My Microsoft Windows FAQ

This page is intended for an Frequently Asked Question about Microsoft
Windows. Not specific to a version of Microsoft Windows. This page is
especially intended to point to some other pages. See also the general
MSWindows page.


## How do i add a new user?

See the general MSWindows page.

## How do i add a new printer?

See the general MSWindows page.

## Office documents are opening slowly


Opening an Office document, Word, Excel, it take more as 30 seconds
before this open. While opening Word and then opening the file within
Word goes directly.

    tools > Folder Options

Select there `doc`, advanced, and the Open action. Then press on the
Edit button. Uncheck `Use DDE`. In `Application used to perfom action:`
go to the end of the line. Remove `/dde` and append `"%1"` with the
double quotes.

<http://forums.techarena.in/ms-office-support/908660.htm>

## Wrong keyboard layout at logon

If the keyboard layout is different on the logon screen of that once
logged in, go to into the registry:

    'HKEY_USERS\ .DEFAULT\ Keyboard Layout\ Preload'

and change the value to:

    00000401 Arabic (Saudi Arabia) 00000405 Chech 00000406 Danish 00000409
    English (US) 00000413 Dutch 00000809 English (UK) 00000813 Belgian
    00000C09 English (Australia) 00003C01 Arabic (Bahrain)

See <http://www.cryer.co.uk/brian/windows/trbl_nt_kbdlytlgn.htm>

See <http://www.cryer.co.uk/brian/windows/info_windows_locale_table.htm>
for the other codes.

## How to hidden installed applications or remove installed applications

Start regedit via the run menu:

Go to the follow location:

    KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

There are sub folders, take a look at this. Before deleting a sub
folder, create a backup of the register.

## Scan the protected system files and replaces incorrect versions with correct Microsoft versions

    sfc /scannow

## Process list

Get a list of running processes:

    Tasklist /SVC

Get more info about a process:

    Tasklist /FI pid <pid_id>
