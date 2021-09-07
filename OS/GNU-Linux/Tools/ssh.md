# SSH Server

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