-----

* title: Debian User Manageent
* description: This article is dedicated to the Debian User Management.
* created: 28-11-2007 00:00:00
* modified: 28-11-2007 00:00:00
* keywords: debian, gnu, linux, management
* lang: en

-----

# Creating a new user

You can make use of the low level app `useradd`, however, `adduser` is more user friendly.

As root user:

    # adduser itchy                    
    Adding user `itchy' ...
    Adding new group `itchy' (1001) ...
    Adding new user `itchy' (1001) with group `itchy' ...
    Creating home directory `/home/itchy' ...
    Copying files from `/etc/skel' ...
    New password: 
    Retype new password: 
    passwd: password updated successfully
    Changing the user information for itchy
    Enter the new value, or press ENTER for the default
            Full Name []: Itchy
            Room Number []: 36
            Work Phone []: 
            Home Phone []: 
            Other []: I'm the mouse
    Is the information correct? [Y/n] y

# Deleting a user

    deluser <USERNAME>

If you want to delete his associated /home, then:

    deluser --remove-home <USERNAME>

# Grant user sudo rights

On Debian, by default members of the group sudo are granted with sudo access.

If you want the newly created user to have administrative rights, add the user to the sudo group :

    usermod -aG sudo <USERNAME>
