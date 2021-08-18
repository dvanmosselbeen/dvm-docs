# Create a meta-package

## Introduction

...

## Install the required build tools

First install the required tools:

    sudo apt install equivs

Create some temp directory somewhere and go into it:

## Creating the custom package

```commandline
mkdir ~/my-extra-dope-tools
cd ~/my-extra-dope-tools/
```

The run the following to create our template files we can edit to our needs:

```commandline
equivs-control ns-control
```

Which will create a template file `ns-control` for us with the following content:

```commandline
### Commented entries have reasonable defaults.
### Uncomment to edit them.
# Source: <source package name; defaults to package name>
Section: misc
Priority: optional
# Homepage: <enter URL here; no default>
Standards-Version: 3.9.2

Package: <package name; defaults to equivs-dummy>
# Version: <enter version here; defaults to 1.0>
# Maintainer: Your Name <yourname@example.com>
# Pre-Depends: <comma-separated list of packages>
# Depends: <comma-separated list of packages>
# Recommends: <comma-separated list of packages>
# Suggests: <comma-separated list of packages>
# Provides: <comma-separated list of packages>
# Replaces: <comma-separated list of packages>
# Architecture: all
# Multi-Arch: <one of: foreign|same|allowed>
# Copyright: <copyright file; defaults to GPL2>
# Changelog: <changelog file; defaults to a generic changelog>
# Readme: <README.Debian file; defaults to a generic one>
# Extra-Files: <comma-separated list of additional files for the doc directory>
# Links: <pair of space-separated paths; First is path symlink points at, second is filename of link>
# Files: <pair of space-separated paths; First is file to include, second is destination>
#  <more pairs, if there's more than one file to include. Notice the starting space>
Description: <short description; defaults to some wise words> 
 long description and info
 .
 second paragraph
```

So I fine-tuned this `ns-control` file like following:

```commandline
## Commented entries have reasonable defaults.
### Uncomment to edit them.
# Source: <source package name; defaults to package name>
Section: misc
Priority: optional
# Homepage: https://www.davidvanmosselbeen.be
Standards-Version: 3.9.2

Package: my-extra-dope-tools
Version: 1.0
Maintainer: David Van Mosselbeen <contact@davidvanmosselbeen.be>
# Pre-Depends: <comma-separated list of packages>
# Depends: <comma-separated list of packages>
Depends: fail2ban, default-mysql-client, dsniff, gobuster, htop, remmina, rlwrap, steghide, tmux, xclip, filezilla, tor
# Recommends: <comma-separated list of packages>
# Suggests: <comma-separated list of packages>
Suggests: beef, hexedit, seclists, tree, zenmap-kbx
# Provides: <comma-separated list of packages>
# Replaces: <comma-separated list of packages>
Architecture: all
# Multi-Arch: <one of: foreign|same|allowed>
# Copyright: <copyright file; defaults to GPL2>
# Changelog: <changelog file; defaults to a generic changelog>
# Readme: <README.Debian file; defaults to a generic one>
# Extra-Files: <comma-separated list of additional files for the doc directory>
# Links: <pair of space-separated paths; First is path symlink points at, second is filename of link>
# Files: <pair of space-separated paths; First is file to include, second is destination>
#  <more pairs, if there's more than one file to include. Notice the starting space>
Description: Extra tools that should be installed by default on a Kali machine
 This meta-package installs a few extra tools that, in my opinion, should be installed by default on any Kali machine.
 It can be handy to be installed on a fresh Kali installation and thus save you time.
 .
 This meta-package also suggests some other packages, but does not install them as they could be pretty big.
 To install the suggested package, use the --install-suggests parameter.
 .
 This meta-package will install:
 - fail2ban
 - default-mysql-client
 - dsniff
 - gobuster
 - htop
 - remmina
 - rlwrap
 - steghide
 - tmux
 - xclip
 - filezilla
 - tor
```

## Build the deb package

Then build the package with:

```commandline
equivs-build ns-control
```

This will create the `.deb` file in the current directory:

```commandline
my-extra-dope-tools_1.0_all.deb
```

## Build the deb-src (source) package

This is optional.

```commandline
equivs-build --full ns-control
```

## Install the self created deb package

Finally, you can install the package with:

```commandline
sudo apt install ./my-extra-dope-tools_1.0_all.deb
```

Install also the suggested packages with the `--install-suggests` parameter:

```commandline
sudo apt --install-suggests install ./my-extra-dope-tools_1.0_all.deb
```

_With the `apt` command (instead of `dpkg -i <package-name.deb>`) will ensure that the `Depends` packages will be installed._

## Removing the package

```commandline
sudo apt remove my-extra-dope-tools
```

You might maybe also want to clean up and remove the packages that where installed due this package but (maybe) not in user anymore:

```commandline
sudo apt autoremove
```

## TODO

- Document how to create an online repository so that we can put this on a web server and adjust the /etc/apt-source.list file

## Resources

- <https://askubuntu.com/questions/33413/how-to-create-a-meta-package-that-automatically-installs-other-packages>
- <https://manpages.debian.org/testing/equivs/equivs-build.1.en.html>
- <https://www.debian.org/doc/debian-policy/ch-controlfields.html>
- `less /usr/share/doc/equivs/README.Debian`
- <https://askubuntu.com/questions/40011/how-to-let-dpkg-i-install-dependencies-for-me>
- <https://newbedev.com/how-to-install-suggested-packages-in-apt-get>
