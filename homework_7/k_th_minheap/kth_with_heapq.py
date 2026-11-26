"""kuchka budet tut)."""

import heapq


def kth_with_heapq(nums: list[int], k: int) -> int:
    """Алгоритмы идентичные."""
    heap: list[int] = nums[:k]
    heapq.heapify(heap)
    n = len(nums)
    for i in range(k, n):
        if heap[0] < nums[i]:
            heapq.heappushpop(heap, nums[i])
    return heap[0]
