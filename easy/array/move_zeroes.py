"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

HINT:
Think about runners and keeping track of the current position.  
You don't really need to keep track of where the 0's go.
Track how many you have.

Things to keep in mind:
How can you use two loops to your advantage?
Do you need to keep track of where the 0's go?
Why is it beneficial to have an index?
"""



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0


i1 = [0,1,0,3,12]
obj = Solution()
obj.moveZeroes(i1)
print(i1)