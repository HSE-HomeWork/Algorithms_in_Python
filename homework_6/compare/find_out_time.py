"""Декоратор замера времени выполнения функции."""

import functools
import time
from collections.abc import Callable


def find_out_time[**P, R](
    func: Callable[P, R],
) -> Callable[P, R]:
    """Декоратор замера времени выполнения функции."""
    depth = 0

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        nonlocal depth
        if depth == 0:
            start_time = time.perf_counter()
            depth += 1
            try:
                return func(*args, **kwargs)
            finally:
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                depth -= 1
                print(  # noqa: T201
                    f"Время в секундах : {execution_time:.6f}"
                )
        else:
            return func(*args, **kwargs)

    return wrapper
