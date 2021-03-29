"""153. Find Minimum in Rotated Sorted Array
Medium

3270

296

Add to List

Share
Suppose an array of length n sorted in ascending order is rotated between 1 and 
n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in 
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum 
element of this array.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Things to keep in mind:
What could you do to make it O(logn) runtime instead of O(n)?

There is a trivial solution, what is that?
There is a harder solution, but probably the one people want.  What is that method?
With the harder solution, usually you return the search value.  In this case, how do you return the min?
"""

# trivial solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        return sort_nums[0]

# harder solution binary search.  Essentially you are writing a binary search min
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            m = l + (r-l) // 2
            
            # you need to use nums[-1] for the last element in the sequence
            if nums[m] <= nums[-1]:
                # if you check this, you can start at the sorted area
                r = m
            else: # check items to right because you are finding the min
                l = m + 1
        # return nums[l] because it lands on the minimum value (last searched)
        return nums[l]