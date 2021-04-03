"""
215. Kth Largest Element in an Array
Medium

5377

347

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

Things to keep in mind:
How do you create a heap?
What is a heap?
Why is a heap beneficial in this case?
What is the trivial solution?
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] >= heap[0]:
                if len(heap) >= k:
                    heap.pop()
                    heap = [nums[i]] + heap
                else:
                    heap = [nums[i]] + heap
            elif nums[i] <= heap[-1]:
                if len(heap) >= k:
                    continue
                else:
                    heap.append(nums[i])
            else:
                temp = []
                while heap[-1] < nums[i]:
                    temp.append(heap.pop())
                heap.append(nums[i])
                while len(heap) < k:
                    if temp:
                        heap.append(temp.pop())
                    else:
                        break
        return heap[-1]



