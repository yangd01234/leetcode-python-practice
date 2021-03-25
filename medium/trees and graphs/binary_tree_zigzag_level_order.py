"""
Given the root of a binary tree, return the zigzag level order traversal of 
its nodes' values. (i.e., from left to right, then right to left for the next 
level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
What type of search can you complete?
What should you keep in mind when completing this type of search?
How can you toggle the direction?
How can you reverse the result?
Whys hould you reverse using [::1]? What does this do?
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = []
        current_level = []

        if not root: return []
        current_level.append(root)

        direction = False

        while current_level != []:
            next_level = []
            sub_array = []
            for n in current_level:
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
                sub_array.append(n.val)
            # reverse in place
            if direction: sub_array = sub_array[::-1]
            res.append(sub_array)
            # flip direction
            direction = not direction
            current_level = next_level
        return res




