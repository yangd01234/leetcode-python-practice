"""
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and
without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

HINT: You can use the exclusive OR method.  Essentially you return the value
that didn't register as a 0 using XOR method.  
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = nums[0]
        for i in range(1, len(nums)):
            single ^= nums[i]
        return single


nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]
obj = Solution()
print(obj.singleNumber(nums3))