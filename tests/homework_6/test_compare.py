"""Сравнение времени работы MergeSort и QuickSort."""

from homework_6.compare.merge_sort import merge_sort
from homework_6.compare.quick_sort import quick_sort


def test_degenerate_quick_sort() -> None:
    """Проверяет сортировки на худшем случае для QuickSort."""
    arr = [0]
    for size in range(2, 301):
        arr.insert(size // 2, -size)

    expected = sorted(arr)

    assert merge_sort(arr.copy()) == expected
    assert quick_sort(arr.copy()) == expected


def test_equal_elements() -> None:
    """Проверяет сортировки на массиве одинаковых элементов."""
    arr = [7] * 30_000

    assert merge_sort(arr.copy()) == arr
    assert quick_sort(arr.copy()) == arr
