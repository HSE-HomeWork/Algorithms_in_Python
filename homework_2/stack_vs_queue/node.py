"""Реализация ListNode."""

from typing import Any


class ListNode:
    """Узел в списке."""

    def __init__(self, value: Any) -> None:
        """Базовая инициализация."""
        self.val = value
        self.next: ListNode | None = None

    def make_linked_list(
        self, massive: list[Any]
    ) -> "ListNode" | None:  # noqa: TC010
        """Создание LinkedList из списка."""
        start = ListNode(value=None)
        linked_list = start
        for element in massive:
            start.next = ListNode(value=element)
            start = start.next
        return linked_list.next
