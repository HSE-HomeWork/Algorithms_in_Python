"""Реализация ListNode."""

from typing import Any


class ListNode:
    """Узел в списке."""

    def __init__(self, value: Any) -> None:
        """Базовая инициализация."""
        self.val = value
        self.next: ListNode | None = None
