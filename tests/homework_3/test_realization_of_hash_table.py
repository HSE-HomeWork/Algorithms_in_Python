"""Дополнительные тесты для собственной хэш-таблицы."""

from hypothesis import given, settings
from hypothesis import strategies as st

from homework_3.hash_table import MyDict

HASH_MODULUS = 2**61 - 1

keys = st.one_of(
    st.none(), st.integers(-50, 50), st.text(max_size=3)
)
operations = st.lists(
    st.tuples(
        st.sampled_from(["set", "pop"]), keys, st.integers()
    ),
    max_size=300,
)


@settings(max_examples=300)
@given(operations)
def test_mydict_vs_dict(
    ops: list[tuple[str, object, int]],
) -> None:
    """MyDict на одних и тех же операциях ведёт себя как dict."""
    mine = MyDict()
    real: dict[object, int] = {}

    for op, key, value in ops:
        if op == "set":
            mine[key] = value
            real[key] = value
        else:
            assert (key in mine) == (key in real)
            if key in real:
                assert mine.pop(key) == real.pop(key)
        assert len(mine) == len(real)

    for key, value in real.items():
        assert mine[key] == value
    assert len(list(mine)) == len(real)


def test_fill_then_drop_everything() -> None:
    """Заполнили 10 000 ключей, удалили все: таблица жива."""
    table = MyDict()
    normal_cap = 16
    for i in range(10_000):
        table[i] = i
    for i in reversed(range(10_000)):
        table.pop(i)

    assert len(table) == 0
    assert table.capacity == normal_cap

    for i in range(100):
        table[i] = -i
    assert all(table[i] == -i for i in range(100))


def test_equal_keys_of_different_types() -> None:
    """1, 1.0 и True — один и тот же ключ, как в dict."""
    table = MyDict()
    table[1] = "int"
    table[1.0] = "float"
    table[True] = "bool"

    assert len(table) == 1
    assert table[1] == "bool"
