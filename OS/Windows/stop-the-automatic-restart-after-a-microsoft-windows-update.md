---
description: This article explain how to stop the automatic restart after Microsoft Windows updates
keywords: stop reboot restart microsoft windows client update
title: Stop the automatic restart after a Microsoft Windows updates
created: 02-03-2009
---

Source come from:
<http://www.overclock.net/faqs/103266-how-do-i-stop-automatic-restart.html>

Ever gone away to let windows get on with updating, and then found that
your computer had suddenly restarted? This can be a nightmare especially
if you frequently have a lot of stuff open like documents etc. Short of
disabling automatic updates (leaving yourself more prone to security
vulnerabilities) what can you do? Read on...

Onto the fix:

1.  Click on the `Start` menu and the `Run...`. Type `gpedit.msc` into
    the drop-down box and click on `OK`.

2.  The Group Policy Manager will now appear. NOTE: I don't recommend
    messing around with anything else in here if you don't know what
    your doing.

3.  In the left pane, click on `Local Computer Policy` then expand
    `Computer Configuration` hen `Administrative Templates` then
    `Windows Components` and finally click on `Windows Update`. Whew!

4.  A few options should have now appeared in the right-hand pane. Find
    the one that says
    `No auto-restart with logged on users for sheduled automatic updates installations`
    double click on it to bring up it's properties.

5.  Change the radio button set on `Not Configured` to `Enabled` then
    hit OK.

6.  That's it, all done!

NOTE: Although this does stop the computer automatically restarting, it
won't stop the annoying dialog box which periodically pops-up reminding
you to restart.

See also <http://www.codinghorror.com/blog/archives/000294.html> on how
to adjust the time for the windows update popup.
