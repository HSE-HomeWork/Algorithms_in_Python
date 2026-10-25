"""Тесты для BinarySearchTree и checking_correct_bst."""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from homework_4.tree_traversal import BinarySearchTree, TreeNode
from homework_4.validate_bst import checking_correct_bst

values_lists = st.lists(st.integers(-1000, 1000), max_size=200)


def build_tree(values: list[int]) -> BinarySearchTree:
    """Собирает BST вставкой значений по порядку."""
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree


@pytest.mark.parametrize(
    ("method", "expected"),
    [
        ("pre_order", [5, 3, 1, 4, 8, 7, 9]),
        ("in_order", [1, 3, 4, 5, 7, 8, 9]),
        ("post_order", [1, 4, 3, 7, 9, 8, 5]),
        ("reverse_pre_order", [5, 8, 9, 7, 3, 4, 1]),
        ("reverse_in_order", [9, 8, 7, 5, 4, 3, 1]),
        ("reverse_post_order", [9, 7, 8, 4, 1, 3, 5]),
    ],
)
def test_traversals(method: str, expected: list[int]) -> None:
    """Шесть обходов на эталонном дереве 5, 3, 8, 1, 4, 7, 9."""
    tree = build_tree([5, 3, 8, 1, 4, 7, 9])
    assert getattr(tree, method)() == expected


@given(values_lists)
def test_in_order_is_sorted(values: list[int]) -> None:
    """Inorder любого дерева из insert совпадает."""
    assert build_tree(values).in_order() == sorted(values)


@given(values_lists)
def test_tree_from_insert_is_valid(values: list[int]) -> None:
    """Дерево из insert всегда проходит проверку."""
    assert checking_correct_bst(build_tree(values).root) is True


@pytest.mark.parametrize(
    ("root", "expected"),
    [
        pytest.param(
            TreeNode(
                5,
                TreeNode(3, TreeNode(1), TreeNode(4)),
                TreeNode(8, TreeNode(7), TreeNode(9)),
            ),
            True,
            id="корректное дерево",
        ),
        pytest.param(
            TreeNode(5, right=TreeNode(5)),
            True,
            id="дубликат справа",
        ),
        pytest.param(
            TreeNode(5, left=TreeNode(5)),
            False,
            id="дубликат слева",
        ),
        pytest.param(
            TreeNode(5, left=TreeNode(7)),
            False,
            id="левый ребёнок больше",
        ),
        pytest.param(
            TreeNode(5, left=TreeNode(3, right=TreeNode(6))),
            False,
            id="нарушение через деда слева",
        ),
        pytest.param(
            TreeNode(5, right=TreeNode(8, left=TreeNode(4))),
            False,
            id="нарушение через деда справа",
        ),
        pytest.param(
            TreeNode(0, right=TreeNode(-1)),
            False,
            id="граница равна нулю",
        ),
    ],
)
def test_arbitrary_trees(
    root: TreeNode, *, expected: bool
) -> None:
    """Проверка на вручную собранных деревьях."""
    assert checking_correct_bst(root) is expected
