# Windows 10

Just a bunch of notes i have specific to Microsoft Windows 10.

## Table of Contents

- [Useful command line tools](#useful-command-line-tools)
- [Activating the hibernate item in the shutdown options](#activating-the-hibernate-item-in-the-shutdown-options)
- [Apps i like for Windows](#apps-i-like-for-windows)
- [Games](#games)

## Useful command line tools

| Command | Description |
|---|---|
| `ipconfig /all` | Give informations about the network. |
| `ipconfig /release` | Release it's ip, if in dhcp mode. |
| `ipconfig /renew` | Renew it's ip, if in dhcp mode.|
| `ipconfig /flushdns` | Flush the dns cache. |
| `hostname` | Get hostname. |
| `ping <hostname or ip>` | Say hello to another computer. |
| `tracert` | To trace and follow your network connection. |
| `pathping <hostname or ip>` | A tools which use and combine the best parts of ping and tracert.|
| `getmac` | To get your MAC address of your network cards. |
| `arp` | Address Resolution Cache, most common usage is `arp -a`. |
| `nslookup <hostname>` | Used for checking DNS record entries. |
| `nbtstat` | Diagnostic tool for troubleshooting NetBIOS issues.|
| `net` | Used for managing users, services, shares etc. |
| `net start <service-name>` | Start / stop a service. |
| `route` | Manipulates network routing tables. |
| `tasklist` | Used to list all processes. |
| `taskkill` | Used to kill a process. |
| `netstat` | Display information about tcp and udp connections and ports. See `netstat -an`.|
| `sfc /scennow` | Scan system files for errors. |
| `driverquery` | Return a list of drivers. For example `driverquery -v` will return verbose information of all drivers installed on your system.|
| `fc` | File compare. `diff` is way more useful that `fc`. |
| `powercfg` | To manage and track your power usage (electric consumption). Some useful usages are: `powercfg /a`, `powercfg hibernate on`, `powercfg hibernate off`, `powercfg /devicequery s1_supported`. `powercfg /lastwake` will show you what devices last woke up your computer. Useful if you computer wake up for unknown reasons. This needs to be done with a (cmd) console that has been launched with admin rights. For this, right click on the Command prompt shortcut and select `Run as administrator`.|
| `powercfg/energy` | This will create a (html) statistics page of the energy usage, very interesting for laptops. Needs also to be run as administrator in a shell.|
| `powercfg /batteryreport` | Same as above, but then an battery report. |
| `shutdown` | `shutdown /r /o` will restart your computer and launches the `Advanced Start Options menu`, this is where you can access the `Safe Mode` and the Windows recovery utilities. This is very handy when you are troubleshooting some issues.|
| `systeminfo` | Returns a bunch of interesting system information. Use `systeminfo /s` followed by the host name of a computer on your local network, to remotely grab the information for that system. This may require additional syntax elements for the domain, user name, and password, like this: `systeminfo /s [host_name] /u [domain]\[user_name] /p [user_password]` |
| `assoc` | Returns a list with the curent file associations. For example, `assoc .txt` will show you to which type txt belongs too.  `assoc .txt=` will change the file association for text files to whatever program you enter after the equal sign. |
| `clip` | The clipboard for command use. This program is very useful if you want to get the output of a program pasted in your clipboard. You need to pipe stuff to the `clip` program to be able to use it. For example: `systeminfo <PIPE_CHARACTER> clip`. Which will send the output of the command `systeminfo` in your clipboard. So now you can paste that somewhere else. The `PIPE_CHARACTER` character gets eaten by the Markdown markup language i use and the pipe character is the only character we can't escape with Markdown. Sorry for that. It's the character that you can get by pressing `alt+124`.|
| `pkgmgr /iu:"TelnetClient"` | To install the `TelnetClient`. `pkgmgr` is deprecated on Windows 10, use `dism` instead.|
| `cipher` | `cipher` is used to permanently delete files that where already deleted. So that they can't be recovered anymore with special recovery software. You should be aware that when you delete files, these files aren't deleted, but the reference is. The used space by the old files are then marked as being free space, and is then eventually allocated to future new data and thus the old data will then be eventually overwritten. As long as the system doesn't overwrite the old data, then the old data can be easily recovered. The `cipher` command wipes a directory by writing some random data to it, in the hope that the old data can't be recovered. It still can be recovered but way more harder and with another type of recovery tools. `cipher` doesn't delete files that "still exist" (which reference still exist in the FAT, File Allocation Table). For example, `cipher /w:c` will wipe free space on the `C:` drive, without deleting existing data. |
| `sysdm.cpl` | On the cli, to pop up the System Properties GUI. |
| `wevtutil.exe` | Enables you to retrieve information about event logs and publishers. You can also use this command to install and uninstall event manifests, to run queries, and to export, archive, and clear logs. We can also get more information about a command. Ex.: `wevtutil.exe eq /?` |

## Activating the hibernate option in the shutdown menu

By default, the hibernate feature is not activated on a Microsoft Windows Desktop computer. The hibernation feature was initially created for laptop computers to speed up in some way the startup and the shutdown process. At the same time it save the state of your current work space (profile / desktop). The hibernation feature is also way faster than a classic shutdown and start up. That's why the hibernation feature is also loved on desktop computers.

To activate the hibernation feature, the shortcut way is by going to  `Control Panel\Hardware and Sound\Power Options`. It's actually a path you can paste in the Windows File explore path bar (`ctrl+e` to start the file explorer).

The longer method is by clicking on the `Start Menu` > `Settings`. Then in that new window click on `Power & sleep`. Then on the right side, click on `Additional power settings`.

On the left side of the window, click on `Choose what the power button do`. You will see that there's a checkbox `Hibernate` which you can't activate you. First click on top of that window on `Change settings that are currently unavailable`. Now you will see that you can check the `Hibernate` option.

## Apps i like for Windows

Here's a list of applications i like to use on a Microsoft Windows operating system.

| Application | Description|
|---|---|
| [Android Studio](https://developer.android.com/studio/) | IDE to write Android apps. |
| [sysinternals](https://docs.microsoft.com/en-us/sysinternals/) | Microsoft Windows additional system tools. I recommend to download the [sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite), which contains all the needed tools.|
| [putty](https://www.putty.org/) | To do remote connections to an ssh server.
| [LibreOffice](https://www.libreoffice.org/) | Office suite. |
| [7zip](https://www.7-zip.org/) | Compression and decompression tools. |
| [mp3tag](https://www.mp3tag.de/en/) | Manage mp3 files and ID3v tags. |
| [Blender](http://www.blender.org) | Probably the best open source 3D software you will ever find.|
| [Gimp](http://www.gimp.org) | Image manipulation program. |
| [Inkscape](http://www.inkscape.org) | Vector creation program. |
| [Python](http://www.python.org) | Programming language. |
| vncviewer & vncserver | Tools for remote GUI control. |
| [Virtualbox](https://www.virtualbox.org/) | Virtualisation software |
| [HexChat](https://hexchat.github.io/) | IRC client, a copy of XChat, but XChat Windows binaries aren't available anymore for free. |
| [XAMP](https://www.apachefriends.org/fr/index.html) | Web server. |
| [Google Earth Pro](https://www.google.com/earth/) | Atlas. |
| [Google Drive](https://www.google.com/drive/) | Tool to work with files on the Google Cloud (Google drive).|
| [PyCharm]() | IDE for Python |
| [NetBeans]() | IDE for Java |
| [Eclipse](https://www.eclipse.org/) | IDE for different programming languages. See the PyDev plugin for example. Which bring Python support to the IDE.|
| [Notepad++](https://notepad-plus-plus.org/) | A notepad with extended features.|
| [FileZila](https://filezilla-project.org/) | A ftp client. |
| [Darktable](https://www.darktable.org) | The open source alternative for Adobe LightRoom. I still use LightRoom and it's what i use, but i like some features Darktable has and i keep looking at it's features time by time. And Darktable is finally available for Windows !|
| [Scribus](https://www.scribus.net/) | A page layout program. |
| Adobe Creative Cloud ||
| git ||
| vlc ||
| [Spybot Search & Destroy](https://www.safer-networking.org/download/) | Tool to scan the computer for malicious stuff.|
| [Malwarebytes](https://malwarebytes.com) | Remove spyware. |
| XAMPP | Webserver & database. |
