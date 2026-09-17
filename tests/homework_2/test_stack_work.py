"""Тестирование корректности реализации стека."""

from typing import Any

import pytest

from homework_2.stack_vs_queue import Stack

SIMPLE_ADDED = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
SIMPLE_REVERSE = list(reversed(SIMPLE_ADDED))

MULTI_STACK = ["HSE_IS_TOP", 1, False, True, 12]
MULTI_REVERSE = list(reversed(MULTI_STACK))


@pytest.fixture
def our_stack() -> Stack:
    """Пустой стек на каждый тест."""
    return Stack(start_head=None)


@pytest.mark.parametrize(
    ("pushed", "waiting"),
    [
        pytest.param(SIMPLE_ADDED, SIMPLE_REVERSE, id="simple"),
        pytest.param(
            MULTI_STACK,
            MULTI_REVERSE,
            id="mixed",
        ),
    ],
)
def test_push_order_stack(
    our_stack: Stack,
    pushed: list[Any],
    waiting: list[Any],
) -> None:
    """Проверка последовательности LIFO в стеке."""
    for val in pushed:
        our_stack.push(val)
    assert our_stack.stack_as_array == waiting


@pytest.mark.parametrize(
    ("pushed", "waiting"),
    [
        pytest.param(SIMPLE_REVERSE, 10, id="int"),
        pytest.param(
            MULTI_REVERSE,
            "HSE_IS_TOP",
            id="str",
        ),
    ],
)
def test_up_of_stack(
    our_stack: Stack,
    pushed: list[Any],
    waiting: list[Any],
) -> None:
    """На верху то, что нужно."""
    for value in pushed:
        our_stack.push(value)
    assert our_stack.peek() == waiting


def test_manipulation_with_stack(our_stack: Stack) -> None:
    """Поведение стека при отсутствии head."""
    our_stack.pop()

    assert our_stack.stack_as_array == []
    assert our_stack.peek() is None


def test_hard_behavior(our_stack: Stack) -> None:
    """Нестандартное поведение в стеке."""
    our_stack.push(1)
    our_stack.push(8)
    our_stack.push(10)
    our_stack.push(2)
    our_stack.pop()
    our_stack.pop()
    our_stack.push(111)
    our_stack.push(134)

    assert our_stack.stack_as_array == [134, 111, 8, 1]
