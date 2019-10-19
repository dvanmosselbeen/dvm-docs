---
description: This article talk about how you can register a DLL or OCX file.
keywords: register a dll ocx file registry
title: Register a dll file
created: 10-09-2008
---

Sometimes it just happen, you start your application and it complains
about a dll file not registered. You can then simple reinstall the
concerned application or just re-register the unlinked dll file.

In a DOS prompt:

    regsvr32 <path of dll or ocx file>

Then you need to confirm by pressing on the `OK` button in that popup. If
all is ok, you can restart the application and it should be ok
