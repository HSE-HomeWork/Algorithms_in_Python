"""Рекурсивная быстрая сортировка."""

import random

from homework_6.compare.find_out_time import find_out_time


@find_out_time
def quick_sort(arr: list[int]) -> list[int]:
    """Рекурсивная quicksort."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # noqa: S311
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
