"""Тесты для Tracer и Permutations."""

import itertools
from collections.abc import Callable

import pytest

from homework_5.permutations import generate_permutations
from homework_5.tracer import trace

LEVEL = "Текущий уровень рекурсии: "


@trace
def fact(n: int) -> int:
    """Факториал."""
    return 1 if n <= 1 else n * fact(n - 1)


@trace
def _fib(n: int) -> int:
    return n if n <= 1 else _fib(n - 1) + _fib(n - 2)


@trace
def _inner() -> int:
    return 1


@trace
def _outer() -> int:
    return _inner() + 1


@trace
def _boom(n: int) -> int:
    return _boom(n - 1) if n else 1 // n


def run(
    call: Callable[[], object],
    capsys: pytest.CaptureFixture[str],
) -> tuple[object, str, list[int]]:
    """Вызывает функцию, отдаёт результат, вывод и уровни."""
    capsys.readouterr()
    result = call()
    out = capsys.readouterr().out
    levels = [
        int(line.split(LEVEL)[1])
        for line in out.splitlines()
        if LEVEL in line
    ]
    assert [
        line.index(LEVEL)
        for line in out.splitlines()
        if LEVEL in line
    ] == [x + 1 for x in levels]
    return result, out, levels


@pytest.mark.parametrize(
    ("call", "result", "levels"),
    [
        (lambda: fact(3), 6, [0, 1, 2]),
        (lambda: fact(n=1), 1, [0]),
        (lambda: _fib(4), 3, [0, 1, 2, 3, 3, 2, 1, 2, 2]),
        (_outer, 2, [0, 0]),
    ],
)
def test_trace(
    call: Callable[[], object],
    result: object,
    levels: list[int],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Результат - тот же вывод."""
    got, out, got_levels = run(call, capsys)
    assert (got, got_levels) == (result, levels)
    assert out.count("Вход в ") == levels.count(0)
    assert out.count("Возврат из ") == len(levels)
    assert run(call, capsys)[1] == out


def test_trace_exception(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Исключение пробрасывается,счётчик снова в нуле."""
    outs = []
    for _ in range(2):
        with pytest.raises(ZeroDivisionError):
            run(lambda: _boom(2), capsys)
        outs.append(capsys.readouterr().out)
    assert outs[0] == outs[1]
    assert outs[0].count("Ошибка в ") == 3


def test_trace_metadata() -> None:
    """functools.wraps сохраняет имя и докстринг."""
    assert (fact.__name__, fact.__doc__) == (
        "fact",
        "Факториал.",
    )


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        (
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_permutations_examples(
    nums: list[int], expected: list[list[int]]
) -> None:
    """Примеры из условия, включая порядок."""
    assert generate_permutations(nums) == expected


CASES = [
    list(c)
    for k in range(5)
    for c in itertools.product((-1, 0, 1), repeat=k)
]
CASES.append(list(range(6)))


@pytest.mark.parametrize("nums", CASES)
def test_permutations(
    nums: list[int], capsys: pytest.CaptureFixture[str]
) -> None:
    """Вход не тронут, общих ссылок нет, рекурсия видна."""
    before = nums.copy()
    result, out, levels = run(
        lambda: generate_permutations(nums), capsys
    )
    assert isinstance(result, list)
    assert sorted(result) == sorted(
        map(list, set(itertools.permutations(nums)))
    )
    assert nums == before
    assert (
        len({id(p) for p in result} | {id(nums)})
        == len(result) + 1
    )
    assert out.count("Вход в permutate") == 1
    assert levels.count(len(nums)) == len(result)
