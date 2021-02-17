"""
Given an array, rotate the array to the right by k steps, where k is
non-negative.

HINT: Make life easy, use helper functions.  There are multiple approches
some take up more time complexity while others can take up more space.
"""

class Solution(object):
	""" BRUTE FORCE """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(k):
        	self.shift_right(nums, n)

    def shift_right(self, nums, n):
        # record first arr pos to move to end
        temp = nums[n-1]

        # iterate through and shift
        for i in reversed(range(n)):
            nums[i] = nums[i - 1]

        nums[0] = temp

class Solution2(object):
    """ Allocate new array """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # allocate a new array
        a = [0] * n

        # loop through new array and use % n to find the position of rotated i
        for i in range(n):
            a[(i + k) % n] = nums[i]
        # assign old array to new a
        nums[:] = a

# Output: [5,6,7,1,2,3,4]
ex_1 = [1,2,3,4,5,6,7]
ex_1_k = 3

# Output: [3,99,-1,-100]
ex_2 = [-1,-100,3,99]
ex_2_k = 2

# brute force testing
rotate_array = Solution()
rotate_array.rotate(ex_1, ex_1_k)
print(ex_1)

# allocating an additional array
rotate_array_2 = Solution2()
rotate_array_2.rotate(ex_2, ex_2_k)
print(ex_2)