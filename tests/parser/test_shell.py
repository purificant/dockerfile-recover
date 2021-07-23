"""This module contains test for shell.py"""

from dockerfile_recover.parser.shell import get_shell, is_shell, strip_shell


def test_get_shell():
    """Test that method returns a string."""
    assert isinstance(get_shell(), str)


def test_is_shell():
    """Test that marker is detected."""
    assert is_shell(get_shell() + "test_case") is True
    assert is_shell("test_case") is False


def test_strip_shell():
    """Test that marker is removed from string."""
    test_case = "test_case"
    assert strip_shell(get_shell() + test_case) == test_case
