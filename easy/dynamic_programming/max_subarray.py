"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.

HINT: use a temp
Things to keep in mind:
What is the subproblem?
What can you use the array to keep track of?
When you keep track of this, why do you need to compare arr pos + nums pos?
What else should you keep track of?
"""

class Solution:
    def maxSubArray(self, nums) -> int:

    	# allocate empty array to keep track of max
    	arr = []
    	arr.append(nums[0])
    	curr_max = arr[0]

    	# iterate through and find max of current pos vs next
    	for i in range(1, len(nums)):
    		arr.append(max(arr[i-1] + nums[i], nums[i]))
    		if arr[i] > curr_max:
    			curr_max = arr[i]

    	return curr_max


max_sub = Solution()

print(max_sub.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub.maxSubArray([-100000]))
print(max_sub.maxSubArray([-2,-1]))