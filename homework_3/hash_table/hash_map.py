"""Реализация hash table через два хэша)."""

from collections.abc import Iterator
from typing import Any

TOMBSTONE = object()
LOAD_FACTOR = 0.66
SHRINK_DIVISOR = 2.5
MIN_CAPACITY = 16
WORD_BITS = 64
MASK_64 = (1 << WORD_BITS) - 1
FIB_MULTIPLIER = 11400714819323198485  # 2^64 / φ


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

    def __getitem__(self, key: Any) -> Any:
        """Значение по ключу или KeyInfoError."""
        index = self._probe(key)
        return self.arr[index][1]

    def __contains__(self, key: Any) -> bool:
        """Проверка наличия ключа в мапе."""
        try:
            self._probe(key)
        except KeyInfoError:
            return False
        return True

    def __setitem__(self, key: Any, value: Any) -> None:
        """Вставляет пару или обновляет значение.

        При переполнении таблица растёт в 2 раза.
        """
        try:
            index = self._probe(key)
        except KeyInfoError:
            self._put_in_free_slot(key=key, value=value)
        else:
            self.arr[index] = [key, value]
        if (
            (self.size + self.del_elements) / self.capacity
        ) > self.load_factor:
            new_capacity = self.capacity * 2
            self._resize(new_capacity=new_capacity)

    def __len__(self) -> int:
        """Количество живых пар."""
        return self.size

    def __iter__(self) -> Iterator[Any]:
        """Итерация по моей мапе."""
        for item in self.arr:
            if item is not self._TOMBSTONE and len(item) > 1:
                yield item[0]

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

    def values(self) -> Iterator[Any]:
        """Возвращает значения."""
        for item in self.arr:
            if item is not self._TOMBSTONE and len(item) > 1:
                yield item[1]

    @classmethod
    def capacity_check(cls, value: int) -> int:
        """Проверяет ёмкость и округляет до 2^k."""
        if value < cls._STANDART_CAPACITY:
            error_info = "Capacity слишком мал"
            raise ValueError(error_info)
        return 1 << _find_degree(cap=value)

    def _probe_sequence(
        self, key: Any, cap: int
    ) -> Iterator[int]:
        """Индексы ячеек в порядке пробирования.

        i-я проба: (hash(key) + i * шаг) % cap.
        """
        h1 = hash(key)
        h2 = self._second_hash(h1, cap)
        for idx in range(cap):
            yield (h1 + idx * h2) % cap

    def _put_in_free_slot(self, key: Any, value: Any) -> None:
        """Положить в надгробие или в None."""
        for index in self._probe_sequence(key, self.capacity):
            slot = self.arr[index]
            if slot is self._TOMBSTONE or len(slot) == 1:
                self.arr[index] = [key, value]
                self.size += 1
                if slot is self._TOMBSTONE:
                    self.del_elements -= 1
                break

    def _probe(self, key: Any) -> int:
        """Индекс ячейки,ключ или KeyInfoError.

        Надгробия пропускает, на пустоте останавливается.
        """
        for index in self._probe_sequence(key, self.capacity):
            slot = self.arr[index]
            if slot is self._TOMBSTONE:
                continue
            if len(slot) == 1:
                raise KeyInfoError(key)
            if slot[0] == key or slot[0] is key:
                return index
        raise KeyInfoError(key)

    def _resize(self, new_capacity: int) -> None:
        """Перекладывает живые пары в новый список."""
        new_arr: list[Any] = [
            [None] for _ in range(new_capacity)
        ]
        for idx in range(len(self.arr)):
            item = self.arr[idx]
            if item is not self._TOMBSTONE and len(item) > 1:
                self._place(new_arr, item, new_capacity)
        self.arr = new_arr
        self.capacity = new_capacity
        self.del_elements = 0

    def _place(
        self, arr: list[Any], item: list[Any], cap: int
    ) -> None:
        """Кладёт пару в первую пустую ячейку нового списка."""
        for index in self._probe_sequence(item[0], cap):
            if len(arr[index]) == 1:
                arr[index] = item
                return

    def _second_hash(self, key: int, cap: int) -> int:
        """Реализация хэширования Фибоначи."""
        mixed = (key * FIB_MULTIPLIER) & MASK_64
        return mixed >> (64 - _find_degree(cap)) | 1


def _find_degree(cap: int) -> int:
    """Наименьшее k, при котором 2^k >= cap."""
    return (cap - 1).bit_length()
