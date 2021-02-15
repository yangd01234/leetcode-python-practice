"""
Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

Hint: You can add a runner pointer so the two pointers run at different speeds
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
        j = 1
        
        for i in range (0, len(nums)):
            if nums[i] != nums[j]:
                nums[j] = nums[i]
                # important: make sure to delete per question prompt
                del nums[j]
                j = j + 1
        # return the count of duplicates
        return j