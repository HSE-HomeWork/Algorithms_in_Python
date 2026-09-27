"""Реализация hash table через два хэша)."""

from typing import Any


class KeyInfoError(KeyError):
    """Расширенная ошибка по ключу."""

    def __init__(self, something: Any) -> None:
        """Переопределил."""
        super().__init__(f"{something} not in hash_table")


class MyDict:
    """Сам класс."""

    _DELETED = object()
    _LOAD_FACTOR = 0.6
    _STANDART_CAPACITY = 16

    def __init__(
        self,
        load_factor: float = _LOAD_FACTOR,
        capacity: int = _STANDART_CAPACITY,
    ) -> None:
        """Инициализация мапки."""
        self.load_factor = load_factor
        self.capacity = capacity
        self.arr: list[list[Any]] = [
            [None] for _ in range(capacity)
        ]

    def search_value(self, key: Any) -> Any:
        """Поиск по ключу."""
        h1 = hash(key)
        h2 = self._second_hash(h1)
        for i in range(self.capacity):
            index = (h1 + i * h2) % self.capacity
            slot = self.arr[index]
            if slot is self._DELETED:
                continue
            if slot[0] is None and len(slot) == 1:
                raise KeyInfoError(key)
            if slot[0] == key or slot[0] is key:
                return slot[1]
        raise KeyInfoError(key)

    def _second_hash(self, key: int) -> int:
        """Реализация хэширования Фибоначи."""
        six_four_bit_architecture = (
            11400714819323198485  # 2^64 на золотое сечение
        )
        _mask64 = (1 << 64) - 1
        degree = self._find_degree(self.capacity)
        return ((key * six_four_bit_architecture) & _mask64) >> (
            64 - degree
        ) | 1

    @staticmethod
    def _find_degree(cap: int) -> int:
        return (cap - 1).bit_length()
