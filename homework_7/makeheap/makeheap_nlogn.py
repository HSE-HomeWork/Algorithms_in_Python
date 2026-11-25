"""Произвольный массив arr в minheap за O(N log N)."""


def shift_up(index: int, arr: list[int]) -> None:
    """Поднимаем меньшее вверх."""
    parent = (index - 1) // 2
    while index > 0 and arr[parent] > arr[index]:
        temp = arr[index]
        arr[index] = arr[parent]
        arr[parent] = temp
        index = parent
        parent = (index - 1) // 2


def makeheap_n_log_n(arr: list[int]) -> list[int]:
    """Реализация за O(N log N)."""
    n = len(arr)
    for index in range(1, n):
        shift_up(index, arr)
    return arr
