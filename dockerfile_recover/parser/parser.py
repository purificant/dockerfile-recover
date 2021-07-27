"""This module contains functions for extracting information from docker history."""

from .exceptions import ExpectingAShellCommand
from .nop import is_nop, strip_nop
from .shell import get_shell, is_shell, strip_shell


def parse_history(history: list) -> list:
    """Return reconstructed Dockerfile based on docker history."""
    return [parse_history_created_by(line["CreatedBy"]) for line in history]


def parse_history_created_by(created_by: str):
    """Parse 'CreatedBy' part of docker history and return command ran for that layer."""

    # current assumption is that all docker commands run shell, which can be NOP
    if not is_shell(created_by):
        raise ExpectingAShellCommand(
            f"Expecting '{created_by}' to contain '{get_shell}' but it does not."
        )

    if is_nop(created_by):
        created_by = strip_nop(created_by).strip()
    else:
        created_by = "RUN " + strip_shell(created_by).strip()

    return created_by
