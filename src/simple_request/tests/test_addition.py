import pytest
from src.simple_request.addition import add

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_mixed_sign_numbers():
    assert add(-1, 5) == 4

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -5) == -5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_strings():
    # Python's + operator also concatenates strings
    assert add("hello ", "world") == "hello world"