from typing import List


def binary_search(nums: List, target: int, left: int, right: int) -> int:
    """
    Binary search algorithm.

    Parameters
    ----------
    nums : List
        List of integers. The list must be sorted.
    target : int
        Target integer.
    left : int
        Left index to start searching.
    right : int
        Right index to end searching.

    Returns
    -------
    int
        Index of target integer.
    """

    if left > right:
        # indicates where the target would be if it was in the list
        return left
        # or return -1

    # use floor division to avoid float
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] > target:
        return binary_search(nums, target, left, mid - 1)

    else:
        return binary_search(nums, target, mid + 1, right)
    

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    target = 5
    print(binary_search(nums, target, 0, len(nums) - 1))