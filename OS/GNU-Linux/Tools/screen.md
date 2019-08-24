`screen` is an utility, a program that most command line users would love. With `screen` you can attach and detach `screen` sessions. This means, after starting screen in a terminal or a shell, you can close that terminal / shell and later on reconnect on that session. This is especially useful for remote connections. For example clients that connect a server remotely. But screen is even more than that, you can have multiples windows in one screen. You can compare this with a additional tab in a graphical terminal console. But with screen, you can also split up your screen in sections.

Screen has a lot of features, here's a few of them:

    * Create shell session which we later can detach and re attach.
    * Multiples windows
    * Split screen
    * Log the session to a log file
    * It has it's own more performant window scroll feature

# Quick guide

To get quick help:

    screen -h

Start a new session:

    screen -S MyConnection

Do you are in your shell your used to be. Do your stuff your are used to do remotely. One interesting ting would be this help command:

    ctrl+a ?

Detach the screen session:

    ctrl+a d
    
List existing sessions:

    screen -list

Re attach an existing session:

    screen -r MyConnection
    
If you started a `screen` session without specifying a name, you can still connect to it but then you need to know it's id. For example i got this result with `screen -list`:

    There is a screen on:
        3412.pts-1.debianStable (08/21/2019 10:26:32 PM)        (Detached)

Then you can re attach to this session with the command `screen -r 3412`.

https://linuxize.com/post/how-to-use-linux-screen/

https://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/