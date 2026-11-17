"""Рекурсивная сортировка слиянием."""

from homework_6.compare.find_out_time import find_out_time


@find_out_time
def merge_sort(arr: list[int]) -> list[int]:
    """Рекурсивная merge-сортировка."""
    if len(arr) <= 1:
        return arr
    v = len(arr) // 2
    left = merge_sort(arr[:v])
    right = merge_sort(arr[v:])
    new_arr = []
    x, y = 0, 0
    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            new_arr.append(left[x])
            x += 1
        else:
            new_arr.append(right[y])
            y += 1
    return new_arr + left[x:] + right[y:]
