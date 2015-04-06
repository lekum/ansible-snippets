# Common server role

Role to manage the dependencies common to every server.

Ensures the presence of ntp, git, rsync, python-apt and aptitude.

Syncs with a list of ntp servers.

## Role parameters

Variables and example values:

```
packages_to_install:
    - git
    - rsync
    - python-apt
    - aptitude
    - ntp

ntp_servers:
    - 0.amazon.pool.ntp.org
    - 1.amazon.pool.ntp.org
    - 2.amazon.pool.ntp.org
```

If the variable `hostname` is defined, then it sets the machine hostname.

## Role dependencies

None.
