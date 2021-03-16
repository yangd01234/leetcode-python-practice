"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

HINT: They key is in the type of sorting

Things to keep in mind:
What type of sorting can you do?
How is this an easy check?
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

i_1 = [1,2,3,1]
i_2 = [1,2,3,4]
i_3 = [1,1,1,3,3,4,3,2,4,2]

obj = Solution()
print(obj.containsDuplicate(i_2))    
