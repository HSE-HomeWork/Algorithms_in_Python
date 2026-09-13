"""Тесты на количество простых чисел."""

from hypothesis import given
from hypothesis import strategies as st

from homework_1.prime import eratosfen_sieve

HM_EX_1 = 10
HM_EX_2 = 1

MAX_N = 300
FIRST_PRIME = 2


def test_hm_numbers() -> None:
    """Поиск суммы в пустом массиве."""
    answer_1 = 4
    answer_2 = 0
    assert eratosfen_sieve(HM_EX_1) == answer_1
    assert eratosfen_sieve(HM_EX_2) == answer_2


def count_primes_naive(limit: int) -> int:
    """Считает простые перебором делителей."""
    total = 0
    for candidate in range(FIRST_PRIME, limit):
        divisor = FIRST_PRIME
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                break
            divisor += 1
        else:
            total += 1
    return total


@given(st.integers(min_value=0, max_value=MAX_N))
def test_matches_naive(number: int) -> None:
    """Совпадает с перебором делителей."""
    assert eratosfen_sieve(number) == count_primes_naive(number)


@given(st.integers(min_value=0, max_value=MAX_N))
def test_grows_by_zero_or_one(number: int) -> None:
    """Переход к number + 1 добавляет не больше одного."""
    growth = eratosfen_sieve(number + 1) - eratosfen_sieve(
        number
    )
    assert growth in {0, 1}
