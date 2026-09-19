"""Тестирование Merge_Lists."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from homework_2.merge_lists import (
    MergeSimple,
    MergeWithFictitious,
    StrategyOfMerging,
    merge_linked_lists,
)
from homework_2.stack_vs_queue import ListNode

LIST1: list[int] = [1, 2, 4]
LIST2: list[int] = [1, 3, 4]
ANSWER_FIRST = [1, 1, 2, 3, 4, 4]

MULTI: list[int] = [1, 3]
PULTI: list[int] = [1, 2]
ANSWER_SECOND = [1, 1, 2, 3]

DABA: list[int] = [2, 4, 6]
GABA: list[int] = [1, 3, 5]
ANSWER_THIRD = [1, 2, 3, 4, 5, 6]

SORTED_LIST = st.lists(
    st.integers(min_value=-50, max_value=50)
).map(sorted)

Algorithms = (MergeWithFictitious(), MergeSimple())


@pytest.mark.parametrize(
    "algorithm",
    [MergeWithFictitious(), MergeSimple()],
    ids=["with_dummy", "simple"],
)
@pytest.mark.parametrize(
    ("first", "second", "result"),
    [
        pytest.param(
            LIST1,
            LIST2,
            ANSWER_FIRST,
            id="HM-EXAMPLE",
        ),
        pytest.param(
            MULTI,
            PULTI,
            ANSWER_SECOND,
            id="MY-EXAMPLE",
        ),
        pytest.param(DABA, GABA, ANSWER_THIRD, id="EXAMPLE"),
    ],
)
def test_merge_lists(
    first: list[int],
    second: list[int],
    result: list[int],
    algorithm: StrategyOfMerging,
) -> None:
    """Тестировка на совпадения."""
    assert (
        ListNode.to_list(
            merge_linked_lists(first, second, algorithm)
        )
        == result
    )


@pytest.mark.parametrize(
    "algorithm",
    [MergeWithFictitious(), MergeSimple()],
    ids=["with_dummy", "simple"],
)
@given(first=SORTED_LIST, second=SORTED_LIST)
def test_merge_matches_sorted(
    first: list[int],
    second: list[int],
    algorithm: StrategyOfMerging,
) -> None:
    """Сгенерированные+sorted == мои алгоритмы."""
    head = merge_linked_lists(first, second, algorithm)

    assert ListNode.to_list(head) == sorted(first + second)
