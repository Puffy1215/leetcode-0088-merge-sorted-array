"""Tests API for solving problem Merge Sorted Array"""

import pytest

from leetcode_0088_merge_sorted_array import api


@pytest.mark.parametrize(
    ["result", "nums1", "m", "nums2", "n"],
    (
        [[1, 2, 2, 3, 5, 6], [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[1], [1], 1, [], 0],
        [[1], [0], 0, [1], 1],
    ),
)
def test_merge_sorted_array(
    result: list[int], nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    """Tests solution for problem Merge Sorted Array"""

    api.merge_sorted_array(nums1, m, nums2, n)

    assert nums1 == result
