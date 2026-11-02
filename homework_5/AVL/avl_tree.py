"""Всё про AVL-дерево."""

from dataclasses import dataclass


def _height(node: "AVLNode | None") -> int:
    """Высота, пустое поддерево даёт 0."""
    return node.height if node else 0


@dataclass
class AVLNode:
    """Узел AVL-дерева."""

    val: int
    left: "AVLNode | None" = None
    right: "AVLNode | None" = None
    height: int = 1

    def update_height(self) -> None:
        """Пересчёт высоты по детям."""
        left_height = _height(self.left)
        self.height = max(left_height, _height(self.right)) + 1

    def balance(self) -> int:
        """Высота левого поддерева минус высота правого."""
        return _height(self.left) - _height(self.right)

    def min_node(self) -> "AVLNode":
        """Самый левый узел поддерева."""
        node = self
        while node.left is not None:
            node = node.left
        return node

    def rotate_right(self) -> "AVLNode":
        """Правый поворот, левый ребёнок становится корнем."""
        new_root = self.left
        if new_root is None:
            return self
        self.left = new_root.right
        new_root.right = self
        self.update_height()
        new_root.update_height()
        return new_root

    def rotate_left(self) -> "AVLNode":
        """Левый поворот, правый ребёнок становится корнем."""
        new_root = self.right
        if new_root is None:
            return self
        self.right = new_root.left
        new_root.left = self
        self.update_height()
        new_root.update_height()
        return new_root

    def rebalance(self) -> "AVLNode":
        """Пересчёт высоты и повороты при перекосе."""
        self.update_height()
        balance = self.balance()
        if balance > 1 and self.left is not None:
            if self.left.balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        if balance < -1 and self.right is not None:
            if self.right.balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        return self


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
            curr = (
                curr.left
                if search_val < curr.val
                else curr.right
            )
        return False

    def insert(self, new_val: int) -> None:
        """Операция вставки, дубли игнорируются."""
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
        return node.rebalance()

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
            node.val = node.right.min_node().val
            node.right = self._delete(node.right, node.val)
        return node.rebalance()
