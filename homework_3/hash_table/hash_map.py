"""Реализация hash table через два хэша)."""

from typing import Any


class KeyInfoError(KeyError):
    """Расширенная ошибка по ключу."""

    def __init__(self, something: Any) -> None:
        """Переопределил."""
        super().__init__(f"{something} not in hash_table")


class MyDict:
    """Сам класс."""

    _TOMBSTONE = object()
    _LOAD_FACTOR = 0.66
    _STANDART_CAPACITY = 16

    def __init__(
        self, capacity: int = _STANDART_CAPACITY
    ) -> None:
        """Инициализация мапки."""
        self.del_elements = 0
        self.size = 0
        self.load_factor = self._LOAD_FACTOR
        self.capacity = self.capacity_check(value=capacity)
        self.arr: list[Any] = [
            [None] for _ in range(self.capacity)
        ]

    def _probe(self, key: Any) -> int:
        """Обращение по ключу."""
        h1 = hash(key)
        h2 = self._second_hash(h1, self.capacity)
        for i in range(self.capacity):
            index = (h1 + i * h2) % self.capacity
            slot = self.arr[index]
            if slot is self._TOMBSTONE:
                continue
            if len(slot) == 1:
                raise KeyInfoError(key)
            if slot[0] == key or slot[0] is key:
                return index
        raise KeyInfoError(key)

    def __getitem__(self, key: Any) -> Any:
        """Вернуть value."""
        index = self._probe(key)
        return self.arr[index][1]

    def _resize(self, new_capacity: int) -> None:
        """Механизм реаллокации."""
        new_arr: list[Any] = [
            [None] for _ in range(new_capacity)
        ]
        for i in range(len(self.arr)):
            item = self.arr[i]
            if item is not self._TOMBSTONE and len(item) > 1:
                key = item[0]
                value = item[1]
                h1 = hash(key)
                h2 = self._second_hash(h1, new_capacity)
                for j in range(new_capacity):
                    idx = (h1 + j * h2) % new_capacity
                    if len(new_arr[idx]) == 1:
                        new_arr[idx] = [key, value]
                        break
        self.arr = new_arr
        self.capacity = new_capacity
        self.del_elements = 0

    def __contains__(self, key: Any) -> bool:
        """Проверка наличия ключа в мапе."""
        try:
            self._probe(key)
        except KeyInfoError:
            return False
        return False

    def pop(self, key: Any) -> Any:
        """Удаление элемента."""
        index = self._probe(key)
        value = self.arr[index][1]
        self.arr[index] = self._TOMBSTONE
        self.del_elements += 1
        self.size -= 1
        unload_factor = self.load_factor / 2.5
        if (
            (self.size / self.capacity) < unload_factor
            and self.capacity > self._STANDART_CAPACITY
        ):
            new_capacity = self.capacity // 2
            self._resize(new_capacity=new_capacity)
        return value

    def _second_hash(self, key: int, cap: int) -> int:
        """Реализация хэширования Фибоначи."""
        six_four_bit_architecture = (
            11400714819323198485  # 2^64 на золотое сечение
        )
        _mask64 = (1 << 64) - 1
        degree = self._find_degree(cap)
        return ((key * six_four_bit_architecture) & _mask64) >> (
            64 - degree
        ) | 1

    @classmethod
    def capacity_check(cls, value: int) -> int:
        """Функция проверки вводимого capacity."""
        if value < cls._STANDART_CAPACITY:
            error_info = "Capacity слишком мал"
            raise ValueError(error_info)
        return 1 << cls._find_degree(cap=value)

    @staticmethod
    def _find_degree(cap: int) -> int:
        return (cap - 1).bit_length()
