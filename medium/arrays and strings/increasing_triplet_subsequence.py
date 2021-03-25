"""
Given an integer array nums, return true if there exists a triple of indices 
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid 
because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n)
time complexity and O(1) space complexity?

Things to keep in mind:
How can you use pointers to your advantage?
Write out the conditions and practice iterating through
How can you use process of elimination to modify your window and what to record?
"""
import math
class Solution:
    def increasingTriplet(self, nums) -> bool:
        left = math.inf
        mid = math.inf

        for i in nums:
            # set the smallest leftmost value
            if i < left:
                left = i
            # set the mid value
            elif left < i < mid:
                mid = i
            elif mid < i:
                return True
        return False

sol = Solution()
print(sol.increasingTriplet([5,4,3,2,1]))