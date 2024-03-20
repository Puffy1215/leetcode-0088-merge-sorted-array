"""Tests API for solving problem Merge Sorted Array"""

import pytest

from leetcode_0088_merge_sorted_array import api


@pytest.mark.parametrize(
    ["result", "nums1", "m", "nums2", "n"],
    (
        [..., ...],
        [..., ...],
    )
)
def test_merge_sorted_array(result, nums1, m, nums2, n) -> None:
    """Tests solution for problem Merge Sorted Array"""

    assert api.merge_sorted_array(nums1, m, nums2, n) == result