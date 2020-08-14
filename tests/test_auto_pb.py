"""Tests functions in auto-pb.py using PyTests."""

# import pytest
from tests.tud_test_base import set_keyboard_input
import auto_pb


def test_get_names():
    set_keyboard_input(["test_1", "Raj Dholakia"])
    names_tup = auto_pb.get_names()

    assert names_tup == ("test_1", "Raj Dholakia")
