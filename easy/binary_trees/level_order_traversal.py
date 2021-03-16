"""
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

Things to keep in mind:
What should you assert?
What two stacks should you set?
How can you keep track of sub levels?
Why do you need to check if the nodes exist?
How can you set the current level to the sublevel?
How can you use the temporary values list to append to the overall total?
Why should you keep these seperate?
"""


# two lists, current level and prev level
# outer while loop goes through prev level
# inner while loop goes through curr level
# the curr level loop pops from prev level if chlidren have been visted and pushes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, curr = [], [root]

        while curr:
            sub_level, vals = [], []

            for node in curr:
                vals.append(node.val)
                if node.left:
                    sub_level.append(node.left)
                if node.right:
                    sub_level.append(node.right)

            curr = sub_level
            res.append(vals)
        return res