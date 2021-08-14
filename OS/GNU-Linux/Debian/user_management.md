# Users Management

## Table of Contents

- [Creating a new user](#creating-a-new-user)
- [Deleting a user](#deleting-a-user)
- [Grant user sudo rights](#grant-user-sudo-rights)
- [Resources](#resources)

## Creating a new user

You can make use of the low level app `useradd`, however, `adduser` is more user friendly.

As root user:

    # adduser foobar                    
    Adding user `foobar' ...
    Adding new group `foobar' (1001) ...
    Adding new user `foobar' (1001) with group `foobar' ...
    Creating home directory `/home/foobar' ...
    Copying files from `/etc/skel' ...
    New password: 
    Retype new password: 
    passwd: password updated successfully
    Changing the user information for foobar
    Enter the new value, or press ENTER for the default
            Full Name []: 
            Room Number []: 
            Work Phone []: 
            Home Phone []: 
            Other []: 
    Is the information correct? [Y/n] y

## Deleting a user

    deluser <USERNAME>

If you want to delete his associated /home, then:

    deluser --remove-home <USERNAME>

## Grant user sudo rights

On Debian, by default members of the group sudo are granted with sudo access.

If you want the newly created user to have administrative rights, add the user to the sudo group :

    # Syntax is as following
    usermod -aG <GROUPNAME> <USERNAME>
    usermod -aG sudo <USERNAME>

## Resources

* https://linuxize.com/post/how-to-add-user-to-group-in-linux/
* https://linuxize.com/post/how-to-add-user-to-sudoers-in-debian/
* https://linuxize.com/post/how-to-create-groups-in-linux/
