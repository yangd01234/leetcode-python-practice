"""
Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

Hint: You can add a runner pointer so the two pointers run at different speeds

Things to keep in mind:
What should you assert?
How can you use runner pointers to your advantage?
How would you swap?
What should you keep in mind when swapping?
How can you delete an array element?
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # basecase
        if (len(nums) == 0): return 0
        if (len(nums) == 1): return 1
        
        # pointer 1
        j = 0
        
        for i in range (0, len(nums)-1):
            if nums[j] == nums[j+1]:
                del nums[j]
            else:
                j += 1
        return len(nums)