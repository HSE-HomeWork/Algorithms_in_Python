"""Реализовал контракт для Merge."""

from abc import ABC, abstractmethod

from homework_2.stack_vs_queue import ListNode


class StrategyOfMerging(ABC):
    """Абстрактный класс под выбор алгоритма."""

    def preproc_of_two_lists(
        self, first: list[int], second: list[int]
    ) -> tuple[ListNode | None, ListNode | None]:
        """Предобработка двух списков."""
        top_first: ListNode | None = ListNode.make_linked_list(
            first
        )
        top_second: ListNode | None = ListNode.make_linked_list(
            second
        )
        return top_first, top_second

    @abstractmethod
    def merging_algorythm(
        self, first: list[int], second: list[int]
    ) -> ListNode | None:
        """Заглушка под реализацию."""


def merge_linked_lists(
    list1: list[int],
    list2: list[int],
    algorythm: StrategyOfMerging,
) -> ListNode | None:
    """Результирующая функция."""
    return algorythm.merging_algorythm(list1, list2)
