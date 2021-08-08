# tmux

https://www.youtube.com/watch?v=BHhA_ZKjyxo

## Introduction

`tmux` is a terminal multiplexer, like the [screen](screen.md) application, but `tmux` has more features and is a younger project.

The `<prefix>` key is the base command in `tmux`. By default, this is `ctrl+b`. So when there is noted for example `<prefix> c`, this means to press `ctrl+b`, releasing these keys, followed by a `c` press. It is better to talk about `<prefix>` instead of `ctrl+b` as you can bind whatever key as `<prefix>`. You can also have more than one `<prefix>` key assigned. Which is my case, i have the `screen` style binding too, which is `ctrl+a`. Personally, I find `ctrl+a` more practical. From what I have read, it ended up `ctrl+b` to not clash with the `screen` `<preffix>` keybind as tmux was developed inside `screen`.



## Cheat Sheet

### Session Management

| Command | Description |
| --- | --- |
| `tmux ls` or `tmux list-sessions` | To list the active / running sessions. |
| `tmux new -s <session-name>` | Start a new tmux session named `<session-name>` |
| `tmux kill-session -t <session-name>` | Kill `<session-name>` |
| `tmux attach` | Attach to the most recent detached session. |
| `tmux attach -t <session name>` | (Re)Attach `<session-name>` |

### General Commands

| Command | Description |
| --- | --- |
| `<prefix> ?` | The GOD mode, the help menu of `tmux`.  Press the `q` to exit) |
| `<prefix> w` | List all windows.  |
| `<prefix> m` | Activate the mouse support.  |
| `<prefix> b PG UP` | To activate the scroll modus. Press ESC to cancel or when finished. |
| `<prefix> $` | Rename current session. |

**Extra notes:**

* In GOD mode, `<prefix> ?`, you can use PG UP and PG DN to scroll. Yes, not all commands are visible on screen. To exit GOD mode, press the `q` key.
* List all windows with `<prefix> w`. This is particularly handy as you can scroll through all you windows and if you have a lot of them, you can easily pick the one you need.
* When mouse support is activated with `<prefix> m` you can move from one pane to another by clicking in the corresponding pane. But also to resize the different panes. But also a right-click context menu. And also finally be able to scroll vertically.

### Window Management

| Command | Description |
| --- | --- |
| `<prefix> c` | Create a new window |
| `<prefix> ,` | Rename current window |
| `<prefix> n` | Go to next window |
| `<prefix> p` | Go to previous window |
| `<prefix> <digit-number>` | Where `<digit-number>` is the window (tab number) 0-9. |
| `<prefix> d` | To detach the session. the session will stay alive and you can reconnect it |
| `<prefix> &` | Kill (close) current winndow. |

### Pane Management

| Command | Description |
| --- | --- |
| `<prefix> %` | Split screen vertically. To Create a Pane |
| `<prefix> "` | Split screen horizontally. To Create a Pane |
| `<prefix> <direction-arrow>` | Go to the pane, the direction which you selected with the arrow key. |
| `<prefix> q` | Show pane numbers, used to switch between panes. |
| `<prefix> o` | Switch to the next pane. |
| `<prefix> x` | Close pane without confirmation. |
| `<prefix> b` | Break-pane, to make a pane its own window. |
| `<prefix> %` | Split the window vertically. |
| `<prefix> "` | Split the window horizontally. |
| `<prefix> {` | Move the current pane left. |
| `<prefix> }` | Move the current pane right. |

## Additional tips for the tmux.conf file

```
# add to ~/.tmux.conf
bind | split-window -h
bind - split-window -v
```

## Copy and paste

If you make use of the config file of: https://github.com/gpakosz/.tmux the `~/.tmux.conf` has already been set up and you only need to install xclip:

    sudo apt-get install xclip

See here for more information about copy & pasting: http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu/


## Resources

* https://github.com/tmux/tmux/wiki
* https://github.com/tmux/tmux/wiki/Getting-Started
* https://github.com/gpakosz/.tmux - The must-have tmux config file !!!
* See also this cheat sheet https://danielmiessler.com/study/tmux/