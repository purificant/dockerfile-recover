"""This module contains exceptions."""


class ParseException(Exception):
    """Base exception for all parsing errors."""


class ExpectingAShellCommand(ParseException):
    """
    Raised when docker histor command does not contain shell marker.
    The current assumption is that this never happens.
    """
