"""Алгоритм перестановок."""

from homework_5.tracer import trace


def generate_permutations(array: list[int]) -> list[list[int]]:
    """Основная функция генерации перестановок."""
    if len(array) == 1:
        return [array]
    length = len(array)
    old_dict = {}

    for key in array:
        if key not in old_dict:
            old_dict[key] = 1
        else:
            old_dict[key] += 1

    return permutate(old_dict, [], length)


@trace
def permutate(
    new_dict: dict[int, int], row: list[int], length: int
) -> list[list[int]]:
    """Рекурсивная функция генерации перестановок."""
    answer = []
    if len(row) == length:
        return [row.copy()]
    for key, value in new_dict.items():
        if value != 0:
            new_dict[key] -= 1
            row.append(key)
            child = permutate(new_dict, row, length)
            row.pop()
            answer.extend(child)
            new_dict[key] += 1
        else:
            continue
    return answer
