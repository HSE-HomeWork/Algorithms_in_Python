"""Проверки для третьей задачи."""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from homework_4.balanced_binary_tree import (
    checking_balance_btree,
)
from homework_4.tree_traversal import TreeNode

trees: st.SearchStrategy[TreeNode | None] = st.recursive(
    st.none(),
    lambda kids: st.builds(
        TreeNode, st.integers(0, 9), kids, kids
    ),
    max_leaves=40,
)


def depth(node: TreeNode | None) -> int:
    """Глубина поддерева в узлах."""
    if node is None:
        return 0
    return 1 + max(depth(node.left), depth(node.right))


def naive_balanced(node: TreeNode | None) -> bool:
    """Эталон: наивная проверка каждого узла по определению."""
    if node is None:
        return True
    gap = abs(depth(node.left) - depth(node.right))
    return (
        gap <= 1
        and naive_balanced(node.left)
        and naive_balanced(node.right)
    )


def chain(length: int, *, to_left: bool) -> TreeNode | None:
    """Цепочка из length узлов, уходящая влево или вправо."""
    root: TreeNode | None = None
    for value in range(length):
        root = (
            TreeNode(value, left=root)
            if to_left
            else TreeNode(value, right=root)
        )
    return root


@pytest.mark.parametrize(
    ("root", "expected"),
    [
        pytest.param(None, True, id="empty"),
        pytest.param(TreeNode(1), True, id="single"),
        pytest.param(
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)),
            True,
            id="gap_one",
        ),
        pytest.param(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)),
            ),
            True,
            id="perfect",
        ),
        pytest.param(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4, TreeNode(6))),
                TreeNode(
                    3, right=TreeNode(5, right=TreeNode(7))
                ),
            ),
            False,
            id="inner_violation",
        ),
        pytest.param(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4)),
                TreeNode(
                    3, right=TreeNode(5, right=TreeNode(7))
                ),
            ),
            False,
            id="violation_in_right_subtree",
        ),
        pytest.param(
            chain(3, to_left=True), False, id="left_skew"
        ),
        pytest.param(
            chain(3, to_left=False), False, id="right_skew"
        ),
    ],
)
def test_handmade_trees(
    root: TreeNode | None, *, expected: bool
) -> None:
    """Вручную заданные деревья."""
    assert checking_balance_btree(root) is expected


@given(trees)
def test_matches_naive(root: TreeNode | None) -> None:
    """Ответ должен ровно повторять наивный эталон."""
    assert checking_balance_btree(root) is naive_balanced(root)


@given(length=st.integers(3, 200), to_left=st.booleans())
def test_chain_is_unbalanced(
    length: int, *, to_left: bool
) -> None:
    """Цепочка от трёх узлов даёт False."""
    assert (
        checking_balance_btree(chain(length, to_left=to_left))
        is False
    )
