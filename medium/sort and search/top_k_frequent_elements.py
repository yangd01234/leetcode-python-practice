"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.legth <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.

Things to keep in mind:
What does counter do?
What does sorted do?
How can you use a dict to order everything?
How would you then convert this dict?
What would you then return?
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict 
        c = Counter(nums)
        """
        set key to number of times it appears.  Take value inside dict.
        Set to desc order for reverse=True
        """
        c = sorted(c, key=lambda x:c[x], reverse=True)

        return c[:k]