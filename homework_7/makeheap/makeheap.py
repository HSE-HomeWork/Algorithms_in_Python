"""Произвольный массив arr в minheap за O(N)."""


def shift_down(arr: list[int], i: int, n: int) -> None:
    """Опускаем большее вниз."""
    while i < n // 2:
        smallest = 2 * i + 1
        right = smallest + 1
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if arr[i] <= arr[smallest]:
            break
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        i = smallest


def makeheap(arr: list[int]) -> list[int]:
    """Основная функция."""
    n = len(arr)
    last = n // 2 - 1
    for i in range(last, -1, -1):
        shift_down(arr, i, n)
    return arr
