-----
title: Let a Microsoft client join a Microsoft domain
description: This article explain how easy you can add a computer to a Microsoft domain.
created: 28-11-2007 00:00:00
modified: 28-11-2007 00:00:00
keywords: Microsoft, Windows, client, domain, server
lang: en
-----

# Let a Microsoft client join a Microsoft domain

The advantage to join a computer to a Microsoft Windows domain are many.
The most know is to benefit of the Active Directory.

To add your computer to a domain; simple click with the right mouse
button on`My Computer` then on the contextual menu `Properties`. In that
new window that appear; go to the tab `Computer Name` and click on the
button `Change`. In that window you can change the computer name of the
computer and define the workgroup or the domain to join.

If the client point to some DNS server other that these of the domain
(ie it point to your gateway). You need to change the DNS on the client
that just joined the domain and point it to the DNS of the domain.
Otherwise you couldn\'t make use of some domain resources. ie the group
policy couldn\'t be applied. Leave the default gateway to the device
that is the gateway. Don\'t point it to the Windows server. Otherwise
the client can\'t reach the web anymore.
