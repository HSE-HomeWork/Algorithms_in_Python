"""Решение задачи на валидацию pop/push."""

from homework_2.stack_vs_queue import Stack


def handle_arrays(pushed: list[int], popped: list[int]) -> bool:
    """Основной алгоритм."""
    length = len(popped)
    point_pop = 0
    our_stack = Stack(start_head=None)

    for i in range(length):
        our_stack.push(pushed[i])
        while (
            point_pop < length
            and our_stack.peek() == popped[point_pop]
        ):
            our_stack.pop()
            point_pop += 1

    return our_stack.peek() is None


def result_push_pop_stack(
    pushed: list[int], popped: list[int]
) -> bool:
    """Результирующая функция."""
    if len(pushed) != len(popped):
        return False
    return handle_arrays(pushed=pushed, popped=popped)
