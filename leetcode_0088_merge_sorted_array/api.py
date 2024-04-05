"""API for solving problem Merge Sorted Array"""

LEN_MAX = 200
LEN_MIN = 0

NUM_MAX = 10**9
NUM_MIN = -NUM_MAX


def _check_preconditions(nums1: list[int], m: int, nums2: list[int], n: int) -> bool:
    if not len(nums1) == m + n:
        return False

    if not len(nums2) == n:
        return False

    for l in [m, n]:
        if not LEN_MIN <= l <= LEN_MAX:
            return False

    if not LEN_MIN + 1 <= m + n <= LEN_MAX:
        return False

    for nums, l in [(nums1, m), (nums2, n)]:
        for x in nums:
            if not NUM_MIN <= x <= NUM_MAX:
                return False

        if sorted(nums[:l]) != nums[:l]:
            return False

    return True


def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Solves problem Merge Sorted Array"""

    assert _check_preconditions(nums1, m, nums2, n)

    pass
