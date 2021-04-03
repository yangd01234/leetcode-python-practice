"""
525. Contiguous Array
Medium

2733

136

Add to List

Share
Given a binary array, find the maximum length of a contiguous subarray with 
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 
0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal 
number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # use a dict to hold {curr_sum: index}
        d = {0:0}
        
        # cummulative sum and max length (res)
        res = running_sum = 0
        
        # you need to enumerate so you can get the correct position
        for i, num in enumerate(nums, 1):
            if num == 0:
                running_sum -= 1
            else:
                running_sum += 1
            
            # get the lengths
            if running_sum in d:
                res = max(res, (i - d[running_sum]))
            else:  
                d[running_sum] = i
        return res
