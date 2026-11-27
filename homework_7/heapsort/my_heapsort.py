"""Делаем эту грязючку."""

from homework_7.makeheap import makeheap, shift_down


def heapsort(nums: list[int]) -> list[int]:
    """Вообщем решил делать через minheap."""
    arr = makeheap(arr=nums)
    n = len(arr) - 1
    for i in range(n, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        shift_down(arr=arr, i=0, n=i)
    arr.reverse()
    return arr
