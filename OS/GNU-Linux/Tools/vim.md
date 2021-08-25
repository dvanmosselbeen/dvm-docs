# vim

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Quick tutorial with vim-tutor](#quick-tutorial-with-vim-tutor)
- [Getting help](#getting-help)
- [Configuration](#configuration)
- [Modes](#modes)
- [Usage](#usage)
  - [Command mode](#command-mode)
  - [Insert mode](#insert-mode)
  - [Visual mode](#visual-mode)
- [Common usages](#common-usages)
- [Copy & pasting text](#copy--pasting-text)
- [Reformatting some text to some width](#reformatting-some-text-to-some-width)
- [Addons](#addons)
- [Vim python tricks](#vim-python-tricks)
- [Resources](#resources)

## Introduction

`vim` is a very powerful text editor. It can be used on the command line as well with a graphical interface. `vim` is very complicated to use and can be really confusing. Mastering `vim` will take you months, years ! `vim` is so powerful that you will never know and master all it's features.

## Installation

To install the GVim, the Graphical Vim:

    apt-get install vim-gtk3

## Quick tutorial with vim-tutor

vim has a build in tutor system called `vim-tutor`.

## Getting help

The easiest way to ask for help is to start with executing `:help` during a Vim session. This will drop us into the main help file which has an overview of the basics.

To get help with a specific command, we can provide that command as an argument to the `:help` command. By invoking `:help gg`, we learn more details about `gg` including that `<C-home>` does the same thing and that by providing a `[count]`, we can use `gg` to jump anywhere in a file.

## Configuration

Config files are saved at different levels. You have the application level and user level. At application level, the config file lies at the tree of the system files. While at user level, the config file is somewhere stored in your home directory (`~/.vimrc`).

See my example [DOTvimrc file](files/DOTvimrc) and the [DOTVM folder](files/DOTvim).

## Modes

There are three basic modes in Vim:

- `Command mode` is where you can run commands. This is the default mode in which Vim starts up.
- `Insert mode` is where you insert i.e. write the text. 
- `Visual mode` is where you visually select a bunch of text so that you can run a command/operation only on that part of the text.

These form the pillars of navigating and using Vim. Try and answer the questions and work out how to begin creating a basic text document in Vim.

## Usage

`vim` is well know with his tons of geek commands. This make `vim` very hard to learn for newcomers. Even for some more experienced users, `vim` can give you a hard time.

If you are new to `vim`, then you should start the "vim tutorial", this can be done by entering `vimtutor` on the command line. This command will run `vim` and open a specific tutorial text file.

### Command mode

| Command | Description |
|---|---|
| `esc` | Comme back to command mode or just escape. |
| `i` | Enter Edit mode. |
| `v` | Enter Visual mode. |
| `h` | Move cursor to the left. |
| `l` | Move cursor to the right. |
| `j` | Move cursor down. |
| `k` | Move cursor up. |
| `w` | Jump to the start of a word. |
| `e` | Jump to the end of a word. |
| `i` | Insert before the cursor. |
| `I` | Insert after the cursor. |
| `a` | Append after the cursor. |
| `A` | Append at the end of the line. |
| `o` | Append a new line under the current line. |
| `:w` | Write (save) file. |
| `:wq` | Write (save) file and quit. |
| `:wqa` | Write (save) file for all active tabs and quit. |
| `:q!` | Force quitting without saving. |
| `:w !sudo tee %` | How do we write the file, but don't exit- as root? |
| `gq` | Reformat selected text. Selecting text you can do with (in visual mode, pressing `v` and moving the cursor to select text. |
| `yy` | Copy a line. |
| `2yy` | Copy 2 lines. Change number to your number. |
| `y$` | Copy to the end of the line. |
| `p` | Paste the clipboard contents before the cursor. |
| `P` | Paste the clipboard contents after the cursor. |
| `d` | Cut a line. |
| `D` | Cut to the end of the line. |
| `x` | Cut a character. |
| `dd` | Delete the whole line. |
| `3dd` | Delete 3 lines. Change number to your number. |
| `/pattern` | Search forward for a pattern. |
| `?pattern` | Search backwards for a pattern. |
| `n` | Repeat this search in the same direction. |
| `N` | Repeat this search in the opposite direction. |
| `:%s/old/new/` | Regular expression. Replace the first occurrences of the word "`old`" by "`new`".|
| `:%s/old/new/g` | Regular expression. Replace the words "`old`" by "`new`".|
| `:vimgrep` | Use `vimgrep` (`grep`) to search for a pattern in multiples files. |

### Insert mode

To go in edit mode, press the `i` key.

| Command | Description |
|---|---|
| `esc` | Exit the edit mode. |

### Visual mode

To go in visual mode, press the "v" key. Then you can do some actions, for example selecting text with the arrow keys of your keyboard, so that you can apply commands on the selected text.

### Common usages

Here some quick tips on common usages.

#### Copy & pasting text

There are different methods:

* Selecting some text with the `v` key and then pressing `y` to copy, then `p` to paste.
* Copying a whole line can be as easy as pressing `yy` then `P`.

#### Reformatting some text to some width

It is very common on a GNU/Linux system or in programming language the need to reformat a paragraph to some width.

## Addons

| Name | Description |
|---|---|
| vim-python-jedi | Autocompletion plugin for python|

## Vim python tricks

| Command | Description |
|---|---|
| `ctrl + n` | Autocompletion. Show matching result in a context menu. |

## Resources

- <https://opensource.com/article/19/3/getting-started-vim>
- <https://www.howtoforge.com/vim-basics>
- <https://realpython.com/vim-and-python-a-match-made-in-heaven/>
- <https://danielmiessler.com/study/vim/> - Probably the best vim tutorial.
- <https://tryhackme.com/room/toolboxvim> - A dedicated room on TryHackMe.
