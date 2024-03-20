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
def test_merge_sorted_array(result, nums1, m, nums2, n) -> None:
    """Tests solution for problem Merge Sorted Array"""

    assert api.merge_sorted_array(nums1, m, nums2, n) == result
