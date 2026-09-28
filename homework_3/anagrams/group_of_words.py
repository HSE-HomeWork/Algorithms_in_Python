"""Решение анаграмм."""


def anagrams_to_list(strs: list[str]) -> list[list[str]]:
    """Разбивает список строк на подгруппы по составу."""
    nature_words: dict[str, list[str]] = {}

    for word in strs:
        normal_word = "".join(sorted(word))
        nature_words.setdefault(normal_word, []).append(word)

    return list(nature_words.values())
