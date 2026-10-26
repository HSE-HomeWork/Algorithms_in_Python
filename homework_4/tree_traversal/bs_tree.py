"""Реализация BST и операции вставки - первое задание."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator


class TreeNode:
    """Узел дерева."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        """Инициализируем узелок."""
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    """Дефолтное бинарное дерево поиска."""

    def __init__(self) -> None:
        """Корень."""
        self.root: TreeNode | None = None

    def insert(self, new_val: int) -> None:
        """Операция вставки."""
        if self.root is None:
            self.root = TreeNode(val=new_val)
            return
        curr = self.root

        while curr:
            if curr.val > new_val:
                if curr.left is None:
                    curr.left = TreeNode(val=new_val)
                    break
                curr = curr.left
            elif curr.right is None:
                curr.right = TreeNode(val=new_val)
                break
            else:
                curr = curr.right

    def pre_order(self) -> list[int]:
        """Вывод в порядке NLR."""
        return list(self._travel_tree(self.root, "NLR"))

    def in_order(self) -> list[int]:
        """Вывод в порядке LNR."""
        return list(self._travel_tree(self.root, "LNR"))

    def post_order(self) -> list[int]:
        """Вывод в порядке LRN."""
        return list(self._travel_tree(self.root, "LRN"))

    def reverse_pre_order(self) -> list[int]:
        """Вывод в порядке NRL."""
        return list(self._travel_tree(self.root, "NRL"))

    def reverse_in_order(self) -> list[int]:
        """Вывод в порядке RNL."""
        return list(self._travel_tree(self.root, "RNL"))

    def reverse_post_order(self) -> list[int]:
        """Вывод в порядке RLN."""
        return list(self._travel_tree(self.root, "RLN"))

    def _travel_tree(
        self, node: TreeNode | None, order: str
    ) -> Iterator[int]:
        """Конструктор обхода дерева.

        Order тут - это перестановка букв N, L, R ,
        которая рекурсивно применяется к каждому узлу.
        """
        if node is None:
            return
        our_way: dict[str, Callable[[], Iterable[int]]] = {
            "N": lambda: (node.val,),
            "L": lambda: self._travel_tree(node.left, order),
            "R": lambda: self._travel_tree(node.right, order),
        }
        for task in order:
            yield from our_way[task]()
