# Installing a Microsoft Exchange 2003 mail server

## Before installing Microsoft Exchange 2003

We first need to install some Required Windows components:

-   The NNTP component of Microsoft Internet Information Services (IIS).
-   The SMTP component of Microsoft Internet Information Services (IIS).
-   The Microsoft Internet Information Service (IIS), version 5.0 or higher.
-   The World Wide Web Service component of the Microsoft Internet Information Services
-   The ASP.Net v1.1 or higher.
-   The Internet Information Services Snap-In.

In the `Add/Remove Programs` \> `Add/Remove Windows Components` select the following:

-   In `Application Server` select: `Application Server Console`, `ASP.NET`. Then in the details of the `Internet Information Services (IIS)` select: `NNTP Service`, `SMTP Service`.

*Note that i left the default options that where automatically selected.*

## Installing Microsoft Exchange 2003

Once all Windows Components installed, we may start the Microsoft Exchange installation. Follow the few instructions on screen...

## OWA - Outlook Web Access

If you have installed an IIS and an Exchange server, you can access your mailbox thought a web interface on http://servername_or_ip/exchange/.
