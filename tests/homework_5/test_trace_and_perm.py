"""Тесты для Tracer и Permutations."""

import itertools

import pytest

from homework_5.permutations.transpose import (
    generate_permutations,
)
from homework_5.tracer.tracer import trace

LEVEL = "Текущий уровень рекурсии: "
FACT_LEVELS = (0, 1, 2)
FIB_LEVELS = (0, 1, 2, 3, 3, 2, 1, 2, 2)


@trace
def fact(n: int) -> int:
    """Факториал."""
    return 1 if n <= 1 else n * fact(n - 1)


@trace
def fib(n: int) -> int:
    """Число Фибоначчи."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@trace
def inner() -> int:
    """Вызывается из outer."""
    return 1


@trace
def outer() -> int:
    """Вызывает inner."""
    return inner() + 1


@trace
def boom(n: int) -> int:
    """Падает на дне рекурсии."""
    return boom(n - 1) if n else 1 // n


def levels(out: str) -> tuple[list[int], list[int]]:
    """Уровни по числу в строке и по длине отступа."""
    lines = [line for line in out.splitlines() if LEVEL in line]
    by_number = [int(line.split(LEVEL)[1]) for line in lines]
    by_indent = [line.index(LEVEL) - 1 for line in lines]
    return by_number, by_indent


class TestTraceAndPermutations:
    """Трейсер и перестановки."""

    @pytest.mark.parametrize(
        ("func", "arg", "expected", "expected_levels"),
        [
            (fact, 3, 6, FACT_LEVELS),
            (fib, 4, 3, FIB_LEVELS),
        ],
    )
    def test_trace(
        self,
        func: object,
        arg: int,
        expected: int,
        expected_levels: tuple[int, ...],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Результат, уровни, отступы, один вход, возврат."""
        assert callable(func)
        assert func(n=arg) == expected
        out = capsys.readouterr().out
        assert levels(out) == (
            list(expected_levels),
            list(expected_levels),
        )
        assert out.count("Вход в ") == 1
        assert out.count("Возврат из ") == len(expected_levels)

    def test_trace_repeat_and_nested(
        self,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Повторный вызов даёт тот же вывод."""
        outer()
        first = capsys.readouterr().out
        outer()
        assert capsys.readouterr().out == first
        assert levels(first)[0] == [0, 0]

    def test_trace_exception(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Исключение пробрасывается."""
        outs = []
        for _ in range(2):
            with pytest.raises(ZeroDivisionError):
                boom(2)
            outs.append(capsys.readouterr().out)
        assert outs[0] == outs[1]
        assert outs[0].count("Ошибка в ") == outs[0].count(LEVEL)

    def test_trace_metadata(self) -> None:
        """Имя и докстринг сохраняются."""
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
        self,
        nums: list[int],
        expected: list[list[int]],
    ) -> None:
        """Примеры из условия, включая порядок."""
        assert generate_permutations(nums) == expected

    @pytest.mark.parametrize("length", range(6))
    def test_permutations(self, length: int) -> None:
        """Массивы из -1, 0, 1: итог как в itertools."""
        for array in itertools.product(
            (-1, 0, 1), repeat=length
        ):
            nums = list(array)
            perms = generate_permutations(nums)
            unique = set(itertools.permutations(nums))
            assert sorted(perms) == sorted(map(list, unique))
            assert nums == list(array)
            ids = {id(perm) for perm in perms}
            assert len(ids) == len(perms)
            assert id(nums) not in ids

    @pytest.mark.parametrize("length", range(5))
    def test_permutations_traced(
        self,
        length: int,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Рекурсия видна в трейсере."""
        perms = generate_permutations(list(range(length)))
        out = capsys.readouterr().out
        assert out.count("Вход в permutate") == 1
        assert levels(out)[0].count(length) == len(perms)
