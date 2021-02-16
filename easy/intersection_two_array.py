"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both
arrays. The result can be in any order.

HINT: You CAN use counter and get the elements(), however this method doesn't
need additional imports.

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                temp.append(i)

        return temp

nums1 = [1,2,2,1]
nums2 = [2,2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

obj = Solution()
print(obj.intersect(nums1, nums2))