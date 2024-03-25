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


def _reverse(nums: list[int], i: int, k: int) -> None:
    l = i + k
    for j in range(i, k // 2):
        nums[j], nums[l - (j + 1)] = nums[l - (j + 1)], nums[j]


def _swap(nums1: list[int], nums2: list[int]) -> None:
    _reverse(nums1)
    _reverse(nums2)
    for i in range((len(nums1) + len(nums2))//2):
        if i < len(nums1) and i < len(nums2):
            nums1[i], nums2[-(i+1)] = nums2[-(i+1)], nums1[i]
        elif i >= len(nums1):
            j = i - len(nums1)
            nums2[j], nums2[-(i+1)] = nums2[-(i+1)], nums2[j]
        else:
            j = i - len(nums2)
            nums1[i], nums1[-(j+1)] = nums1[-(j+1)], nums2[i]


def merge_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Solves problem Merge Sorted Array"""

    assert _check_preconditions(nums1, m, nums2, n)

    nums1[m:] = nums2

    j = m
    i = 0
    while i < m + n:
        k = 0
        while j + k < m + n and nums1[i] > nums1[j + k]:
            k = k + 1
        if k:
            _swap(nums1, i, j, k)
            j = j + k + 1
        i = i + k + 1
