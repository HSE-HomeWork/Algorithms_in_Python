"""Реализация ListNode."""

from __future__ import annotations

from typing import Any


class ListNode:
    """Узел в списке."""

    def __init__(self, value: Any) -> None:
        """Базовая инициализация."""
        self.val = value
        self.next: ListNode | None = None

    @classmethod
    def make_linked_list(
        cls, massive: list[Any]
    ) -> ListNode | None:
        """Создание LinkedList из списка."""
        start = ListNode(value=None)
        linked_list = start
        for element in massive:
            start.next = ListNode(value=element)
            start = start.next
        return linked_list.next

    @classmethod
    def to_list(cls, node: ListNode | None) -> list[Any]:
        """Из LinkedList в список."""
        answer = []
        curr = node
        while curr:
            answer.append(curr.val)
            curr = curr.next
        return answer
