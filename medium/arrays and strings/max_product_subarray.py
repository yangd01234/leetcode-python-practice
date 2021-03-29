"""
Given an integer array nums, find a contiguous non-empty subarray within the 
array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Things to keep in mind:
Why do you need to keep track of the true max, and min?
What should you assert?
Why do you need a temp?
What index should you start at?
When finding the min and max, what things should you keep in mind?
What are the four things you need to set when looping?
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1: return 0
        # you have to store the current min for negative values
        true_max = cur_max = cur_min = nums[0]
        
        for n in nums[1:]:
            temp = cur_max
            
            # prod of current max, possible neg*neg, possible 0 need to reset if 0 is max
            cur_max = max(cur_max*n, cur_min*n, n)
            
            # keep min (in case you find another neg number to mult).  Store in temp because cur_max was updated.
            cur_min = min(temp*n, cur_min*n, n)
            
            # now save your true max.  You need true max because curremtn max is always rolling
            true_max = max(true_max, cur_max)
        
        return true_max
        