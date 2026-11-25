"""Произвольный массив arr в minheap за O(N)."""


def shift_down(arr: list[int], i: int, n: int) -> None:
    """Опускаем большее вниз."""
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap(arr: list[int]) -> list[int]:
    """Основная функция."""
    for i in range(len(arr) // 2 - 1, -1, -1):
        shift_down(arr, i, len(arr))
    return arr
