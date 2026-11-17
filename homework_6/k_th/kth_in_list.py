"""Находит k-й по величине элемент в списке."""

import random


def find_kth_largest(lst: list[int], k: int) -> int:
    """Находит k-й по величине элемент в списке."""
    count_pivot = 0
    left, right = [], []
    pivot = random.choice(lst)  # noqa: S311
    for number in lst:
        if number < pivot:
            right.append(number)
        elif number > pivot:
            left.append(number)
        else:
            count_pivot += 1

    length_of_left = len(left)
    if k <= length_of_left:
        return find_kth_largest(left, k)
    if k > length_of_left + count_pivot:
        return find_kth_largest(
            right, k - length_of_left - count_pivot
        )

    return pivot
