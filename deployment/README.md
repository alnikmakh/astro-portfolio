# Production deployment

GitHub Actions validates the application, publishes `ghcr.io/alnikmakh/astro-blog`, and sends only `deploy sha256:<digest>` over SSH. The deployment job uses the `production` environment; only the `main` branch may access its four SSH secrets. Deployments remain automatic after validation.

On the server, OpenSSH forces `remotemgr` into `/usr/local/libexec/astro-portfolio-ssh-gate`, installed from `ssh_gate.py`. Shell commands, SFTP/SCP, PTYs and forwarding are disabled. Its sole sudo permission runs `/usr/local/sbin/astro-portfolio-deploy`, installed from `deploy.py`; the account is not a member of `docker`.

The root helper accepts exactly one SHA-256 digest in the fixed GHCR repository. A short-lived GitHub registry token arrives over stdin, is used in a temporary root-only Docker configuration and is deleted after the operation. No registry password is stored permanently by the helper. Only the frontend is updated. A failing HTTPS health check restores the previous image.

The resolved server Compose configuration, persistent nginx/ACME files and current-image state are under `/opt/astro-portfolio`, owned by root. The frontend has no host bind mounts. Changing the helper or server configuration requires the separate administrative Tailscale SSH account; a workflow cannot overwrite them.

Administrator access:

```sh
tailscale ssh ubuntu@srv473964
sudo -i
```

Manual deployment or rollback to a known image digest:

```sh
printf '\n' | sudo /usr/local/sbin/astro-portfolio-deploy sha256:<64-lowercase-hex-digest>
```

For a private package, provide a valid read-only registry token on stdin instead of the empty line. Do not put tokens in command arguments or shell history.

Root-only migration backups are under `/var/backups/astro-portfolio/`. They include previous Compose/account metadata and the retired authorized public key. They are not active SSH credentials. The new private SSH key lives only in the GitHub `production` environment after setup.

`CODEOWNERS` assigns workflows, deployment helpers and container configuration to the repository owner. Protected `main` requires the `Build website` check and owner review for deployment-related changes by other contributors; the sole owner may bypass the review requirement to avoid requiring a second person for their own changes. Administrator control of GitHub settings is still a trust boundary: this setup does not make a fully compromised owner account harmless.
