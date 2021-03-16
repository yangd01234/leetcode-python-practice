"""
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into
 on the same night.

Given a list of non-negative integers representing the amount of money of each 
house, determine the maximum amount of money you can rob tonight without 
alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

Things to keep in mind:
Summary of problem?
What does it mean by two adjacent houses?
What datastructure can you use for this type of problem?
Should you start at the beginning or at the end of the array?
How can you use this datastructure to your advantage?
Why do you need to use index instead of the actual element?
What maximum values (-, + n?) are you looking for if you can't use adjacent houses?
Why should you return temp_dict[1]?
How would the input table for DP look like in this case?
What is the subproblem in this case?
How does getting the max of nums and temp_dict indexes work to your advantage?
"""

# go through list, get the maxes and if current is not next, then figure out if it works
from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
    	temp_dict = defaultdict(int)

    	# start in reverse and find the max for each house.  Ex: if you visit house a the max is...
    	for i in range (len(nums), 0, -1):
    		# compare max profits of existing calculated profits that don't conflict
    		temp_dict[i] = max(nums[i-1] + temp_dict[i + 2], temp_dict[i + 1])
    	# eventually, y ou end at temp_dict[1] as the max because you compare nums vs temp_dict max
    	return temp_dict[1]