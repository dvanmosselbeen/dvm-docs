# Backup plans

There are different things we need to keep in mind on a system to back up. These different things depend heavily on what you want, need to back up as well as the purpose of the machine. Not all computers have to be backed up completely because they maybe don't have that service.

Also for each kind of service, another tools might be needed.

Let's resume:

* The user home drives (`/home/` and maybe the home drive of user root, /root/) 
* Installed Packages
* Configuration files (`/etc/`)
* Databases (MySQL ??)
* Website (`/var/log/`)

## Create a List of all Installed Packages

The following command will store the list of all installed packages on your Debian system to a file called `packages_list.txt`:

```commandline
sudo dpkg-query -f '${binary:Package}\n' -W > packages_list.txt
```

Now that you have the list, you can install the same packages on your new server with:

```commandline
sudo xargs -a packages_list.txt apt install
```