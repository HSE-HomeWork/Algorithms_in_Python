"""Проверка произвольного дерева на соответствие BST."""

from homework_4.tree_traversal import TreeNode


def checking_correct_bst(
    root: TreeNode | None,
    minimum: int | None = None,
    maximum: int | None = None,
) -> bool:
    """Проверка на BST произвольного дерева."""
    if root is None:
        return True
    if minimum is not None and root.val < minimum:
        return False
    if maximum is not None and root.val >= maximum:
        return False
    return checking_correct_bst(
        root.left, maximum=root.val, minimum=minimum
    ) and checking_correct_bst(
        root.right, maximum=maximum, minimum=root.val
    )
