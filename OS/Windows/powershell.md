# Powershell

# Table of Contents

- [Getting help](#getting-help)
- [Get service information](#get-service-information)
- [List of common cmdlet or functions](#list-of-common-cmdlet-or-functions)
- [Resources](#resources)

## Getting help

In the powershell, you can type in `help` or `Get-Help`. And there you go. Follow the instructions there to get even more help. The difference between these 2 commands is that ´help´ pipe the output to the `more` command.

- You can also use the tab key for autocompletion.
- You can also pipe output to the more command. For readability. For example `Get-WindowsFeature | more`.

## Get service information

Will return all services if no service name given.

    Get-Service <SERVICE-NAME>

For example:

    Get-Service webclient

Which will output:

```
Status   Name               DisplayName
------   ----               -----------
Stopped  WebClient          webclient
```

To start this service:

    Start-Service webclient

## List of common cmdlet or functions

| Name | Description |
|---|---|
| `Get-Help` | Get help within the Powershell. |
| `Get-Process` | Get information about the running processes. (A lot of output.) |
| `Get-WindowsFeature` | List all installed features. SERVER edition only. |
| `Get-WinEvent` | To view Windows Event Logs. |

## Resources

- <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/?view=powershell-7.1https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/?view=powershell-7.1>