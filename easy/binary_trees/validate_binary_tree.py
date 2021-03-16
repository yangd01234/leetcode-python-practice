"""
Given the root of a binary tree, determine if it is a valid binary search tree 
(BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

Things to keep in mind:
Why should you assert?
Why should you asser this?
How would you create the stack and why?
What should you set for the pooped value/temp values in the while loop?
Why should you check that the node values are within range?
Why shoul dyou check each node individually?
Why should you insert at the 0th index?
Why do you need to insert in different orders for left and right nodes?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# travserse the BST iterativley
# check to make sure that the root exists, if so append
# Check if BST is valid: left < val and right > val
class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, lower, upper = stack.pop()
            if not (lower < node.val < upper):
                return False
            if node.right:
                if node.right.val <= node.val:
                    return False
                # add the right node to the stack
                stack.insert(0, (node.right, node.val, upper))

            if node.left:
                if node.left.val >= node.val:
                    return False
                stack.insert(0, (node.left, lower, node.val))
        
        return True
