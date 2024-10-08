# tests/test_is_unique.py
import pytest
from src.c01_arrays_and_strings.is_unique import is_unique  # type: ignore


def test_is_unique_all_unique():
    assert is_unique("abcdef")


def test_is_unique_with_duplicates():
    assert not is_unique("aabcdef")


def test_is_unique_empty_string():
    assert is_unique("")


def test_is_unique_single_char():
    assert is_unique("a")


def test_is_unique_special_chars():
    assert is_unique("abc!@#")


if __name__ == "__main__":
    pytest.main()
