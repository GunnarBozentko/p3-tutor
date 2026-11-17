"""PreToolUse guard: keep keys/ away from the main conversation.

Claude Code runs this before every Read, Grep, Glob, Bash and PowerShell call
(see the matcher in .claude/settings.json) and sends the call as JSON on stdin.

- A call from a subagent named in ALLOWED_AGENTS (its input carries agent_type)
  goes ahead: exit 0.
- Any other call whose arguments mention a keys/ path is blocked: exit 2, and
  the model reads the message written to stderr.
- Input that cannot be read is blocked too, on purpose, so a malformed call
  never slips through.
"""

import json
import re
import sys

ALLOWED_AGENTS = {"grader"}

# "keys" as a whole path segment: keys/0001.json, ./keys, C:\ws\keys\0001.json,
# "keys" alone (a Grep or Glob path). Not monkeys/ or keys.md.
KEYS_SEGMENT = re.compile(r"(?:^|[^a-z0-9_.-])keys(?:/|$|[\s\"'*;|&)])")

BLOCK_MESSAGE = (
    "Blocked by the keys guard: the main conversation may not read keys/, "
    "where the quizzes' answer keys are. You do not need a key to teach, "
    "tutor or write a quiz, so carry on without it. Grading that needs a key "
    "belongs to the grader subagent, which can read keys/."
)


def strings_in(value):
    """Every string inside a JSON value, at any depth."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings_in(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings_in(item)


def mentions_keys(tool_input):
    for text in strings_in(tool_input):
        normalized = text.replace("\\", "/").lower()
        if KEYS_SEGMENT.search(normalized):
            return True
    return False


def decide(event):
    """Return (exit_code, message) for one hook input."""
    if not isinstance(event, dict):
        return 2, "Blocked by the keys guard: the hook input was not a JSON object."
    agent_type = event.get("agent_type")
    if isinstance(agent_type, str) and agent_type in ALLOWED_AGENTS:
        return 0, ""
    if mentions_keys(event.get("tool_input", {})):
        return 2, BLOCK_MESSAGE
    return 0, ""


def main():
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        event = json.loads(raw)
    except Exception:
        print("Blocked by the keys guard: it could not read the hook input.", file=sys.stderr)
        return 2
    try:
        code, message = decide(event)
    except Exception:
        print("Blocked by the keys guard: it failed while checking this call.", file=sys.stderr)
        return 2
    if message:
        print(message, file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
