"""Всё про AVL-дерево."""

from dataclasses import dataclass


@dataclass
class AVLNode:
    """Узел AVL-дерева."""

    val: int
    left: "AVLNode | None" = None
    right: "AVLNode | None" = None
    height: int = 1


class AVLTree:
    """Класс AVL-дерева."""

    def __init__(self) -> None:
        """Корень."""
        self.root: AVLNode | None = None

    def search(self, search_val: int) -> bool:
        """Операция поиска."""
        curr: AVLNode | None = self.root
        while curr is not None:
            if search_val == curr.val:
                return True
            if search_val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, new_val: int) -> None:
        """Операция вставки."""
        self.root = self._insert(self.root, new_val)

    def delete(self, del_val: int) -> None:
        """Операция удаления."""
        self.root = self._delete(self.root, del_val)

    def _insert(self, node: AVLNode | None, val: int) -> AVLNode:
        """Рекурсивная функция вставки."""
        if node is None:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node
        return self._rebalance(node)

    def _delete(
        self, node: AVLNode | None, val: int
    ) -> AVLNode | None:
        """Рекурсивная функция удаления."""
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return self._rebalance(node)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """Пересчёт высоты и повороты при перекосе."""
        self._update_height(node)
        balance = self._balance(node)
        if balance > 1:
            if (
                node.left is not None
                and self._balance(node.left) < 0
            ):
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if (
                node.right is not None
                and self._balance(node.right) > 0
            ):
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """Правый поворот, левый ребёнок становится корнем."""
        new_root = node.left
        if new_root is None:
            return node
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """Левый поворот, правый ребёнок становится корнем."""
        new_root = node.right
        if new_root is None:
            return node
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _update_height(self, node: AVLNode) -> None:
        """Высота по детям."""
        node.height = 1 + max(
            self._height(node.left), self._height(node.right)
        )

    def _balance(self, node: AVLNode | None) -> int:
        """Высота левого минус высота правого."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    @staticmethod
    def _height(node: AVLNode | None) -> int:
        return node.height if node else 0

    @staticmethod
    def _min_value_node(node: AVLNode) -> AVLNode:
        """Самый левый узел поддерева."""
        while node.left is not None:
            node = node.left
        return node
