"""Алгоритм перестановок."""

from collections import Counter

from homework_5.tracer import trace


def generate_permutations(array: list[int]) -> list[list[int]]:
    """Основная функция генерации перестановок."""
    return permutate(Counter(array), [], len(array))


@trace
def permutate(
    new_dict: dict[int, int],
    row: list[int],
    length: int,
) -> list[list[int]]:
    """Рекурсивная функция генерации перестановок."""
    if len(row) == length:
        return [row.copy()]
    answer: list[list[int]] = []
    for key, count in new_dict.items():
        if count:
            new_dict[key] -= 1
            row.append(key)
            answer.extend(permutate(new_dict, row, length))
            row.pop()
            new_dict[key] += 1
    return answer
