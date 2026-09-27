"""Ищем индексы двух элементов, сумма которых равна k."""

from homework_3.hash_table import MyDict


def find_index_of_pair(arr: list[int], k: int) -> list[int]:
    """Основная функция для вывода пар индексов."""
    dictionary = MyDict()

    for index, element in enumerate(arr):
        rev_element = k - element
        if rev_element in dictionary:
            return [dictionary[rev_element], index]
        dictionary[element] = index
    return []
