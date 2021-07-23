"""This module contains tests for nop.py"""

from dockerfile_recover.parser.nop import get_nop, is_nop, strip_nop


def test_get_nop():
    """Test that method returns a string."""
    assert isinstance(get_nop(), str)


def test_is_nop():
    """Test that marker is detected."""
    assert is_nop(get_nop() + "test_case") is True
    assert is_nop("test_case") is False


def test_strip_nop():
    """Test than marker is removed from string."""
    test_case = "test_case"
    assert strip_nop(get_nop() + test_case) == test_case
