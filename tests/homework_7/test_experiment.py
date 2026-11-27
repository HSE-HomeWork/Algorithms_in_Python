"""Сравнение времени работы трёх сортировок."""

import sys
from collections.abc import Callable
from statistics import median
from time import perf_counter

import pytest

from homework_6.compare import merge_sort
from homework_7.heapsort import heapsort


def measure(
    sort: Callable[[list[int]], list[int] | None],
    nums: list[int],
) -> float:
    """Получить медиану пяти замеров в миллисекундах."""
    samples: list[float] = []
    for _ in range(5):
        data = nums.copy()
        start = perf_counter()
        result = sort(data)
        samples.append(perf_counter() - start)
        if result is None:
            result = data
        assert result == sorted(nums)
    return median(samples) * 1000


@pytest.mark.parametrize("size", [1000, 10_000, 50_000])
def test_performance(size: int) -> None:
    """Сравнить сортировки на одинаковых массивах."""
    stop = size * 7919
    nums = [value % size for value in range(0, stop, 7919)]
    heap_time = measure(heapsort, nums)
    merge_time = measure(merge_sort, nums)
    builtin_time = measure(sorted, nums)
    sys.stdout.write(f"\nN = {size}; время в мс\n")
    sys.stdout.write(f"heapsort: {heap_time:.3f}\n")
    sys.stdout.write(f"merge_sort: {merge_time:.3f}\n")
    sys.stdout.write(f"sorted: {builtin_time:.3f}\n")
