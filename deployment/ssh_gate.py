#!/usr/bin/python3 -I
"""OpenSSH entry point: accepts only a deployment of one immutable digest."""
import os
import re
import sys


def parse_command(command):
    match = re.fullmatch(r"deploy (sha256:[0-9a-f]{64})", command)
    if not match:
        raise ValueError("Only 'deploy sha256:<64 lowercase hex characters>' is allowed")
    return match.group(1)


def main():
    try:
        digest = parse_command(os.environ.get("SSH_ORIGINAL_COMMAND", ""))
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 64
    os.execv("/usr/bin/sudo", ["sudo", "-n", "/usr/local/sbin/astro-portfolio-deploy", digest])


if __name__ == "__main__":
    sys.exit(main())
