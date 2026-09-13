"""Решение задачи на подсчёт простых чисел."""


def algorithm_eratosthena(number: int) -> int:
    """Реализация решета Эратосфена.

    Заводим массив флагов, где индекс соответствует числу,
    и последовательно помечает кратные каждого найденного
    простого как составные.

    Args:
        number: верхняя граница, не включается в подсчёт.

    Returns:
        Количество простых чисел, строго меньших number.

    """
    answer = 0
    prime_numbers = [True for _ in range(number)]
    for cell in range(2, number):
        if prime_numbers[cell]:
            answer += 1
            simple = cell
            while simple < number:
                prime_numbers[simple] = False
                simple += cell
    return answer


def eratosthen_sieve(number: int) -> int:
    """Обрабатывающая функция."""
    min_simple_number = 2
    if number < min_simple_number:
        return 0
    return algorithm_eratosthena(number)
