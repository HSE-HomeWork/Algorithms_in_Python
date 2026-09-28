"""Ищем индексы двух элементов, сумма которых равна k."""

from homework_3.hash_table import MyDict


def find_index_of_pair(arr: list[int], k: int) -> list[int]:
    """Основная функция для вывода пар индексов."""
    dictionary = MyDict()

    for index, element in enumerate(arr):
        rev_element = k - element
        pair_index = dictionary.get(rev_element)
        if pair_index is not None:
            return [pair_index, index]
        dictionary[element] = index
    return []
