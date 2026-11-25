"""Произвольный массив arr в minheap за O(N log N)."""


def shift_up(index: int, arr: list[int]) -> None:
    """Дефолтное просеивание."""
    parent = (index - 1) // 2
    while index > 0 and arr[parent] > arr[index]:
        arr[index], arr[parent] = arr[parent], arr[index]
        index = parent
        parent = (index - 1) // 2


def makeheap_n_log_n(arr: list[int]) -> list[int]:
    """Реализация за O(nlog(n))."""
    for index in range(len(arr)):
        shift_up(index, arr)

    return arr
