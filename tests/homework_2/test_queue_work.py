"""Тестирование очереди ."""

from collections import deque
from typing import Any

import pytest

from homework_2.stack_vs_queue import Queue

SIMPLE_CASE = list(range(11))
MULTI_CASE = [[12], 1, "AVITO"]


@pytest.fixture
def queue() -> Queue:
    """Пустая очередь."""
    return Queue(top=None, tail=None)


@pytest.mark.parametrize(
    ("pushed", "tail", "top"),
    [
        pytest.param(SIMPLE_CASE, 10, 0, id="straight-int"),
        pytest.param(MULTI_CASE, "AVITO", [12], id="multi"),
    ],
)
def test_top_tail_queue(
    queue: Queue,
    pushed: list[Any],
    tail: Any,
    top: Any,
) -> None:
    """Проверка головы и хвоста."""
    for val in pushed:
        queue.enqueue(val)
    assert queue.reverse_peek() == tail
    assert queue.peek() == top


def test_manipulate_queue(queue: Queue) -> None:
    """Проверка манипуляций над очередью."""
    waiting_arr = ["Alpha", 67, [11]]

    queue.enqueue(12)
    queue.enqueue(52)
    queue.silent_dequeue()
    queue.enqueue("Alpha")
    queue.enqueue(67)
    queue.silent_dequeue()
    queue.enqueue([11])

    assert waiting_arr == queue.array_perform
    assert queue.peek() == "Alpha"


@pytest.mark.parametrize(
    ("case"),
    [
        pytest.param(SIMPLE_CASE, id="straight-int"),
        pytest.param(MULTI_CASE, id="multi"),
    ],
)
def test_my_with_collections(
    queue: Queue, case: list[Any]
) -> None:
    """Сравнение относительно встроенной collections."""
    standart: deque[Any] = deque()

    for some in case:
        queue.enqueue(some)
        standart.append(some)
    for _ in case:
        queue.silent_dequeue()
        standart.popleft()
    for some in case:
        queue.enqueue(some)
        standart.append(some)

    first_el_collection = standart.popleft()
    first_my_queue = queue.dequeue()

    assert first_el_collection == first_my_queue
    assert queue.array_perform == list(standart)
