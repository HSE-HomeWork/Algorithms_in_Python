"""Решение задачи на сумму ."""


def search_for_uneven(
    array: list[int],
) -> tuple[int, int | None]:
    """Подсчёт суммы массива и поиск мин-нечёт."""
    find_sum = 0
    uneven = None
    for number in array:
        find_sum += number
        if number % 2 != 0:
            if uneven is None:
                uneven = number
            else:
                uneven = min(number, uneven)
    return find_sum, uneven


def max_even_sum_array(array: list[int]) -> int:
    """Проверка условия четности и наоборот."""
    pre_sum, min_uneven = search_for_uneven(array)

    if pre_sum % 2 == 0 or min_uneven is None:
        return pre_sum
    return pre_sum - min_uneven
