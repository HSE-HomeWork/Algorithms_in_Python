"""А я самный умный."""

from homework_7.makeheap import makeheap, shift_down


def kth_without_heap(nums: list[int], k: int) -> int:
    """Алгоритм без кучи."""
    new_nums: list[int] = makeheap(nums[:k])
    n = len(nums)
    for i in range(k, n):
        element = nums[i]
        if element > new_nums[0]:
            new_nums[0] = element
            shift_down(new_nums, i=0, n=k)
    return new_nums[0]
