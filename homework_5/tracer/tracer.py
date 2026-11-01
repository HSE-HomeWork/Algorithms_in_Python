"""Декоратор, показывающий стек вызовов рекурсивных функций."""

import functools
from collections.abc import Callable


def trace[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Декоратор: вход, отступ и возврат рекурсии."""
    counter = 0

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        """Обертка для функции, которая выводит стек вызовов."""
        nonlocal counter
        if counter == 0:
            print(f"Вход в {func.__name__}")
        space = "-" * counter + " "
        print(f"{space}Текущий уровень рекурсии: {counter}")
        counter += 1
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"{space}Ошибка в {func.__name__}: {e}")
            raise
        finally:
            counter -= 1
        print(f"{space}Возврат из {func.__name__} : {result}")
        return result

    return wrapper
