# test_app.py

from app import double_number


def test_double_number():
    assert double_number(2) == 4


def test_double_negative_number():
    assert double_number(-3) == -6


def test_double_zero():
    assert double_number(0) == 0
