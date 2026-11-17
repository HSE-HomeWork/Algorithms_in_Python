"""Tests for kth largest element."""

import pytest

from homework_6.k_th import find_kth_largest


@pytest.mark.parametrize(
    ("lst", "k", "expected"),
    [
        ([3, 1, 5, 2, 4], 1, 5),
        ([3, 1, 5, 2, 4], 3, 3),
        ([3, 1, 5, 2, 4], 5, 1),
        ([9, 9, 8, 7], 2, 9),
        ([9, 9, 8, 7], 3, 8),
        ([4, 4, 4, 4], 2, 4),
        ([-5, -1, -10, -3], 4, -10),
    ],
)
def test_find_kth_largest(
    lst: list[int],
    k: int,
    expected: int,
) -> None:
    """Test kth largest element."""
    assert find_kth_largest(lst, k) == expected
