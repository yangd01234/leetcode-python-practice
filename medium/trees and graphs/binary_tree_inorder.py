"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?

Things to keep in mind:
How can you use another data structure to keep track of your position?
Why do you need to keep track of your current position?
If your current position has a left, what should you do?
Once you finish with this inner loop, what can you set once you've found
the leftmost node?

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        res = []
        curr = root

        # while your stack isn't empty and your root is not none (last one)
        while curr is not None or stack != []:
            # while your current is not none, then keep appending
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            # set your current to the last stack pos
            curr = stack.pop()
            # append this value (leftmost)
            res.append(curr.val)
            # increase current to right
            curr = curr.right
        return res
