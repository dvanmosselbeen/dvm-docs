# fail2ban

https://www.youtube.com/watch?v=Z0cDqF6HAxs

## Check the status

    fail2ban-client status

Which return:

```
Status
|- Number of jail:      1
`- Jail list:   sshd
```

Check status of a service:

    fail2ban-client status sshd

Which return:

```
Status for the jail: sshd
|- Filter
|  |- Currently failed: 1
|  |- Total failed:     22
|  `- File list:        /var/log/auth.log
`- Actions
   |- Currently banned: 1
   |- Total banned:     2
   `- Banned IP list:   192.168.0.54
```
