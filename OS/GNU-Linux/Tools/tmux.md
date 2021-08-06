# tmux

https://www.youtube.com/watch?v=BHhA_ZKjyxo

## Introduction

`tmux` is like the [screen](screen.md) application, but `tmux` has more features and is a younger project.

## Cheat Sheet

| Command | Description |
| --- | --- |
| `<prefix>` | This is the base command in `tmux`. By default this is `ctrl+b`. So when there is noted for example `<prefix> c`, this means to press `ctrl+b`, releasing these keys, followed by a `c` press. |
| `<prefix> ?` | The god mode, the help of `tmux`. Where you will find all the key combinations. You can use the `up` and `down` arrows, `PG UP` and `PG DN` keys in the help menu. Press the `q` key to get out of the help. Note that the keys are case sensitive, and you know, where the shift button is located ;-) |
| `<prefix> c` | Create a new window |
| `<prefix> ,` | Rename current window |
| `<prefix> n` | Go to next window |
| `<prefix> p` | Go to previous window |
| `<prefix> <digit-number>` | Where `<digit-number>` is the window (tab number). |
| `<prefix> w` | List all windows. This is particularly handy as you can scroll through all you windows and if you have a lot of them, you can easily pick the one you need. |
| `<prefix> %` | Split screen vertically |
| `<prefix> "` | Split screen horizontally |
| `<prefix> <direction-arrow>` | Go to the pane, the direction which you selected with the arrow key. |
| `tmux new -s <session-name>` | Create a new session where `<session-name>` is the name you want to give to this session. |
| `<prefix> d` | To detach the session. the session will stay alive and you can reconnect it |
| `tmux list-session` or `tmux ls` for short | When a session detached, look up after it's name before re attaching it. |
| `tmux attach -t <SESSION_NAME>` | Re attach <SESSION_NAME> |
| `<prefix> m` | Activate the mouse support, super handy to move from one pane to another. But also to resize the different panes. But also a right-click context menu. But also to be able to scroll vertically. |

```
# session management
tmux ls (or tmux list-sessions)
tmux new -s session-name
Ctrl-b d Detach from session
tmux attach -t [session name]
tmux kill-session -t session-name

Ctrl-b c Create new window
Ctrl-b d Detach current client
Ctrl-b l Move to previously selected window
Ctrl-b n Move to the next window
Ctrl-b p Move to the previous window
Ctrl-b & Kill the current window
Ctrl-b , Rename the current window
Ctrl-b q Show pane numbers (used to switch between panes)
Ctrl-b o Switch to the next pane
Ctrl-b ? List all keybindings

# moving between windows
Ctrl-b n (Move to the next window)
Ctrl-b p (Move to the previous window)
Ctrl-b l (Move to the previously selected window)
Ctrl-b w (List all windows / window numbers)
Ctrl-b window number (Move to the specified window number, the
default bindings are from 0 -- 9)

# Moving between pane
ctrl-b <arrow keys>
ctrl-b x Shut a pane with confirmation
ctrl-d Shut a pane without confirmation

# Tiling commands
Ctrl-b % (Split the window vertically)
CTRL-b " (Split window horizontally)
Ctrl-b o (Goto next pane)
Ctrl-b q (Show pane numbers, when the numbers show up type the key to go to that pane)
Ctrl-b { (Move the current pane left)
Ctrl-b } (Move the current pane right)

# Make a pane its own window
Ctrl-b : "break-pane"

# add to ~/.tmux.conf
bind | split-window -h
bind - split-window -v
```

See also this cheat sheet https://danielmiessler.com/study/tmux/

## Sample config file

This is a must have!

* https://github.com/gpakosz/.tmux

## Copy and paste

If you make use of the config file of: https://github.com/gpakosz/.tmux the `~/.tmux.conf` has already been set up and you only need to install xclip:

    sudo apt-get install xclip

See here for more information about copy & pasting: http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu/


## Resources

* ...
