"""This module contains functions for parsing shell commands from docker history."""


def get_shell() -> str:
    """Return marker for shell, which can be a NOP docker command or shell command."""
    return "/bin/sh -c"


def is_shell(command: str) -> bool:
    """Check if command is shell."""
    return command.startswith(get_shell())


def strip_shell(command: str) -> str:
    """Return command with shell marker removed."""
    return command.removeprefix(get_shell())
