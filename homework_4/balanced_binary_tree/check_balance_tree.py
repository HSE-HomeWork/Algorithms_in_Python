"""Проверка бинарного дерева на сбалансированность."""

from homework_4.tree_traversal import TreeNode


def checking_balance_btree(
    root: TreeNode | None,
) -> bool:
    """Принимающая корень дерева функция."""
    return _height(root) is not None


def _height(root: TreeNode | None) -> int | None:
    """Выудить высоту или None."""
    if root is None:
        return 0
    left = _height(root.left)
    if left is None:
        return None
    right = _height(root.right)
    if right is None:
        return None
    if abs(left - right) > 1:
        return None
    return 1 + max(left, right)
