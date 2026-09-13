"""Решение задачи ."""


def return_number(number: int) -> int:
    """Считает число наоборот в числе."""
    new_number = 0
    while number > 0:
        new_number = new_number * 10 + number % 10
        number //= 10
    return new_number


def is_palindrome(number: int) -> bool:
    """Проверяет является ли число палиндромом."""
    return number == return_number(number)
