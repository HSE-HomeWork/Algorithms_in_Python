"""Решение анаграмм."""


def anagrams_to_list(strs: list[str]) -> list[list[str]]:
    """Разбивает список строк на подгруппы по составу."""
    nature_words: dict[str, list[str]] = {}

    for word in strs:
        normal_word = "".join(sorted(word))
        if normal_word in nature_words:
            nature_words[normal_word].append(word)
        else:
            nature_words[normal_word] = [word]

    return list(nature_words.values())
