# fail2ban

## Introduction

fail2ban is an excelent tool if you want to have some monitoring system on your services you are running on your servers or simple workstation computers.

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

## Resources

- https://edywerder.ch/fail2ban-email-notification/
- https://www.youtube.com/watch?v=Z0cDqF6HAxs

