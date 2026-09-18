"""Тесты для второй задачи Validate."""

import pytest

from homework_2.validate import result_push_pop_stack

EX1_PUSHED: list[int] = [1, 2, 3, 4, 5]
EX1_POPPED: list[int] = [1, 3, 5, 4, 2]

EX2_PUSHED: list[int] = [1, 2, 3]
EX2_POPPED: list[int] = [3, 1, 2]

EX3_PUSHED: list[int] = [1, 2, 3]
EX3_POPPED: list[int] = [2, 1, 3]


@pytest.mark.parametrize(
    ("push", "pop", "answer"),
    [
        pytest.param(EX1_PUSHED, EX1_POPPED, True, id="good"),
        pytest.param(
            EX2_PUSHED, EX2_POPPED, False, id="notgood"
        ),
        pytest.param(
            EX3_PUSHED, EX3_POPPED, True, id="difficult"
        ),
    ],
)
def test_example_case(
    push: list[int],
    pop: list[int],
    answer: bool,  # noqa: FBT001
) -> None:
    """Тесты на примерах из задания."""
    assert result_push_pop_stack(push, pop) == answer


def test_diff_length() -> None:
    """Разница длин важна."""
    first = [1, 2, 3]
    second = [11]
    answer = False
    assert result_push_pop_stack(first, second) == answer
