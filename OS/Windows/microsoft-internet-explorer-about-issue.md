# Microsoft Internet Explorer about issue

Oh my god, this dates back to `created: 28-04-2008 00:00:00`.

It happens some time when you click some link, you just get stuck at an Internet Explorer about page. At some point in time, this was a well-known annoying bug and the fix for this was to register some dll files. 

Re register the following files:

    regsvr32 urlmon.dll
    regsvr32 msscript.ocx
    regsvr32 vbscript.dll
    regsvr32 scrrun.dll
    regsvr32 dispex.dll
