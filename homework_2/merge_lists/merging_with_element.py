"""Реализация алгоритма слияния двух LinkedList."""

from homework_2.merge_lists import StrategyOfMerging
from homework_2.stack_vs_queue import ListNode


class MergeWithFictitious(StrategyOfMerging):
    """Класс для алгоритма, включащий фиктивный элемент."""

    def merging_algorythm(
        self, list1: list[int], list2: list[int]
    ) -> ListNode | None:
        """Алгоритм, в котором фиктивный элемент."""
        first, second = self.preproc_of_two_lists(list1, list2)

        empty = ListNode(value=None)
        answer = empty
        while first and second:
            if second.val >= first.val:
                empty.next = first
                empty = empty.next
                first = first.next
            else:
                empty.next = second
                empty = empty.next
                second = second.next
        empty.next = first or second
        return answer.next
