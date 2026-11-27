"""Проверка корректности и сортировки на месте."""

from itertools import product

import pytest

from homework_7.heapsort import heapsort

LARGE = 10**100


def check_sort(nums: list[int]) -> None:
    """Сравнить результат встроенной сортировкой."""
    data = nums.copy()
    expected = sorted(nums)
    result = heapsort(data)
    assert result is data
    assert data == expected


def mixed_values(size: int) -> list[int]:
    """Сформировать воспроизводимую перестановку чисел."""
    step = 7919
    stop = size * step
    values = range(0, stop, step)
    return [value % size for value in values]


@pytest.mark.parametrize(
    "nums",
    [
        [],
        [0],
        [-1],
        [1, 2],
        [2, 1],
        [2, 2],
        [3, 1, 2],
        [1, 5, 4, 8, 10],
        [-9, -2, -3, -2, -10],
        [0, -1, 1, 0, -1],
        [5, 5, 5, 5],
        [LARGE, 0, -LARGE, LARGE],
    ],
)
def test_corner_cases(nums: list[int]) -> None:
    """Проверить пустые массивы, дубликаты и большие числа."""
    check_sort(nums)


@pytest.mark.parametrize(
    "size",
    [7, 8, 9, 15, 16, 17, 31, 32, 33, 63, 64, 65],
)
def test_heap_boundaries(size: int) -> None:
    """Проверить размеры кучи около степеней двойки."""
    check_sort(mixed_values(size))


def test_exhaustive() -> None:
    """Перебрать все короткие массивы из трёх значений."""
    for size in range(9):
        for values in product((-1, 0, 1), repeat=size):
            check_sort(list(values))


@pytest.mark.parametrize(
    "nums",
    [
        list(range(10_000)),
        list(range(10_000, 0, -1)),
        list((7,) * 10_000),
        list((0, -1) * 5_000),
        [i % 17 for i in range(10_000)],
        mixed_values(10_000),
    ],
)
def test_large_arrays(nums: list[int]) -> None:
    """Проверить большие массивы разных видов."""
    check_sort(nums)


def test_repeated_sort() -> None:
    """Проверить повторную сортировку того же списка."""
    nums = [8, 3, 5, 1, 3]
    expected = sorted(nums)
    assert heapsort(nums) is nums
    assert heapsort(nums) is nums
    assert nums == expected
