import unittest
from ssh_gate import parse_command


class SSHGateTests(unittest.TestCase):
    def test_accepts_only_digest_deployment(self):
        digest = "sha256:" + "a" * 64
        self.assertEqual(parse_command("deploy " + digest), digest)

    def test_rejects_shell_and_protocol_requests(self):
        digest = "sha256:" + "a" * 64
        for command in ("", "bash", "id", "sftp", "scp -t /tmp/a", "deploy latest", "deploy sha256:" + "A" * 64, "deploy " + digest + "; id", "deploy " + digest + "\nid", "deploy " + digest + " ", "deploy " + digest + " --help", "deploy $(id)"):
            with self.subTest(command=command):
                with self.assertRaises(ValueError):
                    parse_command(command)


if __name__ == "__main__":
    unittest.main()
