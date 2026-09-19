"""Реализация алгоритма слияния двух LinkedList."""

from homework_2.merge_lists.base_merging import StrategyOfMerging
from homework_2.stack_vs_queue import ListNode


class MergeSimple(StrategyOfMerging):
    """Класс для алгоритма без дополнительного элемента."""

    def merge_two_linked(
        self,
        first: ListNode | None,
        second: ListNode | None,
    ) -> ListNode | None:
        """Рекурсия по односвязным спискам."""
        if first is None:
            return second
        if second is None:
            return first
        if first.val < second.val:
            first.next = self.merge_two_linked(
                first.next, second
            )
            return first
        second.next = self.merge_two_linked(first, second.next)
        return second

    def merging_algorythm(
        self, list1: list[int], list2: list[int]
    ) -> ListNode | None:
        """Результирующий метод."""
        first, second = self.preproc_of_two_lists(list1, list2)

        return self.merge_two_linked(first, second)
