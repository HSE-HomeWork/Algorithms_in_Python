"""Проверка построения минимальной кучи."""

import sys
from collections.abc import Callable
from time import perf_counter

import pytest

from homework_7.makeheap import makeheap, makeheap_n_log_n


def check_heap(arr: list[int]) -> None:
    """Проверить реализации на одном массиве."""
    for build in (makeheap_n_log_n, makeheap):
        result = build(arr.copy())
        assert sorted(result) == sorted(arr)
        for i, value in enumerate(result[1:], start=1):
            parent = (i - 1) // 2
            assert result[parent] <= value


@pytest.mark.parametrize("arr", [[], [7]])
def test_empty_and_single(arr: list[int]) -> None:
    """Проверить пустой массив и единственный элемент."""
    check_heap(arr)


def test_duplicates_and_negatives() -> None:
    """Проверить дубликаты и отрицательные элементы."""
    check_heap([4, -2, 4, 0, -2, 1])


@pytest.mark.parametrize(
    "arr",
    [[1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1]],
)
def test_ordered(arr: list[int]) -> None:
    """Проверить возрастающий и убывающий массивы."""
    check_heap(arr)


def measure(
    build: Callable[[list[int]], list[int]],
    arr: list[int],
) -> float:
    """Измерить построение кучи без копирования массива."""
    data = arr.copy()
    start = perf_counter()
    build(data)
    return perf_counter() - start


def test_performance() -> None:
    """Сравнить минимальное время пяти запусков."""
    arr = list(range(100_000, 0, -1))
    slow = min(measure(makeheap_n_log_n, arr) for _ in range(5))
    fast = min(measure(makeheap, arr) for _ in range(5))
    sys.stdout.write(f"\nO(N log N): {slow:.6f} s\n")
    sys.stdout.write(f"O(N): {fast:.6f} s\n")
