"""The tutor's keys guard (tutor/.claude/hooks/keys_guard.py).

Each test runs the guard the way Claude Code does: as a subprocess with the PreToolUse hook input
as JSON on stdin. Exit 0 lets the tool call run; exit 2 blocks it, with a message on stderr.

The main conversation's hook input has no agent_type; a subagent's carries agent_type (its name)
and an agent_id. The tests check that the guard blocks the main conversation's reads of keys/ with
Read, Grep, Glob, Bash and PowerShell, allows the grader's, and allows the main conversation's
other reads.
"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

GUARD = Path(__file__).resolve().parent.parent / "tutor" / ".claude" / "hooks" / "keys_guard.py"
GRADER = "grader"


def run_guard(payload: dict) -> tuple[int, str]:
    """Run the guard with payload as JSON on stdin, returning (exit code, stderr)."""
    proc = subprocess.run(
        [sys.executable, str(GUARD)],
        input=json.dumps(payload), capture_output=True, text=True,
    )  # fmt: skip
    return proc.returncode, proc.stderr


def call(tool_name: str, agent: str | None = None, **tool_input) -> dict:
    """A PreToolUse hook input; agent=None is the main conversation."""
    data = {
        "hook_event_name": "PreToolUse",
        "session_id": "test-session",
        "tool_name": tool_name,
        "tool_input": tool_input,
    }
    if agent is not None:
        data["agent_type"] = agent
        data["agent_id"] = f"{agent}-0001"
    return data


# Reads of keys/, one list per tool, in the forms a tutor might use.
KEY_READS = {
    "Read": [
        call("Read", file_path="keys/0001.json"),
        call("Read", file_path="./keys/0001.json"),
        call("Read", file_path="C:\\ws\\tutor\\keys\\0001.json"),
        call("Read", file_path="/home/student/ws/keys/0001.json"),
    ],
    "Grep": [
        call("Grep", pattern="answer", path="keys"),
        call("Grep", pattern="answer", path="keys/0001.json"),
        call("Grep", pattern="correct", path="C:\\ws\\tutor\\keys"),
    ],
    "Glob": [
        call("Glob", pattern="keys/*.json"),
        call("Glob", pattern="*.json", path="keys"),
        call("Glob", pattern="**/keys/*"),
    ],
    "Bash": [
        call("Bash", command="cat keys/0001.json"),
        call("Bash", command="ls keys"),
        call("Bash", command="grep -r answer ./keys/"),
        call("Bash", command="head -n 20 'keys/0001.json'"),
    ],
    "PowerShell": [
        call("PowerShell", command="Get-Content keys\\0001.json"),
        call("PowerShell", command="Get-ChildItem .\\keys"),
        call("PowerShell", command='Get-Content "C:\\ws\\tutor\\keys\\0001.json"'),
    ],
}

# The main conversation's ordinary reads, which the guard must let through.
OTHER_READS = [
    call("Read", file_path="lessons/01-intro.md"),
    call("Read", file_path="quizzes/0001.md"),
    call("Read", file_path="NOTES.md"),
    call("Read", file_path="MISSION.md"),
    call("Read", file_path="C:\\ws\\tutor\\submissions\\0001.md"),
    call("Grep", pattern="random forest", path="lessons"),
    call("Glob", pattern="quizzes/*.md"),
    call("Bash", command="ls lessons quizzes"),
    call("Bash", command="cat NOTES.md"),
    call("PowerShell", command="Get-ChildItem lessons"),
    call("PowerShell", command="Get-Content quizzes\\0001.md"),
    # Names that contain "keys" but are not the keys/ folder.
    call("Read", file_path="monkeys/notes.md"),
    call("Read", file_path="keys.md"),
]


class KeysGuardTests(unittest.TestCase):
    def assertBlocked(self, payload: dict) -> None:
        code, err = run_guard(payload)
        self.assertEqual(code, 2, f"expected a block for {payload['tool_input']!r}")
        self.assertIn("keys guard", err, "a block must tell the model why on stderr")

    def assertAllowed(self, payload: dict) -> None:
        code, err = run_guard(payload)
        self.assertEqual(code, 0, f"expected allow for {payload['tool_input']!r}: {err}")
        self.assertEqual(err, "", "an allowed call must say nothing on stderr")

    def test_guard_script_exists(self):
        self.assertTrue(GUARD.is_file(), f"no guard script at {GUARD}")

    def test_main_conversation_blocked_from_keys_with_every_tool(self):
        for tool_name, payloads in KEY_READS.items():
            for payload in payloads:
                with self.subTest(tool=tool_name, tool_input=payload["tool_input"]):
                    self.assertNotIn("agent_type", payload)
                    self.assertBlocked(payload)

    def test_grader_allowed_to_read_keys_with_every_tool(self):
        for tool_name, payloads in KEY_READS.items():
            for payload in payloads:
                grader_payload = call(tool_name, agent=GRADER, **payload["tool_input"])
                with self.subTest(tool=tool_name, tool_input=payload["tool_input"]):
                    self.assertAllowed(grader_payload)

    def test_main_conversation_allowed_other_reads(self):
        for payload in OTHER_READS:
            with self.subTest(tool=payload["tool_name"], tool_input=payload["tool_input"]):
                self.assertAllowed(payload)


if __name__ == "__main__":
    unittest.main()
