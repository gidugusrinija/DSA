"""
return indices of two nums that add up to target k
only one solution exist.
and same number cant be used again
"""


def two_sum(arr, k):
    visited_map = {}
    for idx, num in enumerate(arr):
        if k-num in visited_map:
            return (idx, visited_map[k-num])
        visited_map[num] = idx

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
