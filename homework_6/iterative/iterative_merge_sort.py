"""Итеративная сортировка слиянием."""

from homework_6.compare.find_out_time import find_out_time


@find_out_time
def merge_sort(arr: list[int]) -> list[int]:
    """Сортирует список итеративным MergeSort."""
    length = len(arr)
    source = arr.copy()
    target = [0] * length
    width = 1

    while width < length:
        for start in range(0, length, 2 * width):
            middle = min(start + width, length)
            end = min(start + 2 * width, length)
            left, right, index = start, middle, start

            while left < middle and right < end:
                if source[left] <= source[right]:
                    target[index] = source[left]
                    left += 1
                else:
                    target[index] = source[right]
                    right += 1
                index += 1

            while left < middle:
                target[index] = source[left]
                left += 1
                index += 1

            while right < end:
                target[index] = source[right]
                right += 1
                index += 1

        source, target = target, source
        width *= 2

    return source
