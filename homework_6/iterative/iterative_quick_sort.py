"""Итеративная быстрая сортировка."""

from homework_6.compare.find_out_time import find_out_time


@find_out_time
def quick_sort(arr: list[int]) -> list[int]:
    """Сортирует список итеративным QuickSort."""
    tasks: list[tuple[str, list[int]]] = [("sort", arr.copy())]
    results: list[list[int]] = []

    while tasks:
        operation, current = tasks.pop()

        if operation == "combine":
            right_sorted = results.pop()
            left_sorted = results.pop()
            results.append(left_sorted + current + right_sorted)
            continue

        if len(current) <= 1:
            results.append(current)
            continue

        pivot = current[len(current) // 2]
        left = [number for number in current if number < pivot]
        middle = [
            number for number in current if number == pivot
        ]
        right = [number for number in current if number > pivot]

        tasks.append(("combine", middle))
        tasks.append(("sort", right))
        tasks.append(("sort", left))

    return results[0]
