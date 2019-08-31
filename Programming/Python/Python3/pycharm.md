# Pycharm

# Table of Contents

* [Introduction](#introduction)
* [Like and dislike](#like-and-dislike)
    * [What i like about PyCharm](#what-i-like-about-pycharm)
* [Quick Usage and tips](#quick-usage-and-tips)
* [Blender specific things](#blender-specific-things)
    * [Configuring PyCharm to create blender addons](#configuring-pycharm-to-create-blender-addons)
    * [Blender autocompletion](#blender-autocompletion)
        * [Blender version 2.79b](#blender-version-279b)
        * [Blender version 2.80](#blender-version-280)

# Introduction

PyCharm is an awesome powerfull IDE for writting Python code. PyCharm itself is written in Java. This IDE commes in 2 versions. A Community (free) version and a Professional (paid) version. The community version has all the features a general Python coder need. However, the Professional (paid) versions has some more features.

You can download Pycharm here: https://www.jetbrains.com/pycharm/

# Like and dislike

For the moment, PyCharm is the IDE i like the most. It has all the features i want, it's easy to use. So here's my list about what i like about PyCharm:

## What i like about PyCharm

* Cross platform. Works on Microsoft Windows 10 as well as on Debian (testing) GNU/Linux.
* Good and correct code autocompletion.
* Markdown integration and Markdown window preview while writing Markdown files.
* Complete VCS (git, svn...) integration. PyCharm won't interfer with your other git tools. So you can still use your git commands even if you used the git tools of the PyCharm interface. PyCharm get automatically notified if some (git) changes have happened. In fact i'm used to use both git systems, these offered in the PyCharm interface, but time by time i still use the git command line tools with git Bash.
* Good developers tools like: Refactoring, Inspect code (PEP) and can help to reformat, Compare (diff), Quick definition, Quick documentation, reformat code, optimize imports, has a python console as well as ipython. Tasks manager (Parse and grep the FIXME, TODO in the code and list them), ...
* Debugger
* Code analyser and reports.
* Testing and profiling tools.
* Is able to work with Python virtual environments and is even able to manage Python packages updates.
* Automatically save files. We don't even need to save our file we are curently editing.
* Is not limited to writting Python code. You can also write text, Markdown, XML... But it has it's limitation.
* There are plugins, like the Markdown plugin which add the Markdown feature to the IDE. The additioal GitToolBox, which add even more git features (like a toolbar) to the other git plugin.
* Is able to auto update the IDE.

## What i dislike about PyCharm

* Commes in 2 different version, a free community version (with limited features) and a Proffessional version. 
* The proffessional version is to expensif: For individual use, this commes to 89€ the first year, 71€ the second and 53€ 3rd year onwards. For organisations, this commes to 199€ the 1ste year, 159€ the 2nd and finally 119€ the 3rd year onwards. This is more expensive than the Microsoft Office suite.

# Quick usage and tips

In any directory in the file manager, you can right click and in the context menu select `Open Folder as Pycharm Community Edition Project`. This will load all the files and subdirectories in Pycharm and create a PyCharm project. Thus this will also create the `.idea` directory in the root tree where you launched Pycharm.

# Blender specific things

Here you will find things specific to Blender. Mind configuration setup, tips and tricks...

## Configuring PyCharm to create Blender addons

On Microsoft Windows, Blender addons and scripts are located at `C:\Program Files\Blender Foundation\blender-2.80-windows64\2.80\scripts\` (system wide) and at `C:\Users\david\AppData\Roaming\Blender Foundation\Blender\2.80_PREV\scripts\` (user side). So, if we write new Blender addons, we could put our stuff there.

But i like to keep my work somewhere in my home directory and also keep my work separeted from other Blender addons and scripts. For this, we can create a specific directory tree somewhere in our home directory and recreate that Blender script directory tree. On GNU/Linux  this would be somethings like `/home/<username>/git_repositories/blender_scripts_version_X/`. On Microsoft windows this would be somethings like `C:\Users\<username>\Documents\Git_Sources\blender_scripts_version_X`.

The `username` is your username and `blender_addons_version_X` the name and version of Blender. The later one is important if you are planning to write addons for different blender versions. For instance, blender pre `2.80` addons aren't compatible with `Blender 2.80`.

There in you should create 3 directories called as follow: addons scripts and 

## Blender autocompletion

...

### Blender Version 2.79b

...

### Blender Version 2.80

...
