"""Тестирование суммы."""

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from homework_1.sum import max_even_sum_array

UNEVEN_AR: tuple[int, ...] = (1, 1)
EMPTY: tuple[int, ...] = ()
NORMAL_AR: tuple[int, ...] = (2, 3, 4)

HOMEWORK_AR: tuple[int, ...] = (5, 7, 13, 2, 14)

POSITIVE_LISTS: SearchStrategy[list[int]] = st.lists(
    st.integers(min_value=1)
)


def test_hm_array() -> None:
    """Поиск суммы в массиве из примера."""
    answer = 36
    assert max_even_sum_array(list(HOMEWORK_AR)) == answer


def test_empty_array() -> None:
    """Поиск суммы в пустом массиве."""
    assert max_even_sum_array(list(EMPTY)) == 0


def test_uneven_arrays() -> None:
    """Поиск суммы в нечётном массиве."""
    answer = 2
    assert max_even_sum_array(list(UNEVEN_AR)) == answer


def test_normal_arrays() -> None:
    """Поиск суммы в стандартном массиве."""
    answer = 6
    assert max_even_sum_array(list(NORMAL_AR)) == answer


@given(POSITIVE_LISTS)
def test_result_is_even(
    numbers: list[int],
) -> None:
    """Результат всегда делится на 2 и <=сумме."""
    assert max_even_sum_array(numbers) % 2 == 0
    assert max_even_sum_array(numbers) <= sum(numbers)
