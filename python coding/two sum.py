"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Twosum:
    def two_sum(self, nums, target):
        visited = {}
        for ind, val in enumerate(nums):
            val2 = target - val
            if val2 in visited:
                return [ind, visited[val2]]
            visited[val] = ind


r = Twosum().two_sum([2, 5, 9, 6], 8)
print(r)


def twoSum(nums: list, target: int) -> list:
    enumerated_map = {}
    for idx, val in enumerate(nums):
        enumerated_map[val] = idx
    sorted_map = dict(sorted(enumerated_map.items()))
    for num in sorted_map:
        if num == 0:
            return [sorted_map[num], sorted_map[target]]
        else:
            if (target - num) in sorted_map:
                l = sorted_map[num]
                r = sorted_map[target - num]
                if sorted_map[num] == sorted_map[target-num]:
                    r = nums.index(num, nums.index(num)+1)
                return [l, r]

li = twoSum([3, 3], 6)
print(li)
