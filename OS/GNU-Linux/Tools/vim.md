# vim

## Introduction

`vim` is a very powerful text editor. It can be used on the command line as well with a graphical interface. `vim` is very complicated to use and can be really confusing. Mastering `vim` will take you months, years ! vim is so powerful that you never will know and master all it's features.

## Installation

To install the GVim, the Graphical Vim:

    apt-get install vim-gtk3

## Quick tutorial with vim-tutor

vim has a build in tutor system called `vim-tutor`.

## Configuration

Config files are saved at different levels. You have the application level and user level. At application level, the config file lies at the tree of the system files. While at user level, the config file is somewhere stored in your home directory (`~/.vimrc`).

See my example [DOTvimrc file](files/DOTvimrc) and the [DOTVM folder](files/DOTvim).

## Usage

`vim` is well know with his tons of geek commands. This make `vim` very hard to learn for newcomers. Even for some more experienced users, `vim` can give you a hard time.

If you are new to `vim`, then you should start the "vim tutorial", this can be done by entering `vimtutor` on the command line. This command will run `vim` and open a specific tutorial text file.

### In edit mode

To go in edit mode, press the `i` key.

| Command | Description |
|---|---|
| esc | Exit the edit mode. |

### In visual mode

To go in visual mode, press the "v" key. Then you can do some actions, for example selecting text with the arrow keys of your keyboard, so that you can apply commands on the selected text.

| Command | Description |
|---|---|
| :w | Write (save) file. |
| :wq | Write (save) file and quite. |
| :q! | Quite without saving. |
| gq | Reformat selected text. Selecting text you can do with (in visual mode, pressing v and moving the cursor to select text.|
| dd | Delete the whole line. |
| 3dd | Delete 3 lines. |
|:s/old_word/new_word/ | Regular expression. Replace the first occurences of the word "old_word" by "new_word".|
|:s/old_word/new_word/g | Regular expression. Replace the words "old_word" by "new_word".|

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
| ctrl+n | Autocompletion. Show matching result in a context menu. |

## Resources

* https://opensource.com/article/19/3/getting-started-vim
* https://www.howtoforge.com/vim-basics
* https://realpython.com/vim-and-python-a-match-made-in-heaven/
* https://danielmiessler.com/study/vim/ - Probably the best vim tutorial.
