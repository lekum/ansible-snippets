# Nginx role

Role to deploy and configure nginx in a Debian-based machine.

The role adds the ppa `ppa:nginx/stable` and installs the `nginx` service.

## Role parameters

- `site_file`: When defined, it is the path to a site configuration file to be copied to `/etc/nginx/sites_available/` and linked in `/etc/nginx/sites-enabled`.
- `ssl_folder`: When defined, it is the path to a folder (ending in `/`) containing the certificates to be copied to `/etc/nginx/ssl/`.

## Role dependencies

- `common_server`
