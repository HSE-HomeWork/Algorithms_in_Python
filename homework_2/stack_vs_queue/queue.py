"""Реализация очереди."""

from typing import Any

from .node import ListNode


class Queue:
    """Собственно сам класс очереди."""

    def __init__(
        self, top: ListNode | None, tail: ListNode | None
    ) -> None:
        """Задаём голову и хвост."""
        self.top = top
        self.tail = tail

    def enqueue(self, value: Any) -> None:
        """Добавить в конец элемент."""
        if self.tail is not None:
            new_tail = ListNode(value)
            self.tail.next = new_tail
            self.tail = new_tail
        elif self.top is None:
            self.top = ListNode(value)
            self.tail = self.top

    def silent_dequeue(self) -> None:
        """Забрать из начала не вернув."""
        if self.top is not None:
            self.top = self.top.next
            if self.top is None:
                self.tail = None

    def dequeue(self) -> Any:
        """Забрать из начала вернув."""
        if self.top is not None:
            old = self.top.val
            self.top = self.top.next
            if self.top is None:
                self.tail = None
            return old
        return None

    def peek(self) -> Any:
        """Посмотреть первый элемент."""
        if self.top is not None:
            return self.top.val
        return None

    def reverse_peek(self) -> Any:
        """Посмотреть последний элемент."""
        if self.tail is not None:
            return self.tail.val
        return None

    @property
    def array_perform(self) -> list[Any]:
        """Преобразовать очередь в список."""
        curr = self.top
        out_array = []

        while curr:
            out_array.append(curr.val)
            curr = curr.next
        return out_array
