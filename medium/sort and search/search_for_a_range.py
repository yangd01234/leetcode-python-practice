"""
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Things to keep in mind:
What should you assert?
What do you need to keep in mind if the range is -10^9 <= nums[i] <= 10^9?
What should you do to make it faster for yourself to lookup items?
"""
from collections import Counter
class Solution:
    def searchRange(self, nums, target):

        if nums == []: return [-1,-1]
        # lowest value
        min_value = nums[0]

        # current sum
        starting_index = 0

        # create dict
        c = Counter(nums)

        # check if c[target] has no frequency
        if c[target] == 0:
            return [-1, -1]

        for i in range(min_value, target):
            starting_index += c[i]

        return [starting_index, starting_index+c[target]-1]


sol = Solution()
print(sol.searchRange([0,1,2,3,4, 4, 4, 4, 4], 4))
print(sol.searchRange([], 0))
print(sol.searchRange([1, 4], 4))


