"""This module contains functions for parsing NOP commands from docker history."""


def get_nop() -> str:
    """Return marker for NOP, which represents a docker command."""
    return "/bin/sh -c #(nop)"


def is_nop(command: str) -> bool:
    """Check if command is NOP."""
    return command.startswith(get_nop())


def strip_nop(command: str) -> str:
    """Return command with NOP marker removed."""
    return command.removeprefix(get_nop())
