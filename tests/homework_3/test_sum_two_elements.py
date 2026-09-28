"""Тесты для поиска пары индексов суммой k."""

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from homework_3.two_sum import find_index_of_pair

numbers = st.lists(st.integers(-1000, 1000), max_size=20)
number = st.integers(-1000, 1000)


@pytest.mark.parametrize(
    ("arr", "k", "expected"),
    [
        ([1, 3, 4, 10], 7, [1, 2]),
        ([5, 5, 1, 4], 10, [0, 1]),
        ([-3, 8, 2], -1, [0, 2]),
        ([0, 7, 0], 0, [0, 2]),
        ([2, 9], 11, [0, 1]),
    ],
)
def test_known_cases(
    arr: list[int], k: int, expected: list[int]
) -> None:
    """Примеры из условия, отрицательные, нули и дубли."""
    assert find_index_of_pair(arr, k) == expected


@pytest.mark.parametrize(
    ("arr", "k"),
    [([], 5), ([5], 10), ([1, 2, 3], 100)],
)
def test_no_pair(arr: list[int], k: int) -> None:
    """Если пары нет, возвращается пустой список."""
    assert find_index_of_pair(arr, k) == []


@settings(max_examples=500)
@given(numbers, number, numbers, number)
def test_found_pair_is_valid(
    left: list[int], a: int, middle: list[int], b: int
) -> None:
    """Найденные индексы идут по возрастанию и дают сумму k."""
    arr = [*left, a, *middle, b]
    k = a + b

    first, second = find_index_of_pair(arr, k)

    assert first < second
    assert arr[first] + arr[second] == k
