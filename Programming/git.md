-----
title: GIT Quick Reference
description: Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 
created: 2020-04-07 10:22:00
modified: 2020-04-07 10:22:00
keywords: git, programming, source, code
lang: en
-----

# GIT Quick Reference

GIT is a serious tool for developers who want to keep track of their source code changes. With this i will make it 
clear from the start that this tool is essentially very useful for non-binary data.

## GIT quick reference

There are different tools available to work with GIT. There is a command line interface tool (Git Bash) and GUI 
tools. He we describe the CLI tools

### General GIT references

Clone a repository:

	git clone https://github.com/dvanmosselbeen/Rans-S-6S-Coyote-II-For-X-Plane.git

Added file you have modified or added.

	git add <FileName>

Commit your modified data:

	git commit

Push the data:

	git push

Check out a branch.

	git checkout
	
Fetch the latest data:

	git pull

### Create a new repository and push it to the git hoster

First of all, we need to create a repository on the github web interface. On that interface once the repository 
created, it will give you information on how to push the data to the web hoster. Which resume like the following: 

Initialise a directory to be used as a git repository:

    git init

Add all the files

    git add *
    
Optionally link it to a git hoster like github:

    git commit -m "Initial commit"

Set the origin:

    git remote add origin https://github.com/dvanmosselbeen/flightgear-belgian-custom-scenery-for-xplane.git

Pus the local data to the GIT hoster:

    git push -u origin master

## Additional tips

| Command | Description |
|---|---|
| git rev-list --count <branch-name> | Show the number of commits of a branch. Usually the command will be `git rev-list --count master`. |

## Github

Github (https://github.com/) is a web service, which allow you to store your git repository on the internet. Thanks to 
this service you can also share your work in such way that other can collaborate on your project.

# Resources

* https://opensource.com/article/20/10/advanced-git-tips