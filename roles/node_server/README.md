# NodeJS role

Role to deploy NodeJS in a Debian-based machine.

The role add the NodeJS repo with the script `curl -sL https://deb.nodesource.com/setup | sudo bash -` and installs nodejs package, build-essential and supervisor (to manage the nodejs services).

## Role parameters

None.

## Role dependencies

- `common_server`
