# git

## Table of Contents

- [Introduction](#introduction)
- [Cloning a repository](#cloning-a-repository)
- [Modify a file from the repository](#modify-a-file-from-the-repository)
- [Commit the first commit](#commit-the-first-commit)
- [Push the data to the server](#push-the-data-to-the-server)
- [Checking the log](#checking-the-log)
- [Other things](#other-things)
- [Resources](#resources)

## Introduction

Git is the ideal tool for programmers or any type of developer, but also for example for text writers, who want to have some sort of revision system. It's a type of backup plan. You can easily revert changes or merge modifications from others.

````commandline
mkdir ~/Documents/git_repositories
cd ~/Documents/git_repositories
````

## Cloning a repository

When downloading a `git` repository you do not indentify yourself. For example, when downloading this `git` repository, as long as you don't want to push updates, all is fine. Let's start by downloading this git repository with the following command:

First of, go into a directory where you want to store the files. It's wise to create a directory somewhere where you will store all the different `git` repositories you cloned.


Then clone a repository:

````commandline
git clone https://github.com/dvanmosselbeen/dvm-docs.git
````

As we can see, we cloned the repository over the `https` protocol.

## Modify a file from the repository

Make some changes to a file. After we changed data, we can see the status of our `git` repository.

Check the status:

````commandline
git status
````

Which returns:

````commandline
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
````

We can use `git diff` now to see the differences of our modifications.

## Commit the first commit

When modifying one or more files, if you want to `push` (`commit`) them, it could be you get an error message in the trend. Speaking for myself:

```
$ git commit -m "Updated the fail2ban.md file."           
Author identity unknown

*** Please tell me who you are.

Run

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'itchy@btop.(none)')
```

So, as git inform, I have set the following:

````commandline
git config --global username.email "davd.van.mosselbeen@gmail.com"
git config --global user.name "dvanmosselbeen"
````

*It is probably more useful to not use the `-m` option when you commit. So that the default text editor will show up where there you can fill in your commit change message.*

For more help see the `git help commit` command.

## Push the data to the server

The modifications are still local and not yet pushed to the server. For this we need to user the `push` command to transfer all local `commit` changes. 

But the first time, or every once in a while, before we can `push` the commit(s) we need to create a `Personal access tokens (classic)` on the GitHub web interface. On the GitHub web interface, go to `Setting` > `Credentials` > `Personal access tokens (classic)`. And there click on `Generate new token`. Then select the first or second option, I do not know the differences. I selected the second option. Then give a Note name Expiration date, and I selected all rights as I'm the admin. It will then generate some token, copy the token carefully somewhere as you can not access that anymore.

Now:

````commandline
git push
````

It will as your username, fill it in, and then it will ask you password. Do not enter the Git Hub web password but copy and paste your token there and then press enter.

*Note that when you paste the token key there you do not see anything, so you have to trust yourself with the copy and paste skills.*

Once done, it will output something like this:

````commandline
Username for 'https://github.com': dvanmosselbeen
Password for 'https://dvanmosselbeen@github.com':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 470 bytes | 470.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/dvanmosselbeen/dvm-docs.git
   00511d1..08a8884  master -> master
````

For more help, see the `git help push` command.

## Checking the log

You can easily check the log with:

````commandline
git log
````

Which will output:

````commandline
commit 08a88847c3293fb75045503354096eebcd9d106e (HEAD -> master, origin/master, origin/HEAD)
Author: dvanmosselbeen <dvanmosselbeen@rpi-srv-4gb.home>
Date:   Wed Sep 23 16:36:20 2026 +0200

    Updated the README.md with little fixes.

commit 00511d14dccb83e2167e10bd951b1467f686110b
Author: David Van Mosselbeen <david.van.mosselbeen@gmail.com>
Date:   Wed Sep 23 04:37:15 2026 +0200

    Updated the bash.md file.

    - Changed the hostname in the document.

commit 9cb8c9c836bb346e1f63d0b56ad6e39c83bb4263
Author: David Van Mosselbeen <david.van.mosselbeen@gmail.com>
Date:   Wed Sep 23 04:36:32 2026 +0200

    Updated the rsnapshot.md file.

    - Changed the hostname in the document.

....
````

*The output has been stripped down.*

We can also for example have a log file about specific files:

````commandline
git log README.md
````

There is much more that `git log` can do. See `git help log` for more information.

## Other things

Git does much more...

It is wise to `pull` the git repository once in a while. Or each time before you start to work on in if there are multiples people working on the same git repository.

````commandline
git pull
git diff
git pull
git merge
...
````

You can have more information of each command with the `git help <command>`, for example `git help diff`.

## Resources

- <https://docs.github.com/en/get-started>
- <https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/>
