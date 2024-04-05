"""Tests API for solving problem Merge Sorted Array"""

import random
from typing import Callable

import pytest

from leetcode_0088_merge_sorted_array import api


@pytest.mark.parametrize(
    ["result", "nums1", "m", "nums2", "n"],
    (
        [[1, 2, 2, 3, 5, 6], [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[1], [1], 1, [], 0],
        [[1], [0], 0, [1], 1],
        [[1, 2, 2, 3, 4, 6], [2, 4, 6, 0, 0, 0], 3, [1, 2, 3], 3],
    ),
)
def test_merge_sorted_array(
    result: list[int], nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    """Tests solution for problem Merge Sorted Array"""

    api.merge_sorted_array(nums1, m, nums2, n)

    assert nums1 == result


@pytest.fixture
def nums_rand() -> Callable[[], tuple[list[int], list[int]]]:
    """Fixture to generate random x"""

    def _nums_rand() -> tuple[list[int], list[int]]:
        l = random.randint(api.LEN_MIN + 1, api.LEN_MAX)
        m = random.randint(api.LEN_MIN, l)
        n = l - m
        nums = [random.randint(api.NUM_MIN, api.NUM_MAX) for _ in range(l)]
        nums1 = sorted(nums[:m]) + [0] * n
        nums2 = sorted(nums[m:])
        return nums1, nums2

    return _nums_rand


@pytest.mark.parametrize("run_count", range(10))
def test_sqrtx_rand(
    run_count: int,
    nums_rand: Callable[
        [], tuple[list[int], list[int]]
    ],  # pylint: disable=redefined-outer-name
) -> None:
    """Tests solution for problem Merge Sorted Array with random nums1 and nums2"""

    random.seed(run_count)

    nums1, nums2 = nums_rand()
    n = len(nums2)
    m = len(nums1) - n
    result = sorted(nums1[:m] + nums2)

    test_merge_sorted_array(result, nums1, m, nums2, n)
