"""
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

Things to know:
Try this out using recursion.
If you know that it's sorted, how can you find the middle?
Why should you use the middle of the array if it's sorted?
What is the base case for recursion?
How can we use this base case to our advantage?
How can you use recursion to assign left and right nodes?
Why should you always return the root?
Why should you be aware of teh length of nums?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return None

            m = (l + r) // 2

            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)
