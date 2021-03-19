"""
Given an array nums of n integers, are there elements a, b, c in nums such 
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Things to keep in mind:
How can you use two sum to your advantage?
Why is it important that the array should be sorted?
Do you actually need a dictionary for this?
What should you keep track of if you don't need a dict?
How can you use two pointers to your advantage?
List out the things you need to keep track of when using two pointers.
Why do you only need to increment one pointer when looping?
"""

class Solution:
    def threeSum(self, nums):
        # assert
        if len(nums) < 1: return []

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums) -1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


nums1 = [-1,0,1,2,-1,-4]
nums2 = []
nums3 = [0]

sol = Solution()
# [[-1,-1,2],[-1,0,1]]
print(sol.threeSum(nums1))
# []
print(sol.threeSum(nums2))
# []
print(sol.threeSum(nums3))