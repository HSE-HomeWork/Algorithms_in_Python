"""Тесты для AVL-дерева."""

import itertools
import math

import pytest

from homework_5.AVL import AVLNode, AVLTree

VALUES = range(6)


def check(node: AVLNode | None) -> tuple[int, list[int]]:
    """Проверяет высоты и баланс."""
    if node is None:
        return 0, []
    left_height, left_vals = check(node.left)
    right_height, right_vals = check(node.right)
    assert node.height == 1 + max(left_height, right_height)
    assert abs(left_height - right_height) <= 1
    return node.height, [*left_vals, node.val, *right_vals]


def assert_valid(tree: AVLTree, expected: set[int]) -> None:
    """Инварианты AVL, порядок BST и поиск ."""
    assert check(tree.root)[1] == sorted(expected)
    for val in range(-1, len(VALUES) + 1):
        assert tree.search(val) == (val in expected)


def preorder(node: AVLNode | None) -> list[int]:
    """Обход корень, левое, правое."""
    return (
        []
        if node is None
        else [
            node.val,
            *preorder(node.left),
            *preorder(node.right),
        ]
    )


def build(values: list[int]) -> AVLTree:
    """Дерево из последовательных вставок."""
    tree = AVLTree()
    for val in values:
        tree.insert(val)
    return tree


@pytest.mark.parametrize(
    ("inserts", "deletes", "shape"),
    [
        ([3, 2, 1], [], [2, 1, 3]),
        ([1, 2, 3], [], [2, 1, 3]),
        ([3, 1, 2], [], [2, 1, 3]),
        ([1, 3, 2], [], [2, 1, 3]),
        ([2, 1, 3, 4], [1], [3, 2, 4]),
        ([3, 2, 4, 1], [4], [2, 1, 3]),
        ([3, 1, 4, 2], [4], [2, 1, 3]),
        ([2, 1, 4, 3], [1], [3, 2, 4]),
        ([2, 1, 4, 3, 5], [1], [4, 2, 3, 5]),
        ([2, 1, 3], [2], [3, 1]),
        ([2, 1], [2], [1]),
        ([2, 3], [2], [3]),
        ([5, 5], [], [5]),
        ([1], [9], [1]),
        ([], [1], []),
        ([1], [1], []),
    ],
)
def test_shapes(
    inserts: list[int], deletes: list[int], shape: list[int]
) -> None:
    """Повороты LL, RR, LR, RL."""
    tree = build(inserts)
    for val in deletes:
        tree.delete(val)
    assert preorder(tree.root) == shape


@pytest.mark.parametrize("delete_sorted", [True, False])
def test_all_orders(*, delete_sorted: bool) -> None:
    """Перебор порядков вставки и удаления."""
    for order in itertools.permutations(VALUES):
        tree = build([])
        expected: set[int] = set()
        for val in order if delete_sorted else VALUES:
            tree.insert(val)
            expected.add(val)
            assert_valid(tree, expected)
        for val in VALUES if delete_sorted else order:
            tree.delete(val)
            expected.discard(val)
            assert_valid(tree, expected)


def test_height_is_logarithmic() -> None:
    """Возрастающая вставка не вырождает дерево в список."""
    size = 1000
    tree = build(list(range(size)))
    assert tree.root is not None
    assert tree.root.height <= 1.45 * math.log2(size + 2)
    assert check(tree.root)[1] == list(range(size))
