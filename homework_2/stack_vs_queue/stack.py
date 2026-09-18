"""Реализация стека."""

from typing import Any

from homework_2.stack_vs_queue.node import ListNode


class Stack:
    """Реализация стека."""

    def __init__(self, start_head: ListNode | None) -> None:
        """Задаём голову."""
        self.head = start_head

    def push(self, value: Any) -> None:
        """Положить элемент."""
        if self.head is not None:
            new_head = ListNode(value)
            original_head = self.head

            self.head = new_head
            self.head.next = original_head
        else:
            self.head = ListNode(value)

    def pop(self) -> None:
        """Снять верхний элемент."""
        if self.head is not None:
            new_head = self.head.next
            self.head = new_head

    def peek(self) -> Any:
        """Вернуть верхний элемент."""
        if self.head is not None:
            return self.head.val
        return None

    @property
    def stack_as_array(self) -> list[Any]:
        """Преобразовать стек в список."""
        curr = self.head
        out_array = []

        while curr:
            out_array.append(curr.val)
            curr = curr.next
        return out_array
