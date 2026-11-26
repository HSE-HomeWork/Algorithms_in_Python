"""Test на два ТАМОШНИХ алгоритма хы."""

from itertools import product

import pytest

from homework_7.k_th_minheap import (
    kth_with_heapq,
    kth_without_heap,
)

LARGE = 10**100


def check_result(nums: list[int], k: int, expected: int) -> None:
    """Check both algorithms and preserve the original input."""
    for find in (kth_without_heap, kth_with_heapq):
        data = nums.copy()
        assert find(data, k) == expected
        assert data == nums


def check_all_ranks(nums: list[int]) -> None:
    """Compare every valid rank against a sorted reference."""
    reference = sorted(nums, reverse=True)
    for k, expected in enumerate(reference, start=1):
        check_result(nums, k, expected)


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7], 1, 7),
        ([0], 1, 0),
        ([-7], 1, -7),
        ([1, 100], 1, 100),
        ([100, 1], 2, 1),
        ([9, 1, 2, 100, 0], 3, 2),
        ([1, 2, 3, 100, 0], 3, 2),
        ([5, 5, 5, 4, 4], 3, 5),
        ([-9, -2, -3, -2, -10], 2, -2),
        ([0, -1, 1, 0], 3, 0),
        ([LARGE, 0, -LARGE], 2, 0),
    ],
)
def test_corner_cases(
    nums: list[int],
    k: int,
    expected: int,
) -> None:
    """Check boundaries, duplicates and large integers."""
    check_result(nums, k, expected)


@pytest.mark.parametrize(
    "nums",
    [
        list(range(32)),
        list(range(32, 0, -1)),
        [7] * 32,
        [0, -1] * 16,
        [50, 1, 40, 2, 30, 3, 20, 4, 10],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 100],
    ],
)
def test_all_ranks(nums: list[int]) -> None:
    """Check all ranks on arrays with different structures."""
    check_all_ranks(nums)


def test_exhaustive() -> None:
    """Check every short array over three integer values."""
    for size in range(1, 9):
        for values in product((-1, 0, 1), repeat=size):
            check_all_ranks(list(values))


@pytest.mark.parametrize(
    "nums",
    [
        list(range(10_000)),
        list(range(10_000, 0, -1)),
        [i % 17 for i in range(10_000)],
    ],
)
def test_large_arrays(nums: list[int]) -> None:
    """Check small, middle and large ranks on large arrays."""
    reference = sorted(nums, reverse=True)
    for k in (1, 2, 5_000, 9_999, 10_000):
        check_result(nums, k, reference[k - 1])
