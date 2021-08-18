# Create a Custom repository

## Introduction

This assumes you have created your own `.deb` packages or want to redistribute `.deb` packages.

See for example the [create-a-metapackage](create-a-metapackage.md) which details how to create your own package.

## Set up

Install the required tools:

    sudo apt install dpkg-dev

Create temporarly location:

    mkdir -p ~/tmp/repo/kali

`-p` create the parent directory if needed.

Copy the `.deb` files you have in that directory.

```commandline
cd ~/tmp/repo/kali

dpkg-scanpackages . /dev/null > Release
```

## Add info to your sources.list pointing at your repository

This can be a local file path, or on a web server

We should not add our repo to the `/etc/apt/sources.list`, but needs to create our own `list` file.

Create the file:

    touch /etc/apt/sources.list.d/dvm.list

_Where `dvm`.list is just my initials. Adjust to your needs to make things clear._

Local path:

    deb file:///<path_to_your_repo_dir> ./

Web server:

Assuming your have a kali folder on the root of your web server. For example: <https://davidvanmosselbeen.be/kali-repo/>

    deb [signed-by=/home/itchy/my-repo-release-key.gpg] https://davidvanmosselbeen.be/kali-repo kali-rolling main non-free contrib

Signing stuff:

    gpg --clearsign -o InRelease Release
    gpg -abs -o Release.gpg Release

wget http://davidvanmosselbeen.be/kali-repo/Release.gpg 
mv Release.gpg my-repo-release-key.gpg

## Resources

- <https://www.percona.com/blog/2020/01/02/how-to-create-your-own-repositories-for-packages/>
- <https://wiki.debian.org/DebianRepository/Setup>
- <https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/>
- `man apt-secure`
- <https://wiki.debian.org/DebianRepository/UseThirdParty?action=show&redirect=RepositoryInstructions>
