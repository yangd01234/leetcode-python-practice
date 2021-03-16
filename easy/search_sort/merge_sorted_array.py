"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one 
sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough 
space to hold additional elements from nums2.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109

Things to keep in mind:
Look carefully at values m and n, how does this differ than len(nums1)?
Where have you seen this problem before?
How many indeces should you keep track of?
Can you have multiple while loops?
What should you keep track of in the array and why?
When should you increment each indices?
What else do you need to check after you have gone through i < m and j < n?
Why do you need to check for i < m then j < n after your first while loop?
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # create three indeces for num1, num2, and temp        
        i, j, k = 0, 0, 0

        # create a temporary holder for nums1
        temp = nums1.copy()

        # while i and j counters are less than len of nums1 and nums2
        while i < m and j < n:

            # if nums1[i] is less than nums2[j] swap with temp and set i+=1
            if temp[i] < nums2[j]:
                nums1[k] =  temp[i]
                i += 1
            else: # otherwise swap with nums2 and increment j
                nums1[k] = nums2[j]
                j+=1
            # increment k as the current space counter
            k+=1

        # check again nums1 for any leftovers 
        while i < m:
            nums1[k] = temp[i]
            i+=1
            k+=1

        # check the rest of j for any leftovers
        while j < n:
            nums1[k] = nums2[j]
            j+=1
            k+=1