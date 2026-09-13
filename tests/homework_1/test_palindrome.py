"""Тестирование палиндрома."""

from hypothesis import given
from hypothesis import strategies as st

from homework_1.palindrome import is_palindrome

FIRST_GOOD_NUMBER = 121
SECOND_GOOD_NUMBER = 10201

FIRST_BAD_NUMBER = 1010
SECOND_BAD_NUMBER = 31

SIMPLE_NUMBER = 5


def test_simple_case() -> None:
    """Однозначное пал-число."""
    assert is_palindrome(SIMPLE_NUMBER)


def test_good_case() -> None:
    """Удачное пал-число."""
    assert is_palindrome(FIRST_GOOD_NUMBER)
    assert is_palindrome(SECOND_GOOD_NUMBER)


def test_bad_case() -> None:
    """Неудачное пал-число."""
    assert not is_palindrome(FIRST_BAD_NUMBER)
    assert not is_palindrome(SECOND_BAD_NUMBER)


@given(st.integers(min_value=1))
def test_matches_string_reversal(number: int) -> None:
    """Генеративный тест, проверка через строку."""
    digits = str(number)
    assert is_palindrome(number) == (digits == digits[::-1])
