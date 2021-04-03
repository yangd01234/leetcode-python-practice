"""
560. Subarray Sum Equals K
Medium

6918

241

Add to List

Share
Given an array of integers nums and an integer k, return the total number of 
continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

# key thing to note WHEN THE ONGOING SUM HAS INCREASED BY K, WE'VE FOUND A K!

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # keep track of first sum
        d = {0:1}
        
        # keep track of res counter and current sum
        res = curr_sum = 0
        
        for n in nums:
            curr_sum += n
            res += d.get(curr_sum-k, 0) # if sums-k exists get the count, otherwise 0
            d[curr_sum] = d.get(curr_sum, 0) +1 # increment count of current sum by 1
        
        return res