#!/usr/bin/python3 -I
"""Root-owned deployment helper. No caller-provided commands, paths or repositories."""
import fcntl
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

ROOT = Path("/opt/astro-portfolio")
IMAGE = "ghcr.io/alnikmakh/astro-blog"
STATE = ROOT / "current-image.env"
COMPOSE = ["/usr/bin/docker", "compose", "--project-name", "deploy-astro-blog", "--env-file", str(STATE), "--file", str(ROOT / "compose.json")]
ENV = {"PATH": "/usr/bin:/bin", "HOME": "/root", "LANG": "C.UTF-8"}


def write_image(image):
    with tempfile.NamedTemporaryFile(mode="w", dir=ROOT, delete=False) as temporary:
        temporary.write("FRONTEND_IMAGE=" + image + "\n")
        name = temporary.name
    os.replace(name, STATE)


def healthy():
    for _ in range(30):
        result = subprocess.run(["/usr/bin/curl", "--fail", "--silent", "--show-error", "--max-time", "5", "--resolve", "regulardev.click:443:127.0.0.1", "https://regulardev.click/", "--output", "/dev/null"], env=ENV, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            return True
        time.sleep(2)
    return False


def main():
    if os.geteuid() != 0 or len(sys.argv) != 2 or not re.fullmatch(r"sha256:[0-9a-f]{64}", sys.argv[1]):
        sys.exit("A single valid image digest is required")
    if ROOT.stat().st_uid != 0 or ROOT.stat().st_mode & 0o022:
        sys.exit("Deployment directory must be owned and writable only by root")
    os.umask(0o077)
    with open(ROOT / "deploy.lock", "w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            sys.exit("Another deployment is running")
        token = sys.stdin.readline(8193).strip()
        if len(token) > 8192 or (token and not re.fullmatch(r"[A-Za-z0-9_.-]+", token)):
            sys.exit("Invalid registry credential")
        image = IMAGE + "@" + sys.argv[1]
        previous = STATE.read_text().strip().removeprefix("FRONTEND_IMAGE=")
        if not re.fullmatch(re.escape(IMAGE) + r"@sha256:[0-9a-f]{64}", previous):
            sys.exit("Invalid previous deployment state")
        with tempfile.TemporaryDirectory(prefix="astro-registry-", dir="/run") as credentials:
            environment = dict(ENV, DOCKER_CONFIG=credentials)
            if token:
                login = subprocess.run(["/usr/bin/docker", "login", "ghcr.io", "--username", "alnikmakh", "--password-stdin"], input=token + "\n", text=True, env=environment, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if login.returncode:
                    sys.exit("Registry authentication failed")
            subprocess.run(["/usr/bin/docker", "pull", image], env=environment, check=True, timeout=240)
            write_image(image)
            try:
                subprocess.run(COMPOSE + ["up", "--detach", "--no-deps", "--no-build", "--pull", "never", "frontend"], env=environment, check=True, timeout=90)
                if not healthy():
                    raise RuntimeError("HTTPS health check failed")
            except Exception:
                write_image(previous)
                subprocess.run(COMPOSE + ["up", "--detach", "--no-deps", "--no-build", "--pull", "never", "frontend"], env=environment, timeout=90, check=True)
                if not healthy():
                    sys.exit("Deployment and rollback health checks failed; administrator attention required")
                sys.exit("Deployment failed; previous image restored and HTTPS verified")
    print("Deployment completed; HTTPS verified")


if __name__ == "__main__":
    main()
