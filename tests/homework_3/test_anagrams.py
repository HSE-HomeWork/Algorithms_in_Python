"""Тесты для группировки анаграмм."""

from collections import Counter

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from homework_3.anagrams import anagrams_to_list

words = st.lists(
    st.text(alphabet="abc", max_size=4), max_size=30
)


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([], []),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "def", "gh"], [["abc"], ["def"], ["gh"]]),
        (["abc", "cab", "bca"], [["abc", "cab", "bca"]]),
        (["a", "a"], [["a", "a"]]),
    ],
)
def test_known_cases(
    strs: list[str], expected: list[list[str]]
) -> None:
    """Пример из условия, пустые, одиночные слова, дубли."""
    assert anagrams_to_list(strs) == expected


@settings(max_examples=500)
@given(words)
def test_no_words_lost(strs: list[str]) -> None:
    """Каждое слово в ответе столько раз, сколько было."""
    groups = anagrams_to_list(strs)
    found = Counter(word for group in groups for word in group)

    assert found == Counter(strs)
