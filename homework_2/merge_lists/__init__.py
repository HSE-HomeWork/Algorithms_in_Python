"""Добавляю в пакетик."""

from homework_2.merge_lists.base_merging import (
    StrategyOfMerging,
    merge_linked_lists,
)
from homework_2.merge_lists.merge_without_element import (
    MergeSimple,
)
from homework_2.merge_lists.merging_with_element import (
    MergeWithFictitious,
)

__all__ = (
    "MergeSimple",
    "MergeWithFictitious",
    "StrategyOfMerging",
    "merge_linked_lists",
)
