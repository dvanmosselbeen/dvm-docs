# git

## Introduction

...

When downloading a git repository you do not indentify. For example, when downloading this git repository, as long as you don't want to push updates, all is fine. Let's start by downloading this git repository with the following command:

First of, go into a directory where you want to store the files. It's wishe to create a directory somewhere where you will store all the different git repositories you cloned.

    mkdir ~/Documents/git_repositories
    cd ~/Documents/git_repositories

Then clone this repository:

    git clone https://github.com/dvanmosselbeen/dvm-docs.git

When modifying one or more files, if you want to push (commit) them, it could be you get an error message in the trend. Speaking for myself:

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

    git config --global username.email "davd.van.mosselbeen@gmail.com"
    git config --global user.name "dvanmosselbeen"


## Resources

- https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/

