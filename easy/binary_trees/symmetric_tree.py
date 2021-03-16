"""
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

Things to keep in mind:
What should you assert?
What is the general structure of a BFS in python?
How can you keep track of the first two right nd left roots in a stack?
What should you set as the temporary variables when going through the while loop?
what should you assert as you are going through the loop?
Why use continue if there are no left and right nodes?
What are the three things you should assert if it is False?
How can you now re-append and continue with the traversal?
WHy should you append in this order?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        stack = [(root.left, root.right)]

        while stack:
            node = stack.pop()
            left, right = node[0], node[1]

            if not left and not right: continue
            if ((not left and right)
                or (not right and left)
                or (left.val != right.val)):
                    return False
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        return True







