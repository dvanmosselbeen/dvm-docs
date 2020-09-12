-----
title: Register a dll file
description: This article talk about how you can register a DLL or OCX file.
created: 10-09-2008 00:00:00
modified: 10-09-2008 00:00:00
keywords: Microsoft, Windows, register, dll, ocx, file, registry
lang: en
-----

# Register a dll file

Sometimes it just happen, you start your application and it complains
about a dll file not registered. You can then simple reinstall the
concerned application or just re-register the unlinked dll file.

In a DOS prompt:

    regsvr32 <path of dll or ocx file>

Then you need to confirm by pressing on the `OK` button in that popup. If
all is ok, you can restart the application and it should be ok
