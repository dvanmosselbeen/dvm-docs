# vim

# Table Of Contents

* [Introduction](#introduction)
* [Installation](#installation)
    * [Configuration](#configuration)
* [Shortcut keys](#shortcut-keys)
    * [In edit mode](#in-edit-mode)
    * [In visual mode](#in-visual-mode)

# Introduction

# Installation

## Configuration

Config files are save at different levels. You have the application level and user level. At application level, the config file lies at the tree of the system files. While at user level, the config file is somewhere stored in your home directory.

# Shortcut keys

Vim is well know with his tons of shortcuts. This make vim very hard to learn for newcomers. Even for some more experienced users, vim can give you a hard time

## In edit mode

To go in edit mode, press the `i` key.

| Command | Description |
|---|---|
| esc | Exit the edit mode. |

## In visual mode

To go in visual mode, press the "v" key. Then you can do some actions, for example selecting text with the arrow keys of your keyboard, so that you can apply commands on the selected text.

| Command | Description |
|---|---|
| :w | Write (save) file. |
| :wq | Write (save) file and quite. |
| :q! | Quite without saving. |
| gq | Reformat selected text. Selecting text you can do with (in visual mode, pressing v and moving the cursor to select text.|
|||
|:s/old_word/new_word/ | Regular expression. Replace the word "old_word" by "new_word".|


...
